import { Agent, run } from "@openai/agents";
import "dotenv/config";

const location = 'india';


const helloAgent = new Agent({
    name: "Hello Agent",
    instructions: function() {
        if (location === "india") {
            return "Always say 'Namaste' to the user";
        } else {
            return 'That just talk to the user';
        }
    },
    model: "gpt-4o-mini",
});

run(helloAgent, "Hello, I'm from India, How are you?")
.then(result => {
    console.log(result.finalOutput);
})
.catch(error => {
    console.error(error);
});