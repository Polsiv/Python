from manim import *


class Function(Scene):
    def construct(self):
        ax = Axes(x_range=(-10, 10), y_range=(-10, 10))

        curve = ax.plot()
        self.add(ax)