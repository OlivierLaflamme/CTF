# BlueWhale CTF


Title                         	| Category     | Points   | Flag
------------------------------- | ------------ | -------  | ---------------------------------------
Find me		      				|Web	     |50		|flag:{This_is_s0_simpl3}
Http		 					|Web		 |50		|flag:{Y0u_ar3_s0_Car3ful}
Find		     			 	|Stego	     |50		|flag{hctf_3xF$235#\x5e3}
I was eaten by me		      	|Stego	     |50		|flag{WelcomeT3WhaleCTF}
subspecies						|Stego 		 |50 		|flag{firsttry}
Rainy day						|Stego		 |50 		|GUETCTF{Y0u_sEE_m3}
what is this 					|Stego 		 |100 		|flag{pE3kQzmaMN}
Fit whale						|Stego		 |50		|flag{youfindmeWHALE}
Angry ping 						|Stego 		 |100 		|flag{AppLeU0}
Negative film					|Stego 		 |100		|key_is_SimCTF{LSB_yinxie}
Lowest kiss						|Stego		 |150		|flag{i love u}
IHDR 							|Stego 		 |100 		|FLAG{ihDR_ALSO_FUN}
Really moving 					|Stego		 |100		|key{catch_the_dynamic_flag_is_quite_simple}
Blurred picture 				|Stego		 |100		|flag{At10ISCC421ZLAPL}
Error Compression				|Stego 		 |150		|SCTF{(121.518549,25.040854)}
Prom partner 					|Stego		 |200		|flag{f524415e198cbc8983ac0bed3d0cbcef}
Cross-eyed eyes 				|Stego		 |200		|ISG{E4sY_StEg4n0gR4pHy}

![](https://github.com/ScripTeaseCTF/CTF/blob/master/WhaleCTF/images/allsteganosolve.PNG)  

##  Find me (web/ 50)
F12 that thing  
![](https://github.com/ScripTeaseCTF/CTF/blob/master/WhaleCTF/images/findme.PNG)  
flag:{This_is_s0_simpl3}  

## Http (web/ 50)  
![](https://github.com/ScripTeaseCTF/CTF/blob/master/WhaleCTF/images/http.png)  
flag:{Y0u_ar3_s0_Car3ful}  

## Find (Stego/ 50)
flag{hctf_3xF$235#\x5e3}  
![](https://github.com/ScripTeaseCTF/CTF/blob/master/WhaleCTF/images/find.PNG)  

## I was eaten by me (Stego/ 50)
strings whale1.jpg   
binwalk -e whale1.jpg    
![](https://github.com/ScripTeaseCTF/CTF/blob/master/WhaleCTF/images/iwaseatenbyme.png)    
cd _whale1.jpg.extracted  
cat flag.txt  
flag{WelcomeT3WhaleCTF}   


## subspecies (Stego/ 50)  
![](https://github.com/ScripTeaseCTF/CTF/blob/master/WhaleCTF/images/subspecies.png)   
flag{firsttry}   

## Rainy Day (Stego/ 50)
convert Misc01.jpg out.png   
open out-2.png and voila   
![](https://github.com/ScripTeaseCTF/CTF/blob/master/WhaleCTF/images/rainy.PNG)   
GUETCTF{Y0u_sEE_m3}   

## what is this (Stego/ 100)
strings rabbit.jpg   
#102;&#108;&#97;&#103;&#123;&#112;&#69;&#51;&#107;&#81;&#122;&#109;&#97;&#77;&#78;&#125;  
that should look familiar... its ascii so lets convert to text.  
flag{pE3kQzmaMN}  

## Fit Whale (Stego/ 50)
java -jar stegsolve.jar  
analyze frame browser > flag is located on frame 2   
flag{youfindmeWHALE}  

## Angry ping (Stego/ 100)
I used 29a.ch and changed the color component to reveale a QR code      
![](https://github.com/ScripTeaseCTF/CTF/blob/master/WhaleCTF/images/angrypig.PNG)   
scan the QR code w/ wechat 
flag{AppLeU0}

## Negative film	(Stego/ 100)
lets see if we can detect an lsb with zsteg, we can and it gives us the flag nice    
![](https://github.com/ScripTeaseCTF/CTF/blob/master/WhaleCTF/images/negativefilm.png)  
key_is_SimCTF{LSB_yinxie}  

## IHDR (Stego/ 100)
According to the prompt IHDR, it is possible to modify the height, throw in the winhex modified height:  
![](https://github.com/ScripTeaseCTF/CTF/blob/master/WhaleCTF/images/ihdr1.png)  
![](https://github.com/ScripTeaseCTF/CTF/blob/master/WhaleCTF/images/ihdr2.png)  
![](https://github.com/ScripTeaseCTF/CTF/blob/master/WhaleCTF/images/ihdr3.png)  
FLAG{ihDR_ALSO_FUN}

## Really moving (Stego/ 100)
Open with winhex and find the missing file header, add the file header  
![](https://github.com/ScripTeaseCTF/CTF/blob/master/WhaleCTF/images/reallymov1.png)  
then change to the GIF image, use steg to view directly.  
Because some characters may be a bit unclear, you must carefully check    
![](https://github.com/ScripTeaseCTF/CTF/blob/master/WhaleCTF/images/reallymov2.png)  
get the string: Y2F0Y2hfdGhlX2R5bmFtaWNfZmxhZ19pc19xdWl0ZV9zaW1wbGU=  
decode it and you get the flag   
key{catch_the_dynamic_flag_is_quite_simple}  

## Blurred Picture (Stego/ 100)
run it through steghide and see this   
![](https://github.com/ScripTeaseCTF/CTF/blob/master/WhaleCTF/images/blurred1.PNG)  
At10ISCC4_1Z__P_ thats not the flag we're missing something  
```python
#coding:utf-8
import Image
img = Image.open('1.png')
X = img.size[0]
Y = img.size[1]
#print X,Y
for i in range(X-2):
 for j in range(Y-2):
   a = img.getpixel((i,j))[0]+img.getpixel((i,j))[1]+img.getpixel((i,j))[2]
   b = img.getpixel((i,j+1))[0]+img.getpixel((i,j+1))[1]+img.getpixel((i,j+1))[2]
   c = img.getpixel((i,j+2))[0]+img.getpixel((i,j+2))[1]+img.getpixel((i,j+2))[2]
   if (a > b and c > b) or (a < b and c < b):
     pass
   else:
     img.putpixel((i,j),(255,255,255))
img.show()
```
and voila the flag At10ISCC421ZLAPL  
flag{At10ISCC421ZLAPL}  

## Lowest kiss (Stego/ 150)
![](https://github.com/ScripTeaseCTF/CTF/blob/master/WhaleCTF/images/lowestkiss1.png)    
I want to turn the picture into png, then go to stegsolve, the QR code comes out so im shit lazy use the drawing to change the png format  
![](https://github.com/ScripTeaseCTF/CTF/blob/master/WhaleCTF/images/lowestkiss2.png)   
scan and you get the flag  
flag{i love u}  


## Error compression (Stego/ 150)
open in tweakpng   
![](https://github.com/ScripTeaseCTF/CTF/blob/master/WhaleCTF/images/errorcompress1.PNG)  
seems to be a problem, the front is 65524, the latter is a 45027, and there is a 138 behind?  
Why is this 138 not placed in the underfilled 45027? There are problems with these 138 data!  
use hex edditor to take the wav     
![](https://github.com/ScripTeaseCTF/CTF/blob/master/WhaleCTF/images/errorcompress2.PNG)   
take the 138 values in front of the CRC value  
using the zlib module  
```python 
import zlib

s = open('sctf.png', 'rb').read()[0x15AFFB:0x15B085]
data = zlib.decompress(s)
binstr = str(data)
print(binstr)
```
get binstr:
1111111000100001101111111100000101110010110100000110111010100000000010111011011101001000000001011101101110101110110100101110110000010101011011010000011111111010101010101111111000000001011101110000000011010011000001010011101101111010101001000011100000000000101000000001001001101000100111001111011100111100001110111110001100101000110011100001010100011010001111010110000010100010110000011011101100100001110011100100001011111110100000000110101001000111101111111011100001101011011100000100001100110001111010111010001101001111100001011101011000111010011100101110100100111011011000110000010110001101000110001111111011010110111011011

Get a string of 01 strings ~ 01  
assuming the CTF is either ASCII code, of course, this is definitely not possible.  
Or the QR code of 01~ Look at the length of 625, which is exactly the square of 25.  
 
```python
from PIL import Image

s = "1111111000100001101111111100000101110010110100000110111010100000000010111011011101001000000001011101101110101110110100101110110000010101011011010000011111111010101010101111111000000001011101110000000011010011000001010011101101111010101001000011100000000000101000000001001001101000100111001111011100111100001110111110001100101000110011100001010100011010001111010110000010100010110000011011101100100001110011100100001011111110100000000110101001000111101111111011100001101011011100000100001100110001111010111010001101001111100001011101011000111010011100101110100100111011011000110000010110001101000110001111111011010110111011011"

x = 25			#width    
y = 25 			#height    
im = Image.new("RGB", (x, y))   

k = 0
for i in range(0, x):
	for j in range(0, y):
		if(s[k] == '0'):
			im.putpixel((i, j), (255,255,255))    #rgb
		else:
			im.putpixel((i, j), (0,0,0))
		k += 1

im.save("flag.jpg")   #im.save('flag.jpg')
```   
![](https://github.com/ScripTeaseCTF/CTF/blob/master/WhaleCTF/images/errorcompress3.PNG)   
scan and you get the flag  
SCTF{(121.518549,25.040854)}  
 
## Prom partner (Stego/ 200)
Open with winhex and find a lot of ABCD    
![](https://github.com/ScripTeaseCTF/CTF/blob/master/WhaleCTF/images/prom1.PNG)     
We are opening with exiftool    
We see a conspicuous green test in the picture (in combination with the title description) guess A –> upper B –> lower C –> left D –> right  
After testing, it is actually C –> right D –> left The next step is to write the script to first determine the green coordinates  
(find the start coordinate and the end coordinate to find the middle)  

```python
from PIL import Image
import sys
comment = """
^[[A^[[D^[[C^[[A^[[C^[[C^[[B^[[D^[[A^[[A^[[A^[[A^[[D^[[D^[[D^[[C^[[B^[[A^[[B^[[B^[[A^[[C^[[C^[[D^[[C^[[B^[[C^[[D^[[A^[[B^[[A^[[D^[[B^[[C^[[C^[[A^[[B^[[C^[[A^[[D^[[B^[[C^[[C^[[C^[[D^[[D^[[C^[[C^[[B^[[A^[[A^[[C^[[C^[[C^[[D^[[B^[[B^[[C^[[A^[[B^[[A^[[C^[[C^[[C^[[A^[[D^[[D^[[D^[[B^[[A^[[A^[[A^[[D^[[C^[[C^[[C^[[C^[[D^[[A^[[D^[[A^[[D^[[D^[[B^[[C^[[C^[[D^[[B^[[B^[[A^[[A^[[B^[[A^[[A^[[C^[[B^[[A^[[D^[[A^[[D^[[B^[[D^[[D^[[C^[[D^[[D^[[B^[[A^[[D^[[D^[[C^[[A^[[D^[[A^[[C^[[A^[[A^[[B^[[B^[[C^[[A^[[B^[[A^[[D^[[A^[[B^[[C^[[A^[[B^[[D^[[D^[[B^[[C^[[D^[[B^[[A^[[C^[[B^[[B^[[B^[[B^[[D^[[C^[[C^[[C^[[C^[[D^[[B^[[C^[[B^[[B^[[D^[[B^[[A^[[D^[[C^[[A^[[B^[[D^[[D^[[A^[[B^[[D^[[C^[[B^[[B^[[A^[[D^[[A^[[D^[[B^[[C^[[B^[[A^[[D^[[D^[[D^[[B^[[D^[[B^[[C^[[D^[[C^[[D^[[B^[[A^[[A^[[A^[[D^[[C^[[A^[[A^[[C^[[B^[[C^[[C^[[B^[[C^[[C^[[B^[[B^[[A^[[D^[[B^[[C^[[B^[[D^[[D^[[A^[[C^[[D^[[B^[[B^[[B^[[B^[[D^[[D^[[B^[[C^[[B^[[C^[[C^[[B^[[C^[[C^[[C^[[A^[[C^[[C^[[A^[[C^[[C^[[B^[[D^[[C^[[D^[[D^[[D^[[D^[[D^[[B^[[D^[[C^[[C^[[B^[[C^[[D^[[B^[[D^[[C^[[C^[[C^[[C^[[B^[[D^[[C^[[D^[[B^[[D^[[A^[[C^[[C^[[B^[[C^[[D^[[C^[[A^[[A^[[B^[[D^[[B^[[C^[[D^[[A^[[D^[[B^[[D^[[A^[[B^[[C^[[D^[[B^[[C^[[B^[[A^[[B^[[A^[[B^[[B^[[C^[[B^[[D^[[C^[[A^[[C^[[B^[[C^[[B^[[D^[[D^[[B^[[C^[[D^[[D^[[A^[[B^[[A^[[D^[[D^[[D^[[D^[[C^[[A^[[A^[[B^[[B^[[D^[[A^[[C^[[A^[[A^[[B^[[B^[[C^[[A^[[D^[[A^[[B^[[C^[[D^[[D^[[A^[[D^[[D^[[C^[[A^[[A^[[D^[[C^[[C^[[A^[[C^[[C^[[B^[[D^[[A^[[A^[[C^[[B^[[B^[[C^[[A^[[A^[[C^[[A^[[B^[[C^[[B^[[C^[[C^[[A^[[C^[[C^[[C^[[B^[[C^[[C^[[C^[[C^[[B^[[C^[[A^[[D^[[C^[[A^[[A^[[B^[[C^[[D^[[C^[[C^[[C^[[D^[[A^[[B^[[D^[[B^[[C^[[C^[[B^[[B^[[A^[[D^[[A^[[D^[[B^[[A^[[C^[[A^[[A^[[A^[[A^[[B^[[C^[[A^[[C^[[C^[[D^[[B^[[D^[[D^[[C^[[C^[[B^[[C^[[B^[[C^[[B^[[C^[[B^[[B^[[D^[[A^[[B^[[A^[[C^[[A^[[D^[[D^[[B^[[C^[[C^[[C^[[D^[[B^[[A^[[B^[[A^[[A^[[C^[[A^[[D^[[B^[[A^[[C^[[A^[[D^[[A^[[D^[[D^[[D^[[C^[[D^[[A^[[A^[[C^[[B^[[B^[[D^[[C^[[C^[[A^[[B^[[B^[[C^[[D^[[C^[[B^[[D^[[B^[[D^[[C^[[C^[[D^[[D^[[B^[[D^[[B^[[C^[[A^[[A^[[C^[[B^[[B^[[A^[[A^[[A^[[B^[[C^[[D^[[A^[[C^[[A^[[C^[[D^[[D^[[C^[[D^[[A^[[D^[[D^[[D^[[A^[[C^[[D^[[D^[[A^[[B^[[D^[[D^[[B^[[A^[[B^[[C^[[D^[[C^[[C^[[A^[[B^[[C^[[B^[[B^[[B^[[B^[[C^[[A^[[D^[[A^[[D^[[B^[[B^[[D^[[D^[[D^[[B^[[D^[[A^[[C^[[D^[[C^[[C^[[D^[[C^[[A^[[C^[[B^[[D^[[B^[[B^[[C^[[A^[[B^[[A^[[C^[[D^[[D^[[D^[[C^[[C^[[D^[[D^[[A^[[B^[[D^[[D^[[D^[[C^[[C^[[B^[[D^[[D^[[B^[[B^[[A^[[B^[[B^[[C^[[A^[[A^[[A^[[C^[[D^[[D^[[A^[[D^[[A^[[B^[[C^[[C^[[C^[[B^[[D^[[D^[[D^[[D^[[C^[[D^[[D^[[B^[[C^[[D^[[B^[[B^[[C^[[D^[[B^[[C^[[C^[[D^[[B^[[D^[[C^[[A^[[C^[[C^[[D^[[B^[[D^[[B^[[D^[[A^[[B^[[B^[[B^[[A^[[D^[[C^[[C^[[C^[[C^[[C^[[A^[[D^[[B^[[C^[[A^[[B^[[D^[[B^[[D^[[B^[[B^[[B^[[D^[[C^[[B^[[B^[[B^[[C^[[B^[[A^[[D^[[C^[[C^[[A^[[D^[[A^[[B^[[A^[[D^[[D^[[B^[[A^[[D^[[B^[[C^[[B^[[A^[[D^[[B^[[C^[[D^[[C^[[A^[[B^[[D^[[D^[[D^[[C^[[B^[[B^[[A^[[D^[[D^[[B^[[D^[[D^[[C^[[C^[[D^[[D^[[A^[[B^[[C^[[D^[[D^[[C^[[C^[[D^[[A^[[C^[[A^[[C^[[A^[[D^[[B^[[C^[[A^[[C^[[B^[[C^[[B^[[A^[[D^[[B^[[D^[[A^[[D^[[C^[[A^[[B^[[B^[[D^[[C^[[A^[[C^[[A^[[D^[[D^[[B^[[C^[[D^[[C^[[B^[[C^[[C^[[C^[[B^[[A^[[D^[[B^[[A^[[A^[[D^[[A^[[D^[[D^[[C^[[B^[[D^[[D^[[C^[[D^[[B^[[B^[[A^[[A^[[C^[[A^[[A^[[A^[[A^[[D^[[C^[[D^[[A^[[B^[[C^[[A^[[A^[[C^[[D^[[C^[[D^[[C^[[D^[[A^[[C^[[B^[[C^[[D^[[C^[[B^[[A^[[D^[[B^[[B^[[B^[[B^[[B^[[C^[[A^[[A^[[A^[[A^[[D^[[C^[[C^[[A^[[C^[[B^[[D^[[C^[[D^[[A^[[A^[[B^[[D^[[C^[[A^[[A^[[C^[[B^[[D^[[B^[[C^[[D^[[D^[[C^[[B^[[C^[[A^[[D^[[A^[[D^[[A^[[B^[[D^[[D^[[B^[[A^[[D^[[D^[[A^[[D^[[D^[[D^[[A^[[C^[[A^[[B^[[D^[[D^[[B^[[B^[[B^[[D^[[D^[[A^[[A^[[C^[[B^[[B^[[B^[[C^[[C^[[A^[[C^[[B^[[B^[[D^[[B^[[B^[[C^[[B^[[D^[[D^[[A^[[A^[[B^[[D^[[C^[[C^[[C^[[C^[[B^[[A^[[C^[[C^[[C^[[D^[[D^[[D^[[B^[[C^[[D^[[B^[[D^[[D^[[B^[[B^[[D^[[C^[[C^[[D^[[D^[[A^[[A^[[D^[[C^[[C^[[C^[[B^[[C^[[A^[[D^[[D^[[C^[[A^[[A^[[D^[[C^[[C^[[D^[[D^[[A^[[B^[[B^[[D^[[D^[[A^[[B^[[B^[[D^[[C^[[B^[[D^[[A^[[B^[[C^[[C^[[B^[[D^[[C^[[C^[[C^[[C^[[C^[[C^[[D^[[A^[[B^[[D^[[A^[[A^[[B^[[D^[[C^[[B^[[D^[[D^[[A^[[C^[[C^[[B^[[A^[[A^[[C^[[C^[[B^[[D^[[A^[[A^[[B^[[A^[[A^[[D^[[C^[[C^[[C^[[B^[[A^[[B^[[D^[[D^[[C^[[D^[[B^[[A^[[B^[[B^[[A^[[A^[[A^[[B^[[D^[[D^[[D^[[B^[[C^[[D^[[C^[[A^[[D^[[B^[[A^[[A^[[D^[[A^[[D
"""
comment = comment.replace('^','').replace('[[','')
# A is up
# B is down
# C is right
# D is left

x, y = 4846 + 61, 6900 + 61
size = 122
image = Image.open('Question.jpg')
data = image.load()
string = []
for new_place in comment:
    # new_place = 'A'
    if ( new_place == 'A' ): y -= size
    if ( new_place == 'B' ): y += size
    if ( new_place == 'C' ): x += size
    if ( new_place == 'D' ): x -= size
 
    try:
        string.append(chr(data[x, y][0]))
        # print data[x,y]
    except:
        pass

# print len(string)
sys.stdout.write( "".join(string) )
image.close()
```
![](https://github.com/ScripTeaseCTF/CTF/blob/master/WhaleCTF/images/prom2.PNG)  
ignore the error  
hash it and lowercase it and you got your flag  
flag{f524415e198cbc8983ac0bed3d0cbcef}  

## Cross-eyed eyes (Stego/ 200)
![](https://github.com/ScripTeaseCTF/CTF/blob/master/WhaleCTF/images/final1.PNG)   
okay lets grab it dd if=final.png bs=1 skip=1922524 of=img.png  
open with stegsolve so you know - java -jar stegsolve.jar   
![](https://github.com/ScripTeaseCTF/CTF/blob/master/WhaleCTF/images/final2.PNG)   
ISG{E4sY_StEg4n0gR4pHy}  
 
