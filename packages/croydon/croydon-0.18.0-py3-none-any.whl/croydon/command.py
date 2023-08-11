import asyncio
import importlib
import inspect
import os.path
from argparse import ArgumentParser, Namespace
from typing import Generator, AnyStr, Type, TypeVar, List, Dict
from croydon.types import TConfigType


class Command:

    NAME: str
    HELP: str
    ASYNC_RUN: bool = True

    config: str

    _project_dir: str
    _config_class: TConfigType

    def __init__(self, parser: ArgumentParser) -> None:
        self._project_dir = _get_project_dir()
        self._config_class = _get_config_class()
        parser.add_argument("-c", "--config", default="application.toml", help="configuration file to use")
        self.init_argument_parser(parser)

    def run(self, args: Namespace) -> None:
        self.config = args.config
        self.setup_context()

        asyncio.run(self.setup(args))
        if self.ASYNC_RUN:
            asyncio.run(self.run_async())
        else:
            self.run_sync()

    def setup_context(self):
        from croydon import ctx
        ctx.from_config_file(self._config_class, self.config)

    async def setup(self, args: Namespace) -> None:
        pass

    def init_argument_parser(self, parser: ArgumentParser) -> None:
        pass

    def run_sync(self) -> None:
        pass

    async def run_async(self) -> None:
        pass


CC = Type[Command]
CI = TypeVar("CI", bound=Command)


def _collect_commands() -> List[CC]:

    search_module_paths = ["croydon.commands", "app.commands"]
    commands: List[CC] = []

    def module_names_in_dir(mod_dir: AnyStr) -> Generator[str, None, None]:
        for filename in os.listdir(mod_dir):
            if filename.endswith(".py"):
                filename = os.path.basename(filename)[:-3]
                yield filename

    for modpath in search_module_paths:
        try:
            base_module = importlib.import_module(modpath)
        except ModuleNotFoundError:
            continue
        for modname in module_names_in_dir(os.path.dirname(base_module.__file__)):
            module = importlib.import_module(f"{modpath}.{modname}")
            for cls in module.__dict__.values():
                if inspect.isclass(cls) and issubclass(cls, Command) and cls is not Command:
                    commands.append(cls)

    commands.sort(key=lambda cmd: cmd.NAME)

    return commands


def _get_config_class() -> TConfigType:
    try:
        module = importlib.import_module("app.config")
        config_class = module.__dict__["Config"]
    except (ModuleNotFoundError, KeyError):
        raise RuntimeError("module app.config must be defined and contain a Config class")

    return config_class


def _get_project_dir() -> str:
    try:
        module = importlib.import_module("app.config")
    except ModuleNotFoundError:
        raise RuntimeError("module app.config must be defined and contain a Config class")

    file_dir = os.path.dirname(module.__file__)
    project_dir = os.path.abspath(os.path.join(file_dir, ".."))
    return project_dir


def main():
    parser = ArgumentParser()
    subparsers = parser.add_subparsers(
        title="command",
        required=True,
        help="command to run",
        dest="command"
    )

    cmd_map: Dict[str, CI] = {}

    for cmd_class in _collect_commands():
        sp = subparsers.add_parser(cmd_class.NAME, help=cmd_class.HELP)
        cmd = cmd_class(sp)
        cmd_map[cmd.NAME] = cmd

    args = parser.parse_args()
    cmd = cmd_map.get(args.command)
    cmd.run(args)
