import os

SECRET_KEY = os.environ.get("SECRET_KEY", "secret key!!!!")

FULL_NAME = {
    "first": os.environ.get("first_name"),
    "last": os.environ.get("last_name")
}

DEFAULT = {
    "greeting": "Hello ,\n",
    "intro": """I'm James, a Software Engineer in San Francisco.""",
    "outro": "As a software engineer with lots to look forward to, I would be thrilled to hear back!"
}