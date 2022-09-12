from __future__ import annotations

import logging as log
from datetime import datetime
from typing import Optional

import tcod
import pytz 

import constants


class CustomContext:
	"""An extensible class for handling the game state."""
	def __init__(self, context: tcod.context.Context,):
		self.context = context
		self.drawables: list = []
		self.end_context: bool = False

	def run(self) -> Optional[CustomContext]:
		while not self.end_context:
			self.update()
			self.process()
			self.draw()
		return None

	def update(self) -> None:
		"""Updates all the entities within this context."""
		raise NotImplemented('The update() method has not been implemented yet.')

	def process(self) -> None:
		"""Processes all of the events that happen in this context."""
		while len(self.events) > 0:
			self.events.process()

	def draw(self) -> None:
		"""Draws all the drawable entities in this context."""
		console = self.context.new_console(
			min_columns=constants.WIDTH_TILE, min_rows=constants.HEIGHT_TILE, order="F"
		)
		for drawable in self.drawables:
			log.debug(f"Drawing: {drawable}")
			drawable.draw(console)
		self.context.present(console)
	
	def close(self) -> None:
		"""Stop this context's loop and exit the context."""
		log.info(f'Artone exited at {datetime.now(pytz.timezone("America/Chicago")).time()}.')
		self.end_context = True

	def _handle_input(self) -> None:
		for event in tcod.event.get():
			if event.type == "QUIT":
				"""Quit the game."""
				self.close()
			elif event.type == "KEYDOWN":
				"""Handle player input."""
				sym: int = event.sym
				self._handle_keydown(sym)
	
	def _handle_keydown(self, keystroke: int) -> None:
		if keystroke == tcod.event.K_ESCAPE:
			"""Quit the game."""
			self.close()
	
