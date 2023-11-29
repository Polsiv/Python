from manim import *

class Tracker(Scene):
    def construct(self):
        
        k = ValueTracker(0)

        num = always_redraw(
            lambda: DecimalNumber().set_value(k.get_value())
        )

        self.play(FadeIn(num))
        self.wait()
        self.play(k.animate.set_value(5), run_time = 3, rate_func = smooth)