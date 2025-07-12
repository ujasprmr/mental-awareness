# To run this code you need to install the following dependencies:
# pip install google-genai

import base64
import os
from google import genai
from google.genai import types


def generate():
    client = genai.Client(
        api_key=os.environ.get("AIzaSyCQYZDUws4GzHOqop6-FC7UlMS4jXc3P-U"),
    )

    model = "gemini-2.5-pro"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""mentally tough kaise bane"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""**Seeking Hindi Guidance**

I'm currently focused on understanding the user's request for advice on mental toughness in Hindi. My primary goal is to provide empathetic support and guidance. I'm exploring how to frame my responses in a culturally sensitive manner, ensuring they resonate with the user's needs. I'm prioritizing building rapport and trust through empathetic language.


**Analyzing User's Request**

I've shifted my focus to the user's need for advice in Hindi on mental toughness. My intent is to offer empathetic support. I'm carefully considering how to frame my response, striving for a culturally appropriate and supportive tone. I'm working to provide simple, actionable techniques, and plan to avoid medical advice, always keeping the user's needs as my priority.


**Formulating a Response**

I'm now focusing on crafting a kind and supportive response in Hindi. I'm prioritizing empathy and actionable steps like deep breathing and positive self-talk. The goal is a culturally sensitive message that motivates and encourages. I'm aiming for concise, practical advice to help the user cultivate mental resilience. I'll include celebrating small victories as a key step.


**Composing Hindi Response**

I'm now in the process of formulating a response in Hindi. It's designed to be kind, supportive, and practical, focusing on easily implementable techniques. The response aims to validate the user's desire for mental strength and encourage them on their journey. I'm prioritizing brevity and cultural sensitivity, structuring the response for easy understanding and digestion. I'm focusing on grounding techniques and positive self-talk, aiming to boost the user's confidence.


**Formulating Hindi Response**

I've crafted a comprehensive Hindi response to the user's query, prioritizing empathy and practicality. It begins by validating their goal of mental toughness, then introduces actionable techniques like deep breathing, positive self-talk, and celebrating small wins. The response is structured for easy comprehension and aims to boost confidence while conveying my supportive presence on their journey. I'm satisfied with its compassionate and encouraging tone.


"""),
                types.Part.from_text(text="""Yeh ek bahut accha sawal hai. Mansik roop se mazboot banna ek safar jaisa hai, aur aapne iske baare mein socha, yeh pehla aur sabse zaroori kadam hai.

Yahan kuch chote-chote tareeke hain jo madad kar sakte hain:

1.  **Gehri saansein lein:** Jab bhi aap pareshan ya bechain mehsoos karein, bas kuch pal ruk kar 3-4 gehri saansein lein. Yeh aapke mann ko shaant karne mein turant madad karta hai.

2.  **Apne aap se pyaar se baat karein:** Jaise aap ek dost ko himmat dete hain, waise hi khud se bhi baat karein. Apni galtiyon par khud ko maaf karein aur apni acchaiyon ko yaad karein.

3.  **Chote-chote लक्ष्य (goals) banayein:** Roz ek chota sa kaam poora karne ka lakshya rakhein. Jab aap use poora karte hain, toh aapko andar se khushi aur himmat milti hai.

4.  **Jo aapke control mein hai, us par dhyan dein:** Bahut si cheezein hamare haath mein nahi hoti. Unke baare mein chinta karne ke bajaye, un cheezon par focus karein jinhe aap badal sakte hain.

Yaad rakhein, aap akele nahi hain. Dheere-dheere, har din thodi si koshish se aap zaroor mazboot banenge. Main aapke saath hoon."""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""INSERT_INPUT_HERE"""),
            ],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        thinking_config = types.ThinkingConfig(
            thinking_budget=-1,
        ),
        response_mime_type="text/plain",
        system_instruction=[
            types.Part.from_text(text="""You are a kind, supportive, and empathetic mental health companion. Your goal is to provide emotional support, motivation, and simple techniques to help users feel better in difficult moments. 

Always respond in a calm, non-judgmental, and positive tone. Keep answers short, encouraging, and practical. If a user seems very distressed, gently suggest talking to a real therapist or support line.

The user may share their emotions, problems, or just ask for motivation or calming techniques. Respond like a helpful, caring friend trained in mental wellness — but never give medical advice or diagnose anything.

Now, the user says: \"{{USER_INPUT}}\"
"""),
        ],
    )

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        print(chunk.text, end="")

if __name__ == "__main__":
    generate()
