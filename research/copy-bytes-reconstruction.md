# Crystal CopyBytes reconstruction

All seven catalogued Crystal releases were SHA-256 gated and scanned independently. Each contains exactly one complete 14-byte `CopyBytes` routine. Japanese Crystal is the origin reference; there is no official Korean Crystal release, so English rev0/rev1 and the remaining European languages follow.

The routine copies BC bytes from HL to DE and supports a zero-length request. Its split C-then-B countdown increments both counters before entering the loop so the final low- and high-byte runs are retained. Every release has code SHA-256 `9364deaa0f942c15dcd1ab29a953a4c5a14c0916e877a9e67cee53dc09e3e028`; localization changes only its ROM0 address.

The name and semantics are corroborated by `pret/pokecrystal@3bc8daa4173e96a7f4011dad3922eb6fa5dad5c6`, `home/copy.asm`. Reports publish ROM identities, locations, semantics, and hashes without ROM bytes.
