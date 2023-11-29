from manim import *

class Getters(Scene):
    def construct(self):
        rect = Rectangle(color = RED, height=2, width=3.5).to_corner(UL)
        circ = Circle(radius=0.5).to_edge(DOWN)
        arrow = always_redraw(
            lambda: Line (start=rect.get_bottom(), end=circ.get_top(), buff=0.2).add_tip(tip_length=0.2, tip_width=0.2)
            )
        #buff is for the space between the arrow and the object


        self.play(Create(VGroup(rect, circ, arrow)), run_time= 5)
        self.play(rect.animate.to_edge(UR), circ.animate.scale(0.2), riuntime = 2)
     