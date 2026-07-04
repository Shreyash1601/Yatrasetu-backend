import json

from google import genai
from google.genai import types

from utils.config import Config
from utils.constants import SYSTEM_PROMPT


class GeminiService:

    def __init__(self):
        self.client = genai.Client(
            api_key=Config.GEMINI_API_KEY
        )

        self.model = Config.MODEL_NAME

    def generate_text(self, prompt: str) -> str:
        """
        Generates plain text response from Gemini.
        """

        try:

            response = self.client.models.generate_content(
                model=self.model,
                contents=f"{SYSTEM_PROMPT}\n\n{prompt}"
            )

            return response.text

        except Exception as e:
            raise Exception(f"Gemini Error: {str(e)}")

    def generate_json(self, prompt: str) -> dict:
        """
        Forces Gemini to return valid JSON.
        """

        try:

            response = self.client.models.generate_content(
                model=self.model,
                contents=f"""
{SYSTEM_PROMPT}

Respond ONLY with valid JSON.

{prompt}
""",
                config=types.GenerateContentConfig(
                    response_mime_type="application/json"
                )
            )

            return json.loads(response.text)

        except Exception as e:
            raise Exception(f"Gemini JSON Error: {str(e)}")


# Singleton instance
gemini_service = GeminiService()