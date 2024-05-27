import json

def makeJson(result, total_emotion_result, style_result):
        answer_list = []
        
        for data in result:
            centence_dict_keys = ["text", "conclusion", "neutral_percent", "joy_percent", "sadness_percent", "surprise_percent", "fear_percent", "anger_percent", "profanity_flag"]
            centence_dict_values = [data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8]]
            centence_dict = dict(zip(centence_dict_keys, centence_dict_values))
            answer_list.append(centence_dict)

        total_dict_values = []
        for num in total_emotion_result[1:]:
            total_dict_values.append(num)
        total_dict_keys = ["total_neutral_percent", "total_joy_percent", "total_sadness_percent", "total_surprise_percent", "total_fear_percent", "total_anger_percent"]
        total_dict = dict(zip(total_dict_keys, total_dict_values))
        
        answer_list.append(total_dict)

        if style_result[0] == 'artistic':
            style_class = 'Artistic'
            style_conclusion = 'Художественный'
            
        if style_result[0] == 'publicistic':
            style_class = 'Publicistic'
            style_conclusion = 'Публицистический'
            
        if style_result[0] == 'scientific':
            style_class = 'Scientific'
            style_conclusion = 'Научный'
            
        if style_result[0] == 'conversational':
            style_class = 'Conversational'
            style_conclusion = 'Разговорный'
            
        if style_result[0] == 'official':
            style_class = 'Official-business'
            style_conclusion = 'Официально-деловой'
        
        style_dict = {"style_class" : style_class, 
                      "style_conclusion" : style_conclusion, 
                      "style_artistic_percent" : style_result[1], 
                      "style_publicistic_percent" : style_result[2], 
                      "style_scientific_percent" : style_result[3], 
                      "style_conversational_percent" : style_result[4], 
                      "style_official_percent" : style_result[5]}

        answer_list.append(style_dict)
        print(answer_list)
        return json.dumps(answer_list, ensure_ascii=False, sort_keys=False)