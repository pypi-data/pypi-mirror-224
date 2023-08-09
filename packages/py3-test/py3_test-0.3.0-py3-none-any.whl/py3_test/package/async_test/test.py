"""
@Time   : 2019/3/18
@author : lijc210@163.com
@Desc:  : 功能描述。
"""
import asyncio
import time


async def b():
    time.sleep(1)
    print("ccccccc")


async def a():
    print("start test")
    await b()
    print("end test")


coroutine = a()
loop = asyncio.get_event_loop()
loop.run_until_complete(coroutine)

print("bbb")
