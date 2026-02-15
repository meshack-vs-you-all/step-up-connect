import os
from .base import AIService
from .openai_service import OpenAIService
from .gemini_service import GeminiService

class AIMockService(AIService):
    async def generate_job_description(self, title: str) -> str:
        return f"[Mock Default] Job description for {title}"

    async def generate_skill_summary(self, skill_name: str) -> str:
         return f"[Mock Default] Skill summary for {skill_name}"

def get_ai_service() -> AIService:
    provider = os.getenv("AI_PROVIDER", "mock").lower()
    
    if provider == "openai":
        return OpenAIService()
    elif provider == "gemini":
        return GeminiService()
    else:
        return AIMockService()
