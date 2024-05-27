import React from "react";
import { Mychart } from "./Chart.jsx";
import { TotalChart } from "./TotalChart.jsx";
import { useState, useEffect } from "react";
import { TextStyle } from "./TextStyle.jsx";
import { StyleConclusions } from "./TextStyleConclusion.jsx";
import '../Pages_css/OutPutText.css';
import '../Pages_css/TextStyleConclusion.css';

function OutputText({ inputArray, articleLink = "https://baza.znanierussia.ru/mediawiki/index.php/%D0%BC%D0%BE%D1%8F-%D1%81%D1%82%D0%B0%D1%82%D1%8C%D1%8F" }) {
  console.log(inputArray);
  const [inputValue, setInputValue] = useState("");
  const [array, setArray] = useState(inputArray);

  useEffect(() => {
    setArray(inputArray);
  }, [inputArray]);

  useEffect(() => {
    fetch('http://127.0.0.1:8080/outputText/articleUpdate', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ array }),
    })
  }, [array]);

  const handleChange = (event) => {
    setInputValue(event.target.value);
  };

  const handleSubmit = (index) => {
    fetch('http://127.0.0.1:8080/outputText/articleEdit', {
      method: 'POST',
      headers: {
        'indexToChange': index,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ inputValue }),
    })
    .then((response) => response.json())
    .then((data) => setArray(data));
    console.log(array);
  };

  const handlePublish = (articleLink) => {
    fetch('http://127.0.0.1:8080/outputText/articlePublish', {
      method: 'GET',
      headers: {
        'articleLink': articleLink,
      },
    })
  };


  console.log(JSON.stringify({ inputValue }));

  return (
    <div>
      {array.slice(0, array.length - 2).map((item, index) => (
        <span key={index} className="output-text"  >
          <span className={item["conclusion"]}>{item["text"]}</span>
          {
            <div className="Diogram"> 
                <Mychart array={item} />
            </div>
          }
          {
            <div className="input_edit_block">
              <textarea autosize 
                key={index}
                className="input_edit"
                placeholder="Отредактируйте выделенный фрагмент текста..."
                onChange={handleChange}
                style={{resize: 'none'}}
              >
              </textarea>
              {/* <button className='Fix_btn' type="button" onClick={handleSubmit}> */}
              <button className='Fix_btn' type="button" onClick={() => handleSubmit(index)}>
                <img src="src\Images\Fix_text.png" alt="Fix" />
              </button>
            </div>
          }
          {item["profanity_flag"] && (
            <div className="profanity_flag_block">
              <span className="profanity_flag"><span className="profanity_flag_attention">Внимание: </span>Текст содержит ненормативную лексику</span>
            </div>
          )}
          {<hr className='Strip'></hr>}
        </span>
      ))}
      <div className="TotalDiogram">
        {(array[array.length - 2] != undefined) ? <TotalChart array={array[array.length - 2]} /> : null}
      </div>
      <div className="TextStyle">
        {(array[array.length - 1] != undefined) ? <TextStyle array={array[array.length - 1]} /> : null}
      </div>
      <div className="TextStyleConclusion">
        {(array[array.length - 1] != undefined) ? <StyleConclusions array={array[array.length - 1]} /> : null}
      </div>
      <div>
        {(array != array.length) ? 
          (<button className='Save_btn' type="button" onClick={() => handlePublish(articleLink)}>
            <img src="src/Images/SaveButton.png" alt="Save" />
          </button>)
          : null
        }
      </div>
    </div>
  );
}

export default OutputText;
