import os
import google.generativeai as genai
from .base import AIService

class GeminiService(AIService):
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        if not self.api_key:
             print("Warning: GEMINI_API_KEY not found.")
        else:
            genai.configure(api_key=self.api_key)

    async def generate_job_description(self, title: str) -> str:
        if not self.api_key:
            return f"[Mock Gemini] Job description for {title} (No API Key provided)"
        
        try:
            model = genai.GenerativeModel('gemini-pro')
            response = await model.generate_content_async(f"Generate a detailed job description for a {title}.")
            return response.text
        except Exception as e:
            return f"Error generating description: {str(e)}"

    async def generate_skill_summary(self, skill_name: str) -> str:
        if not self.api_key:
             return f"[Mock Gemini] Skill summary for {skill_name} (No API Key provided)"

        try:
            model = genai.GenerativeModel('gemini-pro')
            response = await model.generate_content_async(f"Explain why learning {skill_name} is valuable and how to start.")
            return response.text
        except Exception as e:
             return f"Error generating summary: {str(e)}"

    async def generate_digest(self, topic: str = "AI Trends") -> str:
        if not self.api_key:
             return f"[Mock Gemini] Digest on {topic} (No API Key provided)"

        try:
            model = genai.GenerativeModel('gemini-pro')
            response = await model.generate_content_async(f"Write a short, engaging news digest about the latest {topic}.")
            return response.text
        except Exception as e:
             return f"Error generating digest: {str(e)}"
