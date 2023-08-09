from typing import Generic, TypeVar

TKey = TypeVar('TKey')
TValue = TypeVar('TValue')


class KeyText(Generic[TKey, TValue]):
    def __init__(self, key: TKey, value: TValue) -> None:
        self.key = key
        self.value = value
        # super().__init__()
