window.onload=function(){
    document.getElementById("search").addEventListener("click",error)
}

function error(){
    error=document.getElementById("errorinput").value;
    error=document.getElementById("errorinput").value;
    if(error==20100){
        document.getElementById("result").innerHTML=error + ": " + "Connection to the Access Point succeeded, but connection to the Wi-Fi Connection servers couldn't be established. Either you forgot to set the DNS and are trying to connect to the now-defunct official servers, or the custom server is currently down for maintenance. May also be a result of not properly patching your game to remove the SSL checks."
    }
    else if(error==23302){
        document.getElementById("result").innerHTML=error + ": " + "You're connected on a browser-login based Wifi, but the Wifi redirected you because you need to re-sign back into the Wifi (this usally refers to Hotel/Airport Wifi). Resign back into the Wifi and reconnect, error code should go away."
    }
    else if(error==23400){
        document.getElementById("result").innerHTML=error + ": " + "Apache Security is not allowing Whitespace. To server admins: Add this to your apache2.conf file - HttpProtocolOptions Unsafe"
    }
    else if(error==23403){
        document.getElementById("result").innerHTML=error + ": " + "This only occurs if you have multiple Nginx Server Blocks with one of them having a SSL cert and the SSL cert is blocking the naswii connection."
    }
    else if(error==23404){
        document.getElementById("result").innerHTML=error + ": " + "Internal server error - To server admins: This usually means that Apache's virtual hosts aren't found on the server (or if nas_server.py is using port 80 when Apache is also using it) - naswii is returning HTTP 404"
    }
    else if(error==23500){
        document.getElementById("result").innerHTML=error + ": " + "Internal server error - To server admins: This might mean you haven't enabled Apache's proxy modules. On Ubuntu, try running sudo a2enmod proxy*"
    }
    else if(error==23502){
        document.getElementById("result").innerHTML=error + ": " + "Game server offline but reachable outside of game (i.e web server is up)"
    }
    else if(error==23800){
        document.getElementById("result").innerHTML=error + ": " + "Game not supported on your desired server. Some servers restrict what games are allowed. You must contact the server owner to determine what games are officially supported. You may also consult the List of Servers page."
    }
    else if(error==23888){
        document.getElementById("result").innerHTML=error + ": " + "Console registered successfuly - awaiting activation. Some servers may have this feature enabled as a defence mechanism to thwart abusive users from circumventing bans. It may take 24 hours or longer for your console to activate. This is a MANUAL activation process, and is not automatic."
    }
    else if(error==23913){
        document.getElementById("result").innerHTML=error + ": " + "User ID creation denied because you are a banned user."
    }
    else if(error==23914){
        document.getElementById("result").innerHTML=error + ": " + "You have been banned from NinjaWFC servers."
    }
    else if(error==23917){
        document.getElementById("result").innerHTML=error + ": " + "You have been banned from NinjaWFC servers."
    }
    else if(error==23921){
        document.getElementById("result").innerHTML=error + ": " + "This error should never appear, please contact NinjaKing#2527 on discord."
    }
    else if(error>=51300 && error<=51399){
        document.getElementById("result").innerHTML=error + ": " + "The console is unable to connect to the access point. Double-check the settings and try again."
    }
    else if(error>=52100 && error<=52103){
        document.getElementById("result").innerHTML=error + ": " + "The console can't contact the server. It could be a problem with your internet or the server could be temporarily offline." 
    }
    else if(error>=52200 && error<=52203){
        document.getElementById("result").innerHTML=error + ": " + "This error seems to appear when attempting to connect to the server multiple times without properly disconnecting first. Reboot your console and try again."
    }
    else if(error==60000){
        document.getElementById("result").innerHTML=error + ": " + "Error relating to your user profile. Most likely, you're trying to connect to the custom server using save data that still has your Friend Code from the official server stored in it. On the DS, you should be able to fix this by deleting your NWFC Configuration, on the Wii you either have to delete your save file for the game you're trying to connect with or manually remove friend code information by editing your save file. This may improve in the future."
    }
    else if(error==61010){
        document.getElementById("result").innerHTML=error + ": " + "Game Unsupported. This usually means that the game the user is trying to play isn't whitelisted on your server."  
    }
    else if(error==61020){
        document.getElementById("result").innerHTML=error + ": " + "Profile Server unreachable. Probably not a problem on your end."
    }
    else if(error==61070){
        document.getElementById("result").innerHTML=error + ": " + "Profile Server unreachable."
    }
    else if(error==84020){
        document.getElementById("result").innerHTML=error + ": " + "QR Server unreachable. Probably not a problem on your end."
    }
    else if(error==85030){
        document.getElementById("result").innerHTML=error + ": " + "You were suddenly disconnected from your accesspoint. Check if your router is still online and reachable." 
    }
    else if(error==86420){
        document.getElementById("result").innerHTML=error + ": " + "A direct connection was attempted with another player but the connection failed. Possible reasons could be firewall, ports or latency." 
    }
    else if(error==91010){
        document.getElementById("result").innerHTML=error + ": " + "The server has been shut down or restarted for maintenance. This error can also mean you were kicked from the server"
    }
    else if(error==94020){
        document.getElementById("result").innerHTML=error + ": " + "This error should never appear on NinjaWFC. Please message NinjaKing#2527 on discord."
    }
    else if(error==95020){
        document.getElementById("result").innerHTML=error + ": " + "Server hiccuped when trying to connect you to a WW. Reconnect and try again. This can also mean that the server needs to restart, if this problem remains, please contact NinjaKing#2527 on discord." 
    }
    else if(error==98020){
        document.getElementById("result").innerHTML=error + ": " + "The gamestats server is not implemented. If you have well-documented packet captures from the official WFC, you should file an issue with them and perhaps a volunteer programmer can implement it. For the time being, the game is unsupported."
    }
    else{
        document.getElementById("result").innerHTML="This error does not exist." 
    }
}