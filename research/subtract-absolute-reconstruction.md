# Crystal SubtractAbsolute reconstruction

All seven verified Crystal releases contain the same complete seven-byte routine immediately after `Divide`. The nonnegative path returns `A - B` with carry clear. The negative path takes the two's complement of the wrapped subtraction, returns `B - A`, and explicitly sets carry. The reference source marks the function unreferenced; that status is recorded rather than treated as proof that no retail path can reach it.

Naming and semantics follow `pret/pokecrystal@3bc8daa4173e96a7f4011dad3922eb6fa5dad5c6`, `home/math.asm`. Reports retain addresses and hashes without publishing ROM bytes.
