from manim import *

class GraphTesting(Scene):
    def construct(self):
        plane = NumberPlane(x_range=[-8, 8, 1], x_length=10, y_range=[-8, 8, 1], y_length=10)
        plane.set_opacity(0.8).add_coordinates(color = RED_B)
 
        labels = plane.get_axis_labels(x_label = "x", y_label="f(x) = x^3")
        parabola = plane.plot(lambda x: x**3, x_range = [-4, 4, 1],  color = BLUE)

        self.play(DrawBorderThenFill(plane), run_time = 2)
        self.play(Create(labels), run_time = 2)
        self.play(Create(parabola), run_time = 3, rate_funct = smooth)