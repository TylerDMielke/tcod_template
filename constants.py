from tcod.context import (
    SDL_WINDOW_RESIZABLE,
)


CHAR_SIZE: int = 16

WIDTH_PIXEL: int = 1280
HEIGHT_PIXEL: int = 720 

WIDTH_TILE: int = int(WIDTH_PIXEL / CHAR_SIZE)
HEIGHT_TILE: int = int(HEIGHT_PIXEL / CHAR_SIZE)

SDL_FLAGS = SDL_WINDOW_RESIZABLE

TILESET_PATH: str = 'tilesets/perfect_dosvga437.ttf'
