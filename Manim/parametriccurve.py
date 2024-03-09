from manim import *

class Parametric(Scene):
    def construct(self):
        plane = NumberPlane(x_range=[-8, 8, 1], x_length=15, y_range=[-8, 8, 1], y_length=15).add_coordinates(color=WHITE)
        self.play(Create(plane), rate_func=smoothstep, run_time=2)

        function = MathTex("r(t) = 1\cos(4t)").to_corner(UR)
        parametric_curve = ParametricFunction(
             lambda t: np.array([
               np.cos(4 * t) * np.cos(t),
               np.cos(4 * t) * np.sin(t), 
               0
            ]),
            t_range=[0, 2*np.pi],
            color= color.interpolate_color(BLUE, PURPLE, alpha = 1)
        )

        self.play(Create(function))
        self.play(Create(parametric_curve))

        self.wait(1)  # Wait for a moment before ending the scene
