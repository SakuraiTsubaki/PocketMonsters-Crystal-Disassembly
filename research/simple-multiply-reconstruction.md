# Crystal SimpleMultiply reconstruction

All seven verified Crystal releases contain the same complete 11-byte `SimpleMultiply` routine immediately before `SimpleDivide`. It returns immediately for a zero multiplicand; otherwise it preserves BC and computes the 8-bit product by adding C exactly A times. The reports retain each release-specific home-bank address and prove the shared code hash without publishing ROM bytes.

Naming and control-flow semantics follow `pret/pokecrystal@3bc8daa4173e96a7f4011dad3922eb6fa5dad5c6`, `home/math.asm`.
