
import asyncio
import random
import time

async def newsProducer(myQueue):
    while True:
        await asyncio.sleep(1)
        print("Putting new item onto queue")
        await myQueue.put(random.randint(1, 5))

async def newsConsumer(id, myQueue):
    while True:
        print("Consumer: {} attempting to get from queue".format(id))
        item = await myQueue.get()

        if item is None:
            break

        print("Consumer: {} consumed article with id: {}".format(id, item))

async def main(loop):

    myQueue = asyncio.Queue(loop = loop, maxsize=10)

    await asyncio.wait([newsProducer(myQueue), newsConsumer(1, myQueue), newsConsumer(2, myQueue)])

loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))

print("All workers completed")
loop.close()