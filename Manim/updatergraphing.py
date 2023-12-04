from manim import *

class UpdatersGraphing(Scene):
    def construct(self):

       

        k = ValueTracker(2)
        ax = Axes(x_range=[-5, 5, 1], y_range=[0, 10, 1], x_length=10, y_length=10).to_edge(DOWN).add_coordinates()
        func = ax.plot(lambda x: x**2, x_range=[-4, 4], stroke_width=5, color = GREEN_C)
        slope = always_redraw(
            lambda: ax.get_secant_slope_group(x= k.get_value(), graph=func, dx = 0.001, secant_line_color=RED_D, secant_line_length=2)
        )

        point = always_redraw(
            lambda: Dot().move_to(
            ax.c2p(k.get_value(), func.underlying_function(k.get_value()))
            )
        )
        #c2p coordinates to point

        self.play(Create(VGroup(ax, func)), run_time = 3,rate_func = smooth)
        self.play(Create(VGroup(slope, point)), run_time= 2)
        self.play(k.animate.set_value(-2), run_time = 3)
