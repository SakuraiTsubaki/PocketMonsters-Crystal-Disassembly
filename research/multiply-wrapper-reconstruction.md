# Crystal Multiply wrapper reconstruction

All seven verified Crystal releases contain the complete 11-byte `Multiply` wrapper immediately after `SimpleDivide`. It preserves HL/BC and uses `RST $08` to call the build-specific bank 1 core. Japanese targets `$01:$6917`; English rev0/rev1 `$01:$66de`; German `$01:$66ff`; French `$01:$66f8`; Italian `$01:$66f7`; Spanish `$01:$66fd`.

Naming and semantics follow `pret/pokecrystal@3bc8daa4173e96a7f4011dad3922eb6fa5dad5c6`, `home/math.asm` and `macros/farcall.asm`. No ROM bytes are published.
