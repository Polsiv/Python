from manim import *
class Test(Scene):
  def construct(self):
    integral = MathTex(r"2\left(\frac{x^3}{3} + x \Big|_0^2\right)")
    self.play(Write(integral))