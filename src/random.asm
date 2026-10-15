; Generation II hardware-divider RNG, reconstructed across all catalogued Crystal releases.
; Japanese: $2f5e; English rev0/rev1: $2f8c; German/Spanish: $2f76;
; French: $2f79; Italian: $2f7a.

Random::
    push bc
    ldh a, [rDIV]
    ld b, a
    ldh a, [hRandomAdd]
    adc b
    ldh [hRandomAdd], a
    ldh a, [rDIV]
    ld b, a
    ldh a, [hRandomSub]
    sbc b
    ldh [hRandomSub], a
    pop bc
    ret
