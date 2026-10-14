# Standard-font loader provenance

Every catalogued Crystal retail ROM was independently identity-gated before its standard-font loader was located. The Japanese release places the 65-byte routine at `0xfb485`; English revisions 0 and 1 and the German, French, Italian, and Spanish releases place the byte-identical global routine at `0xfb449`.

All releases target the 128-tile 1bpp font at bank `0x3e`, address `0x4200`, and VRAM `0x8800`. With the LCD disabled the routine branches to the direct 1bpp copier. With the LCD enabled it divides the font into four 32-tile chunks targeting `0x8800`, `0x8a00`, `0x8c00`, and `0x8e00` through the HDMA-aware transfer routine.

The structure and names are corroborated by `pret/pokecrystal` source commit `3bc8daa4173e96a7f4011dad3922eb6fa5dad5c6` and symbols commit `887a080f34ffd6a4c1b2201e266ed0599654d222`. The local ROM hashes and generated reports are authoritative here. No ROM bytes are published.
