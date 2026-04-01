import random


def create_marketing_hook(topic, platform):
    emojis = ["🚀", "💡", "🎯", "🔥"]
    selected_emoji = random.choice(emojis)  # Using a 'Library' tool
    if platform == "Twitter":
        return f"🔥 Hot Take on {topic}: AI is the future!"
    elif platform == "LinkedIn":
        return f"Professional Insight: Exploring the impact of {topic} on modern business."
    elif platform == "Instagram":
        return f"{selected_emoji}Have you seen this hook for {topic}retun with emoji"
    else:
        return f"Check out this content about {topic}."


# Using the tool (The 'Build' part)
my_post = create_marketing_hook("Python", "Instagram")

print(f"Agent Output: {my_post}")
