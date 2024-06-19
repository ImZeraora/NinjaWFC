window.onload=function(){
    document.getElementById("search").addEventListener("click",error);
    document.getElementById("header").className="headerslide";
    time();
}

function error(){
    error=document.getElementById("errorinput").value;
    error=document.getElementById("errorinput").value;
    if(error==20000){
        document.getElementById("result").innerHTML=error + ": " + "[NASWII_ERROR_BASE] This error should never appear. Contact ImZeraora on discord!"
    }
    else if(error==20001){
        document.getElementById("result").innerHTML=error + ": " + "[NASWII_ERROR_LOGIN_OK] This error should never appear. Contact ImZeraora on discord!"
    }
    else if(error==20002){
        document.getElementById("result").innerHTML=error + ": " + "[NASWII_ERROR_ACCTCREATE_OK] This error should never appear. Contact ImZeraora on discord!"
    }
    else if(error==20007){
        document.getElementById("result").innerHTML=error + ": " + "[NASWII_ERROR_SVCLOC_OK] This error should never appear. Contact ImZeraora on discord!"
    }
    else if(error==20064){
        document.getElementById("result").innerHTML=error + ": " + "[NASWII_ERROR_PROFANITY] This error should never appear. Contact ImZeraora on discord!"
    }
    else if(error==20100){
        document.getElementById("result").innerHTML=error + ": " + "[NASWII_ERROR_UNKNOWN] Make sure you patched your game correctly. If you think you patched the game correctly and this message still appears, contact ImZeraora on discord!"
    }
    else if(error==23502){
        document.getElementById("result").innerHTML=error + ": " + "[NASWII_ERROR_GAMESPY_MAINTENANCE] This error should never appear. Contact ImZeraora on discord!"
    }
    else if(error==23800){
        document.getElementById("result").innerHTML=error + ": " + "[NASWII_ERROR_DEVICE_BANNED] Your console was banned from the NinjaWFC servers for violating the terms of service. If you think the ban was unjustified, contact ImZeraora on discord!"
    }
    else if(error==23888){
        document.getElementById("result").innerHTML=error + ": " + "[NASWII_ERROR_DEVICE_INVALID] This error should never appear. Contact ImZeraora on discord!"
    }
    else if(error==23913){
        document.getElementById("result").innerHTML=error + ": " + "[NASWII_ERROR_DEVICE_ALREADY_EXISTS] This error should never appear. Contact ImZeraora on discord!"
    }
    else if(error==23914){
        document.getElementById("result").innerHTML=error + ": " + "[NASWII_ERROR_DEVICE_NOT_FOUND] This error should never appear. Contact ImZeraora on discord!"
    }
    else if(error==23917){
        document.getElementById("result").innerHTML=error + ": " + "[NASWII_ERROR_MAX_USER_COUNT_EXCEEDED] This error should never appear. Contact ImZeraora on discord!"
    }
    else if(error==23921){
        document.getElementById("result").innerHTML=error + ": " + "[NASWII_ERROR_GAME_NOT_SUPPORTED] This error should never appear. Contact ImZeraora on discord!"
    }
    else if(error>=51300 && error<=51399){
        document.getElementById("result").innerHTML=error + ": " + "[NASWII_ERROR_USER_DELETED] This error should never appear. Contact ImZeraora on discord!"
    }
    else if(error>=52100 && error<=52103){
        document.getElementById("result").innerHTML=error + ": " + "[NASWII_ERROR_GAME_INVALID] This error should never appear. Contact ImZeraora on discord!" 
    }
    else if(error>=52200 && error<=52203){
        document.getElementById("result").innerHTML=error + ": " + "[NASWII_ERROR_GAME_DISCONTINUED] This error should never appear. Contact ImZeraora on discord!"
    }
    else if(error==60000){
        document.getElementById("result").innerHTML=error + ": " + "[WL_ERROR_PAYLOAD_OK] This error should never appear. Contact ImZeraora on discord!"
    }
    else if(error==61010){
        document.getElementById("result").innerHTML=error + ": " + "[WL_ERROR_PAYLOAD_STAGE0_MISSING_STAGE1] This error should never appear. Contact ImZeraora on discord!"  
    }
    else if(error==61020){
        document.getElementById("result").innerHTML=error + ": " + "[WL_ERROR_PAYLOAD_STAGE0_HASH_MISMATCH] This error should never appear. Contact ImZeraora on discord!"
    }
    else if(error==61070){
        document.getElementById("result").innerHTML=error + ": " + "[WL_ERROR_PAYLOAD_STAGE1_ALLOC] This error should never appear. Contact ImZeraora on discord!"
    }
    else if(error==84020){
        document.getElementById("result").innerHTML=error + ": " + "[WL_ERROR_PAYLOAD_STAGE1_MAKE_REQUEST] This error should never appear. Contact ImZeraora on discord!"
    }
    else if(error==85030){
        document.getElementById("result").innerHTML=error + ": " + "[WL_ERROR_PAYLOAD_STAGE1_RESPONSE] This error should never appear. Contact ImZeraora on discord!" 
    }
    else if(error==86420){
        document.getElementById("result").innerHTML=error + ": " + "[WL_ERROR_PAYLOAD_STAGE1_HEADER_CHECK] This error should never appear. Contact ImZeraora on discord!" 
    }
    else if(error==91010){
        document.getElementById("result").innerHTML=error + ": " + "[WL_ERROR_PAYLOAD_STAGE1_LENGTH_ERROR] This error should never appear. Contact ImZeraora on discord!"
    }
    else if(error==94020){
        document.getElementById("result").innerHTML=error + ": " + "[WL_ERROR_PAYLOAD_STAGE1_SALT_MISMATCH] This error should never appear. Contact ImZeraora on discord!"
    }
    else if(error==95020){
        document.getElementById("result").innerHTML=error + ": " + "[WL_ERROR_PAYLOAD_STAGE1_GAME_ID_MISMATCH] This error should never appear. Contact ImZeraora on discord!" 
    }
    else if(error==98020){
        document.getElementById("result").innerHTML=error + ": " + "[WL_ERROR_PAYLOAD_STAGE1_SIGNATURE_INVALID] This error should never appear. Contact ImZeraora on discord!"
    }
    else if(error==98020){
        document.getElementById("result").innerHTML=error + ": " + "[WL_ERROR_PAYLOAD_STAGE1_WAITING] This error should never appear. Contact ImZeraora on discord!"
    }
    else if(error==98020){
        document.getElementById("result").innerHTML=error + ": " + "[WL_ERROR_PAYLOAD_GAME_MISMATCH] This error should never appear. Contact ImZeraora on discord!"
    }
    else{
        document.getElementById("result").innerHTML="This error does not exist. If you recieved this error message, please contact ImZeraora on discord." 
    }
}
