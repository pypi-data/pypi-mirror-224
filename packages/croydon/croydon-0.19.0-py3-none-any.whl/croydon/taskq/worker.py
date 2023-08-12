import asyncio
from abc import abstractmethod, ABC
from .types import TBaseTask
from .. import getctx


class BaseWorker(ABC):

    @abstractmethod
    async def run_task(self, task: TBaseTask) -> None: ...

    async def run(self):
        try:
            async for task in getctx().queue.tasks():
                getctx().log.debug("worker accepted task %s", task)
                await self.run_task(task)
        except asyncio.CancelledError:
            pass
