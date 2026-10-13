# Crystal release candidates

This foundation pass records the seven distinct retail identities available in the local corpus: the Japanese origin release, English USA/Europe revisions 0 and 1, and German, French, Italian, and Spanish revision 0 releases. No official Korean Crystal release is assumed, and no unobserved localized identity is synthesized.

Every entry passed Nintendo logo, header checksum, and global checksum validation with `SakuraiTsubaki/Disassembly` commit `4393d06d0d6a2e3c14d0e1aca6549655e08efec2` (`tools/inspect_gb_rom.py` v1.1.0). The evidence also preserves the Japanese cartridge header's RAM size code `0x05`, distinct from `0x03` in every western release. The localized headers carry the manufacturer codes `BYTD`, `BYTF`, `BYTI`, and `BYTS`, binding the German, French, Italian, and Spanish identities without relying on filenames.

All identities remain `candidate`. Valid internal checksums establish structural integrity, not independent canonical provenance. Promotion to `verified` requires corroboration from a trusted independent reference or a reproducible matching build.

No ROM binary or byte extract is included.
