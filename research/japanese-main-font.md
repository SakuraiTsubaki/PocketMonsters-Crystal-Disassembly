# Japanese main font

Japanese Crystal stores its standard 128-tile 1bpp font at bank 62 address `0x4200`, file offsets `0xF8200` through `0xF8600`. Its Japanese standard loader begins at file offset `0xFB485`; the first transfer points to `3e:4200`, targets `vTiles1`, and covers 128 tiles.

The data boundary and loading semantics are corroborated by `pret/pokecrystal` source commit `3bc8daa4173e96a7f4011dad3922eb6fa5dad5c6` (`engine/gfx/load_font.asm` and `gfx/font.asm`) and symbols commit `887a080f34ffd6a4c1b2201e266ed0599654d222` (`pokecrystal.sym`: `Font` at `3e:4200`). The Japanese ROM's own pointer and range hash are authoritative for this repository.

The range SHA-256 is `0902d141b40af70008d3176cf4cc13f5d5a10812ffaf08ecee5752fa7e31b8ca`, identical to Japanese Gold and Silver. `graphics/font/main-font-jp.png` is a deterministic 4× nearest-neighbour rendering. No ROM image or raw ROM range is published.
