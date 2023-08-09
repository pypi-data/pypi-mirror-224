from tornado import IOLoop, Queue, gen

q = Queue(maxsize=10)


@gen.coroutine
def consumer():
    while True:
        item = yield q.get()
        try:
            print("Doing work on %s" % item)
            yield gen.sleep(0.01)
        finally:
            q.task_done()


@gen.coroutine
def producer():
    for item in range(15):
        yield q.put(item)
        print("Put %s" % item)


@gen.coroutine
def main():
    # Start consumer without waiting (since it never finishes).
    IOLoop.current().spawn_callback(consumer)
    yield producer()  # Wait for producer to put all tasks.
    yield q.join()  # Wait for consumer to finish all tasks.
    print("Done")


IOLoop.current().run_sync(main)
