from dataclasses import dataclass, field
from typing import Generic, Optional, TypeVar, Union

H = TypeVar('H')


@dataclass
class Clipboard:

    clipboard: str = field(default_factory=str)

    def copy(self, text: str) -> None:
        self.clipboard = text

    def paste(self) -> str:
        return self.clipboard

    def is_empty(self) -> bool:
        return bool(self.clipboard)


@dataclass
class History(Generic[H]):

    past: list[H] = field(default_factory=list)
    future: list[H] = field(default_factory=list)

    def snapshot(self, item: H) -> None:
        self.past.append(item)
        self.future.clear()

    def reset(self) -> None:
        self.past.clear()
        self.future.clear()

    def undo(self, current: H) -> H:
        if self.past:
            self.future.append(current)
            return self.past.pop()
        else:
            return current

    def redo(self, current) -> H:
        if self.future:
            self.past.append(current)
            return self.future.pop()
        else:
            return current


class Editor:

    def __init__(self, name: str, clipboard: Clipboard) -> None:
        self.name: str = name
        self.clipboard: Clipboard = clipboard

        self.text: str = ''
        self.text_history: History[str] = History()

        self.cursor: int = 0
        self.cursor_history: History[int] = History()

        self.selection: tuple[int, int] = ()
        self.selection_history: History[tuple[int, int]] = History()

        self.actions = {
            'APPEND': self.append,
            'DELETE': self.delete,
            'MOVE': self.move,
            'SELECT': self.select,
            'COPY': self.copy,
            'PASTE': self.paste,
            'UNDO': self.undo,
            'REDO': self.redo,
        }

    def action(self, action: str, *args: list[str]) -> Optional[str]:
        return self.actions[action](*args)

    def append(self, text: str) -> str:
        if self.selection or text:
            self._history_snapshot()

        if self.selection:
            self.text = self._delete_between(*self.selection)
            self.move(self.selection[0])

        self.text = self.text[:self.cursor] + text + self.text[self.cursor:]
        self.cursor = self.cursor + len(text)

        return self._get_output()

    def delete(self) -> str:
        if self.selection or self.cursor < len(self.text):
            self._history_snapshot()

        if self.selection:
            self.text = self._delete_between(*self.selection)
            self.move(self.selection[0])
        else:
            self.text = self.text[:self.cursor] + self.text[self.cursor+1:]

        return self._get_output()

    def move(self, cursor: Union[str, int]) -> None:
        self.selection = ()
        self.cursor = self._restrict_cursor_bounds(int(cursor))

    def select(self, start: Union[str, int], end: Union[str, int]) -> None:
        start = self._restrict_cursor_bounds(int(start))
        end = self._restrict_cursor_bounds(int(end))
        if start == end:
            self.move(start)
        else:
            self.selection = (start, end)

    def copy(self) -> None:
        if self.selection:
            self.clipboard.copy(self._get_between(*self.selection))

    def paste(self) -> Optional[str]:
        if self.clipboard.is_empty():
            return None
        else:
            return self.append(self.clipboard.paste())

    def undo(self) -> str:
        self.text = self.text_history.undo(self.text)
        self.cursor = self.cursor_history.undo(self.cursor)
        self.selection = self.selection_history.undo(self.selection)

        return self._get_output()

    def redo(self) -> str:
        self.text = self.text_history.redo(self.text)
        self.cursor = self.cursor_history.redo(self.cursor)
        self.selection = self.selection_history.redo(self.selection)

        return self._get_output()

    def close(self) -> None:
        self.text_history.reset()
        self.cursor_history.reset()
        self.selection_history.reset()

        self.cursor = len(self.text)

    def _get_output(self) -> str:
        return self.text

    def _history_snapshot(self) -> None:
        self.text_history.snapshot(self.text)
        self.cursor_history.snapshot(self.cursor)
        self.selection_history.snapshot(self.selection)

    def _restrict_cursor_bounds(self, cursor: int) -> int:
        return min(max(0, cursor), len(self.text))

    def _get_between(self, start: int, end: int) -> str:
        return self.text[start:end]

    def _delete_between(self, start: int, end: int) -> str:
        return self.text[:start] + self.text[end:]


class IDE:

    def __init__(self) -> None:
        self.clipboard: Clipboard = Clipboard()
        self.active: Editor = Editor(name='', clipboard=self.clipboard)
        self.editors: dict[str, Editor] = {self.active.name: self.active}
        self.active_history: dict[str, None] = {}
        self.outputs: list[str] = []

        self.actions = {
            'OPEN': self.open,
            'CLOSE': self.close,
        }

    def action(self, action: str, *args: list[str]) -> None:
        if action in self.actions:
            self.actions[action](*args)
        else:
            output = self.active.action(action, *args)
            if output is not None:
                self.outputs.append(output)

    def open(self, name: str) -> None:
        # Open the new editor and add active editor at the top of the history
        # We remove the new editor to refresh its order in the history
        self.active_history.pop(name, None)
        self.active_history[self.active.name] = None

        if name not in self.editors:
            self.editors[name] = Editor(name=name, clipboard=self.clipboard)
        self.active = self.editors[name]

    def close(self) -> None:
        self.active.close()
        name, _ = self.active_history.popitem()
        self.active = self.editors[name]

    def get_outputs(self) -> list[str]:
        return self.outputs

def textEditor(queries: list[list[str]]) -> list[str]:
    ide = IDE()

    for query in queries:
        ide.action(*query)

    return ide.get_outputs()
