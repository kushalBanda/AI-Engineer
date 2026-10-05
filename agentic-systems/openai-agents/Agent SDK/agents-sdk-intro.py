# Converted from agents-sdk-intro.ipynb

# ## OpenAI's Agents SDK


# OpenAI have released an **Agents SDK**, their version of an open source agent development library.
#
# OpenAI have outlined a few features of the library:
#
# ```
# * Agent loop: Built-in agent loop that handles calling tools, sending results to the LLM, and looping until the LLM is done.
# * Python-first: Use built-in language features to orchestrate and chain agents, rather than needing to learn new abstractions.
# * Handoffs: A powerful feature to coordinate and delegate between multiple agents.
# * Guardrails: Run input validations and checks in parallel to your agents, breaking early if the checks fail.
# * Function tools: Turn any Python function into a tool, with automatic schema generation and Pydantic-powered validation.
# * Tracing: Built-in tracing that lets you visualize, debug and monitor your workflows, as well as use the OpenAI suite of evaluation, fine-tuning and distillation tools.
# ```
#
# ([source](https://openai.github.io/openai-agents-python/))
#
# We'll focus on covering the essentials here - including the **agent loop**, **python-first**, **guardrails**, and **function tools** features.
#
# Let's start by installing the library:


!uv pip install -qU openai-agents==0.0.3


# First let's set our [OpenAI API key](https://platform.openai.com/settings/organization/api-keys).


import os
from getpass import getpass

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY") or \
  getpass("Enter your OpenAI API key: ")


from agents import Agent, Runner

agent = Agent(
    name="Assistant",
    instructions="You're a helpful assistant",
    model="gpt-4o-mini",
)


# ## Running our Agent


# OpenAI gives us three methods for running our agent, all via a `Runner` class — those methods are:
#
# 1. `Runner.run()` which runs in async.
# 2. `Runner.run_sync()` which runs in sync.
# 3. `Runner.run_streamed()` which runs in async _and_ streams the response back to us.
#
# We'll quicky test method **(1)**:


result = await Runner.run(
    starting_agent=agent,
    input="tell me a short story"
)
result.final_output


# In most scenarios we'll likely want to be using method **(3)**, ie running async and streaming tokens. To do this we need to write a little more code to handle the async streaming and print the tokens as they're returned.
#
# First, we create a `RunResultStreaming` object by calling `Runner.run_streamed(...)`, we then _asynchronously_ iterate through the streamed events returned by our LLM using the `response.stream_events()` method:


response = Runner.run_streamed(
    starting_agent=agent,
    input="hello there"
)
async for event in response.stream_events():
    print(event)


# We can filter these various event types to find only raw tokens like so:


from openai.types.responses import ResponseTextDeltaEvent

# we do need to reinitialize our runner before re-executing
response = Runner.run_streamed(
    starting_agent=agent,
    input="tell me a short story"
)

async for event in response.stream_events():
    if event.type == "raw_response_event" and \
        isinstance(event.data, ResponseTextDeltaEvent):
        print(event.data.delta, end="", flush=True)


# ## Tools


# OpenAI included **function tools** as a key feature in their Agents SDK announcement. After turning everyone away from using _function calling_ to instead use _tool calling_, OpenAI have now decided that an LLM deciding to execute some code will be called _"function tools"_.
#
# To use _function tools_ in Agents SDK we simply decorate a function with the `@function_tool` decorator like so:


from agents import function_tool

@function_tool
def multiply(x: float, y: float) -> float:
    """Multiplies `x` and `y` to provide a precise
    answer."""
    return x*y


# Note that we have taken extra care to include a clear and descriptive function name, relatively clear parameter names, type annotations for both input parameters and expected output, and a natural language docstring that will be fed to the LLM and explain to it _what_ this tool does.
#
# To run our agent _with_ tools we simply pass our new tool into the `tools` parameter during `Agent` initialization.


agent = Agent(
    name="Assistant",
    instructions=(
        "You're a helpful assistant, remember to always "
        "use the provided tools whenever possible. Do not "
        "rely on your own knowledge too much and instead "
        "use your tools to help you answer queries."
    ),
    model="gpt-4o-mini",
    tools=[multiply]  # note that we expect a list of tools
)


# Now let's initialize a new runner and execute our agent with tools:


response = Runner.run_streamed(
    starting_agent=agent,
    input="what is 7.814 multiplied by 103.892?"
)

async for event in response.stream_events():
    print(event)


# If we look closely at the fourth event object we will see `ResponseFunctionToolCall`, meaning our `multiply` tool was called by our LLM. Following this event object we can also see several events containing the `ResponseFunctionCallArgumentsDeltaEvent` type inside the `data` field — these are the input parameters for our tool.
#
# Let's rerun that but this time we will process the event outputs to generate a cleaner and more readable output.


from openai.types.responses import (
    ResponseFunctionCallArgumentsDeltaEvent,  # tool call streaming
    ResponseCreatedEvent,  # start of new event like tool call or final answer
)

response = Runner.run_streamed(
    starting_agent=agent,
    input="what is 7.814 multiplied by 103.892?"
)

