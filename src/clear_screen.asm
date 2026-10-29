SECTION "Clear Screen Reconstruction", ROM0

ClearTilemap::
    ld hl, wTilemap
    ld a, " "
    ld bc, SCREEN_AREA
    call ByteFill
    ldh a, [rLCDC]
    bit B_LCDC_ENABLE, a
    ret z
    jp WaitBGMap

ClearScreen::
    ld a, PAL_BG_TEXT
    ld hl, wAttrmap
    ld bc, SCREEN_AREA
    call ByteFill
    jr ClearTilemap
