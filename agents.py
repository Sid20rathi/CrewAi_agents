from crewai import Agent 
from tools import youtube_channel_tool


blog_researcher = Agent(
    role='Blog Researcher',
    goal='get the relevant  video content for the topic{topic} from the yt channel',
    verbose=True,
    memory=True,
    backstory=(
        "expert in understanding videos and their content and their relevance to the topic and gather relevant information from the internet also "
    ),
    tools=[],
    allow_delegation = True
)

blog_writer= Agent(
    role='Blog Writer',
    goal='Narrate compelling stories about the topic{topic} using the information gathered from the yt channel',
    verbose=True,
    memory=True,
    backstory=(
        "Expert content creator with a talent for transforming research into engaging blog posts. Skilled at crafting narratives that capture the essence of video content while adding valuable context and insights. Able to maintain the original voice and style while enhancing readability and SEO performance. Experienced in creating content that resonates with target audiences and drives engagement."
    ),
    tools=[youtube_channel_tool],
    allow_delegation = False
)





