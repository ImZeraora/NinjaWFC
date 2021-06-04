"""DWC Network Server Emulator
    Copyright (C) 2014 polaris-
    Copyright (C) 2014 msoucy
    Copyright (C) 2015 Sepalani
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.
    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from twisted.web import server, resource
from twisted.internet import reactor
from twisted.internet.error import ReactorAlreadyRunning
from multiprocessing.managers import BaseManager
import time
import datetime
import json
import logging

import other.utils as utils
import dwc_config

logger = dwc_config.get_logger('InternalStatsServer')


class GameSpyServerDatabase(BaseManager):
    pass

GameSpyServerDatabase.register("get_server_list")


class StatsPage(resource.Resource):
    """Servers statistics webpage.
    Format attributes:
     - header
     - row
     - footer
    """
    isLeaf = True
    header = """<html>
    <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="NinjaWFC, A online replacement for Nintendo Wi-Fi Connection.">
    <meta name="keywords" content="Wi-Fi, Mario Kart Wii, NinjaWFC">
    <meta name="author" content="TheNinjaKingOW">
    <title>NinjaWFC</title>
    <link rel="icon" href="https://i.ibb.co/GMK2Zst/logo.png">
    </head>
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto+Mono:ital@1&display=swap');

        body {
            font-family: 'Roboto Mono', monospace;
            padding: 0;
            margin: 0;
            border: 0;
        }

        #logo-home {
            width: 8%;
            position: absolute;
            top: 15px;
            left: 100px;
        }

        header {
            background-color: RGB(56, 20, 96);
            height: 200px;
            padding: 0%;
            margin: 0%;
            border: 0%;
            position: absolute;
            top: 0%;
            width: 100%;
            border-bottom-left-radius: 25px;
            border-bottom-right-radius: 25px;
            opacity: 0%;
        }

        #NinjaWFCTitle {
            border-radius: 25px;
            background: #ffffff;
            padding: 20px;
            width: 200px;
        }

        #NinjaWFCForm{
            border-radius: 25px;
            background: #ffffff;
            padding: 20px;
            width: 200px;
            right: 50px;
            top: 106px;
            position: absolute;
            text-align: center;
          }

        #time{
            top: 0px;
            right: 50px;
            position: absolute;
            border-radius: 25px;
            background: #ffffff;
            padding: 15px;
            display: block;
        }

        #creator, #error, #statstable{
            margin-top: 250px;
            text-align: center;
        }

        #nav1,#nav2,#nav3,#nav4,#nav5,#nav6, #nav7{
            border-radius: 25px;
            background: #ffffff;
            padding: 20px;
            display: inline;
        }

        #nocolorlinks{
            color: black;
            text-decoration: none;
            display:inline-block
        }

        .christmas{
            background: repeating-linear-gradient(
            45deg,
            white,
            white 50px,
            red 50px,
            red 60px
            
            );
            border: red 10px solid;
            width: 98.9%;
            border-right: red 11px solid;
        }
        #creatorimg{
            width: 200px;
            height: 200px;
            border: black 5px solid;
        }
        #creatorname{
            text-decoration: black underline;
        }
        #nav{
            text-align: center;
            list-style: none;
            margin-top: 50px;
        }
        #news, #tutorialheader, #codeheader{
            text-align: center;
            margin-top: 225px;
        }
        #ninjawfccode{
            border-radius: 25px;
            background: #ffffff;
            border: black 3px solid;
            padding: 20px;
            width: 400px;   
        }
        .button.alternative {
            --color-hover: #2B3044;
            --background: #362A89;
            --hover-back: #6D58FF;
            --hover-front: #F6F8FF;
          }
          .button {
            --color: #fff;
            --color-hover: var(--color);
            --background: #2B3044;
            --background-hover: var(--background);
            --hover-back: #6D58FF;
            --hover-front: #5C86FF;
            padding: 8px 28px;
            border-radius: 20px;
            line-height: 24px;
            font-size: 14px;
            font-weight: 600;
            letter-spacing: 0.02em;
            border: none;
            outline: none;
            position: relative;
            overflow: hidden;
            cursor: pointer;
            -webkit-appearance: none;
            -webkit-tap-highlight-color: transparent;
            -webkit-mask-image: -webkit-radial-gradient(white, black);
            color: var(--c, var(--color));
            background: var(--b, var(--background));
            transition: color 0.2s linear var(--c-d, 0.2s), background 0.3s linear var(--b-d, 0.2s);
          }
          .button:not(.simple):before, .button:not(.simple):after {
            content: "";
            position: absolute;
            background: var(--pb, var(--hover-back));
            top: 0;
            left: 0;
            right: 0;
            height: 200%;
            border-radius: var(--br, 40%);
            transform: translateY(var(--y, 50%));
            transition: transform var(--d, 0.4s) ease-in var(--d-d, 0s), border-radius 0.5s ease var(--br-d, 0.08s);
          }
          .button:not(.simple):after {
            --pb: var(--hover-front);
            --d: .44s;
          }
          .button div {
            z-index: 1;
            position: relative;
            display: flex;
          }
          .button div span {
            display: block;
            -webkit-backface-visibility: hidden;
                    backface-visibility: hidden;
            transform: translateZ(0);
            -webkit-animation: var(--name, none) 0.7s linear forwards 0.18s;
                    animation: var(--name, none) 0.7s linear forwards 0.18s;
          }
          .button.in {
            --name: move;
          }
          .button.in:not(.out) {
            --c: var(--color-hover);
            --b: var(--background-hover);
          }
          .button.in:not(.out):before, .button.in:not(.out):after {
            --y: 0;
            --br: 5%;
          }
          .button.in:not(.out):after {
            --br: 10%;
            --d-d: .02s;
          }
          .button.in.out {
            --name: move-out;
          }
          .button.in.out:before {
            --d-d: .06s;
          }
          
          @-webkit-keyframes move {
            30%, 36% {
              transform: translateY(calc(-6px * var(--move))) translateZ(0) rotate(calc(-13deg * var(--rotate) * var(--part)));
            }
            50% {
              transform: translateY(calc(3px * var(--move))) translateZ(0) rotate(calc(6deg * var(--rotate) * var(--part)));
            }
            70% {
              transform: translateY(calc(-2px * var(--move))) translateZ(0) rotate(calc(-3deg * var(--rotate) * var(--part)));
            }
          }
          
          @keyframes move {
            30%, 36% {
              transform: translateY(calc(-6px * var(--move))) translateZ(0) rotate(calc(-13deg * var(--rotate) * var(--part)));
            }
            50% {
              transform: translateY(calc(3px * var(--move))) translateZ(0) rotate(calc(6deg * var(--rotate) * var(--part)));
            }
            70% {
              transform: translateY(calc(-2px * var(--move))) translateZ(0) rotate(calc(-3deg * var(--rotate) * var(--part)));
            }
          }
          @-webkit-keyframes move-out {
            30%, 36% {
              transform: translateY(calc(6px * var(--move))) translateZ(0) rotate(calc(13deg * var(--rotate) * var(--part)));
            }
            50% {
              transform: translateY(calc(-3px * var(--move))) translateZ(0) rotate(calc(-6deg * var(--rotate) * var(--part)));
            }
            70% {
              transform: translateY(calc(2px * var(--move))) translateZ(0) rotate(calc(3deg * var(--rotate) * var(--part)));
            }
          }
          @keyframes move-out {
            30%, 36% {
              transform: translateY(calc(6px * var(--move))) translateZ(0) rotate(calc(13deg * var(--rotate) * var(--part)));
            }
            50% {
              transform: translateY(calc(-3px * var(--move))) translateZ(0) rotate(calc(-6deg * var(--rotate) * var(--part)));
            }
            70% {
              transform: translateY(calc(2px * var(--move))) translateZ(0) rotate(calc(3deg * var(--rotate) * var(--part)));
            }
          }
        #creatorimg, #creatorimg3{
            width: 200px;
            height: 200px;
            border: black 5px solid;
        }
        #creatorimg2{
            width: 150px;
            height: 200px;
            border: black 5px solid;
        }
        #creatorname{
            text-decoration: black underline;
        }
        .wrapper { 
          height: 100%;
          width: 100%;
        background: linear-gradient(124deg, #ff2400, #e81d1d, #e8b71d, #e3e81d, #1de840, #1ddde8, #2b1de8, #dd00f3, #dd00f3);
        background-size: 1800% 1800%;
        
        -webkit-animation: rainbow 18s ease infinite;
        -z-animation: rainbow 18s ease infinite;
        -o-animation: rainbow 18s ease infinite;
          animation: rainbow 18s ease infinite;}
        
        @-webkit-keyframes rainbow {
            0%{background-position:0% 82%}
            50%{background-position:100% 19%}
            100%{background-position:0% 82%}
        }
        @-moz-keyframes rainbow {
            0%{background-position:0% 82%}
            50%{background-position:100% 19%}
            100%{background-position:0% 82%}
        }
        @-o-keyframes rainbow {
            0%{background-position:0% 82%}
            50%{background-position:100% 19%}
            100%{background-position:0% 82%}
        }
        @keyframes rainbow { 
            0%{background-position:0% 82%}
            50%{background-position:100% 19%}
            100%{background-position:0% 82%}
        }
        #eastereggfnf1{
          display: none;
          width: 150px;
          height: 213px;
          position: absolute;
          top: 500px;
          left: 580px;
        }
        #eastereggfnf2{
          display: none;
          width: 450px;
          height: 320px;
          position: absolute;
          top: 388px;
          left: 750px;
        }
        #eastereggfnf3{
          display: none;
          width: 150px;
          height: 147px;
          position: absolute;
          top: 564px;
          left: 1200px;
        }
        #featurelist{
          list-style: none;
          text-align: center;
        }
        @keyframes headerslide{
          0% {opacity: 0%; position: absolute; top:-210px;}
          25% {opacity: 25%;}
          50% {opacity: 50%;}
          75% {opacity: 75%;}
          100%{opacity: 100%; position: absolute; top: 0px;}
        }
        .headerslide{
          animation: headerslide 1.5s linear 1;
          animation-fill-mode: forwards;
        }
        #monthimg{
          position: fixed;
          bottom: 0%;
          right: 0%;
          width: 250px;
          height: 250px;
          display: none;
        }
        #videoshowcase{
          display: block;
        }
        @media screen and (max-width: 1440px) {
        #monthimg{
          position: fixed;
          bottom: 0%;
          right: 0%;
          width: 0px;
          height: 0px;
          display: none;
        }
        #logo-home {
          width: 50px;
          position: absolute;
          top: 100px;
          left: 25px;
      }
      #videoshowcase{
        display: none;
      }
      #nav1,#nav2,#nav3,#nav5,#nav6,#nav7, #NinjaWFCForm{
        border-radius: 25px;
        background: #ffffff;
        padding: 20px;
        display: none;
    }
    #nav4{
            border-radius: 25px;
            background: #ffffff;
            padding: 20px;
            display: inline;
            position: absolute;
            top: 125px;
            left: 150px;
            
    }
    #time{
      display: block;
      position: absolute;
      top: 125px;
      right: 25px;
    }
  }
    </style>
    <body>
    <header id="header">
        <center>
            <h2 id="NinjaWFCTitle"><a href="http://www.ninjawfc.com/" id="nocolorlinks">NinjaWFC</a></h2>
        </center>
        <a href="http://www.ninjawfc.com/"><img src="https://i.ibb.co/GMK2Zst/logo.png" id="logo-home"></a>
        <p id="time">Offline</p>
        <center>
            <ul id="nav">
                <li id="nav4"><a href="http://www.ninjawfc.com/index.html" id="nocolorlinks">Home Page</li></a>
                <li id="nav2"><a href="http://www.ninjawfc.com/creator.html" id="nocolorlinks">Creators and Supporters</li></a>
                <li id="nav3"><a href="http://www.ninjawfc.com/codes.html" id="nocolorlinks">Codes</li></a>
                <li id="nav5"><a href="http://www.ninjawfc.com/error.html" id="nocolorlinks">Error Codes</li></a>
                <li id="nav6"><a href="http://www.ninjawfc.com/tutorial.html" id="nocolorlinks">Tutorial</li></a>
                <li id="nav7"><a href="http://www.ninjawfc.com:9009" id="nocolorlinks">Log In</li></a>
            </ul>
        </center>
        <p id="NinjaWFCForm"><a href="https://forms.gle/DSQSFC7Rs6H41Fyp9" id="nocolorlinks">Requests?</a></p>
    </header>
    <center>
    <table border='1' id="statstable">
        <tr>
            <td>Game ID</td><td>Number of Online Players</td>
        </tr>"""
    row = """
        <tr>
            <td id="game">%s</td>
            <td><center>%d</center></td>
        </tr>"""  # % (game, len(server_list[game]))
    footer = """</table>
    <br>
    <p>This page was last updated: %s</p><br>
    <center>
    <script>
    var current = new Date();
    var chours = current.getHours();
    var cmin = current.getMinutes();
    var cmonth = current.getMonth();
    var cdate = current.getDate();
    var timeam = "am";
    var audio = new Audio();
    var page="stats.html"
    window.onload = function () {
    document.getElementById("header").className = "headerslide";

    time();

    if (page == "index.html" || page == "codes.html") {

    }
    else if (page == "stats.html" || page == "error.html") {

    }
    else if (page == "tutorial.html") {

    }

    else {

        document.getElementById("creatorimg").addEventListener('click', ninjasound);
        document.getElementById("creatorimg2").addEventListener('click', oversound);
        document.getElementById("creatorimg3").addEventListener('click', wafflessound);
    }
    document.querySelectorAll('.button').forEach(button => {

        let div = document.createElement('div'),
            letters = button.textContent.trim().split('');

        function elements(letter, index, array) {

            let element = document.createElement('span'),
                part = (index >= array.length / 2) ? -1 : 1,
                position = (index >= array.length / 2) ? array.length / 2 - index + (array.length / 2 - 1) : index,
                move = position / (array.length / 2),
                rotate = 1 - move;

            element.innerHTML = !letter.trim() ? '&nbsp;' : letter;
            element.style.setProperty('--move', move);
            element.style.setProperty('--rotate', rotate);
            element.style.setProperty('--part', part);

            div.appendChild(element);

        }

        letters.forEach(elements);

        button.innerHTML = div.outerHTML;

        button.addEventListener('mouseenter', e => {
            if (!button.classList.contains('out')) {
                button.classList.add('in');
            }
        });

        button.addEventListener('mouseleave', e => {
            if (button.classList.contains('in')) {
                button.classList.add('out');
                setTimeout(() => button.classList.remove('in', 'out'), 950);
            }
        });

    });
}

