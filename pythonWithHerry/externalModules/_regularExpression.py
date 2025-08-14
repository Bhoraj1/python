import re

text = "The quick brown box jumps over the lazy dog Box box"
# search for an pattern that matches the word "box"
match = re.search("bo", text)
# # print(match)
if match:
    print(match.group())
    print("Found")
    print("Start index",match.start())
    print("End index", match.end())

# #Find all occurrences of the pattern
matches = re.findall("box", text, re.IGNORECASE)  # case-insensitive search
print("Matches:",matches)   


# # Virtually Replace the pattern with another string
with open("data.txt", "r", encoding="utf-8") as f:
    text = f.read()
    print("Original text:", text)
    
new_text = re.sub("pass", "meow", text)  #flags=re.IGNORECASE 
print("New text:", new_text)


# for more : https://regexr.com/


# next code ----------------------------------
# Open and read the contents of data.txt
with open("data.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Search for a pattern, for example "box"
match = re.search("container", text)

if match:
    print("Found")
    print("Start index:", match.start())
    print("End index:", match.end())
else:
    print("Pattern not found")
