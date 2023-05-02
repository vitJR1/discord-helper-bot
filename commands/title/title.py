from abc import ABC, abstractmethod


class Header(ABC):
    @abstractmethod
    def generate(self, text: str) -> str:
        pass


class H1(Header):
    def generate(self, text: str) -> str:
        return f"<h1>{text}</h1>"


class H2(Header):
    def generate(self, text: str) -> str:
        return f"<h2>{text}</h2>"


class H3(Header):
    def generate(self, text: str) -> str:
        return f"<h3>{text}</h3>"


class Title:
    def __init__(self, text: str, level: int):
        self.text = text
        self.level = level

        if level not in range(1, 4):
            raise ValueError("Header level should be between 1 and 3")

    def __str__(self) -> str:
        header_class = {1: H1, 2: H2, 3: H3}[self.level]
        return header_class().generate(self.text)
