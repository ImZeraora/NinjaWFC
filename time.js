window.onload = function () {
    document.getElementById("header").className = "headerslide";
    document.getElementById("logo-home").addEventListener("click", defaulttheme);

    time();
}

function defaulttheme(){
    document.getElementById("monthimg").src="";

        document.getElementById("header").style.backgroundColor = "RGB(56,20,96)";
        document.getElementById("body").style.backgroundColor = "white";
        document.getElementById("body").style.color = "black";

        if (page == "index.html") {
            document.getElementById("newsp").innerHTML = "If you are reading this, it means that the website has worked and you can now connect to NinjaWFC! The website will be \"completed\" by the end of June and will have features like, Being able to detect how many players are on the server with more advanced methods, interactive design, and possibly mobile support (more to come).";
        }
        else {
        }
        document.getElementById("NinjaWFCTitle").innerHTML = "NinjaWFC";

        document.getElementById("logo-home").src = "https://i.ibb.co/GMK2Zst/logo.png";

        document.getElementById("monthimg").style.display="none";
}

function time(){
  var now = new Date();
  var datetime = now.toLocaleString();

  // Insert date and time into HTML
  document.getElementById("timestamp").innerHTML = datetime;
}




    setInterval(function () {

        time()

    }, 1000);