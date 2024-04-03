import os
from openai import AzureOpenAI
from dotenv import load_dotenv
load_dotenv()

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-02-01",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

response = client.completions.create(
    model="gpt-35-turbo-instruct",
    prompt= """
    
           # language=en-ca
           # Create a function to call an Entra ID Protected API Passing in a bearer token using the MSAL library
           # us this version of the MSAL library: https://pypi.org/project/msal/1.27.0/
            
            """

,
    max_tokens=800
)

for choice in response.choices:
    print(choice.text)


