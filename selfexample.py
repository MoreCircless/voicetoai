import gradio as gr
import whisper
import os
from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()

client = OpenAI()
client.api_key = os.getenv("OPENAI_API_KEY")

whisper = whisper.load_model("base")


def elpatron(test):
    result = whisper.transcribe(audio=test, verbose=True, language="en")
    text = result.get("text", "")
    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": f"{text}"
        }
    ]
    )   
    return completion.choices[0].message.content



if __name__ == "__main__":
    gr.Interface(
        theme=gr.themes.Soft(),
        fn=elpatron,
        live=True,
        inputs= gr.Audio(sources="microphone", type="filepath"),
        outputs="text"
        ).launch()