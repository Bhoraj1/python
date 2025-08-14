import requests

r = requests.get('https://chatgpt.com/?openaicom_referred=true')
# print(r.text)
with open("data.txt", "w", encoding="utf-8") as f:  
    #encoding is used for saving like emoji ,special symbols,non-english characters.
    f.write(r.text)

 