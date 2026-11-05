# Crystal banked-WRAM access reconstruction

crystal-jp-rev0 is the Japanese origin reference. All 7 cataloged Crystal releases (Japanese, English, German, French, Italian, Spanish) verify the adjacent FarCopyWRAM, GetFarWRAMByte, and GetFarWRAMWord suite immediately after GetFarWord. Each helper saves and restores rWBK while selecting bank A. Gold and Silver do not receive synthetic copies of this Crystal-specific suite. No ROM bytes are published.
