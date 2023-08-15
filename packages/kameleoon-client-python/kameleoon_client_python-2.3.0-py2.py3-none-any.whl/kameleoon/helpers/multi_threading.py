"""Helpers for running functions in multi-threading"""

import asyncio
import threading
import concurrent.futures
import time
from typing import Any, Coroutine, List, Optional


class ThreadEventLoop:
    """
    ThreadEventLoop is helper object to handle asynchronous tasks execution in a separate thread.
    """

    def __init__(self) -> None:
        self.loop: Optional[asyncio.AbstractEventLoop] = None
        self.thread: Optional[threading.Thread] = None

    def __thread_main(self) -> None:
        self.loop = asyncio.new_event_loop()
        self.loop.run_forever()

    def start(self) -> None:
        """Starts the thread and the event loop"""
        if self.thread is not None:
            return
        self.thread = threading.Thread(target=self.__thread_main, daemon=True)
        self.thread.start()

    def __get_loop(self) -> asyncio.AbstractEventLoop:
        while self.loop is None:
            time.sleep(0.01)
        return self.loop

    def stop(self) -> None:
        """Stops the thread and the event loop"""
        if self.thread is None:
            return
        loop = self.__get_loop()
        while len(asyncio.all_tasks(loop)) > 0:
            time.sleep(0.01)
        loop.call_soon_threadsafe(loop.stop)
        self.thread.join()
        loop.close()

    def run_coro(self, coro: Coroutine[Any, Any, Any]) -> concurrent.futures.Future[Any]:
        """
        Puts the specified coroutine to the event loop for background execution.
        :param coro: Coroutine to be executed
        :type coro: Coroutine[Any, Any, Any]
        """
        if self.thread is None:
            self.start()
        return asyncio.run_coroutine_threadsafe(coro, self.__get_loop())


def run_in_threads_if_required(background_thread: bool, func, args: List[Any], thread_name: str):
    """
    it's wrapper function which run the `func`
    in another thread if multi_threading option is True
    else it calls the `func` in the same thread
    :param background_thread: Flag to determine if run in multi-threading
    :type background_thread: Boolean
    :param func: Function need to be called
    :type func: Function
    :param args: List of arguments for `func`
    :type args: List[Any]
    :param thread_name: Name of thread if `func` runs
    in another thread
    :type args: str
    """
    if background_thread:
        thread = threading.Thread(target=func, args=args)
        thread.daemon = True
        thread.setName(thread_name)
        thread.start()
    else:
        func(*args)
