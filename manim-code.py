from manim import *

class TransformExample(Scene):
    def construct(self):
        circle = Circle()
        blue_circle = circle.set_fill(BLUE, opacity=0.5)
        
        square = Square()
        
        self.play(Create(blue_circle))
        self.wait(1)
        self.play(Transform(blue_circle, square))
        self.wait(1)