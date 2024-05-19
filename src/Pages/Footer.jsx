import Cooperation from './Cooperation';
import Logo from './Logo';
import Contacts from './Contacts';
import '../Pages_css/Footer.css';

function Footer() {

  return (
    <div className='Footer'>
        <Logo/>
        <Cooperation/>
        <div className='emoji'>
          <img src="src\Images\emoji.png" alt="" />
        </div>
      <div className='Strip_block'>
          <hr className='Strip'></hr>
      </div>
      <Contacts/>
    </div>
  )
}

export default Footer
