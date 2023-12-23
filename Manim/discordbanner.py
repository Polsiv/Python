from manim import *

class Banner(Scene):
    def construct(self):
        e1 = MathTex(r"e^{i\theta} = \cos(\theta) + i\sin(\theta)")
        e2 = MathTex(r"e^{i\pi} = \cos(\pi) + i\sin(\pi)")
        e3 = MathTex(r"e^{i\pi} = -1")
        e4 = MathTex(r"e^{i\pi} + 1 = 0")

        self.play(Write(e1), run_time = 2)
        self.wait()
        self.play(ReplacementTransform(e1, e2))
        self.wait()
        self.play(ReplacementTransform(e2, e3))
        self.wait()
        self.play(ReplacementTransform(e3, e4))
        self.play(e4.animate.set_fill(color = GREEN_D))
        self.wait()
        self.play(FadeOut(e4))