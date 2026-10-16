# Crystal Divide wrapper reconstruction

All seven verified Crystal releases contain the complete 18-byte wrapper immediately after `Multiply`. It preserves HL, DE, and BC, saves the active ROM bank through the `homecall` expansion, switches to the release-specific bank 1 `_Divide` target with `RST $10`, calls it, restores the prior bank, restores the registers, and returns. Every release uses `hROMBank` at `$ff9d`; Japanese targets `$01:$6977`, English rev0/rev1 `$01:$673e`, and the four European targets are retained per report.

The routine divides `hDividend` (length in B, maximum four bytes) by `hDivisor`, producing `hQuotient` and `hRemainder`. Naming and macro expansion follow `pret/pokecrystal@3bc8daa4173e96a7f4011dad3922eb6fa5dad5c6`, `home/math.asm` and `macros/farcall.asm`. No ROM bytes are published.
