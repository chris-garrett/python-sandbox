import asyncio


async def worker_task1():
    while True:
        # suck on queue/stream for results
        print("worker_task1 running")
        await asyncio.sleep(10)


async def main():
    app_task = asyncio.create_task(worker_task1())
    await asyncio.gather(app_task)


if __name__ == "__main__":
    asyncio.run(main())
