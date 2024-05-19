import { Link } from 'react-router-dom';
import '../Pages_css/Header.css';

function Header() {

  return (
    <div className='Head'>
      <img src="src/Images/LOGO_tea.png" alt="" className='Logo'/>
      <nav>
        <ul>
          <li className='navigation  '><Link to='/'>ТЕКСТ</Link></li>
          <li className='navigation  '><Link to='/Document'>ЗАГРУЗИТЬ ДОКУМЕНТ</Link></li>
          <li className='navigation  '><Link to='/Url'>URL</Link></li>
        </ul>
      </nav>
    </div>
  )
}

export default Header
