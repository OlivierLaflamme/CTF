# nactf
## Notice I did solve more challenges but these are only the ones that I care about logging   

Title                         	| Category     | Points   | Flag
------------------------------- | ------------ | -------  | ---------------------------------------
Least Significant Avenger  		|Forensics	   |50		  |nactf{h4wk3y3_15_th3_l34st_51gn1f1c4nt_b1t}
The Meta Meme					|Forensics 	   |75		  |nactf{d4mn_th15_1s_s0_m3t4}
Unzip Me						|Forensics 	   |150		  |nactf{w0w_y0u_unz1pp3d_m3}
Kellen's Broken File			|Forensics	   |150 	  |nactf{kn0w_y0ur_f1l3_h34d3rsjeklwf}
Kellen's PDF sandwich			|Forensics	   |150		  |?? nacntf{w3_l0lcv_rd_0f_t4nk5ejwjfae}
Filesystem Image				|Forensics     |200		  |nactf{lqwkzopyhu}
Scooby Doo 						|Web		   |100		  |nactf{uIt1m4T3_sh4ggY}
Sesame Street					|Web		   |150		  |nactf{c000000000ki3s}
Get a GREP #0!					|General 	   |100 	  |nactf{v1kram_and_h1s_10000_l3av3s}
Get a GREP #1!					|General	   |125		  |nactf{r3gul4r_3xpr3ss10ns_ar3_m0r3_th4n_r3gul4r_euaiooa}

## Least Significant Avenger  
Title suggests LSB so lets zsteg to see  
![](https://github.com/ScripTeaseCTF/CTF/blob/master/NewarkAcademyCTF2019/images/avenger.PNG)   
nactf{h4wk3y3_15_th3_l34st_51gn1f1c4nt_b1t}  

## The Meta Meme
Its a pdf and the title suggests metadata sooo...  
![](https://github.com/ScripTeaseCTF/CTF/blob/master/WhaleCTF/images/meta.PNG)  
nactf{d4mn_th15_1s_s0_m3t4}  

## Unzip Me 
![](https://github.com/ScripTeaseCTF/CTF/blob/master/WhaleCTF/images/unzipme.PNG)  
zip1.zip had: nactf{w0w  
zip2.zip had: _y0u_unz1pp  
zip3.zip had: 3d_m3}  
Together they make nactf{w0w_y0u_unz1pp3d_m3}  

## Kellen's Broken File  
So this file wasnt broken for me at all i could open it and read the flag 
![](https://github.com/ScripTeaseCTF/CTF/blob/master/WhaleCTF/images/kellens.PNG)   
but im assuming i'd have had to do something like   
pdftocairo -pdf Kellens_broken_file.pdf KellensFixed.pdf   ???? 
meh who cares   
nactf{kn0w_y0ur_f1l3_h34d3rsjeklwf}   

## Kellen's PDF sandwich
the title is fairly subjective so binwalk that shit and you'll see a png inside a png... 
i couldnt dd it...  
```bash
dd if=MeltedFile.pdf bs=1 skip=220 of=answer.pdf 
```
```bash
foremost -i MeltedFile.pdf
``` 
you get a file 0000.png containing the second part of the flag and the first part was in the original pdf  
_0f_t4nk5ejwjfae}  
now the original part was nacntf{w3_l0lcv_rd  
so if you combine it, it should be...   
nacntf{w3_l0lcv_rd_0f_t4nk5ejwjfae} but its not fuck sakes it will be like "we love world of tanks"  


## Filesystem Image
mount it and use the tree command, scroll down and find the flag.txt  
path will be lq/wk/zo/py/hu/flag.txt and submit the flag according to the defined scope   
nactf{lqwkzopyhu}


## Scooby Doo
this was actually funny to solve bacause you can simply change the CSS opacity of the images and get the flag that way..  
But lets do it the right way change the javascript counter and click once to make it pass required 
![](https://github.com/ScripTeaseCTF/CTF/blob/master/WhaleCTF/images/doo1.PNG)    
and voila   
![](https://github.com/ScripTeaseCTF/CTF/blob/master/WhaleCTF/images/doo2.PNG)      


## Sesame Street
pretty simple the cookie is unix time change that to after the date of avail flag and voila  
![](https://github.com/ScripTeaseCTF/CTF/blob/master/WhaleCTF/images/street.PNG)    
reload the page and you have your flag   
nactf{c000000000ki3s}   

## Get a GREP #0!
```bash
tree | cat * */*/*/* | grep nactf*
```   
nactf{v1kram_and_h1s_10000_l3av3s}  

## Get a GREP #1!	
```bash 
cat flag.txt | egrep [aeiou]{7}\}
```   
nactf{r3gul4r_3xpr3ss10ns_ar3_m0r3_th4n_r3gul4r_euaiooa}
