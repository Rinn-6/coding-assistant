import os
import openai
import json

# Load OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Function to review code
def review_code(file_content):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a professional code reviewer."},
            {"role": "user", "content": f"Review this code and suggest improvements:\n{file_content}"}
        ]
    )
    return response["choices"][0]["message"]["content"]

# Load changed files (simulating Git diff)
changed_files = {
    "sort.py": "def quicksort(arr):\n    if len(arr) <= 1:\n        return arr\n    pivot = arr[len(arr) // 2]\n    left = [x for x in arr if x < pivot]\n    middle = [x for x in arr if x == pivot]\n    right = [x for x in arr if x > pivot]\n    return left + middle + right"
}

# Generate AI reviews
reviews = {file: review_code(content) for file, content in changed_files.items()}

# Save reviews to JSON
with open(".github/scripts/review_comments.json", "w") as file:
    json.dump(reviews, file)
