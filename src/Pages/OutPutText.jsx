import React from "react";
import { Mychart } from "./Chart.jsx";
import { TotalChart } from "./TotalChart.jsx";
import { useState } from "react";
import '../Pages_css/OutPutText.css';

function OutputText({ array }) {
  console.log(array);
  const [inputValue, setInputValue] = useState("");
  const [responseData, setResponseData] = useState([]);

  const handleChange = (event) => {
    setInputValue(event.target.value);
  };

  const handleSubmit = () => {
    fetch('http://127.0.0.1:8080/text', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ inputValue }),
    })
    .then((response) => response.json())
    .then((data) => setResponseData(data));
  };

  const handleSave = () => {
    fetch('http://127.0.0.1:8080/text', {
      method: 'GET',
      headers: {
        'publishArticle': true,
      },
    })
  };


  console.log(JSON.stringify({ inputValue }));

  return (
    <div>
      {array.slice(0, array.length - 1).map((item, index) => (
        <span key={index} className={item["conclusion"] + " output-text"}>
          {item["text"]}
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
              <button className='Fix_btn' type="button" onClick={handleSubmit}>
                <img src="src\Images\Fix_text.png" alt="Fix" />
              </button>
            </div>
          }
          {item["profanity_flag"] && (
            <div className="profanity_flag_block">
              <span className="profanity_flag"><span className="profanity_flag_attention">Внимание:</span>Текст содержит ненормативную лексику</span>
            </div>
          )}
          {<hr className='Strip'></hr>}
        </span>
      ))}
      <div className="TotalDiogram">
        {(array[array.length - 1] != undefined) ? <TotalChart array={array[array.length - 1]} /> : null}
      </div>
      <div>
        {(array != array.length) ? 
          (<button className='Save_btn' type="button" onClick={handleSave}>
            <img src="src/Images/SaveButton.png" alt="Save" />
          </button>)
          : null
        }
      </div>
    </div>
  );
}

export default OutputText;
