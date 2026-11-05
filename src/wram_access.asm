SECTION "Banked WRAM Access Reconstruction", ROM0

FarCopyWRAM::
    ldh [hTempBank], a
    ldh a, [rWBK]
    push af
    ldh a, [hTempBank]
    ldh [rWBK], a
    call CopyBytes
    pop af
    ldh [rWBK], a
    ret

GetFarWRAMByte::
    ldh [hTempBank], a
    ldh a, [rWBK]
    push af
    ldh a, [hTempBank]
    ldh [rWBK], a
    ld a, [hl]
    ldh [hFarByte], a
    pop af
    ldh [rWBK], a
    ldh a, [hFarByte]
    ret

GetFarWRAMWord::
    ldh [hTempBank], a
    ldh a, [rWBK]
    push af
    ldh a, [hTempBank]
    ldh [rWBK], a
    ld a, [hli]
    ld h, [hl]
    ld l, a
    pop af
    ldh [rWBK], a
    ret
