from crewai import  Task
from tools import youtube_channel_tool
from agents import blog_researcher,blog_writer

research_task = Task(
    description=(
        "identify the video{topic}."
        "Get detailed information about the video from the yt channel"

    ),
    expected_output='A detailed 3 paragraphs long report based on the {topic} of video and relevant information from the internet',
    tools=[youtube_channel_tool],
    agent=blog_researcher
)

write_task = Task(
    description=(
        "get the info from the youtube channel on the topic {topic}."
    ),
    expected_output='Summarize the info from the youtube channel video on the topic{topic} and create the content for the blog',
    tools=[youtube_channel_tool],
    agent=blog_writer,
    async_execution=False,
    output_file='new-blog-post.md'
)






