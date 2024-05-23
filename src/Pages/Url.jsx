import { useState } from "react";
import '../Pages_css/Url.css';
import OutputText from "./OutPutText.jsx";


function Url() {
  
  const [responseData, setResponseData] = useState([]);
  const [inputValue, setInputValue] = useState("");

  const handleChange = (event) => {
    setInputValue(event.target.value);
  };

  const handleSubmit = () => {
    fetch('http://127.0.0.1:8080/url', {
      method: 'POST',
      headers: {
        'Content-Type': 'text/html; charset=utf',
      },
      body: inputValue,
    })
    .then((response) => response.json())
    .then((data) => setResponseData(data));
  };

  
  return (
    <div className="section">


      <div className="answer_block">
        <input type="text" className='input_field' placeholder='Введите ссылку на источник(URL)...' onChange={handleChange} />
        <button className='Processing_btn' type="button" onClick={handleSubmit}>
          <img src="src/Images/Processing.png" alt="Processing" />
        </button>
      </div>
      <div className='answer-url'>
        <div className='answer-url-frame'>
          {responseData.length!=0 ? <OutputText inputArray={responseData}/> : null}
        </div>
      </div>  
    </div>
    
  );
};

export default Url;
