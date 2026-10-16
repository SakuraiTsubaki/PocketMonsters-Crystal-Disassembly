# Crystal _Multiply core reconstruction

The `Multiply` far-call target and `Divide` homecall target bound an exact 96-byte bank 1 routine in all seven verified Crystal releases. Every Crystal release has one shared code hash. Its control flow is identical to Gold/Silver; only the HRAM math layout is two bytes earlier (`hMultiplier` at `$ffb7`, four-byte `hProduct` at `$ffb3..$ffb6`). The routine performs eight shift-add iterations over a three-byte big-endian multiplicand.

The Japanese build is the origin reference; English rev0/rev1, German, French, Italian, and Spanish binaries independently match the complete verifier. Naming follows `pret/pokecrystal@3bc8daa4173e96a7f4011dad3922eb6fa5dad5c6`, `engine/math/math.asm`. Reports contain hashes and decoded addresses, not ROM bytes.
