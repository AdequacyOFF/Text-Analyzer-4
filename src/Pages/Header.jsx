import { Link } from 'react-router-dom';
import '../Pages_css/Header.css';

function Header() {

  return (
    <div className='Head'>
      <img src="src/Images/LOGO_tea.png" alt="" className='Logo'/>
          <Link to='/' className='txt'>ТЕКСТ</Link>
          <Link to='/Document' className='doc'>ЗАГРУЗИТЬ ДОКУМЕНТ</Link>
          <Link to='/Url' className='url'>URL</Link>
    </div>
  )
}

export default Header
