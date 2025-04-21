from binascii import hexlify

def cast_shadow(riddle, ember):
    ember_glow = ember.encode()
    riddle_glow = riddle.encode()
    return bytes(r ^ e for r, e in zip(riddle_glow, ember_glow * (len(riddle_glow) // len(ember_glow) + 1)))

ember = "mystery"
riddles = ["Whispered lore", "CIR{shared_ember}"]
shadows = [hexlify(cast_shadow(r, ember)).decode() for r in riddles]
print(shadows)