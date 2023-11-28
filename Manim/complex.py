from manim import *

class Testing(Scene):
    def construct(self):
        name = Text("Paulsiv")
        sq = Square(side_length=1)
        tri = Triangle().scale(0.6  ).shift(RIGHT * 5)

        self.play(Create(tri))
        self.wait()
        self.play(Write(name))