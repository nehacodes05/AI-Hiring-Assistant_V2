import os
import json

from dotenv import load_dotenv
from google import genai
from utils.prompts import ATS_PROMPT

# load environment variable from .env
load_dotenv()


# create Gemini client once when the application starts
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def analyze_resume_with_gemini(resume_text):

    prompt = f"""
    {ATS_PROMPT}

    Resume:

    {resume_text}
    """

    response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)

    response_text = response.text

    print(resume_text)
    print(type(resume_text))
    analysis = json.loads(response_text)

    print(analysis)
    print(type(analysis))

    return analysis
