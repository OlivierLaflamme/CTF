# otwadvent2018


Title                         | Category     | Points   | Flag
----------------------------- | ------------ | -------  | ---------------------------------------
EasterEgg1		      | web	     |50	|AOTW{D0ra_th3_haxxpl0rer}
EasterEgg2		      |web	     |50	|AOTW{Jingle_All_The_Way!!!1}
Lostpresent		      |pwn	     |200	|AOTW{SanT4zLiT7L3xm4smag1c}





## EasterEgg1 (web/bonus 50)

go to robots.txt

![Image 1](https://github.com/ScripTeaseCTF/CTF/blob/master/otwadvent2018/images/1.PNG)

then go to static/__s3cret.txt and scroll to bottom of the page 

![Image 1](https://github.com/ScripTeaseCTF/CTF/blob/master/otwadvent2018/images/2.PNG) 
    
![Image 1](https://github.com/ScripTeaseCTF/CTF/blob/master/otwadvent2018/images/3.PNG)


flag is therefore

AOTW{D0ra_th3_haxxpl0rer}


## EasterEgg2 (web/bonus 50)

go to /static/js/app.js 


	...
	if(lockedcount != $scope.lockedCount) {
	  if($scope.lockedCount != -1) {
	        if(localStorage.getItem("gfx") != 2) {
		    var audio = new Audio('/static/audio/santabells.mp3');
		    audio.play();
		    $scope.showsanta = true;
			$("#santa").html(atob("PHA+QU9UV3tKaW5nbGVfQWxsX1RoZV9XYXkhISExfTwvcD4="));
		    console.log("GFX enabled");
		} else {
		    console.log("GFX disabled");
		}
		console.log("Detected new unlocked challenges");
	  }
	  $scope.lockedCount = lockedcount;
	...

base64 decode "PHA+QU9UV3tKaW5nbGVfQWxsX1RoZV9XYXkhISExfTwvcD4"

and you obtaine the flag worth 50 points 

AOTW{Jingle_All_The_Way!!!1}

## Lostpresent (pwn/misc 200)

ssh to ssh -p 1211 shelper@3.81.191.176

the password is >>> shelper

![Image 1](https://github.com/ScripTeaseCTF/CTF/blob/master/otwadvent2018/images/4.PNG)

lets enumerate all binaries having SUID permission.

![Image 1](https://github.com/ScripTeaseCTF/CTF/blob/master/otwadvent2018/images/6.PNG)

we can use sudo, good. and by the looks of it /home/santa looks very promising. now we have very few sudo allowed commands. however, we can obtain the flag using the find command as seen below 


![Image 1](https://github.com/ScripTeaseCTF/CTF/blob/master/otwadvent2018/images/5.PNG)

AOTW{SanT4zLiT7L3xm4smag1c}
