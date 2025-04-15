from crewai_tools import YoutubeChannelSearchTool
import os
from dotenv import load_dotenv
load_dotenv()
Groqapi=os.getenv("GroqApi")
HuggingFaceApi=os.getenv("HuggingFaceApi")




youtube_channel_tool = YoutubeChannelSearchTool(
    youtube_channel_handle='@InspiredForImpact',
    config=dict(
        llm=dict(
            provider="groq",
            config=dict(
                model="llama-3.2-90b-text-preview",
                api_key=Groqapi,
              
            ),
        ),
        embedder=dict(
            provider="huggingface", 
            config=dict(
                model="sentence-transformers/all-MiniLM-L6-v2",
                api_key=HuggingFaceApi,
              
            ),
        ),
    )
)

