#!/usr/bin/env python3

import asyncio
import logging
import sys
from asyncio.subprocess import PIPE, create_subprocess_exec
from collections.abc import Callable
from contextlib import suppress
from itertools import count

from monitorio.server import Context, Singleton, serve


def log() -> logging.Logger:
    """Logger for this module"""
    return logging.getLogger("monitorio")


class GlobalMonitorContext(Context, metaclass=Singleton):
    ...


def view(view_definition_fn: Callable[[], int]) -> None:
    """"""
    name = view_definition_fn.__name__
    print(f"define view {name}")
    GlobalMonitorContext().add(name, view_definition_fn)


async def process_output(command, when: str):
    def cleaned(raw: bytes, log_widget) -> str:
        line = raw.decode().strip("\n")
        log_widget.write_line(line)
        return line

    async def listen(stream, log_widget):
        return [cleaned(raw_line, log_widget) async for raw_line in stream]

    logger = GlobalMonitorContext().current_logger()
    iterations = None
    for iteration in count():
        if iterations is not None and iteration >= iterations:
            break
        log().info("start task %r: %d", command, iteration)
        process = await create_subprocess_exec(command, stdout=PIPE, stderr=PIPE)
        stdout, stderr, return_code = await asyncio.gather(
            asyncio.ensure_future(listen(process.stdout, logger)),
            asyncio.ensure_future(listen(process.stderr, logger)),
            process.wait(),
        )
        log().info("task %r: %d, returned %d", command, iteration, return_code)

        yield stdout

        await asyncio.sleep(int(when))


async def iterate(**generator_defs):
    async def bundle(coro):
        async for result in coro:
            yield coro, result

    def task_from(name, coro):
        return asyncio.create_task(anext(bundle(coro)), name=name)

    tasks = set(task_from(name, coro) for name, coro in generator_defs.items())

    while tasks:
        done, tasks = await asyncio.wait(fs=tasks, return_when=asyncio.FIRST_COMPLETED)
        for event in done:
            with suppress(StopAsyncIteration):
                coro, result = event.result()
                name = event.get_name()
                tasks.add(task_from(name, coro))
                yield name, result


class Monitor:
    def __init__(self, name: str, log_level="INFO") -> None:
        self.name = name
        self.log_level = log_level

    def __enter__(self) -> "Monitor":
        return self

    def __exit__(self, *args: object) -> bool:
        if sys.exc_info() != (None, None, None):
            raise

        serve(GlobalMonitorContext(), self.log_level)
        return True


# with suppress(FileNotFoundError):
# with open(CONFIG_FILE) as config_file:
# config = yaml.load(config_file, yaml.Loader)
# print(config)
