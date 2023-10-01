import asyncio

async def greet(name):
    await asyncio.sleep(1)
    return f"Hello, {name}!"

async def main():
    task1 = greet("Alice")
    task2 = greet("Bob")
    
    results = await asyncio.gather(task1, task2)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    asyncio.run(main())
