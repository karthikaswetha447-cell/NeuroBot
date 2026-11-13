
import os
import gradio as gr
from groq import Groq

client = Groq(api_key=os.environ["GROQ_API_KEY"])
model_name = "openai/gpt-oss-20b"

def neurobot(message, history):
    messages = [
        {
            "role": "system",
            "content": "You are NeuroBot, a friendly AI assistant created by NeuroGen AI Academy. Answer clearly and helpfully."
        }
    ]

    for item in history or []:
        if isinstance(item, dict):
            if item.get("role") in ["user", "assistant"]:
                messages.append({
                    "role": item["role"],
                    "content": item["content"]
                })

    messages.append({"role": "user", "content": message})

    response = client.chat.completions.create(
        model=model_name,
        messages=messages
    )

    return response.choices[0].message.content

demo = gr.ChatInterface(
    fn=neurobot,
    title="🤖 NeuroBot",
    description="Your AI Assistant | Powered by NeuroGen AI Academy"
)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=int(os.environ.get("PORT", 7860)))
