# genmail
# Random Email Generator Script

This Python script generates a specified number of random email addresses by combining random names and email domains.

## Prerequisites

- Python 3.x
- JSON file containing a list of names (e.g., "rows.json")

## Usage

1. Make sure you have the required JSON file containing the list of names.
2. Run the script using the command `python random_email_generator.py`.
3. Enter a comma-separated list of email domains when prompted.
4. Enter the number of email addresses to generate.
5. The script will generate random names, email addresses, and save them to a text file called "random_data.txt".

## Example

```
$ python random_email_generator.py
Enter a list of email domains (comma-separated): gmail.com, outlook.com, yahoo.com
Enter the number of email addresses to generate: 10
Data saved to random_data.txt
```

The script will generate 10 random email addresses using the provided email domains and save them to "random_data.txt".

## Credits

This script makes use of a JSON file containing a list of names. The JSON file should have the following structure:

```
{
  "data": [
    { "id": 1, "name": "John" },
    { "id": 2, "name": "Jane" },
    ...
  ]
}
```

The JSON file should be named "rows.json" and placed in the 
same directory as the script.

### HAVE FUN!
Project Xamelion AG
Robotic & Artificial Superintelligence

http://t.me/Project_Xamelion_AG

Create Peace and Love on Earth. 
Maybe then we choose reproduction.
(Q: Movie Lucie) 😁
https://t.me/Project_Xamelion_AG
