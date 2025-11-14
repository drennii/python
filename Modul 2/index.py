words=("spam","eggs","bread")



print(words[0])

contact_info={ "Alice":"555-1234",
               "Bob":"555-5678"
}

alice_phone=contact_info["Alice"]
print(alice_phone)

contact_info["Eve"]="777-4567"

print(contact_info)

del contact_info["Bob"]
print(contact_info)

keys=contact_info.keys()
print(keys)

values=contact_info.values()
print(values)

contact_info{
    "Alice":{
        "phone_number": "55-1234",
        "email":"alice@gmail.com"
        }
    "Bob":{
        "phone_number":"777-4567",
        "email":"bob@gmail.com"
     }
}
bob_info=contact=information["Bob"]
print(bob_info)

