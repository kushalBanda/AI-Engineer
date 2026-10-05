import { Agent, run, tool } from "@openai/agents";
import "dotenv/config";

const agent = new Agent({
    name: "Weather Agent",
    instructions: "You are a weather agent that can tell the weather of a given location",
    model: 'gpt-4o-mini',
    tools: [
        {
            name: 'get_weather',
            description: 'Get the weather of a given location',
            parameters: {
                type: 'object',
                properties: {
                    location: { type: 'string', description: 'The location to get the weather of' }
                }
            }
        }
    ]
})

async function main (query = '') {
    const result = await run(agent, query);
    console.log(result.finalOutput);
}

main("What is the weather in Tokyo?");