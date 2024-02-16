from manim import *

class Parametric(Scene):
    def construct (self):
        plane = NumberPlane(x_range=[-8, 8, 1], x_length=15, y_range=[-8, 8, 1], y_length=15).shift(DOWN*3)

        self.play(Create(plane), rate_func = smoothstep)

