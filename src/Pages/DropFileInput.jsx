import React, { useRef, useState } from 'react';
import PropTypes from 'prop-types';

import '../Pages_css/DropFileInput.css';

import { ImageConfig } from './ImageConfig.js'; 
import uploadImg from '../assets/cloud-upload-regular-240.png';

const DropFileInput = props => {

    const wrapperRef = useRef(null);

    const [fileList, setFileList] = useState([]);

    const onDragEnter = () => wrapperRef.current.classList.add('dragover');

    const onDragLeave = () => wrapperRef.current.classList.remove('dragover');

    const onDrop = () => wrapperRef.current.classList.remove('dragover');

    const onFileDrop = (e) => {
        const newFile = e.target.files[0];
        if (newFile) {
            const updatedList = [...fileList, newFile];
            setFileList(updatedList);
            props.onFileChange(updatedList);
        }
    }

    const fileRemove = (file) => {
        const updatedList = [...fileList];
        updatedList.splice(fileList.indexOf(file), 1);
        setFileList(updatedList);
        props.onFileChange(updatedList);
    }

    return (
        <div className="DragAndDrop">
            <div
                ref={wrapperRef}
                className="drop-file-input"
                onDragEnter={onDragEnter}
                onDragLeave={onDragLeave}
                onDrop={onDrop}
            >
                <div className="drop-file-input__label">
                    <img src={uploadImg} alt="" />
                    <p>ПЕРЕНЕСИТЕ ИЛИ НАЖМИТЕ ДЛЯ ЗАГРУЗКИ ФАЙЛА</p>
                </div>
                <input type="file" value="" onChange={onFileDrop}/>
            </div>
            {
                fileList.length > 0 ? (
                    <div className="drop-file-preview">
                        <p className="drop-file-preview__title">
                            Готов к загрузке
                        </p>
                        {
                            fileList.map((item, index) => (
                                
                                <div key={index} className="drop-file-preview__item">
                                    <img src={ImageConfig[item.type.split('/')[1]] || ImageConfig['default']} alt="" />
                                    <div className="drop-file-preview__item__info">
                                        <p>{item.name}</p>
                                        <p>{item.size}B</p>
                                    </div>
                                    <span className="drop-file-preview__item__del" onClick={() => fileRemove(item)}>x</span>
                                </div>
                                
                            ))
                            
                        }
                        <button onClick={(event) => {
                                event.preventDefault();
                                const response = fetch('https://example.com/api/upload', {
                                  method: 'POST',
                                  body: blob(fileList),
                                  headers: {
                                    'Content-Type': 'boundary',
                                  },
                                });
                              
                                response.then((data) => {
                                  if (!response.ok) {
                                    throw new Error('Failed to upload files');
                                  }
                                });
                              }}>
                            Upload
                        </button>
                    </div>
                ) : null
            }
        </div>
    );
}

DropFileInput.propTypes = {
    onFileChange: PropTypes.func
}

export default DropFileInput;
