from dataclasses import dataclass
from typing import Any


@dataclass
class GameEvent:
    """Represents an event that happens within the game that should be handled later."""
    function: callable
    args: list[Any]
    kwargs: dict[str, Any]
    priority: int

    def __str__(self) -> str:
        str_repr: str = '<GameEvent:'
        str_repr = f'{str_repr} <Priority : {str(self.priority)}>'
        str_repr = f'{str_repr} <Function Name: {str(self.function)}>'
        if len(self.args) > 0:
            str_repr = f'{str_repr} <Argument Values:'
            for arg in self.args:
                if arg:
                    str_repr = f'{str_repr} {str(arg)}'
            str_repr = f'{str_repr}>'
        if len(self.kwargs) > 0:
            str_repr = f'{str_repr} <Keyword Argument Values:'
            for key, value in self.kwargs.items():
                str_repr = f'{str_repr} {key}: {value}'
            str_repr = f'{str_repr}>'
        str_repr = f'{str_repr} /GameEvent>'
        return str_repr
    

class GameEventHandler:
    """Handles the queueing and execution of GameEvents."""
    def __init__(self) -> None:
        self.events: list[GameEvent] = []
    
    def __len__(self) -> int:
        return len(self.events)
    
    def __str__(self) -> str:
        str_repr: str = '< GameEventHandler:'
        str_repr = f'{str_repr} Length: {len(self.events)}'
        if len(self.events) > 0:
            str_repr = f'{str_repr} < Events:'
            for event in self.events:
                str_repr.join(str(event))
            str_repr = f'{str_repr} Events >'
        str_repr = f'{str_repr} /GameEventHandler>'
        return str_repr
        
    def register(
        self, function: callable, args: list[Any] = [], kwargs: dict[str, Any] = {}, priority: int = 0
    ) -> None:
        """Append a new event to be processed later."""
        if not isinstance(args, list):
            raise ValueError(f'Cannot register args of type: {type(args)}')
        if not isinstance(kwargs, dict):
            raise ValueError(f'Cannot register kwargs of type: {type(kwargs)}')
        new_event = GameEvent(function, args, kwargs, priority)
        # log.debug(f'Registering new GameEvent: {str(new_event)}')
        self.events.append(new_event)
        # self.events.sort(key=attrgetter('priority'), reverse=True)

    def process(self) -> None:
        """Process the next event in the queue."""
        event: GameEvent = self.events.pop()
        if event:
            # log.debug(f'Processing GameEvent: {str(event)}')
            event.function(*event.args, **event.kwargs)
    
    def clear(self) -> None:
        """Purge this handler of all events."""
        self.events.clear()
