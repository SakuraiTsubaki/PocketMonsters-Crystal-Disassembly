# Pocket Monsters Crystal ClearBox disassembly

`crystal-jp-rev0` is the Japanese origin reference. All 7 cataloged releases (Japanese, English, German, French, Italian, Spanish) have one verified ClearBox path. The routine fills a B-by-C rectangle at HL, preserving the row start and dimensions while advancing by the 20-tile screen width. Crystal loads the blank tile and falls through to FillBoxWithByte. Candidate status is retained; maps publish control-flow, operands, provenance and hashes, never ROM bytes.
