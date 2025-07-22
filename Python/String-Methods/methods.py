# Assignment 3: String Methods

# 1. Combine first and last name
first_name = "Priyanka"
last_name = "Desale"
full_name = first_name + " " + last_name
print("Full Name:", full_name)

# 2. Formatted string with item and price
item = "Laptop"
price = 799.99
print(f"The price of {item} is ${price}")

# 3. Convert string to uppercase
text = "hello world"
print("Uppercase:", text.upper())

# 4. Use .join() to form a sentence
words = ['Python', 'is', 'awesome']
sentence = " ".join(words)
print("Joined Sentence:", sentence)

# 5. Print today's date in DD-MM-YYYY format
from datetime import datetime
today = datetime.today()
formatted_date = today.strftime("%d-%m-%Y")
print("Today's Date:", formatted_date)
