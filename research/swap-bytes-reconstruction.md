# Crystal SwapBytes reconstruction

crystal-jp-rev0 is the Japanese origin reference. All 7 cataloged Crystal releases (Japanese, English, German, French, Italian, Spanish) place the 13-byte SwapBytes routine immediately after CopyBytes. It exchanges BC bytes between HL and DE in place. Gold and Silver do not expose this Crystal-specific home routine, so they are not assigned synthetic evidence. No ROM bytes are published.
