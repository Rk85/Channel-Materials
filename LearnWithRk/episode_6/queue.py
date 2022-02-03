import asyncio

queue_size = int(input("Please mention the size of the queue: "))
queue = []

async def process_queue():
    max_try = 3
    curr_try = 0
    while curr_try < max_try:
        if queue:
            curr_element = queue.pop(0)
            print("Processing the element %d" %(curr_element))
        else:
            curr_try = curr_try + 1
            await asyncio.sleep(1)

async def schedule_process():
    curr_element_no = 0
    while curr_element_no < queue_size:
        print("Queuing the element %s" %(curr_element_no))
        queue.append(curr_element_no)
        curr_element_no = curr_element_no + 1
        await asyncio.sleep(1)

async def main():
    f1 = loop.create_task(schedule_process())
    f2 = loop.create_task(process_queue())
    await asyncio.wait([f1, f2])

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