async for event in response.stream_events():
    if event.type == "raw_response_event":
        if isinstance(event.data, ResponseFunctionCallArgumentsDeltaEvent):
            # this is streamed parameters for our tool call
            print(event.data.delta, end="", flush=True)
        elif isinstance(event.data, ResponseTextDeltaEvent):
            # this is streamed final answer tokens
            print(event.data.delta, end="", flush=True)
    elif event.type == "agent_updated_stream_event":
        # this tells us which agent is currently in use
        print(f"> Current Agent: {event.new_agent.name}")
    elif event.type == "run_item_stream_event":
        # these are events containing info that we'd typically
        # stream out to a user or some downstream process
        if event.name == "tool_called":
            # this is the collection of our _full_ tool call after our tool
            # tokens have all been streamed
            print()
            print(f"> Tool Called, name: {event.item.raw_item.name}")
            print(f"> Tool Called, args: {event.item.raw_item.arguments}")
        elif event.name == "tool_output":
            # this is the response from our tool execution
            print(f"> Tool Output: {event.item.raw_item['output']}")


# ## Guardrails


# OpenAI have also included guardrails in the Agents SDK. These come as _input guardrails_ and _output guardrails_, the `input_guardrail` checks that the input going into your LLM is "safe" and the `output_guardrail` checks that the output from your LLM is "safe".
#
# Let's see how to use them. First, we'll implement a guardrail powered by another LLM (more tokens means more $$$ for OpenAI).


from pydantic import BaseModel

# define structure of output for any guardrail agents
class GuardrailOutput(BaseModel):
    is_triggered: bool
    reasoning: str

# define an agent that checks if user is asking about political opinions
politics_agent = Agent(
    name="Politics check",
    instructions="Check if the user is asking you about political opinions",
    output_type=GuardrailOutput,
)


# We can call this agent directly:


query = "what do you think about the labour party in the UK?"

result = await Runner.run(starting_agent=politics_agent, input=query)
result


# The output from our agent is hidden away in there, we extract it like so:


result.final_output


# To integrate this with our other agents we need to move our logic into a single function decorated with the `@input_guardrail` decorator.
#
# When defining these guardrails we need to follow the following structure:
#
# * Input parameters must include a `ctx` (context), `agent`, and `input` (the user's query in this case). Note that below we will only use the `input` parameter.
# * Output must be a `GuardrailFunctionOutput` object.


from agents import (
    GuardrailFunctionOutput,
    RunContextWrapper,
    input_guardrail
)

# this is the guardrail function that returns GuardrailFunctionOutput object
@input_guardrail
async def politics_guardrail(
    ctx: RunContextWrapper[None],
    agent: Agent,
    input: str,
) -> GuardrailFunctionOutput:
    # run agent to check if guardrail is triggered
    response = await Runner.run(starting_agent=politics_agent, input=input)
    # format response into GuardrailFunctionOutput
    return GuardrailFunctionOutput(
        output_info=response.final_output,
        tripwire_triggered=response.final_output.is_triggered,
    )


# Now we can initialize our normal agent with the `input_guardrails` parameter:


agent = Agent(
    name="Assistant",
    instructions=(
        "You're a helpful assistant, remember to always "
        "use the provided tools whenever possible. Do not "
        "rely on your own knowledge too much and instead "
        "use your tools to help you answer queries."
    ),
    model="gpt-4o-mini",
    tools=[multiply],
    input_guardrails=[politics_guardrail],  # note this is a list of guardrails
)


# Now let's run it! We'll stick with `Runner.run` for the sake of brevity:


result = await Runner.run(
    starting_agent=agent,
    input="what is 7.814 multiplied by 103.892?"
)
result.final_output


# Let's see if our guardrail will trigger:


result = await Runner.run(
    starting_agent=agent,
    input="what do you think about the labour party in the UK?"
)


# Great, our guardrail triggered! The `output_guardrail` type is implemented in almost the exact same way, but uses the `@output_guardrail` decorator when defining the guardrail function, and the `output_guardrails` parameter when defining our `Agent`.


# ## Conversational Agents


# So far we've only seen how to use our agents with single messages. Many use-cases require chat history to make our agents conversational. To implement that we simply provide a list of messages to our `Runner`.
#
# Let's see how this works, first we send a single message:


result = await Runner.run(
    starting_agent=agent,
    input="remember the number 7.814 for me please"
)
result.final_output


# Fortunately, we can help our agent remember this information. We can use the `.to_input_list()` method to format our `result` into a list of messages for our next query.


result.to_input_list()


# We merge this with our next message:


result = await Runner.run(
    starting_agent=agent,
    input=result.to_input_list() + [
        {"role": "user", "content": "multiply the last number by 103.892"}
    ]
)
result.final_output





# It looks like our agent can remember our previous interactions after all!


# ---


# That is our rapid-fire overview of OpenAI's new Agents SDK. We've covered most of the essentials here but there are many other features in the library, and many of the features we included here come with plenty of different ways to use. The SDK is already fairly substantial and certainly worth keeping an eye on.


