from subprocess import PIPE

from tornado import Subprocess, gen


@gen.coroutine
def run_command(command):
    process = Subprocess([command], stdout=PIPE, stderr=PIPE, shell=True)
    yield process.wait_for_exit()  # This waits without blocking the event loop.
    out, err = process.stdout.read(), process.stderr.read()
    print(out, err)
    # Do whatever you do with out and err


run_command("sh /usr/local/test/tailweb/test1.sh")
