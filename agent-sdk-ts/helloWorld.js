import { Agent, run } from "@openai/agents";
import "dotenv/config";

const helloAgent = new Agent({
    name: "Hello Agent",
    instructions: "You are an agent that always says hello world",
    model: "gpt-4o-mini",
});

run(helloAgent, "Hello, How are you?")
.then(result => {
    console.log(result.finalOutput);
})
.catch(error => {
    console.error(error);
});