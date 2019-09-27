# BlueWhale CTF


Title                         	| Category     | Points   | Flag
------------------------------- | ------------ | -------  | ---------------------------------------
unzip  		      				|Forensics	   |50		  | picoCTF{unz1pp1ng_1s_3a5y}
Glory of the Garden  		    |Forensics	   |50		  | picoCTF{more_than_m33ts_the_3y3DBce41ae}
So Meta				  		    |Forensics	   |150		  | picoCTF{s0_m3ta_7ce44fc5}
What Lies Within				|Forensics	   |150		  | picoCTF{h1d1ng_1n_th3_b1t5}
Extensions	(first Blood)		|Forensics	   |150		  | picoCTF{now_you_know_about_extensions}
like 1000 	(2nd blood :(		|Forensics	   |250		  | picoCTF{l0t5_0f_TAR5}
shark on wire 1					|Forensics	   |150		  | picoCTF{StaT31355_636f6e6e}


## unzip (Forensics/50)
unzip the image and open it in 29a.ch  
https://29a.ch/photo-forensics/#forensic-magnifier  
voila~!     
![](https://github.com/OlivierLaflamme/CTF/blob/master/picoCTF2019/images/unzip.PNG)  
picoCTF{unz1pp1ng_1s_3a5y}  

## Glory of the Garden (Forensics/50)   
flag is hidden so do a simple string extraction...   
picoCTF{more_than_m33ts_the_3y3DBce41ae}    
 
## So Meta (Forensics/150)    
again flag is hidden so do a simple string extraction...   
picoCTF{s0_m3ta_7ce44fc5}  
  
## What Lies Within (Forensics/150)  
use zsteg to find a decoding   
![](https://github.com/OlivierLaflamme/CTF/blob/master/picoCTF2019/images/whatlieswithin.PNG)   
picoCTF{h1d1ng_1n_th3_b1t5}     

## Extensions (Forensics/150)   
open the file looks like a png and its not currupted, so rename and open   
![](https://github.com/OlivierLaflamme/CTF/blob/master/picoCTF2019/images/extensions.PNG)    
picoCTF{now_you_know_about_extensions}  

## like 1000 (Forensics/250)
I really wanted to get the 1st blood for this so i didnt write a bash script i simply used an autoclicker and took 20 seconds   
but i know i should have used something like the well known 'extractnested.py' script pip install nested.tar.archives.extractor==1.1    
![](https://github.com/OlivierLaflamme/CTF/blob/master/picoCTF2019/images/like1000.PNG)    
picoCTF{l0t5_0f_TAR5}   

## shark on wire 1 (Forensics/150)
open in wireshark and 'udp.stream eq 6' follow the UDP stream and voila  
picoCTF{StaT31355_636f6e6e}  




