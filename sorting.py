def sort_contacts(contacts):


  return sorted(contacts, key=lambda contact: contact[0])

def filter_contacts_by_name_prefix(contacts, prefix):
  return [contact for contact in contacts if contact[0].lower().startswith(prefix.lower())]

contacts = [
    ("Alice", "alice@email.com", "123-456-7890"),
    ("Bob", "bob@email.com", "234-567-8901"),
    ("Charlie", "charlie@email.com", "345-678-9012"),
    ("David", "david@email.com", "456-789-0123"),
]

sorted_contacts = sort_contacts(contacts.copy())  

print("Contacts Sorted by Name:")
for name, email, phone in sorted_contacts:
  print(f"- {name} ({email}, {phone})")

filtered_prefix = "C"
filtered_contacts = filter_contacts_by_name_prefix(contacts.copy(), filtered_prefix)

print(f"\nContacts Starting with '{filtered_prefix}':")
for name, email, phone in filtered_contacts:
  print(f"- {name} ({email}, {phone})")