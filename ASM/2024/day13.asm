section .data

    filename db "day13.txt", 0

    nums dq 6
    char db 0

section .text

%include "macros.inc"
%include "common.inc"

global solve
global _start

solve:
    ret

_start:
    push rbp
    mov rbp, rsp
    sub rsp, 0x50

    ; Open file
    mov rdi, filename
    call open_file
    mov dword [rbp-0x4], eax

    ; Answers P1 and P2
    mov qword [rbp-0x18], 0x0
    mov qword [rbp-0x10], 0x0

.button:

    xor ecx, ecx
    mov rdi, rax
    lea rsi, [char]
    mov rdx, 1

.button-find:

    ; read(fd, char, 1)
    mov rax, SYS_READ
    syscall

    ; Check if we find a plus
    cmp byte [char], '+'
    jne .button-find

.button-copy:

    ; Read until not a number

    ; Print P1 and P2
    mov rdi, qword [rbp-0x18]
    call print_int
    mov rdi, qword [rbp-0x0]
    call print_int

    ; Close file
    mov eax, dword [rbp-0x4]
    close_file rax

    ; Exit
    exit_program 0
    leave
    ret
