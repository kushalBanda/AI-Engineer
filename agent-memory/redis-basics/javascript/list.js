const client = require("./client");

async function init() {
    await client.lpush("mylist", '1')
    await client.lpush("mylist", '2')
    await client.lpush("mylist", '3')
    await client.lpush("mylist", '4')
    await client.lpush("mylist", '5')

    const result = await client.rpop("mylist");
    console.log("List: ", result);
}


init();