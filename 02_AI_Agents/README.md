# 02 AI Agents

## About
An agent is a program that reads the user's message, decides what to do,
and then answers. It can use tools (like a calculator) and keep memory.
These four programs build a simple agent step by step.
They use plain Python only. No AI model or internet is needed.

## Steps
1. Rule based agent: replies using fixed keyword rules.
2. Calculator agent: uses one tool.
3. Multi tool agent: chooses one tool out of several.
4. Memory agent: remembers information during the conversation.

## Files
| File | What it does |
|---|---|
| 01_rule_based_agent.py | Answers hello, course, fees and bye using keyword rules |
| 02_calculator_agent.py | Sends the text after "calculate" to a calculator tool |
| 03_multiple_tools_agent.py | Chooses between a calculator, a time tool, a date tool and a course answer |
| 04_agent_with_memory.py | Saves the user's name in a dictionary and can show it again |

## Example conversation
Program 02:
- User: calculate 10 + 20
- Agent: The calculated answer is: 30

Program 03:
- User: what is the time
- Agent: Current time is: (current time in HH:MM:SS)

Program 04:
- User: my name is Rahul
- Agent: Nice to meet you, rahul
- User: what is my name
- Agent: Your name is rahul

## Key points
- Tool: a function the agent can call (calculator, show_time, show_date).
- The agent chooses the tool by looking for a keyword in the user's text.
- The order of the if and elif checks matters. The first match wins.
- Memory: a dictionary (memory = {}) that keeps data while the program runs.
- Type exit to stop programs 02, 03 and 04. In program 01 type bye.

## Limits of these agents
- They do not understand meaning. They only look for keywords.
  For example, the keyword "time" also matches inside other words.
- The calculator uses eval(). eval() runs any Python code that is typed,
  so it is not safe for a real application. It is used here for learning only.
- Memory is lost when the program stops. It is not saved in a file.
- A real AI agent uses a language model to understand the request and choose the tool.

## Concepts covered
- Functions as tools
- Keyword matching with if, elif and else
- while loop for a conversation
- Dictionary as memory
- String methods: lower, replace, strip
- datetime module for time and date

## Requirements
- Python 3 (no extra library)

## Run
python 01_rule_based_agent.py
python 02_calculator_agent.py
python 03_multiple_tools_agent.py
python 04_agent_with_memory.py
