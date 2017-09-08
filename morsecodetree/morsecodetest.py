from morsecodetree import MorseCodeTree

endecor = MorseCodeTree()

assert endecor.decode(".") is "E", "Decoding Error for E!"
assert endecor.decode(".-") is "A", "Decoding Error for A!"
assert endecor.decode(".-..") is "L", "Decoding Error for L!"
assert endecor.decode("-.-") is "K", "Decoding Error for K!"
assert endecor.decode("--..") is "Z", "Decoding Error for Z!"
assert endecor.decode("..--") is None, "Decoding Error for Illegal sequence!"
assert endecor.encode("A") == ".-", "Encoding Error for A!"
assert endecor.encode("T") == "-", "Encoding Error for T!"
assert endecor.encode("S") == "...", "Encoding Error for A!"
assert endecor.encode("K") == "-.-", "Encoding Error for K!"
assert endecor.encode("V") == "...-", "Encoding Error for V!"
assert endecor.encode("Q") == "--.-", "Encoding Error for Q!"