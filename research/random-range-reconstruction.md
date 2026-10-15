# Crystal RandomRange reconstruction

All seven verified Crystal releases contain the complete 26-byte `RandomRange` immediately after `BattleRandom`. It accepts a nonzero exclusive upper bound, rejects the incomplete high tail, and reduces the accepted sample with `SimpleDivide`, avoiding modulo bias.

Japanese uses `$2f83`; English rev0/rev1 `$2fb1`; German and Spanish `$2f9b`; French `$2f9e`; Italian `$2f9f`. Every release reads `hRandomAdd=$ffe1`; its `Random` and `SimpleDivide` targets are recorded independently. Crystal has no official Korean version, so the evidence order is Japanese, English, then the remaining official languages.

The source basis is `pret/pokecrystal@3bc8daa4173e96a7f4011dad3922eb6fa5dad5c6`, `home/random.asm`. No ROM bytes are published.
