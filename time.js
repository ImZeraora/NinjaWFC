window.onload=function(){
    if(page=="index.html" || page=="codes.html"){
    }
    else{
    document.getElementById("creatorimg").addEventListener('click', ninjasound)
    }
    time();
}

function ninjasound(){
    audio=new Audio('gladiator.wav')
    audio.play();
}

function time(){
    current=new Date();
    chours=current.getHours();
    cmin=current.getMinutes();
    if(chours > 12){
    chours = chours - 12;
    timeam="pm"
    }
    else{

    }
    if(cmin <= 9)
    document.getElementById("time").innerHTML=chours + ":" + "0" + cmin + timeam;
    else{
    document.getElementById("time").innerHTML=chours + ":" + cmin + timeam;
    }
    setInterval(function(){
    time()
    
    
    
    
    }, 60000);
    if(cmonth==4 && cdate==14){
        document.getElementById("logo-home").src="Zeraoralogo.png";
        document.getElementById("header").style.backgroundColor="RGB(246,211,134)";
        document.getElementById("NinjaWFCTitle").innerHTML="ZeraoraWFC";
        document.getElementById("newsp").innerHTML="If you are reading this, it means that the website has worked and you can now connect to ZeraoraWFC! The website will be \"completed\" by the end of June and will have features like, Being able to detect how many players are on the server with more advanced methods, interactive design, and possibly mobile support (more to come).";
    }
    else if(cmonth >= 5 && cmonth < 8){
        document.getElementById("header").style.backgroundColor="RGB(255,168,7)";
    }

    else if(cmonth==11){
        document.getElementById("header").className="christmas";
    }

    else{
        document.getElementById("header").style.backgroundColor="RGB(56,20,96)";
        document.getElementById("newsp").innerHTML="If you are reading this, it means that the website has worked and you can now connect to NinjaWFC! The website will be \"completed\" by the end of June and will have features like, Being able to detect how many players are on the server with more advanced methods, interactive design, and possibly mobile support (more to come).";
        document.getElementById("NinjaWFCTitle").innerHTML="NinjaWFC";
        document.getElementById("logo-home").src="logo.png";
    }
}