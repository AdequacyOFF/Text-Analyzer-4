import React from 'react';
import '../Pages_css/TextStyleConclusion.css';

export function StyleConclusions({ array }) {
  console.log("StyleConclusions array: ", array);
  
  return (
    <div>
      <span className={array["style_class"]}><span className='StyleConclusions_definition'>Стиль текста:  </span>{array["style_conclusion"]}</span>
    </div>
  );
}

