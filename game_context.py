from __future__ import annotations

import tcod


class CustomContext:
	def __init__(self, context: tcod.context.Context,):
		self.context = context
		self.drawables: list = []

	def run(self) -> CustomContext:
		cont_update: bool = True
		cont_draw: bool = True

		while cont_update and cont_draw:
			cont_update = self.update()
			cont_draw = self.draw()

		return self

	def update(self) -> bool:
		raise NotImplementedError('Base class: CustomContext does not have an update() method.')

	def draw(self) -> bool:
		raise NotImplementedError('Base class: CustomContext does not have an draw() method.')
	
	def _draw_drawables(self, console: tcod.Console) -> None:
		for drawable in self.drawables:
			if drawable is not None:
				drawable.draw(console)
