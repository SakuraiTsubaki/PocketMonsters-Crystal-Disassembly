# Pocket Monsters Crystal SpeechTextbox disassembly

`crystal-jp-rev0` is the Japanese origin reference. All 7 cataloged releases (Japanese, English, German, French, Italian, Spanish) contain one 10-byte entry that loads the release-specific textbox tilemap pointer, sets a 4-by-18 interior, and tail-jumps to the independently verified Textbox entry. Candidate status is retained; evidence contains hashes and decoded operands, not ROM bytes.
