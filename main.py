from crew_logic import research_agent, writer_agent, editor_agent
from agents import init_gemini

def main():
    init_gemini()
    topic = "How AI is changing education"

    print("🎓 Researching the topic...")
    notes = research_agent(topic)
    print(f"\n📚 Research Notes:\n{notes}")

    print("\n✍️ Writing blog post...")
    blog = writer_agent(notes)
    print(f"\n📝 Draft Blog:\n{blog}")

    print("\n🧹 Editing the blog post...")
    final = editor_agent(blog)
    print(f"\n✅ Final Blog Post:\n{final}")

if __name__ == "__main__":
    main()
