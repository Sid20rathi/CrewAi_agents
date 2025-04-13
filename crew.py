from crewai import Crew,Process
from agents import blog_researcher,blog_writer
from tasks import research_task,write_task
from crewai import LLM
import os
from dotenv import load_dotenv
load_dotenv()
Groqapi=os.getenv("GroqApi")


llm = LLM(
    model="groq/llama-3.2-90b-text-preview",
    temperature=0.7,
    api=Groqapi
)

crew = Crew(
    agents=[blog_researcher,blog_writer],
    tasks=[research_task,write_task],
    process=Process.sequential,
    llm = llm,
    memory=True,
    cache=True,
    max_rpm=100,
    share_crew=True
)

result = crew.kickoff(inputs={'topic':'Rasraj Ji Maharaj se Janiye Hanuman Ji ki Bhakti kase kare'})
print(result)

