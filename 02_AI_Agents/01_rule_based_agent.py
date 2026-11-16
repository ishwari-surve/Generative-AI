# ============================================================
# Program : Simple Rule Based AI Agent
# Author  : Ishwari Vijaykumar Surve
# Target:
# Build a simple agent that replies using fixed keyword rules
# ============================================================

print("=" * 60)
print("   Generative AI : AI Agents")
print("   Program : Simple Rule Based AI Agent")
print("=" * 60)

def simple_agent(user_input):
    user_input = user_input.lower()

    if "hello" in user_input:
        return "Hello Jay Ganesh.. How can I help you?"

    elif "course" in user_input:
        return "Courses available: C, C++, Java, Python, AI, ML and Logic Building."

    elif "fees" in user_input:
        return "Please contact the institute office for the detailed fee structure."

    elif "bye" in user_input:
        return "Thank you! Have a great day."

    else:
        return "Sorry, I did not understand your query."

while True:
    query = input("User: ")

    response = simple_agent(query)
    print("Agent:", response)

    if "bye" in query.lower():
        break
