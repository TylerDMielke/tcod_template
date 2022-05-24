import tcod

from constants import *
from game_context import AtriochContext 


def main() -> None:
	"""The driving method of the tcod app."""
	tileset = load_tileset()

	with tcod.context.new(
		width=WIDTH_PIXEL, height=HEIGHT_PIXEL, tileset=tileset, title='TCOD Template'
	) as context:
		game_context: AtriochContext = AtriochContext(context)

		while True:
			game_context = game_context.run()


def load_tileset() -> tcod.tileset.Tileset:
	"""Helper function that sets up the tileset for the game."""
	# This is used if the tileset is in a tilesheet
	return tcod.tileset.load_tilesheet(
		"tilesets/myne_18x18.png",
		16,
		16,
		tcod.tileset.CHARMAP_CP437,
	)


if __name__ == "__main__":
	main()
