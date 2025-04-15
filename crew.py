from crewai import Crew,Process
from agents import blog_researcher,blog_writer
from tasks import research_task,write_task
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
load_dotenv()
Groqapi=os.getenv("GroqApi")
agent_llm = ChatGroq(model="llama-3.2-90b-text-preview", api_key=Groqapi)




crew = Crew(
    agents=[blog_researcher,blog_writer],
    tasks=[research_task,write_task],
    process=Process.sequential,
    llm = agent_llm,
    memory=True,
    cache=True,
    max_rpm=100,
    share_crew=True
)

result = crew.kickoff(inputs={'topic':'Rasraj Ji Maharaj se Janiye Hanuman Ji ki Bhakti kase kare'})
print(result)

