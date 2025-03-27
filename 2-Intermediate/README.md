# Intermediate

## Table of Contents
 - [What to Expect](#what-to-expect)
 - [OpenAI API](#openai-api)
    - [Starting Out](#starting-out)
 - [Agents](#agents)
 - [Local AI](#local-ai)

## What to Expect
I'm expecting this section to really open your eyes to truly see the possibilities of what's really out there. If you have the mind of a programmer or developer, you'll be able to leverage this content pretty heavily. Ahead, I'll have some straightforward content that should help you see the big picture.

## OpenAI API
An API is an Application Programing Interface. Think of it as a way to communicate with an app. We use the APIs from OpenAI to get responses in different forms, including text, images, and audio. The [documentation](https://platform.openai.com/docs/guides/text?api-mode=chat) does a good job of showcasing those specific use cases. Trust me when I say that this usage will take your mindset and applications to a whole new level.

### Starting out
Unfortunately, API usage is generally not free. When you work with generative AI, you're charged by the number of "tokens" that you use in the initial as, and the number of tokens that the AI provides. A token is roughly 3 to 4 characters. You can view the standard pricing of different LLMs and modalities from OpenAI [here](https://platform.openai.com/docs/pricing). 

Easily enough, OpenAI has some pretty easy documentation for [getting started](https://platform.openai.com/docs/libraries?desktop-os=windows&language=python). You'll need an API key set in an environment variable on your device and the OpenAI library installed in your preferred development kit. The environment variable is in place to ensure integrity of your key. Otherwise, if hardcoded, people will see and use your key at your expense.

## Agents
You'll notice in this directory theres a folder titled [CrewAI-Screenplay](https://github.com/GoatEXE/Intro-to-AI/tree/main/2-Intermediate/CrewAI-Screenplay). CrewAI is an older method to employing "agents" ino a workflow, and I had created it to test the theory of it's usage. Think of an agent as someone who has a very specific job. In this case, I created agents to fulfill the role of a character with a specific personality. The manager coordinates these agents toward a specific outcome, which you should notice opens up into the world of automation. Thankfully, OpenAI now has a [development kit](https://platform.openai.com/docs/quickstart?api-mode=chat#build-agents) for agents as well.

## Local AI
Having a local AI means that you can reliably promise that your conversations and exchange of data never leaves your network. This means you can pass production data to it and modify or organize it while knowing that data isn't going anywhere toward the training of AI. All you'd need is a server or host PC (with respectable resources) and anohter device to communicate from. You can see this in action from the [Ollama-API](https://github.com/GoatEXE/Intro-to-AI/tree/main/2-Intermediate/Ollama-API)