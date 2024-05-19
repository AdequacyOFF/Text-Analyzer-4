function Contacts() {
    return (
        <div className='contact_information'>
        <div className='Copyright'>
          <div className='icons_contact'>
            <img src="src\Images\telegram.png" alt="telegram" onClick={() => window.open("https://t.me/siferony")} />
            <img src="src\Images\GitHub.png" alt="GitHub" onClick={() => window.open("https://github.com/AdequacyOFF")}/>
            <img src="src\Images\mail.png" alt="Mail" onClick={() => window.open("https://yandex.ru")}/>
          </div>
          <p>©2024 AdequacyOFF</p>
        </div>
      </div>
    )
}

export default Contacts;