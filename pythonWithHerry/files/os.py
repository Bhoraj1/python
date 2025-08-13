import os
# For showing current directory
print(os.getcwd())

# For verifying folder(Boolean)
# print(os.path.exists("dir"))

#show folder list
# a = os.listdir("../../15daysPython/01days")
# print(a)

# For Deleting file
os.remove("sample.txt")

# os.rmdir("dir")  #we need shutil package for delete files
