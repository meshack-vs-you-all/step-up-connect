from abc import ABC, abstractmethod

class AIService(ABC):
    @abstractmethod
    async def generate_job_description(self, title: str) -> str:
        pass

    @abstractmethod
    async def generate_skill_summary(self, skill_name: str) -> str:
        pass
