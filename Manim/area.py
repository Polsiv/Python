from manim import *

class GraphTesting(Scene):
    def construct(self):
        plane = NumberPlane(x_range=[-8, 8, 1], x_length=15, y_range=[-8, 8, 1], y_length=15).shift(DOWN*3)
        plane.set_opacity(0.8).add_coordinates(color=WHITE)
        sub_plane = NumberPlane(x_range=[-8, 8, 0.5], x_length=15, y_range=[-8, 8, 0.5], y_length=15, stroke_width=0.1).shift(DOWN*3)
        sub_plane.set_opacity(0.2)

        labels = plane.get_axis_labels(x_label="x", y_label="y")
        

        parabola = plane.plot(lambda x: x**2 + 1, x_range=[-4, 4], stroke_width=5, color = GREEN_C)

        func_label = MathTex("f(x)={x}^{2} + {1}").to_corner(UR)

        area = plane.get_riemann_rectangles(graph = parabola, x_range = [-2, 2], dx = 0.01, stroke_width=0.1)

        func_integral = MathTex("\int_{-2}^{2}x^2 + 1\,dx").to_corner(UL)
        self.play(DrawBorderThenFill(VGroup(plane, sub_plane)), run_time=2)
        self.play(Create(labels))
        self.play(Create(func_label))
        self.play(Create(parabola), run_time= 2, rate_func=smooth)
        self.play(Create(area), rate_func = smooth, run_time = 3)
        self.wait()

        self.play(plane.animate.set_opacity(0.2))
        self.play(Create(func_integral), run_time = 2,rate_func = smooth)

        self.play(FadeOut(VGroup(labels, parabola, func_label, area, func_integral, plane, sub_plane)))
        self.wait()