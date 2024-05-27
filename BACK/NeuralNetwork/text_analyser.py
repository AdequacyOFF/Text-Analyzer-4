from transformers import BertTokenizer, BertForSequenceClassification
from pymystem3 import Mystem

import os
import torch
import gdown

from NeuralNetwork.mlp_model import MLP
import NeuralNetwork.utils as U
from NeuralNetwork.JsonMaker import makeJson

class TextAnalyser:
    def __init__(self, device='cuda:0'):
        # Device of the model
        if device == 'cuda:0' and not torch.cuda.is_available():
            self.device = 'cpu'
            print('\nCUDA is not available! Use CPU.')
        else:
            print('\nGood news - CUDA is available!')
            self.device = device
        
        # Emotion classification labels
        self.emotions_labels = ['neutral', 'joy', 'sadness', 'surprise', 'fear', 'anger']
        
        # Text style classification labels
        self.style_labels = ['artistic', 'publicistic', 'scientific', 'conversational', 'official']
        
        # Define parent directory for finding path to model checkpoint
        # and file with profanity 
        self.parent_dir = os.path.dirname(os.path.abspath(__file__))
        path_to_ckp = os.path.join(self.parent_dir, 'ckp')
        path_to_bert = os.path.join(path_to_ckp, 'bert')
        path_to_style_classifier = os.path.join(path_to_ckp, 'style_classifier.pth')
        path_to_profanity = os.path.join(path_to_ckp, 'profanity.txt')
        
        # If directory with model was not found
        if not os.path.exists(path_to_ckp):
            print('\nNo local neural network model files were found. Install them using the URL.\n')
            url = "https://drive.google.com/drive/folders/11r4dcUjVBCg0mJHfyhyWffTyYQHNhx7O?usp=drive_link"
            gdown.download_folder(url, output=path_to_ckp)
        
        # Load models
        self.tokenizer = BertTokenizer.from_pretrained(path_to_bert)
        self.model = BertForSequenceClassification.from_pretrained(path_to_bert, num_labels=len(self.emotions_labels),
                                                                   problem_type='multi_label_classification')
        
        self.style_classifier = MLP(312, len(self.style_labels))

        if self.device == 'cpu':
            self.style_classifier.load_state_dict(torch.load(path_to_style_classifier, map_location=torch.device('cpu')))
        else:
            self.style_classifier.load_state_dict(torch.load(path_to_style_classifier))
            
        # Put models on the device
        self.model = self.model.to(self.device)
        self.style_classifier = self.style_classifier.to(self.device)
        
        # Load list with profanity from the file
        self.profanity_list = []
        
        with open(path_to_profanity, 'r', encoding='utf8') as f:
            for line in f.readlines():
                self.profanity_list.append(line[:-1])
                    
        self.lemmatizer = Mystem()
        
    
    def bert_output(self, text):
        encoding = self.tokenizer.encode_plus(text,
            add_special_tokens=True,
            max_length=512,
            return_token_type_ids=False,
            truncation=True,
            padding='max_length',
            return_attention_mask=True,
            return_tensors='pt'
        )
        
        input_ids = encoding['input_ids'].flatten().to(self.device)
        attention_mask = encoding['attention_mask'].flatten().to(self.device)

        # Pass data throw thr model
        outputs = self.model.bert(
            input_ids=input_ids.unsqueeze(0),
            attention_mask=attention_mask.unsqueeze(0)
        )

        return outputs
            
            
    def emotion_output(self, data):
        # If text is given
        if type(data) is str:
            # Tokenize text
            encoding = self.tokenizer.encode_plus(data,
                add_special_tokens=True,
                max_length=512,
                return_token_type_ids=False,
                truncation=True,
                padding='max_length',
                return_attention_mask=True,
                return_tensors='pt'
            )
            
            input_ids = encoding['input_ids'].flatten().to(self.device)
            attention_mask = encoding['attention_mask'].flatten().to(self.device)
            
            # Pass data throw the model
            outputs = self.model(
                input_ids=input_ids.unsqueeze(0),
                attention_mask=attention_mask.unsqueeze(0)
            )
            
            out = outputs.logits
        # If bert output is given
        else:
            out = self.model.classifier(data.pooler_output)
            
        # Apply softmax to output 
        return torch.softmax(out, dim=1).view(-1).detach()


    def style_output(self, data):
        # If text is given
        if type(data) is str:
            t = self.tokenizer(data, padding=True, truncation=True, return_tensors='pt')
            
            model_output = self.model.bert(**{k: v.to(self.device) for k, v in t.items()})
            
            embeddings = model_output.last_hidden_state[:, 0, :]
        # If bert output is given
        else:
            embeddings = data.last_hidden_state[:, 0, :]
            
        embeddings = torch.nn.functional.normalize(embeddings)
            
        # Put them to the MLP model
        output = self.style_classifier(embeddings[0])
        
        # Apply softmax to output 
        return torch.softmax(output, dim=0).detach()
    

    def emotion_analys(self, text, output=None):
        # Get probabilities from the model
        if output is None:
            probs = self.emotion_output(text)
        else:
            probs = self.emotion_output(output)
            
        # Define prediction of the model
        prediction = self.emotions_labels[torch.argmax(probs)]
        
        # Convert probabilities to percents
        neutral_percent = round(probs[0].item() * 100, 2)
        joy_percent = round(probs[1].item() * 100, 2)
        sadness_percent = round(probs[2].item() * 100, 2)
        surprise_percent = round(probs[3].item() * 100, 2)
        fear_percent = round(probs[4].item() * 100, 2)
        anger_percent = round(probs[5].item() * 100, 2)
        
        # Make profanity analys
        prof_flag = self.profanity_analys(text)
        
        return (text, prediction, neutral_percent, joy_percent, sadness_percent, 
                surprise_percent, fear_percent, anger_percent, prof_flag)
    

    def style_analys(self, data):
        # Get probabilities from the model
        probs = self.style_output(data)
        
        # Define prediction of the model
        prediction = self.style_labels[torch.argmax(probs)]
        
        # Convert probabilities to percents
        artistic_percent = round(probs[0].item() * 100, 2)
        publicistic_percent = round(probs[1].item() * 100, 2)
        scientific_percent = round(probs[2].item() * 100, 2)
        conversational_percent = round(probs[3].item() * 100, 2)
        official_percent = round(probs[4].item() * 100, 2)
        
        return (prediction, artistic_percent, publicistic_percent, scientific_percent, 
                conversational_percent, official_percent)
        
    
    def profanity_analys(self, text):
        r = U.find_intersection(U.split_words(text.lower()), self.profanity_list)
        r1 = U.find_intersection(U.only_words(self.lemmatizer.lemmatize(text)), self.profanity_list)

        if len(r) == 0 and len(r1) == 0:
            return False
        else:
            return True
    
    
    def summary(self, text, sen_num=2, to_json=True):
        bert_out = self.bert_output(text)
        
        style_result = self.style_analys(bert_out)
        
        # Split text on pairs of <sen_num> sentences
        sentences = U.sentencer(text, sen_num)
        
        # Probabilities for the whole text
        total = self.emotion_analys(text, bert_out)
        total_emotion_result = (total[1], 
                                total[2], 
                                total[3], 
                                total[4], 
                                total[5], 
                                total[6], 
                                total[7])
        
        result = []
        
        # Iterate on sentences
        for sentence in sentences:
            out = self.emotion_analys(sentence)
            result.append(out)
        
        return makeJson(result, total_emotion_result, style_result)
    
    