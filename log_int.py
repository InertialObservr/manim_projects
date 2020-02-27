from manimlib.imports import *

class logAnim(Scene):
    def construct(self):
        color = BLACK
        sc = 1
        lhs = TexMobject("\\int^x_1", "x^n", " \\ d x ", color=color).scale(sc).shift(2*LEFT)
        eq =  TexMobject("\\ = \\ ",color=color).scale(sc).next_to(lhs,1.2*RIGHT)
        rhs = TexMobject("{ x^{n+1}-1 \\over n+1}",color=color).scale(sc).next_to(eq, RIGHT)
        
        
        self.play(Write(lhs))
        self.play(Write(eq))
        self.wait(1)
        self.play(Write(rhs))
        self.play(ApplyMethod(rhs.shift, RIGHT))
        
        lLim = TexMobject("\\lim_{ n\\to -1}",color=color).scale(sc).next_to(lhs, LEFT)
        rLim = TexMobject("\\lim_{ n\\to -1}",color=color).scale(sc).next_to(rhs, .3*LEFT)
        
        
        self.play(FadeInFrom(lLim, LEFT), FadeInFrom(rLim, LEFT))
        self.wait(1)
        
        grand = lhs.get_parts_by_tex("x^n")
        integral = TexMobject("{1 \\over x }",color=color).scale(sc).move_to(grand)
        self.play(ReplacementTransform(grand, integral), FadeOut(lLim))
        self.wait(1)
        
        LH = TexMobject(" \\frac{d}{dn}( x^{ n +1} - 1 ) \\over \\frac{d}{dn} ( n +1 ) ",color=color).scale(sc).move_to(rhs).shift(.5*RIGHT)
        
        self.play(ReplacementTransform(rhs, LH))
        
        self.wait(2)
        
        new = TexMobject("\\frac{d}{dn}", "x^{ n +1 }",color=color).scale(sc).move_to(rhs).shift(.5*LEFT)
        
        self.play(ReplacementTransform(LH, new))
        
        self.wait(1.5)
        
        exp = new.get_part_by_tex("x^{ n +1 }")
        

        elog = TexMobject("e^", "{( n + 1 ) \\ln( x )}", color=color).scale(sc).move_to(exp).shift(RIGHT*.7)
        
        self.play(ReplacementTransform(exp, elog))
        
        self.wait(1.5)
        
        
        deriv = new.get_part_by_tex("\\frac{d}{dn}")
        res = TexMobject("\\ln(x)", color=color).scale(sc).move_to(deriv).shift(.2*RIGHT)
        
        self.play(ReplacementTransform(deriv, res), ApplyMethod(elog.shift, .4*RIGHT))
        # self.play(ApplyMethod(elog.shift, LEFT*.7), FadeInFrom(res, RIGHT))
        self.wait(1)
        
        
        # ApplyMethod(limGroup.shift, LEFT)
      
        
        
        self.play(CyclicReplace(res, rLim))
        limGroup = Group(rLim, elog)
        one = TexMobject("\\cdot 1", color=color).scale(sc).next_to(res,RIGHT).shift(.1*LEFT)
        # self.play(ApplyMethod(res.shift, LEFT) )
        self.wait(1.5)
        self.play(ReplacementTransform(limGroup, one))
        self.wait(.5)

        
        
        square = Rectangle(color=BLACK)
        final = Group(lhs, integral, eq, res)   
        
        self.play(ApplyMethod(final.shift, RIGHT),FadeOutAndShift(one, RIGHT))
        square.surround(final)
        self.play(Write(square))
        
        self.wait(4)
