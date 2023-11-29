from manim import *

class Testing(Scene):
    def construct(self):
        name = Text("Paulsiv")
        sq = Square(side_length=1)
        tri = Triangle().scale(0.6).shift(LEFT * 2)
        tri2 = Triangle(stroke_color=BLUE_A, fill_color = RED, fill_opacity = 0.5).scale(1.2).to_edge(UR)
        #UR MEANS UP RIGHT
        circle = Circle(stroke_color = YELLOW)

        self.play(Create(tri))
        self.wait()

        self.play(Write(name))
        self.play(name.animate.to_edge(DL))

        self.play(DrawBorderThenFill(tri2))
        self.wait()
        
        self.play(Create(sq))
        self.play(sq.animate.scale(3), tri2.animate.to_edge(DL), run_time = 3)
        self.wait()

        self.play(circle.animate.set_fill(color= YELLOW, opacity = 0.5))
        self.wait(2)
        