#!/usr/bin/env python3

"""Monitor I/O"""

import asyncio
import logging
import signal
import threading
from collections.abc import Callable
from pathlib import Path

from rich.logging import RichHandler
from textual import on
from textual.app import App, ComposeResult
from textual.containers import VerticalScroll
from textual.message import Message
from textual.widgets import Footer, Header, Pretty, RichLog

from monitorio.logging_utils import setup_logging

CONFIG_FILE = Path("~/.config/monitorio/monitorio.yaml").expanduser()


def log() -> logging.Logger:
    """Logger for this module"""
    return logging.getLogger("monitorio")


class RichLogHandler(RichHandler):
    def __init__(self, widget: RichLog):
        super().__init__(
            # show_time = False,
            # omit_repeated_times = False,
            # show_level = False,
            show_path=False,
            # enable_link_path = False,
            markup=False,
            # rich_tracebacks = False,
            # tracebacks_width: Optional[int] = None,
            # tracebacks_extra_lines: int = 3,
            # tracebacks_theme: Optional[str] = None,
            # tracebacks_word_wrap: bool = True,
            # tracebacks_show_locals: bool = False,
            # tracebacks_suppress: Iterable[Union[str, ModuleType]] = (),
            # locals_max_length: int = 10,
            # locals_max_string: int = 80,
            # log_time_format = "[%x %X]",
            # keywords= None,
        )
        self.widget: RichLog = widget

    def emit(self, record: logging.LogRecord) -> None:
        message = self.format(record)
        message_renderable = self.render_message(record, message)
        traceback = None
        log_renderable = self.render(
            record=record, traceback=traceback, message_renderable=message_renderable
        )
        self.widget.write(log_renderable)


class MonitorioMonitor(App[None]):
    """Terminal monitor for Monitorio"""

    CSS_PATH = "monitorio.css"

    def __init__(self) -> None:
        super().__init__()

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Footer()
        yield VerticalScroll()
        yield RichLog(
            # max_lines=None,
            # min_width=78,
            # wrap=False,
            # highlight=True,
            # markup=True,
            # auto_scroll=True,
            # name=None,
            # id=None,
            # classes=None,
            # disabled=False
        )

    @staticmethod
    async def task(data, command, timeout, times, update, cleanup):
        try:
            log().info("task %r started", command)
            for i in range(times):
                log().info("task %r: %d", command, i)
                data[command] = i
                update()
                await asyncio.sleep(timeout)
        except Exception:
            log().exception("exception in %r", command)
        finally:
            log().info("task %r terminated", command)
            await cleanup()

    async def create_widget(self, data) -> Pretty:
        await self.query_one(VerticalScroll).mount(widget := Pretty(data))
        return widget

    async def remove_widget(self, widget: Pretty) -> None:
        await widget.remove()

    async def add_task(self, command: str, timeout: int, times: int):
        widget = await self.create_widget(new_data := {})
        asyncio.ensure_future(
            self.task(
                new_data,
                command,
                timeout,
                times,
                lambda: widget.update(new_data),
                lambda: self.remove_widget(widget),
            )
        )
        return widget

    async def on_mount(self) -> None:
        """UI entry point"""

        log().handlers = [RichLogHandler(self.query_one(RichLog))]

        await self.add_task("df", 5, 3)
        await self.add_task("ps", 3, 2)

    @on(Message)
    async def on_msg(self, *event: str) -> None:
        """Generic message handler"""
        # log().debug("Event: %s", event)

    async def exe(self, on_exit: Callable[[], None]) -> None:
        """Execute and quit application"""
        try:
            await self.run_async()
        finally:
            on_exit()


def terminate(terminator: threading.Event) -> None:
    """Sends a signal to async tasks to tell them to stop"""
    try:
        terminator.set()
        for task in asyncio.all_tasks():
            task.cancel()
        asyncio.get_event_loop().stop()
    except Exception:  # pylint: disable=broad-except
        log().exception("terminate:")


async def print_messages(msg_queue: asyncio.Queue[str]) -> None:
    """Dumply print messages"""
    while True:
        print(f"|{await msg_queue.get()}")


def install_signal_handler(loop: asyncio.AbstractEventLoop, on_signal: Callable[[], None]) -> None:
    """Installs the CTRL+C application termination signal handler"""
    for signal_enum in [signal.SIGINT, signal.SIGTERM]:
        loop.add_signal_handler(signal_enum, on_signal)


def serve(log_level=None) -> None:
    """Synchronous entry point"""
    setup_logging(log_level)

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    terminator = threading.Event()

    asyncio.ensure_future(
        MonitorioMonitor().exe(lambda: terminate(terminator))
        # if sys.stdout.isatty()
        # else print_messages(msg_queue)
    )

    try:
        install_signal_handler(loop, lambda: terminate(terminator))
        log().info("CTRL+C to quit")
        loop.run_forever()
    finally:
        log().debug("finally - loop.run_forever()")
