
import asyncio

async def myWorker():
    #return number * 2
    print("Hello World")

async def main(coros):
    """as_completed() function"""
    #for fs in asyncio.as_completed(coros):
    #    print(await fs)
    print("my Main")

#coros = [myWorker(1) for i in range(5)]

try:
    loop = asyncio.get_event_loop()
    #loop.run_until_complete(main(coros))

    """gather() function"""
    #loop.run_until_complete(asyncio.gather(*[myWorker() for i in range(5)]))

    """wait()"""
    loop.run_until_complete(asyncio.wait([myWorker() for i in range(5)], timeout=2))
except KeyboardInterrupt:
    pass

finally:
    loop.close()