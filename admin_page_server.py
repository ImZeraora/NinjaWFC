"""DWC Network Server Emulator
    Copyright (C) 2014 SMTDDR
    Copyright (C) 2014 kyle95wm
    Copyright (C) 2014 AdmiralCurtiss
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
import base64
import codecs
import sqlite3
import collections
import json
import os.path
import logging

import other.utils as utils
import gamespy.gs_utility as gs_utils
import dwc_config

logger = dwc_config.get_logger('AdminPage')
_, port = dwc_config.get_ip_port('AdminPage')


# Example of adminpageconf.json
#
# {"username":"admin","password":"opensesame"}
#
# NOTE: Must use double-quotes or json module will fail
# NOTE2: Do not check the .json file into public git!

adminpageconf = None
admin_username = None
admin_password = None

if os.path.exists('adminpageconf.json'):
    try:
        adminpageconf = json.loads(file('adminpageconf.json').read().strip())
        admin_username = str(adminpageconf['username'])
        admin_password = str(adminpageconf['password'])
    except Exception as e:
        logger.log(logging.WARNING,
                   "Couldn't read adminpageconf.json. "
                   "Admin page will not be available.")
        logger.log(logging.WARNING, str(e))
        adminpageconf = None
        admin_username = None
        admin_password = None
else:
    logger.log(logging.INFO,
               "adminpageconf.json not found. "
               "Admin page will not be available.")


class AdminPage(resource.Resource):
    isLeaf = True

    def __init__(self, adminpage):
        self.adminpage = adminpage

    def get_header(self, title=None):
        if not title:
            title = 'NinjaWFC Admin Page'
        s = """
        <html>
        <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="NinjaWFC, A online replacement for Nintendo Wi-Fi Connection.">
    <meta name="keywords" content="Wi-Fi, Mario Kart Wii, NinjaWFC">
    <meta name="author" content="TheNinjaKingOW">
            <title>%s</title>
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
                <li id="nav1"><a href="http://www.ninjawfc.com/index.html" id="nocolorlinks">Home Page</li></a>
                <li id="nav1"><a href="http://www.ninjawfc.com/creator.html" id="nocolorlinks">Creators and Supporters</li></a>
                <li id="nav1"><a href="http://www.ninjawfc.com/codes.html" id="nocolorlinks">Codes</li></a>
                <li id="nav1"><a href="http://www.ninjawfc.com:9001" id="nocolorlinks">Stats</li></a>
                <li id="nav1"><a href="http://www.ninjawfc.com/error.html" id="nocolorlinks">Error Codes</li></a>
                <li id="nav1"><a href="http://www.ninjawfc.com/tutorial.html" id="nocolorlinks">Tutorial</li></a>
            </ul>
        </center>
    </header>
    <center>
            <p>
                %s | %s | %s
            </p>
        """ % (title,
               '<a href="/banhammer">All Users</a>',
               '<a href="/consoles">Consoles</a>',
               '<a href="/banlist">Active Bans</a>')
        return s

    def get_footer(self):
        s = """
        </center>
        <script>
    var current = new Date();
    var chours = current.getHours();
    var cmin = current.getMinutes();
    var cmonth = current.getMonth();
    var cdate = current.getDate();
    var timeam = "am";
    var audio = new Audio();
    window.onload = function () {
        document.getElementById("header").className="headerslide";
        time();
        changename();
    }
    function changename() {
        if (document.getElementById("game").textContent == "mariokartwii") {
            document.getElementById("game").textContent = "Mario Kart Wii";
        }
        else {

        }
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
        </body>
        </html>
        """
        return s

    def is_authorized(self, request):
        is_auth = False
        response_code = 401
        error_message = "Authorization required!"
        address = request.getClientIP()
        try:
            expected_auth = base64.encodestring(
                admin_username + ":" + admin_password
            ).strip()
            actual_auth = request.getAllHeaders()['authorization'] \
                .replace("Basic ", "") \
                .strip()
            if actual_auth == expected_auth:
                logger.log(logging.INFO, "%s Auth Success", address)
                is_auth = True
        except Exception as e:
            logger.log(logging.INFO, "%s Auth Error: %s", address, str(e))
        if not is_auth:
            logger.log(logging.INFO, "%s Auth Failure", address)
            request.setResponseCode(response_code)
            request.setHeader('WWW-Authenticate', 'Basic realm="ALTWFC"')
            request.write(error_message)
        return is_auth

    def update_banlist(self, request):
        address = request.getClientIP()
        dbconn = sqlite3.connect('gpcm.db')
        gameid = request.args['gameid'][0].upper().strip()
        ipaddr = request.args['ipaddr'][0].strip()
        actiontype = request.args['action'][0]
        if not gameid.isalnum():
            request.setResponseCode(500)
            logger.log(logging.INFO,
                       "%s Bad data %s %s",
                       address, gameid, ipaddr)
            return "Bad data"

        # This strips the region identifier from game IDs, not sure if this
        # actually always accurate but limited testing suggests it is
        if len(gameid) > 3:
            gameid = gameid[:-1]

        if actiontype == 'ban':
            dbconn.cursor().execute(
                'INSERT INTO banned VALUES(?,?)',
                (gameid, ipaddr)
            )
            responsedata = "Added gameid=%s, ipaddr=%s" % (gameid, ipaddr)
        else:
            dbconn.cursor().execute(
                'DELETE FROM banned WHERE gameid=? AND ipaddr=?',
                (gameid, ipaddr)
            )
            responsedata = "Removed gameid=%s, ipaddr=%s" % (gameid, ipaddr)
        dbconn.commit()
        dbconn.close()
        logger.log(logging.INFO, "%s %s", address, responsedata)
        request.setHeader("Content-Type", "text/html; charset=utf-8")

        referer = request.getHeader('referer')
        if not referer:
            referer = "/banhammer"
        request.setHeader("Location", referer)

        request.setResponseCode(303)
        return responsedata

    def update_consolelist(self, request):
        address = request.getClientIP()
        dbconn = sqlite3.connect('gpcm.db')
        macadr = request.args['macadr'][0].strip()
        actiontype = request.args['action'][0]
        if not macadr.isalnum():
            request.setResponseCode(500)
            logger.log(logging.INFO, "%s Bad data %s", address, macadr)
            return "Bad data"
        if actiontype == 'add':
            dbconn.cursor().execute(
                'INSERT INTO pending VALUES(?)',
                (macadr,)
            )
            dbconn.cursor().execute(
                'INSERT INTO registered VALUES(?)',
                (macadr,)
            )
            responsedata = "Added macadr=%s" % (macadr)
        elif actiontype == 'activate':
            dbconn.cursor().execute(
                'INSERT INTO registered VALUES(?)',
                (macadr,)
            )
            responsedata = "Activated console belonging to %s" % (macadr)
        else:
            dbconn.cursor().execute(
                'DELETE FROM pending WHERE macadr=?',
                (macadr,)
            )
            dbconn.cursor().execute(
                'DELETE FROM registered WHERE macadr=?',
                (macadr,)
            )
            responsedata = "Removed macadr=%s" % (macadr)
        dbconn.commit()
        dbconn.close()
        logger.log(logging.INFO, "%s %s", address, responsedata)
        request.setHeader("Content-Type", "text/html; charset=utf-8")
        request.setHeader("Location", "/consoles")
        referer = request.getHeader('referer')
        request.setResponseCode(303)
        if not referer:
            referer = "/banhammer"
        request.setHeader("Location", referer)

        request.setResponseCode(303)
        return responsedata

    def render_banlist(self, request):
        address = request.getClientIP()
        dbconn = sqlite3.connect('gpcm.db')
        logger.log(logging.INFO, "%s Viewed banlist", address)
        responsedata = """
        <a href="http://%%20:%%20@%s">[CLICK HERE TO LOG OUT]</a>
        <table border='1'>
        <tr>
            <td>gameid</td>
            <td>ipAddr</td>
        </tr>""" % (request.getHeader('host'))

        for row in dbconn.cursor().execute("SELECT * FROM banned"):
            gameid = str(row[0])
            ipaddr = str(row[1])
            # TODO: Use .format()/positional arguments
            responsedata += """
            <tr>
                <td>%s</td>
                <td>%s</td>
                <td>
                <form action='updatebanlist' method='POST'>
                    <input type='hidden' name='gameid' value='%s'>
                    <input type='hidden' name='ipaddr' value='%s'>
                    <input type='hidden' name='action' value='unban'>
                    <input type='submit' value='----- UNBAN -----'>
                </form>
                </td>
            </tr>""" % (gameid, ipaddr, gameid, ipaddr)

        responsedata += "</table>"
        dbconn.close()
        request.setHeader("Content-Type", "text/html; charset=utf-8")
        return responsedata

    def render_not_available(self, request):
        request.setResponseCode(403)
        request.setHeader('WWW-Authenticate', 'Basic realm="ALTWFC"')
        request.write('No admin credentials set. Admin page is not available.')

    def render_blacklist(self, request):
        sqlstatement = """
        SELECT users.profileid, enabled, data, users.gameid, console,
               users.userid
        FROM nas_logins
        INNER JOIN users
        ON users.userid = nas_logins.userid
        INNER JOIN (
            SELECT max(profileid) newestpid, userid, gameid, devname
            FROM users
            GROUP BY userid, gameid
        ) ij
        ON ij.userid = users.userid
        AND users.profileid = ij.newestpid
        ORDER BY users.gameid"""
        dbconn = sqlite3.connect('gpcm.db')
        banned_list = []
        for row in dbconn.cursor().execute("SELECT * FROM BANNED"):
            banned_list.append(str(row[0])+":"+str(row[1]))
        responsedata = """
        <a href="http://%%20:%%20@%s">[CLICK HERE TO LOG OUT]</a>
        <br><br>
        <table border='1'>"
        <tr>
            <td>ingamesn or devname</td>
            <td>gameid</td>
            <td>Enabled</td>
            <td>newest dwc_pid</td>"
            <td>gsbrcd</td>
            <td>userid</td>
            <td>ipAddr</td>
        </tr>""" % request.getHeader('host')

        for row in dbconn.cursor().execute(sqlstatement):
            dwc_pid = str(row[0])
            enabled = str(row[1])
            nasdata = collections.defaultdict(lambda: '', json.loads(row[2]))
            gameid = str(row[3])
            is_console = int(str(row[4]))
            userid = str(row[5])
            gsbrcd = str(nasdata['gsbrcd'])
            ipaddr = str(nasdata['ipaddr'])
            ingamesn = ''
            if 'ingamesn' in nasdata:
                ingamesn = str(nasdata['ingamesn'])
            elif 'devname' in nasdata:
                ingamesn = str(nasdata['devname'])
            if ingamesn:
                ingamesn = gs_utils.base64_decode(ingamesn)
                if is_console:
                    ingamesn = codecs.utf_16_be_decode(ingamesn)[0]
                else:
                    ingamesn = codecs.utf_16_le_decode(ingamesn)[0]
            else:
                ingamesn = '[NOT AVAILABLE]'
            responsedata += """
            <tr>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
            """ % (ingamesn,
                   gameid,
                   enabled,
                   dwc_pid,
                   gsbrcd,
                   userid,
                   ipaddr)
            if gameid[:-1] + ":" + ipaddr in banned_list:
                responsedata += """
                    <td>
                    <form action='updatebanlist' method='POST'>
                        <input type='hidden' name='gameid' value='%s'>
                        <input type='hidden' name='ipaddr' value='%s'>
                        <input type='hidden' name='action' value='unban'>
                        <input type='submit' value='----- unban -----'>
                    </form>
                    </td>
                </tr>""" % (gameid, ipaddr)
            else:
                responsedata += """
                    <td>
                    <form action='updatebanlist' method='POST'>
                        <input type='hidden' name='gameid' value='%s'>
                        <input type='hidden' name='ipaddr' value='%s'>
                        <input type='hidden' name='action' value='ban'>
                        <input type='submit' value='Ban'>
                    </form>
                    </td>
                </tr>
                """ % (gameid, ipaddr)

        responsedata += "</table>"
        dbconn.close()
        request.setHeader("Content-Type", "text/html; charset=utf-8")
        return responsedata.encode('utf-8')

    def enable_disable_user(self, request, enable=True):
        address = request.getClientIP()
        responsedata = ""
        userid = request.args['userid'][0]
        gameid = request.args['gameid'][0].upper()
        ingamesn = request.args['ingamesn'][0]

        if not userid.isdigit() or not gameid.isalnum():
            logger.log(logging.INFO,
                       "%s Bad data %s %s",
                       address, userid, gameid)
            return "Bad data"

        dbconn = sqlite3.connect('gpcm.db')
        if enable:
            dbconn.cursor().execute(
                'UPDATE users SET enabled=1 '
                'WHERE gameid=? AND userid=?',
                (gameid, userid)
            )
            responsedata = "Enabled %s with gameid=%s, userid=%s" % \
                           (ingamesn, gameid, userid)
        else:
            dbconn.cursor().execute(
                'UPDATE users SET enabled=0 '
                'WHERE gameid=? AND userid=?',
                (gameid, userid)
            )
            responsedata = "Disabled %s with gameid=%s, userid=%s" % \
                           (ingamesn, gameid, userid)
        dbconn.commit()
        dbconn.close()
        logger.log(logging.INFO, "%s %s", address, responsedata)
        request.setHeader("Content-Type", "text/html; charset=utf-8")
        request.setHeader("Location", "/banhammer")
        request.setResponseCode(303)
        return responsedata

    def render_consolelist(self, request):
        address = request.getClientIP()
        dbconn = sqlite3.connect('gpcm.db')
        active_list = []
        for row in dbconn.cursor().execute("SELECT * FROM REGISTERED"):
            active_list.append(str(row[0]))
        logger.log(logging.INFO, "%s Viewed console list", address)
        responsedata = (
            '<a href="http://%20:%20@' + request.getHeader('host') +
            '">[CLICK HERE TO LOG OUT]</a>'
            "<form action='updateconsolelist' method='POST'>"
            "macadr:<input type='text' name='macadr'>\r\n"
            "<input type='hidden' name='action' value='add'>\r\n"
            "<input type='submit' value='Register and activate console'>"
            "</form>\r\n"
            "<table border='1'>"
            "<tr><td>macadr</td></tr>\r\n"
        )
        for row in dbconn.cursor().execute("SELECT * FROM pending"):
            macadr = str(row[0])
            if macadr in active_list:
                responsedata += """
                <tr>
                    <td>%s</td>
                    <td>
                    <form action='updateconsolelist' method='POST'>
                        <input type='hidden' name='macadr' value='%s'>
                        <input type='hidden' name='action' value='remove'>
                        <input type='submit' value='Un-register console'>
                    </form>
                    </td>
                </tr>""" % (macadr, macadr)
            else:
                responsedata += """
                <tr>
                    <td>%s</td>
                    <td>
                    <form action='updateconsolelist' method='POST'>
                        <input type='hidden' name='macadr' value='%s'>
                        <input type='hidden' name='action' value='activate'>
                        <input type='submit' value='Activate console'>
                    </form>
                    </td>
                </tr>""" % (macadr, macadr)
        responsedata += "</table>"
        dbconn.close()
        request.setHeader("Content-Type", "text/html; charset=utf-8")
        return responsedata

    def render_GET(self, request):
        if not adminpageconf:
            self.render_not_available(request)
            return ""
        if not self.is_authorized(request):
            return ""

        title = None
        response = ''
        if request.path == "/banlist":
            title = 'NinjaWFC Banned Users'
            response = self.render_banlist(request)
        elif request.path == "/banhammer":
            title = 'NinjaWFC Users'
            response = self.render_blacklist(request)
        elif request.path == "/consoles":
            title = "NinjaWFC Console List"
            response = self.render_consolelist(request)
        return self.get_header(title) + response + self.get_footer()

    def render_POST(self, request):
        if not adminpageconf:
            self.render_not_available(request)
            return ""
        if not self.is_authorized(request):
            return ""

        if request.path == "/updatebanlist":
            return self.update_banlist(request)
        if request.path == "/updateconsolelist":
            return self.update_consolelist(request)
        else:
            return self.get_header() + self.get_footer()


class AdminPageServer(object):
    def start(self):
        site = server.Site(AdminPage(self))
        reactor.listenTCP(port, site)
        logger.log(logging.INFO,
                   "Now listening for connections on port %d...",
                   port)
        try:
            if not reactor.running:
                reactor.run(installSignalHandlers=0)
        except ReactorAlreadyRunning:
            pass


if __name__ == "__main__":
    AdminPageServer().start()