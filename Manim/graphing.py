from manim import *

class GraphTesting(Scene):
    def construct(self):
        plane = NumberPlane(x_range=[-8, 8, 1], x_length=15, y_range=[-8, 8, 1], y_length=15)
        plane.set_opacity(0.8).add_coordinates(color = WHITE)
        sub_plane = NumberPlane(x_range=[-8, 8, 0.5], x_length=15, y_range=[-8, 8, 0.5], y_length=15, stroke_width = 0.1)
        sub_plane.set_opacity(0.2)
 
        labels = plane.get_axis_labels(x_label = "x", y_label="f(x) = x^3")
        parabola = plane.plot(lambda x: x**3, x_range = [-4, 4], stroke_width = 5)  
       

        self.play(DrawBorderThenFill(VGroup(plane, sub_plane)), run_time = 2)
        self.play(Create(labels), run_time = 1)
        self.play(Create(parabola), run_time = 3, rate_func = smooth)   