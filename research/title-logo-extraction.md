# Crystal title-logo extraction

This unit preserves the complete language-specific title logos for all seven
verified local Crystal ROMs. Japanese is the origin reference. Crystal has no
official Korean release in this catalog, so English is followed by German,
French, Italian, and Spanish. No ROM bytes or compressed streams are committed.

## Code-derived locations

Crystal's title routine differs from Gold and Silver. The logo and the crystal
background are decompressed directly within ROM bank `0x43`; there is no far
decompress bank argument to copy from the earlier games. The relevant loader
sequence is `ld hl, TitleLogoGFX`, `ld de, vTiles1`, `call Decompress`, followed
by a second stream targeting `vTiles0`.

Japanese loader code at `0x10EDDA` points to `0x10F32B`, yielding 144 tiles.
Every non-Japanese build uses loader `0x10EDF0` and stream offset `0x10F326`,
yielding 156 tiles. English revisions 0 and 1 decompress identically, but the
German, French, Italian, and Spanish hashes are all distinct because their
version labels are embedded in the artwork. Separate public PNGs therefore
preserve every official localization rather than substituting English.

## Public-source cross-reference and reproduction

`pret/pokecrystal` commit `5beda23ffa505f62e1dad7e3d7c214d1737b3358`
labels the stream `TitleLogoGFX` in `engine/movie/title.asm` and documents its
VRAM destination and 7-by-20 tile draw. The local ROM instructions independently
establish the offsets recorded here.

Run `tools/extract_gb_lz_2bpp.py` from `SakuraiTsubaki/Disassembly` with each
report's complete-ROM SHA-256 and source offset, using 20 tiles per row. The
extractor verifies the ROM identity and emits deterministic PNGs plus hashes,
without publishing compressed or decompressed ROM bytes.
