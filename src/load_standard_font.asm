; Semantic reconstruction of the retail Crystal standard-font loader.
; ROM ranges and hashes are recorded in analysis/*-standard-font-loader.json.

LoadStandardFont::
    ld de, $4200
    ld hl, $8800
    ld bc, $3e80
    ldh a, [rLCDC]
    bit 7, a
    jp z, Copy1bpp

    ld de, $4200
    ld hl, $8800
    ld bc, $3e20
    call Get1bppViaHDMA
    ld de, $4300
    ld hl, $8a00
    ld bc, $3e20
    call Get1bppViaHDMA
    ld de, $4400
    ld hl, $8c00
    ld bc, $3e20
    call Get1bppViaHDMA
    ld de, $4500
    ld hl, $8e00
    ld bc, $3e20
    call Get1bppViaHDMA
    ret
