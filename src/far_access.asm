SECTION "Far Access Reconstruction", ROM0

GetFarByte::
    ldh [hTempBank], a
    ldh a, [hROMBank]
    push af
    ldh a, [hTempBank]
    rst Bankswitch
    ld a, [hl]
    ldh [hFarByte], a
    pop af
    rst Bankswitch
    ldh a, [hFarByte]
    ret

GetFarWord::
    ldh [hTempBank], a
    ldh a, [hROMBank]
    push af
    ldh a, [hTempBank]
    rst Bankswitch
    ld a, [hli]
    ld h, [hl]
    ld l, a
    pop af
    rst Bankswitch
    ret
