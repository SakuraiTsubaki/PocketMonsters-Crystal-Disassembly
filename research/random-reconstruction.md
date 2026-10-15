# Crystal Random reconstruction

All seven catalogued Crystal releases were SHA-256 gated and scanned independently. Each contains exactly one bank-0 routine matching the complete 19-byte control/data shape of `Random`. Japanese is the origin reference; no official Korean Crystal exists, so English and the remaining European languages follow.

Every Crystal release uses the same code hash `aaec7ea8640c2ff5aab78c3b6a2af39c89ed1393960bfc236aed907c8a087846` and HRAM state at `hRandomAdd=$FFE1`, `hRandomSub=$FFE2`; localization only relocates the routine. It samples `DIV`, adds it with carry to the first state byte, subtracts the second state byte with carry from a new `DIV` sample, and returns the updated subtraction state in A.

Names and semantics are corroborated by `pret/pokecrystal@3bc8daa4173e96a7f4011dad3922eb6fa5dad5c6`, `home/random.asm`. Reports retain identity, address, state and hashes without publishing ROM bytes.
