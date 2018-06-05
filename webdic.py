import requests
    
# Get the word for searching 
word = "tax+meaning"

# Compite it into url
url = "https://www.google.com.tw/search?q=" + word

# Get translation into web content. 
webcontent = requests("https://www.google.com.tw/search?q=tax+meaning")

# Convert into plain text.
print(webcontent)
   

