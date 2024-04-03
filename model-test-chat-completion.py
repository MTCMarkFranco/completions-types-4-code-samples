import os
from openai import AzureOpenAI
from dotenv import load_dotenv
load_dotenv()

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-02-01",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

messages = [
    {
        "role": "system",
        "content": "You are an AI assistant."
    },
    {
        "role": "user",
        "content": "Create a function to call an Entra ID Protected API Passing in a bearer token using the MSAL library. Use this version of the MSAL library: https://pypi.org/project/msal/1.27.0/"
    }
]

response = client.chat.completions.create(
    model="gpt-4",
    messages= messages,
    max_tokens=800
)

print(response.choices[0].message.content)
