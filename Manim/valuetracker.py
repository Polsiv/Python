from manim import *

class Tracker(Scene):
    def construct(self):
        
        k = ValueTracker(0)

        num = DecimalNumber().set_value(k.get_value())

        self.play(FadeIn(num))
        self.wait()
        self.play(FadeOut(num))