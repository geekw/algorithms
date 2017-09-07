from morsecodetree import MorseCodeTree

decoder = MorseCodeTree()

assert decoder.translate(".") is "E", "Decoding Error for E!"
assert decoder.translate(".-") is "A", "Decoding Error for A!"
assert decoder.translate(".-..") is "L", "Decoding Error for L!"
assert decoder.translate("-.-") is "K", "Decoding Error for K!"
assert decoder.translate("--..") is "Z", "Decoding Error for Z!"
assert decoder.translate("..--") is None, "Decoding Error for Illegal sequence!"
