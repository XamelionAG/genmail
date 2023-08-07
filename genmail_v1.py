import random
import string
import json

# Read the data from the local file
with open("rows.json") as file:
    json_data = file.read()

# Parse the JSON data
data = json.loads(json_data)
names = data["data"]

def get_random_name():
    # Get a random name from the data
    random_name = random.choice(names)[11]
    
    return random_name.lower()

def generate_email_address(name, domain):
    # Generate an email address by appending "@" and a domain name
    email = name + "@" + domain
    return email

# List of email domains
email_domains = input("Enter a list of email domains (comma-separated, without space): ").split(",")

# Number of email addresses to generate
num_emails = int(input("Enter the number of email addresses to generate: "))

# Generate random names, email addresses, and URLs
data = []
for _ in range(num_emails):
    name = get_random_name()
    domain = random.choice(email_domains)
    email = generate_email_address(name, domain)
    
    data.append({
        "Name": name,
        "Email": email #,
    })

# Save the data to a text file
with open("random_data.txt", "w") as file:
    for entry in data:
        file.write(entry['Email'] + ",\n")

print("Data saved to random_data.txt")

