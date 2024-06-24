from asyncflows import AsyncFlows

async def main():
    # Load the flow from the file
    flow = AsyncFlows.from_file("hello_world.yaml")
    # Run the flow with a variable
    result = await flow.set_vars(name="Vincent").run()
    # Print the result
    print(result)

import asyncio
asyncio.run(main())
