import openai
import gradio as gr
import os
from dotenv import load_dotenv

# Load your API keys from .env file
load_dotenv()

openai_api_key = os.getenv("api_key")
organization_id = os.getenv("organization")
project_id = os.getenv("project")

# Create the OpenAI client securely
client = openai.OpenAI(
    api_key=openai_api_key,
    organization=organization_id,
    project=project_id
)

# Your GPT function
def ask_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a poetic storyteller who turns boring facts into epic YouTube scripts."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

# Launch Gradio interface
gr.Interface(fn=ask_gpt, inputs="text", outputs="text").launch()
