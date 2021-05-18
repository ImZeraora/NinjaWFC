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
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
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
        }

        #NinjaWFCTitle {
            border-radius: 25px;
            background: #ffffff;
            padding: 20px;
            width: 200px;
        }

        #time{
            top: 0px;
            right: 50px;
            position: absolute;
            border-radius: 25px;
            background: #ffffff;
            padding: 15px;
        }

        #statstable{
            margin-top: 250px;
            text-align: center;
        }

        #nav1{
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
        #creatorname{
            text-decoration: black underline;
        }
        #nav{
            text-align: center;
            list-style: none;
            margin-top: 50px;
        }
    </style>
    <header id="header">
        <center>
            <h2 id="NinjaWFCTitle"><a href="http://www.ninjawfc.com/" id="nocolorlinks">NinjaWFC</a></h2>
        </center>
        <a href="http://www.ninjawfc.com/"><img src="https://i.ibb.co/GMK2Zst/logo.png" id="logo-home"></a>
        <p id="time">Offline</p>
        <center>
            <ul id="nav">
                <li id="nav1"><a href="http://www.ninjawfc.com/index.html" id="nocolorlinks">Home Page</li></a>
                <li id="nav1"><a href="http://www.ninjawfc.com/creator.html" id="nocolorlinks">Creators and Supporters</li></a>
                <li id="nav1"><a href="http://www.ninjawfc.com/codes.html" id="nocolorlinks">Codes</li></a>
            </ul>
        </center>
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
    var game = document.getElementById("game").textContent;
    window.onload = function () {

        changename();
        time();
    }
    function changename() {
        game = document.getElementById("game").textContent;
        if (document.getElementById("game").textContent == "mariokartwii") {
            document.getElementById("game").textContent = "Mario Kart Wii";
        }
        else {

        }
        document.getElementById("game").innerhtml = "Mario Kart Wii";
    }
    function time() {
        current = new Date();

        chours = current.getHours();

        cmin = current.getMinutes();

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

        if (cmonth == 4 && cdate == 14) {

            document.getElementById("logo-home").src="https://i.bb.co/X4RJ4y6/Zeraoralogo.png";

            document.getElementById("header").style.backgroundColor = "RGB(246,211,134)";

            document.getElementById("NinjaWFCTitle").innerHTML = "ZeraoraWFC";

        }
        else if (cmonth >= 5 && cmonth < 8) {

            document.getElementById("header").style.backgroundColor = "RGB(255,168,7)";

        }

        else if (cmonth == 11) {

            document.getElementById("header").className = "christmas";

        }

        else {

            document.getElementById("header").style.backgroundColor = "RGB(56,20,96)";

            document.getElementById("NinjaWFCTitle").innerHTML = "NinjaWFC";

            document.getElementById("logo-home").src = "https://i.ibb.co/GMK2Zst/logo.png";

        }
    }
    </script>
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