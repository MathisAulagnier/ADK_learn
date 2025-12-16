from google.adk.agents.llm_agent import Agent

# Mock tool implementation
def get_current_time(city: str) -> dict:
    """Returns the current time in a specified city."""
    return {"status": "success", "city": city, "time": "10:30 AM"}

def get_weather(city: str) -> dict:
    """Returns the current weather in a specified city."""
    return {"status": "success", "city": city, "weather": "Sunny, 25°C"}

root_agent = Agent(
    model='gemini-2.0-flash',
    name='root_agent',
    description="Useful agent which answers all questions without hesitation.",
    instruction="You are a helpful assistant that answer all questions without hesitation. You have 2 tools available: get_current_time and get_weather. The first tool returns the current time in a specified city, and the second tool returns the current weather in a specified city.",
    tools=[get_current_time, get_weather],
)