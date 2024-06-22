from asyncflows import AsyncFlows


async def main():
    flow = AsyncFlows.from_file("hello_world.yaml")

    result = await flow.set_vars(name="Sheila").run()
    print(result)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
