; Generation II byte-copy routine across all catalogued Crystal releases.
; Japanese is the origin reference; no official Korean Crystal release exists.

CopyBytes::
    inc b
    inc c
    jr .HandleLoop
.CopyByte:
    ld a, [hli]
    ld [de], a
    inc de
.HandleLoop:
    dec c
    jr nz, .CopyByte
    dec b
    jr nz, .CopyByte
    ret
