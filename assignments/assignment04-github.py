# Write a program in Python that will read a file from a repository
# The program should then replace all the instances of the text "Andrew" with your name. 
# The program should then commit those changes and push the file back to the repository 
# (You will need authorisation to do this).
# Author: Tanja Juric

# How to use API keys to access data

import requests
import json
#from config import config as cfg

filename = "assignment04.txt"

#url = 'https://api.github.com/repos/andrewbeattycourseware/datarepresentation/contents/code'
url = 'https://github.com/Tanja888/WSAA-coursework/blob/main/assignments/assignment04.txt'

#apikey = cfg["githubkey"]
response = requests.get(url)

print(response.status_code)
#print (response.json())

with open(filename, 'r') as fp:
    print(fp.read())
