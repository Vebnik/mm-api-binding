from colorama import Fore, Style
from typing import Any
from os import getenv


class Logger:

    mode: str = getenv('MODE', 'PROD')

    @classmethod
    def info(cls, message: Any) -> None:
        if cls.mode in ['DEV']:
            print(f'[INFO] {Fore.YELLOW + str(message)}')
            cls.reset_out()

    @classmethod
    def success(cls, message: Any) -> None:
        if cls.mode in ['DEV']:
            print(f'[SUCCESS] {Fore.GREEN + str(message)}')
            cls.reset_out()

    @classmethod
    def error(cls, message: Any) -> None:
        if cls.mode in ['DEV']:
            print(f'[ERROR] {Fore.RED + str(message)}')
            cls.reset_out()

    @classmethod
    def reset_out(cls) -> None:
        print(Style.RESET_ALL, end='')

