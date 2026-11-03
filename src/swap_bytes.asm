SECTION "SwapBytes Reconstruction", ROM0

SwapBytes::
.loop
    ld a, [hl]
    push af
    ld a, [de]
    ld [hli], a
    pop af
    ld [de], a
    inc de
    dec bc
    ld a, b
    or c
    jr nz, .loop
    ret
