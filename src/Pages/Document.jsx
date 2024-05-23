import { useState } from "react";
import '../Pages_css/Document.css';
import DropFileInput from './DropFileInput';
import OutputText from "./OutPutText.jsx";

function Document() {

  const [data, setData] = useState([]);

   const updateData = (newData) => {
    setData(newData);
  };

  const onFileChange = (files) => {
    console.log(files);
}

  return (
    <div className='section'>
      <div className='answer-doc'>
        {data.length!=0 ? <OutputText inputArray={data}/> : null}
        
      </div>
      <div className='DropFileInput'>
          <DropFileInput onFileChange={(files) => onFileChange(files)} updateData={updateData}/> {/* Функция для перетаскивания файлов */}
      </div>
      {/* <form action="/">
        <button className='btn-doc-doc btn-doc-text-doc'>ТЕКСТ</button>
      </form>
      <form action="/Url">
        <button className='btn-url-doc btn-url-text-doc'>URL</button>
      </form> */}
    </div>
  )
}

export default Document
