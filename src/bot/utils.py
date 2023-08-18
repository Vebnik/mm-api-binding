from colorama import Fore, Back, Style
from typing import Any

class Logger:
    @classmethod
    def info(cls, message: Any) -> None:
        print(f'[INFO] {Fore.YELLOW + str(message)}')
        cls.reset_out()

    @classmethod
    def success(cls, message: Any) -> None:
        print(f'[SUCCESS] {Fore.GREEN + str(message)}')
        cls.reset_out()

    @classmethod
    def error(cls, message: Any) -> None:
        print(f'[ERROR] {Fore.RED + str(message)}')
        cls.reset_out()

    @classmethod
    def reset_out(cls) -> None:
        print(Style.RESET_ALL, end='')