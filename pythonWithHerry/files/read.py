# f = open("test.txt", "r")

# content = f.read()
# print(content)

# f.close()

# ------------------------
# with open("john.txt","r") as f:
#   content = f.read()
#   print(content)
#   #no need to close file if we use with because it alrady closed by default.



# line by line ----------------------------
f = open("john.txt","r")

for line in f:
    print(line)

f.close()