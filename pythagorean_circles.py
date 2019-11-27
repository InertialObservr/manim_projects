#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 15:10:43 2019

@author: dillonberger
"""

from manimlib.imports import *
import numpy as np


#add basic TexMobjects adjacent to obj
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


#add basic TexMobjects adjacent to obj .. fix is a shift applied 
#afterward to correct for slight misalignments 
#add_obj() should be depracated by taking fix=np.array([0,0,0])
#but i was too lazy 
def add_obj_shift(obj, string="-", where=RIGHT, color=WHITE, 
                  fix = np.array([0,-.9,0])):

    if color==WHITE:
    	colors={}
    else: 
    	colors={string: color}

    new_obj=TexMobject(
            string,
            tex_to_color_map = colors
        )
        
    return new_obj.next_to(obj, where).shift(fix)

#self explanatory 
def get_angle(v1, v2):
    n1 = v1/np.linalg.norm(v1)
    n2 = v2/np.linalg.norm(v2)
    
    dprod = np.dot(n1, n2)
    
    return np.arccos(dprod)
    

class triangle(Scene):
    def construct(self):
        
    
        bot = Line(
                np.array([-2, -1, 0]),
                np.array([2, -1 , 0]),
                color=PURPLE
                )
        
        vert = Line(
                np.array([2, -1 , 0]),
                np.array([2, 1, 0]),
                color=GREEN
                )
        hyp = Line(
                np.array([2, 1, 0]),
                np.array([-2, -1, 0]),
                color=ORANGE
                )
        bot.shift(2*UP)
        vert.shift(2*UP)
        hyp.shift(2*UP)

        
        a = add_obj(bot, "{2a}", color=PURPLE, where=DOWN)
        
        b = add_obj(vert, "{2b}", color=GREEN, where=RIGHT)
        
        c = add_obj_shift(hyp, "{2c}", color=ORANGE, where=UP)
        
        aGroup = Group(bot, a)
        bGroup = Group(vert, b)
        cGroup = Group(hyp, c)
        
        
        
     
        
        hypT = Line(
        np.array([-np.sqrt(20)/2 ,-1.5, 0]),
        np.array([np.sqrt(20)/2, -1.5,0]),
        color=ORANGE
        )
        hypT.shift(4*LEFT)
        
        cT = add_obj(hypT, "{2c}", color=ORANGE, where=DOWN)
        
        cGroupT = Group(hypT, cT)
        
        
        botT = Line(
        np.array([-2,0,0]),
        np.array([2,0,0]),
        color=PURPLE
        )
        
        
        
        aT = add_obj(botT, "{2a}", color=PURPLE, where=DOWN)
        
        aGroupT = Group(botT, aT)
        aGroupT.next_to(cGroupT, 4*RIGHT)
        
        
        vertT = Line(
        np.array([-1 ,0, 0]),
        np.array([1,0,0]),
        color=GREEN
        )
        
        
        
        bT = add_obj(vertT, "{2b}", color=GREEN, where=DOWN)
        
        bGroupT = Group(vertT, bT)
        bGroupT.next_to(aGroupT, 4*RIGHT)
        
        linGroup = Group(aGroupT, bGroupT, cGroupT)
        
        l_circ = Circle(radius = np.sqrt(20)/2, color=ORANGE, fill_color=ORANGE, fill_opacity=.5)
        l_circ.next_to(cGroupT, UP).shift(np.array([0,-1,0]))
        
        m_circ = Circle(radius = 2, color=PURPLE, fill_color=PURPLE, fill_opacity=.5)
        m_circ.next_to(aGroupT, UP).shift(np.array([0,-1,0]))
        
        r_circ = Circle(radius = 1, color=GREEN, fill_color=GREEN, fill_opacity=.5)
        r_circ.next_to(bGroupT, UP).shift(np.array([0,0,0]))
        
        c2 = TexMobject(
                "{c}^2", tex_to_color_map={"{c}": ORANGE}
                )
        c2.next_to(l_circ, 2.5*UP)
        c2.scale(2)
        
        a2 = TexMobject(
                "{a}^2", tex_to_color_map={"{a}": PURPLE}
                )
    
        a2.next_to(m_circ, 4*UP)
        a2.scale(2)
        
        b2 = TexMobject(
                "{b}^2", tex_to_color_map={"{b}": GREEN}
                )
    
        b2.next_to(r_circ, 8*UP)
        b2.scale(2)
        
        eq = add_obj(l_circ,"=", where=RIGHT)
        pl = add_obj(m_circ,"+", where=RIGHT)
        
        eqU = add_obj(eq,"=", where=10.5*UP)
        plU = add_obj(pl,"+", where=10.5*UP).shift(.8*LEFT)
        
        eqU.scale(2)
        plU.scale(2)
        
        p1 = add_obj_shift(c2, "\\pi", where=LEFT, fix=np.array([0,-.235,0]))
        p1.scale(2)
        
        p2 = add_obj_shift(a2, "\\pi", where=LEFT, fix=np.array([0,-.235,0]))
        p2.scale(2)
 
        p3 = add_obj_shift(b2, "\\pi", where=LEFT, fix=np.array([0,-.235,0]))
        p3.scale(2)       

        self.play(GrowFromCenter(bot))
        self.play(GrowFromCenter(vert))
        self.play(GrowFromCenter(hyp))
        self.play(GrowFromCenter(a),GrowFromCenter(b),GrowFromCenter(c))
        self.wait(3)
        self.play(Transform(cGroup, cGroupT))
        self.play(Transform(aGroup, aGroupT))
        self.play(Transform(bGroup, bGroupT))
        self.wait(1)
        self.play(ApplyMethod(linGroup.shift, 1.5*UP),
                  FadeOut(aGroup), FadeOut(bGroup), FadeOut(cGroup))
        self.wait(2)
        self.play(CounterclockwiseTransform(cGroupT, l_circ),
                  CounterclockwiseTransform(aGroupT, m_circ),
                  CounterclockwiseTransform(bGroupT, r_circ),
                  FadeIn(c2), FadeIn(eq), FadeIn(pl), FadeIn(a2), FadeIn(b2),
                  FadeIn(eqU), FadeIn(plU))
        self.wait(1)
        self.play(FadeIn(p1), FadeIn(p2), FadeIn(p3))
        self.wait(5)
        
        
        
