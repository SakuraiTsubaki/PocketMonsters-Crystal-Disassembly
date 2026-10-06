# Japanese CGB mode startup branches

Crystal's startup check branches at `0x0172`/ `0x0175`. The non-CGB path
joins at `0x0177`; the CGB path sets two Crystal-specific mode flags before
clearing hardware state and waiting for LY `0x91`. Its WRAM store at
`0xD000` differs from Gold/Silver. Both RGBDS blocks and structural reports
are hash-bound without publishing standalone ROM fragments.
