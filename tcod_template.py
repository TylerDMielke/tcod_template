import cProfile
import logging as log
import pstats
from datetime import date, datetime
from pathlib import Path
from typing import Optional

import tcod

from constants import *
from game_context import CustomContext 


def main() -> None:
	"""The driving method of the tcod app."""
	initialize_logging(log.INFO)
	log.info(f'tcdo_template started at {datetime.now(pytz.timezone("America/Chicago")).time()}')

	tileset = load_tileset()

	with tcod.context.new(
		width=WIDTH_PIXEL, height=HEIGHT_PIXEL, tileset=tileset, title='TCOD Template'
	) as tcod_context:
		game_context: Optional[CustomContext] = CustomContext(tcod_context)

		while game_context is not None:
			game_context = game_context.run()
		
		tcod_context.close()


def load_tileset() -> tcod.tileset.Tileset:
	"""Helper function that sets up the tileset for the game."""
	# This is used if the tileset is in a tilesheet
	return tcod.tileset.load_tilesheet(
		"tilesets/myne_18x18.png",
		CHAR_SIZE,
		CHAR_SIZE,
		tcod.tileset.CHARMAP_CP437,
	)


def initialize_logging(level: int) -> None:
	"""Helper method that sets up logging for Artone."""
	logging_directory = Path('logs/')
	logging_directory.mkdir(exist_ok=True)

	logging_file: str = f'{str(logging_directory)}/{date.today()}.log'
	logging_file_path = Path(logging_file)
	if not logging_file_path.exists:
		logging_file_path.touch()
	
	log.basicConfig(filename=logging_file, format='%(levelname)s:%(message)s', level=level)


if __name__ == '__main__':
	profiling = False 
	if profiling:
		profile_file: str = f'logs/binprofile'
		with cProfile.Profile() as profile:
			main()
		profile.dump_stats(profile_file)
		with open(f'logs/{date.today()}.profile', 'w') as f:
			stats = pstats.Stats(profile_file, stream=f)
			stats.sort_stats(pstats.SortKey.CALLS, pstats.SortKey.TIME)
			stats.print_stats('Repositories.*artone')
	else:
		main()
