def twist_words(secret, wind):
    echo = ""
    for glyph in secret:
        if glyph.isalpha():
            base = 65 if glyph.isupper() else 97
            echo += chr((ord(glyph) - base + wind) % 26 + base)
        else:
            echo += glyph
    return echo

relic = "MEET ME AT THE MOSQUE CIR{veiled_flag}"
veiled = twist_words(relic, 3)
print(veiled)