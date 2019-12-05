#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 10:26:51 2019

@author: dillonberger
"""

from manimlib.imports import *

def add_obj(obj, string="-", where=RIGHT, color=WHITE):

    if color==WHITE:
    	colors={}
    else: 
    	colors={string: color}

    new_obj=TexMobject(
            string,
            tex_to_color_map = colors
        )
        
    return new_obj.next_to(obj, where)

class Lagrangian(Scene):
    def construct(self):
        
        F = TexMobject(
                "\\mathbf{F}" , color=YELLOW
                )
        eq = TexMobject(
                "\\ = \\"
                )
        
        m = TexMobject(
                "m", color=YELLOW
                )


        a = TexMobject(
                "\\mathbf{a}", color=BLUE
                )
        

        
 
        
        ddt = TexMobject(
                "{ \\mathrm{d} \\over \\mathrm{d} t }"
                ).scale(2)
        
        eq.next_to(F, RIGHT)
        m.next_to(eq, RIGHT)
        a.next_to(m, .2*RIGHT)
                
        
        group = Group(F, eq, m,a).shift(LEFT).shift(UP)
        group.scale(2)
        
        dvdt = TexMobject(
                "{ \\mathrm{d} \\mathbf{v} \\over \\mathrm{d} t }",
                tex_to_color_map = {"\\mathbf{v}": BLUE}
                )
        dvdt.scale(2).next_to(m, RIGHT)
        v = dvdt.get_part_by_tex("\\mathbf{v}")
        d = dvdt.get_part_by_tex("\\mathrm{d}")
            
        ddt.move_to(dvdt)
        
        grad = TexMobject("- \\nabla U ( \\mathbf{x} )  ", tex_to_color_map={"U": WHITE,"\\mathbf{x}": BLUE}).scale(1.5)
        newF = TexMobject(
                "\\mathbf{F}" , color=YELLOW
                ).scale(1.5)
        neweq = TexMobject("=").scale(1.5)
        newF.next_to(F, 8*DOWN)
        neweq.next_to(newF,RIGHT)
        grad.next_to(neweq, RIGHT)
        
        


        ## Replacement transform replaces the object in the group .. use this
        
        self.play(Write(F))
        self.play(Write(eq))
        self.play(Write(m))
        self.play(Write(a))
        self.wait(1)
        self.play(ReplacementTransform(a, dvdt))
        self.wait(1)
        self.play(CyclicReplace(dvdt, m))
        self.wait(1)
        self.play(ApplyMethod(m.next_to, dvdt,RIGHT), ApplyMethod(v.next_to, m, .2*RIGHT),
                  ApplyMethod(d.shift, RIGHT*.01))
        mv = Group(m,v)
        self.wait(1)
        p = TexMobject("\\mathbf{p}", color=BLUE).move_to(mv).scale(2.1)
        self.play(ReplacementTransform(mv, p))
        self.play(ApplyMethod(p.next_to, d, RIGHT*.3))
        self.wait(1)
        self.play(GrowFromCenter(neweq), FadeInFrom(newF, 2*LEFT), FadeInFrom(grad, 2*RIGHT))
        dpdt = Group(dvdt, p)
        self.wait(1)
        self.play(ApplyMethod(grad.next_to, eq, LEFT*2), FadeOutAndShift(F, 10*LEFT),
                  ApplyMethod(dpdt.scale, 1.5/2) , FadeOutAndShift(newF, 10*LEFT), 
                  FadeOutAndShift(neweq,20*DOWN) )
        newtons_law = Group(grad, eq, dpdt)
        self.play(ApplyMethod(newtons_law.shift, RIGHT))
        newton_text = TexMobject(
                "\\text{Newton's $2^{nd}$ Law}", color=RED
                ).scale(2).next_to(newtons_law, UP*2)
        self.play(Write(newton_text))    
        box = Group(newtons_law, newton_text)
        self.play(ApplyMethod(box.scale, .4))
        self.play(ApplyMethod(box.shift, 1.5*UP+ 5.35*LEFT))
        
        lag_0 = TexMobject(
                "\\text{Lagrangian} \\ = \\ \\text{Kinetic Energy} - \\text{Potential Energy} ",
                tex_to_color_map={"\\text{Kinetic Energy}": BLUE, "\\text{Potential Energy}": WHITE,
                                  "\\text{Lagrangian}": YELLOW}
                )
        
        lag = TexMobject(
                "\\mathcal{L} \\ = \\ \\frac{1}{2} {m} \\mathbf{v} ^2 \\ -  \\ U( \\mathbf{x} )",
                tex_to_color_map = {"\\mathcal{L}": YELLOW,"\\mathbf{v}": BLUE, 
                                    "\\mathbf{x}": BLUE}
                ).scale(2)
        lag_text = TexMobject("\\text{Lagrangian}", color=RED).next_to(lag, UP*2).scale(2)
        
        
        dummyLHS = TexMobject("\\mathcal{L}", color=YELLOW).shift(UP*.5).scale(1.5)
        
        keq = TexMobject("\\ = \\").next_to(dummyLHS, 2*RIGHT).scale(1.5)
        
        dummy = TexMobject(
                "\\frac{1}{2} {m} \\mathbf{v} ^2",
                tex_to_color_map = {"\\mathbf{v}": BLUE 
                                    }
                ).next_to(keq, 2*RIGHT).scale(1.5) 
        
        dummypot = TexMobject("\\ -  \\ U( \\mathbf{x} )",
                              tex_to_color_map={"\\mathbf{x}": BLUE}).next_to(dummy, 2*RIGHT).scale(1.5)
        
        

        
        eqGroup = Group(dummyLHS, keq, dummy, dummypot).move_to(ORIGIN).shift(UP*.5)
        
        summation = TexMobject("\\mathcal{L} \\ = \\ \\frac{1}{2} m \\sum_{k=1}^3 \\mathbf{v} _k^2\\ -  \\ U( \\mathbf{x} )", 
                   tex_to_color_map = {"\\mathbf{v}" :BLUE, "\\mathbf{x}": BLUE,
                                       "\\mathcal{L}": YELLOW}).move_to(dummy).scale(1.5)
        
        self.play(Write(lag_0))
        self.wait(2)
        self.play(ReplacementTransform(lag_0, lag))
        self.wait(1)
        self.play(Write(lag_text))
        self.wait(1.5)
        lag_box = Group(lag, lag_text)
        self.play(ApplyMethod(lag_box.match_width, box), ApplyMethod(lag_box.match_height, box))
        self.play(ApplyMethod(lag_box.next_to, box, 7*RIGHT))
        el_eqns = TexMobject(
                "{\\mathrm{d} \\over \\mathrm{d} t}",
                "{\\partial", "\\mathcal{L}", "\\over", "\\partial", "\\dot{\\mathbf{x}}", "_i}",
                "\\ = \\", 
                "{\\partial", "\\mathcal{L}", "\\over", "\\partial", "\\mathbf{x}", "_i }"
                
                ).set_color_by_tex("\\mathcal{L}", YELLOW).set_color_by_tex("\\mathbf{x}", BLUE)
        el_eqns.set_color_by_tex("\\dot{\\mathbf{x}}", BLUE).scale(2).shift(DOWN)
        el_text= TexMobject("\\text{Euler-Lagrange Equations}", color=RED).scale(2).next_to(el_eqns,2*UP)
        self.play(Write(el_eqns))
        self.wait(1.5)
        xdot = el_eqns.get_part_by_tex("\\dot{\\mathbf{x}}")
        vee = TexMobject("\\mathbf{v}", color=BLUE).scale(2.2).move_to(xdot).shift(DOWN*.1)
        self.play(ReplacementTransform(xdot, vee))
        explain = TextMobject("For each vector component $i$", color=YELLOW)
        explain.next_to(el_eqns, 2*DOWN)
        self.play(Write(explain))
        self.wait(1.5)
        self.play(Write(el_text), FadeOutAndShift(explain, DOWN))
        self.wait(1.5)
        el_box = Group(el_eqns, el_text,vee)
        self.play(ApplyMethod(el_box.match_width, box), ApplyMethod(el_box.match_height, box))
        self.play(ApplyMethod(el_box.next_to, lag_box, 7*RIGHT))
        bgroup = Group(box, lag_box, el_box)
        self.wait(1)
        self.play(TransformFromCopy(lag, eqGroup))
        self.wait(1.5)
        self.play(ReplacementTransform(eqGroup, summation), FadeOut(dummypot))
        self.wait(3)
        el_1 = TexMobject("{\\partial", "\\mathcal{L}", "\\over", "\\partial", "\\mathbf{v}", "_i}" ,
                          "\\ = \\"
                          ).set_color_by_tex("\\mathcal{L}", YELLOW).set_color_by_tex("\\mathbf{v}", BLUE).scale(1.2)
        el_1.next_to(summation, 3.5*DOWN).shift(3*LEFT)
        
        rhs = TexMobject("m" ,"\\mathbf{v}", "_i}").set_color_by_tex("\\mathbf{v}", BLUE).scale(1.2)
        rhs.next_to(el_1, RIGHT)
        self.play(TransformFromCopy(el_eqns, el_1 ))
        self.wait(1)
        self.play(Write(rhs))
        self.wait(2)
        mom = TexMobject("\\mathbf{p} _i",tex_to_color_map={"\\mathbf{p}": BLUE}).scale(1.2).move_to(rhs)
        self.play(ReplacementTransform(rhs, mom))
        derivt = TexMobject("\\frac{\\mathrm{d}}{\\mathrm{d} t}").scale(1.2).next_to(el_1,LEFT)
        pdot = TexMobject("{\\mathrm{d} \\mathbf{p} _i \\over \\mathrm{d} t }",
                          tex_to_color_map={"\\mathbf{p}":BLUE}).move_to(mom).scale(1.2)
        self.wait(1)
        self.play(FadeInFrom(derivt, LEFT), ReplacementTransform(mom, pdot))
        self.wait(1.5)
        derivx = TexMobject("{\\partial", "\\mathcal{L}", "\\over", "\\partial", "\\mathbf{x}", "_i }"
                
                ).set_color_by_tex("\\mathcal{L}", YELLOW).set_color_by_tex("\\mathbf{x}", BLUE)
        derivx.next_to(summation, 3.5*DOWN).shift(2.5*RIGHT).scale(1.2)
        dU = TexMobject(
                " = - { \\partial U \\over \\partial \\mathbf{x} _i}",
                tex_to_color_map={"\\mathbf{x}": BLUE}).scale(1.2)
        dU.next_to(derivx, RIGHT)
        self.play(TransformFromCopy(el_eqns,derivx))
        self.wait(1)
        self.play(Write(dU))
        self.wait(1.5)
        gp = Group(derivt, el_1, pdot, derivx, dU)
        self.play(ReplacementTransform(summation, lag), ApplyMethod(gp.shift, 2*UP))
        brace = Brace(gp, 3*DOWN)
        eqText= brace.get_text("These are equal, by the Euler-Lagrange Equations", color=YELLOW)
        self.wait(1)
        self.play(GrowFromCenter(brace), Write(eqText))
        self.wait(3)
        equality = TexMobject(
                "- { \\partial U \\over \\partial", "\\mathbf{x}", "_i} \\ = \\", 
                "{\\mathrm{d}", "\\mathbf{p}", "_i \\over \\mathrm{d} t}"
                ,
                tex_to_color_map={"\\mathbf{p}": BLUE, "\\mathbf{x}": BLUE}
                ).scale(2)
        self.play(FadeOutAndShift(brace, DOWN), FadeOutAndShift(eqText, DOWN),
                  ReplacementTransform(gp, equality))
        equality_text = TextMobject("Now, write this as a vector equation", color=YELLOW)
        equality_text.next_to(equality, 4*DOWN).scale(1.3)
        self.play(Write(equality_text))
        final = TexMobject(
                "-\\nabla U(", "\\mathbf{x}", ") \\ = \\ ","{\\mathrm{d}", 
                "\\mathbf{p}", "\\over \\mathrm{d} t}",
                tex_to_color_map={"\\mathbf{p}": BLUE, "\\mathbf{x}": BLUE}
                ).scale(2)
        self.wait(1.5)
        self.play(FadeOutAndShift(equality_text, DOWN), ReplacementTransform(equality, final))
        square = Rectangle(color=YELLOW)
        square.surround(final)
        self.wait(1.5)
        self.play(Write(square))
        g = Group(square, final)
        n2 = TextMobject("Newton's $2^{nd}$ Law", color=RED).next_to(g, UP).shift(DOWN*.5).scale(1.5)
        self.play(ApplyMethod(g.shift, DOWN), Write(n2) )
        self.wait(5)
        
        
