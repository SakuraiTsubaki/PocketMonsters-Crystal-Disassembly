SECTION "ClearBox Reconstruction", ROM0

ClearBox::
    ld a, " "
    ; fallthrough
FillBoxWithByte::
.row
    push bc
    push hl
.col
    ld [hli], a
    dec c
    jr nz, .col
    pop hl
    ld bc, SCREEN_WIDTH
    add hl, bc
    pop bc
    dec b
    jr nz, .row
    ret
