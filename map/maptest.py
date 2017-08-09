from linearmap import Map

contacts = Map()
contacts.add("Robin Wei", "18094207926")
contacts.add("Maggie Liu", "15951937658")
print len(contacts)
print "Jack Ma" in contacts
print "Robin Wei" in contacts

for item in contacts:
    print item.key, item.value
