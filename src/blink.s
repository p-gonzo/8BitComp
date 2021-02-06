    .org $8000      ; For our processeor, the ROM address space starts at $8000
    lda #$ff
    sta $6002

    lda #$55
    sta $6000

    lda #$aa
    sta $6000

    jmp $8005
    
    .org $fffc      ; Go to $fffc, set the init vector and pad the last two bytes.
    .word $8000
    .word $0000