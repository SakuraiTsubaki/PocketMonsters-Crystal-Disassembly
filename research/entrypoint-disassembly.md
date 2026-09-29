# Japanese cartridge entry disassembly

The exact-hash Japanese origin candidate stores `00c36e01` at cartridge offset `0x0100`. This decodes as `nop` followed by `jp $016e`. The committed RGBDS source reconstructs all four bytes, and tests bind the encoded bytes to both the analysis report and source-slice SHA-256 `8f3926056f4a79f731b9fb6b53440d27e675aead717331be6e49e5fb4ab4e94d`.

This establishes the fixed cartridge entry only. It neither promotes the candidate release nor claims that the branch target's complete routine has been disassembled.

