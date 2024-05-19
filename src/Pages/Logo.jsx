function Logo(){
    return (
        <div className='Logo_footer'>
            <img className='Logo_znania' src="src\Images\Logo_znania.png" alt="" onClick={() => window.open("https://знаниевики.рф")}/>
            <img className='Logo_AdOFF' src="src\Images\Logo_AdOFF.png" alt="" onClick={() => window.open("https://github.com/AdequacyOFF")} />
            <img  className='Logo_tea_footer' src="src\Images\Logo_tea_footer.png" alt="" />
        </div>
    )
}

export default Logo;