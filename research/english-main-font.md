# English main font

The official English Crystal releases store the standard 128-tile 1bpp font at bank 62 address `0x4200`, file offsets `0xF8200` through `0xF8600`. `pret/pokecrystal` source commit `3bc8daa4173e96a7f4011dad3922eb6fa5dad5c6` and symbols commit `887a080f34ffd6a4c1b2201e266ed0599654d222` identify this range as `Font`; its source PNG decodes to the same range and occurs at this primary location in the retail ROM.

English revisions 0 and 1 share range SHA-256 `2b3fe12a895c2b028aef61e94dbaacd5ddfd3ff1e4f4d3c1815daf99dfb298f7`. `graphics/font/main-font-en.png` is a deterministic 4× nearest-neighbour rendering; raw ROM bytes are not published.
