import { Link } from 'react-router-dom';
import '../Pages_css/Header.css';

function Header() {

  return (
    <div className='Head'>
      <img src="src/Images/LOGO_tea.png" alt="" className='Logo'/>
          <Link to='/' className='txt' title='В данном разделе вы можете написать свою статью или же вставить какой-либо текст для его последующего анализа и редактирования'>ТЕКСТ</Link>
          <Link to='/Document' className='doc' title='В данном разделе вы можете загрузить файл с вашей статьёй для её последующего анализа и редактирования'>ЗАГРУЗИТЬ ДОКУМЕНТ</Link>
          <Link to='/Url' className='url' title='В данном разделе вы можете вставить ссылку на интернет-статью для её автоматического считывания и последующего анализа и редактирования'>URL</Link>
    </div>
  )
}

export default Header
