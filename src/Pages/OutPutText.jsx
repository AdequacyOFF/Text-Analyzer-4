import React from "react";
import { Mychart } from "./Chart.jsx";
import { TotalChart } from "./TotalChart.jsx";
import { useState } from "react";
import { TextStyle } from "./TextStyle.jsx";
import '../Pages_css/OutPutText.css';

function OutputText({ inputArray }) {
  console.log(inputArray);
  const [inputValue, setInputValue] = useState("");
  const [array, setArray] = useState(inputArray);

  const handleChange = (event) => {
    setInputValue(event.target.value);
  };

  const handleSubmit = (index) => {
    fetch('http://127.0.0.1:8080/outputText/articlePut', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ array }),
    });

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

  const handleSave = () => {
    fetch('http://127.0.0.1:8080/outputText/articlePublish', {
      method: 'GET',
      headers: {
        'publishArticle': true,
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
              <span className="profanity_flag"><span className="profanity_flag_attention">Внимание:</span>Текст содержит ненормативную лексику</span>
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
