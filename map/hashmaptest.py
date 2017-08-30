from hashmap import HashMap

contacts = HashMap()
contacts.add("Robin Wei", "18094207926")
contacts.add("Maggie Liu", "15951937658")
contacts.add("Vicky Wei", "18094207926")
contacts.add("Xue Liu", "15951937658")
contacts.add("Andy Wei", "18094207926")
contacts.add("Maggie Wei", "15951937658")
contacts.add("Wei Wei", "18094207926")
contacts.add("Yi Liu", "15951937658")
assert len(contacts) == 8, "Wrong length!"
assert "Jack Ma" not in contacts, "Should not be in!"
assert "Robin Wei" in contacts, "Should be in!"
contacts.remove("Robin Wei")
assert len(contacts) == 7, "Wrong remove!"
contacts.add("Wei Wei", "13655197501")
assert contacts.value_of("Wei Wei") is "13655197501", "Wrong Overwriting!"

