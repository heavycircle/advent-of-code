BITS 64

section .text

global _start

_start:
    ; exit(0)
    mov rax, 60
    xor rdi, rdi
    syscall
