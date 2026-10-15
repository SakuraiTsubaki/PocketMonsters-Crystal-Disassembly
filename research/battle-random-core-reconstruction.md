# Crystal _BattleRandom core reconstruction

All seven SHA-256-gated Crystal releases contain the complete 55-byte `_BattleRandom` at the target proven by their wrapper reports. Non-link battles tail-jump to each build's verified `Random`; link battles consume a ten-byte shared stream and refresh every seed with `seed = (seed * 5 + 1) mod 256` at the stream boundary.

Japanese uses `$0f:$6dea`, link mode `$c2dc`, count `$c6d9`, and seeds `$d22b`. All international releases use link mode `$c2dc`, count `$c6e5`, and seeds `$d1fa`; their entry addresses and `Random` destinations differ by localization and are retained per report. English rev0/rev1 are identical for this function. Crystal has no official Korean build, so review order is Japanese, English, then the other official languages.

The source basis is `pret/pokecrystal@3bc8daa4173e96a7f4011dad3922eb6fa5dad5c6`, `engine/battle/core.asm`. Reports publish only identities, structural operands, control flow, and hashes—not ROM bytes.
