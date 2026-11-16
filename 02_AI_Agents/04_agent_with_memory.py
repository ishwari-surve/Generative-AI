# ============================================================
# Program : AI Agent with Memory
# Author  : Ishwari Vijaykumar Surve
# Target:
# Build an agent that remembers the user's name during
# the conversation and can show what is stored in memory 
# ============================================================

print("=" * 60)
print("   Generative AI : AI Agents")
print("   Program : AI Agent with Memory")
print("=" * 60)

memory = {}

def agent(user_input):
    words = user_input.split()

    if "my name is" in user_input.lower():
        name = user_input.lower().replace("my name is", "").strip()
        memory["name"] = name
        return f"Nice to meet you, {name}"

    elif "what is my name" in user_input.lower():
        if "name" in memory:
            return f"Your name is {memory['name']}"
        else:
            return "I do not know your name yet."

    elif "show memory" in user_input.lower():
        return str(memory)

    else:
        return "I can remember your name. Try: My name is Rahul"

while True:
    query = input("User: ")

    if query.lower() == "exit":
        print("Agent: Goodbye!")
        break

    print("Agent:", agent(query))
