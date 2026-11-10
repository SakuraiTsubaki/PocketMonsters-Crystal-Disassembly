# Crystal DisableLCD

The Japanese release `crystal-jp-rev0` is the origin reference. All 7 cataloged releases (Japanese, English, German, French, Italian, Spanish) contain exactly one ROM0 implementation. It preserves IE, disables the VBlank interrupt while waiting for LY=145, clears LCDC bit 7, clears IF and restores IE. Evidence records release identity, address and code hash without ROM bytes. Korean precedes English where available; release status is unchanged.
