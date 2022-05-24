from __future__ import annotations
from typing import Optional

import tcod
import numpy as np


class AtriochContext:
	def __init__(
		self, context: tcod.context.Context,
	):
		self.context = context
		self.drawables: list = []  # TODO: This will eventually be slow. Numpy?

	def run(self) -> AtriochContext:
		cont_update: bool = True
		cont_draw: bool = True

		while cont_update and cont_draw:
			cont_update = self.update()
			cont_draw = self.draw()

		return self

	def update(self) -> bool:
		raise NotImplementedError('Base class: AtriochContext does not have an update() method.')

	def draw(self) -> bool:
		raise NotImplementedError('Base class: AtriochContext does not have an draw() method.')
	
	def _draw_drawables(self, console: tcod.Console) -> None:
		for drawable in self.drawables:
			if drawable is not None:
				drawable.draw(console)
