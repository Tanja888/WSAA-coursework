from github import Github
from config import config as cfg
import requests

apikey = cfg["githubkey"]
g = Github(apikey)

# Clone URL of a repository 
repo = g.get_repo("Tanja888/WSAA-coursework")
# print(repo.clone_url)

fileInfo = repo.get_contents("assignment04.txt")
urlOfFile = fileInfo.download_url
# print(urlOfFile)

response = requests.get(urlOfFile)
contentOfFile = response.text
print(contentOfFile)

# Replace the instances of Andrew with Tanja
newContents = contentOfFile.replace("Andrew", "Tanja")
print(newContents)

# Update the contents of the file on Github
# update_file(path, message, content, sha, branch=NotSet, committer=NotSet, author=NotSet)
gitHubResponse = repo.update_file(fileInfo.path, "updated by prog", newContents, fileInfo.sha)
print(gitHubResponse)