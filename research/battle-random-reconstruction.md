# Crystal BattleRandom reconstruction

All seven catalogued Crystal releases were SHA-256 gated and inspected immediately after their verified `Random` routines. Each contains the complete 18-byte bank-switch wrapper and uses `hROMBank=$ff9d`, bank `$0f`, and a release-specific `_BattleRandom` call target.

Japanese, the origin reference, uses `$2f71` → `$0f:$6dea` and temporary `$cfaa`. English rev0/rev1 use `$2f9f` → `$0f:$6dd8`; German and Spanish use `$2f89` → `$0f:$6dd9`; French uses `$2f8c` → `$0f:$6ddb`; Italian uses `$2f8d` → `$0f:$6dd9`. All non-Japanese releases use temporary `$cfb6`.

Names and semantics are corroborated by `pret/pokecrystal@3bc8daa4173e96a7f4011dad3922eb6fa5dad5c6`, `home/random.asm`. Reports preserve release identity, operands, and hashes without ROM bytes. Crystal has no official Korean release, so the language order is Japanese, English, then the other official localizations.
