  .org $8000      ; For our processeor, the ROM address space starts at $8000
reset_vector:     ; The reset_vector label is at location $8000    
  
  lda #$ff        ; Initialize 65c2 interface adapter
  sta $6002

  lda #$50
  sta $6000

rotate_loop:
  ror             ; Rotate all of the bits in the a register to the right
  sta $6000

  jmp rotate_loop
  
  .org $fffc      ; Go to $fffc, set the reset vector and pad the last two bytes.
  .word reset_vector
  .word $0000