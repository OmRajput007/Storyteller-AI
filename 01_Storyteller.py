import openai
import gradio as gr

client = openai.OpenAI(
    api_key="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",    
    organization="org-dPxocCavkHBZMkU78g4EFuGf",             
    project="proj_6WQjQzvnrtQoY5Yiq3mAHgTj"                  
)


def ask_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"You are a poetic storyteller who turns boring facts into epic YouTube scripts."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

gr.Interface(fn=ask_gpt, inputs="text", outputs="text").launch()

