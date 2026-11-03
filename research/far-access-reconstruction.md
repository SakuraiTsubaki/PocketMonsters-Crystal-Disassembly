# Crystal far-ROM access reconstruction

crystal-jp-rev0 is the Japanese origin reference. All 7 cataloged releases (Japanese, English, German, French, Italian, Spanish) independently verify adjacent GetFarByte and GetFarWord routines. Both save the current ROM bank, switch to the bank in A, read through HL, restore the previous bank, and return without publishing ROM bytes. The crystal profile records its distinct temporary-storage convention.
