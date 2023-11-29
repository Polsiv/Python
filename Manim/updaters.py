from manim import *

class Updaters(Scene):
    def construct(self):
        num = always_redraw(
            lambda: Text("ln(2)")
        )
        box = always_redraw(
            lambda: SurroundingRectangle(
                num, color=BLUE, fill_opacity=0.5, buff=2,
            )
        )

        myname = Text("Paulsiv", color=BLUE_C).next_to(box, UP, buff=1)

        self.play(Create(VGroup(num, box, myname)), run_time=6)
        self.play(myname.animate.shift(RIGHT * 2, DOWN * 6), run_time=2)  # Fix the typo here
