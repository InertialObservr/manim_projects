"""
Created on Wed Apr 29 11:26:23 2020

@author: dillonberger
"""


from manimlib.imports import *
import numpy as np
from math import atan

from matplotlib import cm


sc = .6
color = WHITE
N = 18 


viridis = cm.get_cmap('viridis_r', N-1)



def mkTri(n):
    verts = [[n-1,0,0], [n,0,0], [n,np.sqrt(n),0]]
    poly = Polygon(*verts, color=WHITE, fill_opacity = .7  , fill_color = rgba_to_color(viridis(n)),
                   stroke_width=2)
    return poly

def mkLab(n,sc=sc):
    triLab = TexMobject('\\sqrt{'+str(n)+'}',color=color).move_to([n -.26, np.sqrt(n)/2.5, 0])
    triLab.scale(sc)
    return triLab

def linInterp(x1,x2):
    xs = np.arange(x1,x2, (x2-x1)/500)
    pts = []
    objs = np.zeros(len(xs), dtype=object)
    
    for i in range(1,len(xs)):
        
        objs[i] = Line((xs[i-1], np.sqrt(xs[i-1]),0),(xs[i], np.sqrt(xs[i]),0),color=color)
        
        
        pts.append(
            
            Write( 
                objs[i]
             )   
            
            )
        
    return pts, np.trim_zeros(objs)
    
def FlipAnim(obj):
    anim = ApplyMethod(obj.flip, [0,1,0])
    return anim

def rotAnim(obj, n):
    anim = Rotate(obj, PI/2, about_point=[n,0,0])
    return anim

def centerAtOrigin(obj,n):
    anim = ApplyMethod(obj.shift, [np.sqrt(n+1)-n,0,0])
    return anim
        
def rotToPlace(obj, n, about = ORIGIN):
    θ = 0
    
    for nn in range(1,n+1):
        θ = θ + np.arctan(1/np.sqrt(nn))
        
        
    anim = Rotate(obj, θ, about_point=about, CONFIG={"replace_mobject_with_target_in_scene": True})
    
    return anim
    
    


    
    

class Tri(Scene):
    
    CONFIG = {
        "camera_class": Camera,
        "camera_config": {"frame_center": [7,1,0], "background_color":BLACK},
        }
    
    
    def construct(self):
        

        LineAnim, LineObjects = linInterp(0,N)
        
        triList = []
        labList = []
        TriLabTups = np.zeros(N, dtype=object)
        TriLabGroups = np.zeros(N, dtype=object)
        
        for n in range(1,N):
           TriLabTups[n-1] = [mkTri(n),mkLab(n)]
           TriLabGroups[n-1] = Group(mkTri(n), mkLab(n))
           
           triList.append( ShowCreation( TriLabTups[n-1][0] ) )
           labList.append( ShowCreation( TriLabTups[n-1][1] ) )
           
        label = TexMobject('f(x)  =  \\sqrt{x}', color=color).move_to([4.5,3,0])
        label.scale(1.25)
        LineAnim.append(FadeIn(label))
        
        self.play(*triList)
        self.wait(1)
        self.play(*labList)
        self.wait(1)
        self.play(*LineAnim)
        self.wait(1)
        

        
        
        flipList = []
        rotList = []
        centList = []
        finRotList = []
        for n in range(1,len(TriLabGroups)-1):
            obj2 = TriLabGroups[n]
            tri = TriLabTups[n]
            
            flipList.append(FlipAnim(obj2[0]))
            flipList.append( ApplyMethod(obj2[1].shift, .5*LEFT) )
            rotList.append(rotAnim(obj2,n))
            centList.append(centerAtOrigin(obj2, n))
            
            
        
        tupArray = np.array(TriLabTups).flatten()
        tupArray = np.trim_zeros(tupArray)      
        
        
        i = 0
        for ele in tupArray:
            if i==0:
                i+=1
                continue
            for el in ele:
                self.remove(el)
                i+=1
        
        self.play(*flipList, run_time=.8)
        self.wait(1)
        self.play(*rotList, run_time=.8)
        self.wait(1)
        self.play(*centList, run_time=.8)
        self.wait(1)
        
        
        
        fade = [FadeOut(label)]
        for li in LineObjects:
            fade.append(FadeOut(li))
            
            
        
        
        self.play(*fade)
        
        self.wait(.2)
        
        
        
        self.remove(TriLabTups[0][0] )
        self.remove(TriLabTups[0][1] )
        
        
        toGroup = np.array(TriLabGroups).flatten()
        toGroup = np.trim_zeros(toGroup)      
        initGroup = Group(*toGroup)
        
        self.play(ApplyMethod(initGroup.shift, [7,1.5,0]) , run_time=.75)
        self.wait(.5)
        
        for n in range(1,len(TriLabGroups)-1):
            obj2 = TriLabGroups[n]
            tri = TriLabTups[n]    
            finRotList.append(rotToPlace(obj2,n, about=toGroup[0].get_corner(DOWN+LEFT)))
        
        self.play(*finRotList, run_time=.7)
        
        self.wait(4)
        
        
        self.play(FadeOut(initGroup))
