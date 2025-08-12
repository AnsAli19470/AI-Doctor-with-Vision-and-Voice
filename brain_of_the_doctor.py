import os
import base64
from dotenv import load_dotenv
from groq import Groq

# 1. Load API key
load_dotenv()
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")


# 2. Encode image
#image_path = 'mm.jpg'
def encode_image(image_path):   
    image_file=open(image_path, "rb")
    return base64.b64encode(image_file.read()).decode('utf-8')

# 3. Use vision-capable model
query = "What is wrong with this condition?"
model = "meta-llama/llama-4-scout-17b-16e-instruct"

def analyze_imaege_with_querry(query, model,encode_image):
    client = Groq()
    messages = [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": query},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{encode_image}"
                    }
                }
            ]
        }
    ]

    # 4. Create chat completion
    chat_completion = client.chat.completions.create(
    messages=messages,
        model=model
        
    )

    # 5. Print result
    return chat_completion.choices[0].message.content
