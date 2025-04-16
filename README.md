## Overview

This project is designed to automate the process of researching and writing blog posts based on video content from YouTube channels. It utilizes AI agents to perform tasks such as video research and content creation, leveraging advanced language models and embedding tools.

## Components

### Agents

- **Blog Researcher**: An AI agent responsible for gathering relevant video content from YouTube channels and the internet. It is equipped with memory capabilities and can delegate tasks.
- **Blog Writer**: An AI agent skilled in transforming research into engaging blog posts. It focuses on creating narratives that capture the essence of video content while enhancing readability and SEO performance.

### Tasks

- **Research Task**: This task involves identifying videos related to a given topic and gathering detailed information from YouTube channels.
- **Write Task**: This task summarizes the information from YouTube videos and creates content for blog posts.

### Tools

- **YouTube Channel Search Tool**: A tool configured to search for video content on specific YouTube channels using AI models for language processing and embedding.

## Configuration

The project uses environment variables to configure API keys for language models and embedding tools. Ensure that the `.env` file contains the necessary keys:

- `GroqApi`: API key for the Groq language model.
- `HuggingFaceApi`: API key for the Hugging Face embedding model.

## Usage

1. **Setup**: Ensure that the environment variables are set up in the `.env` file.
2. **Execution**: Run the main script to initiate the crew and execute tasks based on the provided topic.

## Dependencies

- Python packages: `crewai`, `crewai_tools`, `dotenv`, `langchain_groq`
- Ensure that the virtual environment is activated and dependencies are installed.

