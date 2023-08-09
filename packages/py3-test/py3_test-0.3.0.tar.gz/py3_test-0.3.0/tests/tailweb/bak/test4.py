import logging
import shlex
import subprocess

import tornado
import tornado.ioloop


def call_subprocess(context, command, callback=None):
    context.ioloop = tornado.ioloop.IOLoop.instance()
    context.pipe = p = subprocess.Popen(
        shlex.split(command),
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        close_fds=True,
    )
    context.ioloop.add_handler(
        p.stdout.fileno(),
        context.async_callback(on_subprocess_result, context, callback),
        context.ioloop.READ,
    )


def on_subprocess_result(context, callback, fd, result):
    try:
        if callback:
            callback(context.pipe.stdout)
    except Exception as e:
        logging.error(e)
    finally:
        context.ioloop.remove_handler(fd)
