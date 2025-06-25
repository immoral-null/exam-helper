import base64
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI
from openai.types.chat import ChatCompletionUserMessageParam

load_dotenv()
client = OpenAI()


def ask_chatgpt(image_path: Path) -> str:
    with image_path.open("rb") as f:
        img_b64 = base64.b64encode(f.read()).decode()

    message: ChatCompletionUserMessageParam = {
        "role": "user",
        "content": [  # type: ignore
            {"type": "text", "text": "Answer this exam question clearly and briefly."},
            {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{img_b64}"}},
        ],
    }

    resp = client.chat.completions.create(
        model="gpt-4o",
        messages=[message],
        max_tokens=500,
    )

    return resp.choices[0].message.content.strip()
