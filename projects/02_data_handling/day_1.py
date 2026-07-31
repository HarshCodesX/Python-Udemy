"""
 Challenge: CLI Contact Book (CSV-Powered)

Create a terminal-based contact book tool that stores and manages contacts using a CSV file.

Your program should:
1. Ask the user to choose one of the following options:
   - Add a new contact
   - View all contacts
   - Search for a contact by name
   - Exit
2. Store contacts in a file called `contacts.csv` with columns:
   - Name
   - Phone
   - Email
3. If the file doesn't exist, create it automatically.
4. Keep the interface clean and clear.

Example:
Add Contact
View All Contacts
Search Contact
Exit

Bonus:
- Format the contact list in a table-like view
- Allow partial match search
- Prevent duplicate names from being added
"""

import csv
import os

FILENAME = "contacts.csv"

if not os.path.exists(FILENAME):
    with open(FILENAME, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Phone", "Email"])

def add_contact():
   name = input("Name: ").strip()
   phone = input("Phone: ").strip()
   email = input("Email: ").strip()

   #check for duplicates
   with open(FILENAME, 'r', encoding="utf-8") as f:
      reader = csv.DictReader(f)
      for row in reader:
          if row["name"].lower() == name.lower():
              print("Contact name already exists")
              return
   
   with open(FILENAME, 'a', encoding="utf-8") as f:
       writer = csv.writer(f)
       writer.writerow([name, phone, email])
       print("Contact added")

def view_contacts():
    with open(FILENAME, 'r', encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)
        if len(rows) < 1:
            print("no contacts found")
            return
        print("\nYour contacts: \n")
        for row in rows[1:]: #to start from second row as rows[0] is the heading - name, phone, email
            print(f"{row[0]} | {row[1]} | {row[2]}")
        print()

def search_contact():
    term = input("Enter the name to search: ").strip().lower()
    found = False
    with open(FILENAME, 'r', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if term in row["Name"].lower:
                print(f"{row["Name"]} | {row["Phone"]} | {row["Email"]}")
                found = True
    if not found:
        print("No matching contact found")
       

   

