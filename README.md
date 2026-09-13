# PocketMonsters-Crystal-Disassembly

Multi-version disassembly and reproducible source reconstruction of **Pokémon Crystal**, covering code, data, graphics, text, maps, scripts, audio, and build tooling across supported language and revision releases.

**ROM binaries are not stored in this repository.** The end goal is to rebuild each supported release from repository source data alone and verify the generated ROM byte-for-byte against known reference hashes.

## Target releases

- Japanese — Rev 0
- English (USA/Europe) — Rev 0
- English (USA/Europe) — Rev A / Rev 1
- German — Rev 0
- French — Rev 0
- Italian — Rev 0
- Spanish — Rev 0

Reference filenames, cartridge header metadata, MD5, SHA-1, and SHA-256 values are recorded in [`manifests/releases.json`](manifests/releases.json).

## Repository policy

The ROM image itself is the only project artifact that must not be committed. Disassembly source, reconstructed game data, graphics source, text, maps, scripts, audio source, tooling, manifests, analysis, verification data, and other reproducible project material belong in the repository.

Generated `.gb`/`.gbc` files and local reference ROMs are excluded by [`.gitignore`](.gitignore).

## Reconstruction goal

The project will progressively replace opaque ROM regions with named, editable source representations, including:

- RGBDS assembly for executable code and data tables
- readable text source and character mappings
- Pokémon, move, item, trainer, encounter, Pokédex, and related game data
- map block data, map metadata, events, and scripts
- Pokémon, trainer, tileset, UI, font, palette, tilemap, and other graphics sources
- music, sound effects, cries, wave data, and audio engine data
- extraction, conversion, build, comparison, and regression-test tooling

The intended completed workflow is:

```text
git clone
    ↓
source + assets + tools
    ↓
RGBDS / project build tools
    ↓
reconstructed Crystal ROM
    ↓
reference hash verification
```

## Current status

**Phase 0 — repository bootstrap**

- Repository created
- ROM binaries excluded from version control
- Seven reference releases identified
- Reference hashes and cartridge-header metadata recorded
- Full multi-version source reconstruction pending

## Reference projects

This project follows the reproducible-source philosophy established by Pokémon reverse-engineering projects such as `pret/pokecrystal`, while targeting a unified multi-language, multi-revision Crystal reconstruction.
