# Crystal SetHPPal

The Japanese release `crystal-jp-rev0` is the origin reference. All 7 cataloged releases (Japanese, English, German, French, Italian, Spanish) contain exactly one five-byte wrapper directly before their verified `GetHPPal`. It calls the release-specific target, writes D to [HL], and returns. Evidence records both addresses and the wrapper hash without ROM bytes. Korean precedes English where available; release status is unchanged.
