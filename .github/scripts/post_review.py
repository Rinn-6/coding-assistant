import os
import json
import requests

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_REPO = os.getenv("GITHUB_REPOSITORY")
PR_NUMBER = os.getenv("GITHUB_REF").split("/")[-1]

HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json",
}

# Load AI-generated reviews
with open(".github/scripts/review_comments.json") as file:
    review_comments = json.load(file)

# Post reviews to PR
for filename, comment in review_comments.items():
    url = f"https://api.github.com/repos/{GITHUB_REPO}/pulls/{PR_NUMBER}/comments"
    data = {
        "body": f"### AI Code Review:\n{comment}",
        "commit_id": os.getenv("GITHUB_SHA"),
        "path": filename,
        "position": 1,
    }
    requests.post(url, headers=HEADERS, json=data)
