# Crystal SimpleDivide reconstruction

All seven verified Crystal releases were inspected at their verified `RandomRange` call target. Each contains the complete nine-byte repeated-subtraction routine, returning quotient B and remainder A for dividend A and nonzero divisor C.

Japanese uses `$30dc`; English rev0/rev1 `$3110`; German and Spanish `$30fa`; French `$30fd`; Italian `$30fe`. All share code hash `076069c0b328a081fe3c9743adb8359b5739d024cbe928ee03b1e57e97cf357a`.

Naming and semantics follow `pret/pokecrystal@3bc8daa4173e96a7f4011dad3922eb6fa5dad5c6`, `home/math.asm`. Crystal has no official Korean release. No ROM bytes are published.
