# European main fonts

The official German, French, Italian, and Spanish Crystal releases store their 128-tile 1bpp standard fonts at bank 62 address `0x4200`, file offset `0xF8200`. The `Font` boundary is corroborated by `pret/pokecrystal` source commit `3bc8daa4173e96a7f4011dad3922eb6fa5dad5c6` and symbols commit `887a080f34ffd6a4c1b2201e266ed0599654d222`. Each local retail ROM was identity-gated by whole-file SHA-256 and passed Nintendo-logo, header-checksum, and global-checksum validation before extraction.

The localized cartridge headers provide language-specific manufacturer codes: German `BYTD`, French `BYTF`, Italian `BYTI`, and Spanish `BYTS`. These identities are now synchronized across `project.json`, the release CSV, and the header report; they remain `candidate` until independently corroborated or reproduced by an exact build.

German and French share range SHA-256 `5eb8c0af5deff7c6b4cbc7167dd0885b6cffcfc932b1905c4e9d38acdda4b850`. Spanish and Italian share `a2b514b0b097d985feb645afe5a3af19884308b6259c6facb1814bae6af1b950`. Separate language PNG paths preserve direct provenance even when the glyph bytes match.

All PNGs are deterministic 4× nearest-neighbour renderings. No ROM image or raw ROM range is published.
