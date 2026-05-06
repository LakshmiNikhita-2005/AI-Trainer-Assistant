from openai import OpenAI

client = OpenAI(api_key="your_api_key_here")

def generate_content(text, task):

    prompt = f"""
    You are an AI trainer.

    Based on the following course material:

    {text[:3000]}

    Generate {task}.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content