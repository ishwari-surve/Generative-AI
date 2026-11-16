# ============================================================
# Program : AI Agent with Calculator Tool
# Author  : Ishwari Vijaykumar Surve
# Target:
# Build an agent that uses a calculator tool when the user
# writes "calculate" followed by an expression
# ============================================================

print("=" * 60)
print("   Generative AI : AI Agents")
print("   Program : AI Agent with Calculator Tool")
print("=" * 60)

def calculator(expression):
    try:
        result = eval(expression)
        return result
    except:
        return "Invalid mathematical expression"

def agent(user_input):
    if "calculate" in user_input.lower():
        expression = user_input.lower().replace("calculate", "")
        answer = calculator(expression)
        return f"The calculated answer is: {answer}"
    else:
        return "I can calculate mathematical expressions. Example: calculate 10 + 20"

while True:
    query = input("User: ")

    if query.lower() == "exit":
        print("Agent: Goodbye!")
        break

    response = agent(query)
    print("Agent:", response)
