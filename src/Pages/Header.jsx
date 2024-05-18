import { Link } from 'react-router-dom';
import '../Pages_css/Header.css';

function Header() {

  return (
    <div className='Head'>
      <img src="src/Images/LOGO_tea.png" alt="" className='Logo'/>
      <nav>
        <ul>
          <li className='navigation txt '><Link to='/'>ТЕКСТ</Link></li>
          <li className='navigation doc '><Link to='/Document'>ЗАГРУЗИТЬ ДОКУМЕНТ</Link></li>
          <li className='navigation url '><Link to='/Url'>URL</Link></li>
        </ul>
      </nav>
    </div>
  )
}

export default Header
