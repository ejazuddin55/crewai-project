from agents import run_agent

def research_agent(topic):
    prompt = f"Research this topic and provide 5 important points: {topic}"
    return run_agent(prompt)

def writer_agent(research_notes):
    prompt = f"Write a short blog post (600 words) using these notes:\n{research_notes}"
    return run_agent(prompt)

def editor_agent(blog_text):
    prompt = f"Edit and improve this blog post for grammar and clarity:\n{blog_text}"
    return run_agent(prompt)
