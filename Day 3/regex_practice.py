import re 


text_to_search = """
Hello, my name is John Doe, and I live at 123 Main St. in Springfield. 
My email address is john.doe123@example.com, and my phone number is (555) 123-4567.

abcdefg

I recently bought the following items:
- A new laptop for $1,299.99 (Model: X1#Pro@2024)
- A chair for $150
- 3 packs of AAA batteries (SKU: BAT-AAA-5678)

My friend's name is Jane Smith; her email is jane_smith89@mail.co.uk. 
She owes me $250, which she promised to pay by 12/31/2024.

Some random symbols: @#$%^&*()_+=[]{};:'"<>?/\\|`~!
Some random numbers: 42, 31415, 8675309.
"""


pattern = re.compile(r'.')

matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)
