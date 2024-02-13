from manim import *

#the class is my canvas and inhertis from Scene
class FirstExample(Scene):
    def construct(self):
        blue_circle = Circle(color=BLUE, fill_opacity=0.5)
        green_square = Square(color=GREEN, fill_opacity=0.5)
        yellow_triangle = Triangle(color=YELLOW, fill_opacity=0.5)

        green_square.next_to(blue_circle, RIGHT)
        yellow_triangle.next_to(blue_circle, LEFT)


        self.add(blue_circle, green_square, yellow_triangle)
        self.play(Create(blue_circle))

