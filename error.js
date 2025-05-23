window.onload=function(){
    document.getElementById("search").addEventListener("click",error);
    document.getElementById("header").className="headerslide";
    time();
}

function error(){
    error=document.getElementById("errorinput").value;
    error=document.getElementById("errorinput").value;
    if(error==22001){
        document.getElementById("result").innerHTML=error + ": " + "An additional step is required to play this game on NinjaWFC! Contact ImZeraora on discord!"
    }
    else if(error >= 22002 && error <= 22003){
        document.getElementById("result").innerHTML=error + ": " + "You have been banned from NinjaWFC."
    }
    else if(error==22004){
        document.getElementById("result").innerHTML=error + ": " + "You were kicked from NinjaWFC by a server moderator."
    }
    else if(error >= 22005 && error <= 22006){
        document.getElementById("result").innerHTML=error + ": " + "The console you are using is not the device this profile was made on. Please try creating a new profile."
    }
    else if(error==22007){
        document.getElementById("result").innerHTML=error + ": " + "The friend code you're trying to use is already in use by another player! Please create a new profile!"
    }
    else if(error==22008){
        document.getElementById("result").innerHTML=error + ": " + "The payload sent by NinjaWFC is invalid. Try restarting your game, if that does not work, message ImZeraora on discord!"
    }
    else if(error==22009){
        document.getElementById("result").innerHTML=error + ": " + "You were banned from NinjaWFC for having an invalid VR/BR amount. VR/BR must be with 1-32767!"
    }
    else if(error==20000){
        document.getElementById("result").innerHTML=error + ": " + "[NASWII_ERROR_BASE] This error should never appear. Contact ImZeraora on discord!"
    }
    else if(error==20001){
        document.getElementById("result").innerHTML=error + ": " + "[NASWII_ERROR_LOGIN_OK] This error should never appear. Contact ImZeraora on discord!"
    }
    else if(error==20003){
        document.getElementById("result").innerHTML=error + ": " + "[NASWII_ERROR_ACCTCREATE_OK] This error should never appear. Contact ImZeraora on discord!"
    }
    else if(error==20007){
        document.getElementById("result").innerHTML=error + ": " + "[NASWII_ERROR_SVCLOC_OK] This error should never appear. Contact ImZeraora on discord!"
    }
    else if(error==20064){
        document.getElementById("result").innerHTML=error + ": " + "[NASWII_ERROR_PROFANITY] This error should never appear. Contact ImZeraora on discord!"
    }
    else if(error==20100){
        document.getElementById("result").innerHTML=error + ": " + "[NASWII_ERROR_UNKNOWN] Make sure your device is connected to the internet. If your device is connected to the internet, This error should never appear. Contact ImZeraora on discord!"
    }
    else if(error>=20101){
        document.getElementById("result").innerHTML=error + ": " + "[NASWII_ERROR_GAMESPY_MAINTENANCE] This error should never appear. Contact ImZeraora on discord!"
    }
    else if(error>=20103){
        document.getElementById("result").innerHTML=error + ": " + "[NASWII_ERROR_DEVICE_INVALID‎] This error should never appear. Contact ImZeraora on discord!" 
    }
    else if(error>=20104){
        document.getElementById("result").innerHTML=error + ": " + "[NASWII_ERROR_DEVICE_ALREADY_EXISTS] This error should never appear. Contact ImZeraora on discord!"
    }
    else if(error==0){
        document.getElementById("result").innerHTML=error + ": " + "[WL_ERROR_PAYLOAD_OK] This error should never appear. Contact ImZeraora on discord!"
    }
    else if(error==20901){
        document.getElementById("result").innerHTML=error + ": " + "[WL_ERROR_PAYLOAD_STAGE0_MISSING_STAGE1] This error should never appear. Contact ImZeraora on discord!"  
    }
    else if(error==20902){
        document.getElementById("result").innerHTML=error + ": " + "[WL_ERROR_PAYLOAD_STAGE0_HASH_MISMATCH] This error should never appear. Contact ImZeraora on discord!"
    }
    else if(error==20910){
        document.getElementById("result").innerHTML=error + ": " + "[WL_ERROR_PAYLOAD_STAGE1_ALLOC] This error should never appear. Contact ImZeraora on discord!"
    }
    else if(error==20911){
        document.getElementById("result").innerHTML=error + ": " + "[WL_ERROR_PAYLOAD_STAGE1_MAKE_REQUEST] This error should never appear. Contact ImZeraora on discord!"
    }
    else if(error==20912){
        document.getElementById("result").innerHTML=error + ": " + "[WL_ERROR_PAYLOAD_STAGE1_RESPONSE] This error should never appear. Contact ImZeraora on discord!" 
    }
    else if(error==20913){
        document.getElementById("result").innerHTML=error + ": " + "[WL_ERROR_PAYLOAD_STAGE1_HEADER_CHECK] This error should never appear. Contact ImZeraora on discord!" 
    }
    else if(error==20914){
        document.getElementById("result").innerHTML=error + ": " + "[WL_ERROR_PAYLOAD_STAGE1_LENGTH_ERROR] This error should never appear. Contact ImZeraora on discord!"
    }
    else if(error==20915){
        document.getElementById("result").innerHTML=error + ": " + "[WL_ERROR_PAYLOAD_STAGE1_SALT_MISMATCH] This error should never appear. Contact ImZeraora on discord!"
    }
    else if(error==20916){
        document.getElementById("result").innerHTML=error + ": " + "[WL_ERROR_PAYLOAD_STAGE1_GAME_ID_MISMATCH] This error should never appear. Contact ImZeraora on discord!" 
    }
    else if(error==20917){
        document.getElementById("result").innerHTML=error + ": " + "[WL_ERROR_PAYLOAD_STAGE1_SIGNATURE_INVALID] This error should never appear. Contact ImZeraora on discord!"
    }
    else if(error==20918){
        document.getElementById("result").innerHTML=error + ": " + "[WL_ERROR_PAYLOAD_STAGE1_WAITING] This error should never appear. Contact ImZeraora on discord!"
    }
    else if(error==20930){
        document.getElementById("result").innerHTML=error + ": " + "[WL_ERROR_PAYLOAD_GAME_MISMATCH] This error should never appear. Contact ImZeraora on discord!"
    }
    else{
        document.getElementById("result").innerHTML="This error does not exist. If you recieved this error message, please contact ImZeraora on discord." 
    }
}