function ninjasound() {

    audio = new Audio('gladiator.wav');

    audio.play();

}

function oversound() {

    audio = new Audio('lucario.wav');

    audio.play();

}
function wafflessound() {

    audio = new Audio('waffles.wav');

    audio.play();

}

function time() {

  if (document.getElementById("game")) {
    if (document.getElementById("game").innerHTML == "mariokartwii") {
      document.getElementById("game").innerHTML = "Mario Kart Wii";
    }
    else if (document.getElementById("game").innerHTML == "mariokartds") {
      document.getElementById("game").innerHTML = "Mario Kart DS";
    }
    else {

    }
  }
  else {

  }
    current = new Date();

    chours = current.getHours();

    cmin = current.getMinutes();
    cdate = current.Date

    if (chours > 12) {

        chours = chours - 12;

        timeam = "pm"

    }

    else {

    }

    if (cmin <= 9) {

        document.getElementById("time").innerHTML = chours + ":" + "0" + cmin + timeam;

    }

    else {

        document.getElementById("time").innerHTML = chours + ":" + cmin + timeam;

    }



    setInterval(function () {

        time()

    }, 60000);

    if (cmonth == 3 && cdate == 14) {

        document.getElementById("logo-home").src = "https://i.imgur.com/dJ3cQyl.png";

        document.getElementById("header").style.backgroundColor = "RGB(246,211,134)";

        document.getElementById("NinjaWFCTitle").innerHTML = "ZeraoraWFC";
    }
    else if (cmonth >= 5 && cmonth < 8) {
        document.getElementById("header").style.backgroundColor = "RGB(255,168,7)";
    }
    else if(cmonth==9){
        document.getElementById("header").style.backgroundColor = "RGB(235,97,35)";
        document.getElementById("body").style.backgroundColor = "black";
        document.getElementById("body").style.color = "white";
        document.getElementById("time").style.color = "black";
    }
    else if (cmonth == 11) {

        document.getElementById("header").className = "christmas";

    }

    else {

        document.getElementById("monthimg").src="";

        document.getElementById("header").style.backgroundColor = "RGB(56,20,96)";
        
        document.getElementById("NinjaWFCTitle").innerHTML = "NinjaWFC";

        document.getElementById("logo-home").src = "https://i.ibb.co/GMK2Zst/logo.png";

    }
}
    </script>
    </body>
    </html>"""  # % (self.stats.get_last_update_time())

    def __init__(self, stats):
        self.stats = stats

    def render_GET(self, request):
        if "/".join(request.postpath) == "json":
            raw = True
            force_update = True
        else:
            raw = False
            force_update = False

        server_list = self.stats.get_server_list(force_update)

        if raw:
            # List of keys to be removed
            restricted = ["publicip", "__session__", "localip0", "localip1"]

            # Filter out certain fields before displaying raw data
            if server_list is not None:
                for game in server_list:
                    for server in server_list[game]:
                        for r in restricted:
                            if r in server:
                                server.pop(r, None)

            output = json.dumps(server_list)

        else:
            output = self.header
            if server_list is not None:
                output += "".join(self.row % (game, len(server_list[game]))
                                  for game in server_list
                                  if server_list[game])
            output += self.footer % (self.stats.get_last_update_time())

        return output


class InternalStatsServer(object):
    """Internal Statistics server.
    Running on port 9001 by default: http://127.0.0.1:9001/
    Can be displayed in json format: http://127.0.0.1:9001/json
    """
    def __init__(self):
        self.last_update = 0
        self.next_update = 0
        self.server_list = None
        # The number of seconds to wait before updating the server list
        self.seconds_per_update = 60

    def start(self):
        manager_address = dwc_config.get_ip_port('GameSpyManager')
        manager_password = ""
        self.server_manager = GameSpyServerDatabase(address=manager_address,
                                                    authkey=manager_password)
        self.server_manager.connect()

        site = server.Site(StatsPage(self))
        reactor.listenTCP(dwc_config.get_port('InternalStatsServer'), site)

        try:
            if not reactor.running:
                reactor.run(installSignalHandlers=0)
        except ReactorAlreadyRunning:
            pass

    def get_server_list(self, force_update=False):
        if force_update or self.next_update == 0 or \
           self.next_update - time.time() <= 0:
            self.last_update = time.time()
            self.next_update = time.time() + self.seconds_per_update
            self.server_list = self.server_manager.get_server_list() \
                                                  ._getvalue()

            logger.log(logging.DEBUG, "%s", self.server_list)

        return self.server_list

    def get_last_update_time(self):
        return str(datetime.datetime.fromtimestamp(self.last_update))


if __name__ == "__main__":
    stats = InternalStatsServer()
    stats.start()