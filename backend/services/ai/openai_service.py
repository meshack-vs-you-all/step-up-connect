import os
import openai
from .base import AIService

class OpenAIService(AIService):
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        if not self.api_key:
             # In production, log warning or raise error. For now, we allow mock fallback if key missing.
             print("Warning: OPENAI_API_KEY not found.")
        else:
            openai.api_key = self.api_key

    async def generate_job_description(self, title: str) -> str:
        if not self.api_key:
            return f"[Mock OpenAI] Job description for {title} (No API Key provided)"
        
        try:
            response = await openai.ChatCompletion.acreate(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful HR assistant."},
                    {"role": "user", "content": f"Generate a detailed job description for a {title}."}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error generating description: {str(e)}"

    async def generate_skill_summary(self, skill_name: str) -> str:
        if not self.api_key:
            return f"[Mock OpenAI] Skill summary for {skill_name} (No API Key provided)"

        try:
            response = await openai.ChatCompletion.acreate(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are an expert career coach."},
                    {"role": "user", "content": f"Explain why learning {skill_name} is valuable and how to start."}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
             return f"Error generating summary: {str(e)}"
