# Crystal _Divide core reconstruction

The verified `Divide` homecall target begins a complete 131-byte bank 1 routine in all seven Crystal releases. Japanese is the origin reference; English rev0/rev1, German, French, Italian, and Spanish share one full code hash. The control flow is identical to Gold/Silver, while the HRAM layout is two bytes earlier. Crystal uses `hDivisor`/`hRemainder` at `$ffb7` and `hDividend`/`hQuotient` at `$ffb3..$ffb6`.

The routine implements restoring long division for one to four big-endian dividend bytes. Naming and control flow follow `pret/pokecrystal@3bc8daa4173e96a7f4011dad3922eb6fa5dad5c6`, `engine/math/math.asm`. The verifier proves the full terminal path and final `ret`; reports contain decoded addresses and hashes, not ROM bytes.
