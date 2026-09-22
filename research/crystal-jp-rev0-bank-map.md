# Crystal Japanese revision 0 bank map

The Japanese origin candidate `crystal-jp-rev0` is 2 MiB and divides exactly into 128 physical 16 KiB ROM banks. `analysis/crystal-jp-rev0-bank-fingerprints.json` records a SHA-256 fingerprint, Shannon entropy, distinct-byte count, and zero/`0xff` counts for every bank. `analysis/banks.csv` maps bank 0 to the fixed `0x0000–0x3fff` CPU window and switchable banks to `0x4000–0x7fff`.

Bank 0 is classified only as `header-and-code`; remaining non-padding banks stay `unclassified` until instruction/data boundaries are established from stronger evidence. Fingerprinting provides stable boundaries and change detection without claiming that entropy distinguishes code from data.

The 128 physical banks produce 99 distinct bank hashes. Banks `0x60` through `0x7c` are 29 identical padding banks, while non-padding banks `0x59` and `0x5a` are also byte-identical. This repetition is recorded as an observed layout property, not interpreted as code or data semantics.

The source remains a `candidate`, not a verified retail baseline. No ROM bytes or extracted byte ranges are stored.
