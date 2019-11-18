from manimlib.imports import *
#from manimHelper import add_obj

#define helper function for adding TexMobjects 
#manimHelper is a function library I wrote to which
#add_obj belongs. I posted it here explicitly for 
#reading convenience

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

class geoSeries(Scene):
    def construct(self):
        # for x in range(-4, 4):
        #     for y in range(-4, 4):
        #         self.add(Dot(np.array([x, y, 0]), color=DARK_GREY))
        ## only run while creating for help with aboslute coordinates 
        
                
                
        tex1a = TexMobject(
            "r"+"S",
            tex_to_color_map={"S": ORANGE, "r":BLACK}
        )
        
        tex1a.shift(np.array([-1,2,0]))
        
        tex1b = add_obj(tex1a, string="=")
 
        tex1c = TexMobject(
            "1 + r + r^2 + \\cdots",
            tex_to_color_map={"r": BLUE}
        )
        
        tex1c.next_to(tex1b, RIGHT)
         


        tex2a = TexMobject(
            "r" + "S",
            tex_to_color_map={"S": ORANGE, "r": BLUE}
        )
        
        tex2a.next_to(tex1a, np.array([0,-3,0]))
        
        tex2b = add_obj(tex2a, "=")
        
        tex2c = TexMobject(
            "{r} + {r}^2 + \\cdots",
            tex_to_color_map={"{r}": BLUE}
        )
        
        tex2c.next_to(tex2b, RIGHT)


        

#############################################
        
        tex1aCopy = TexMobject(
            "r"+"S",
            tex_to_color_map={"S": ORANGE, "r":BLACK}
        )
        
        tex1aCopy.shift(np.array([-1,2,0]))
        
        tex1bCopy = add_obj(tex1aCopy, string="=")
        
        tex1cCopy = TexMobject(
            "{1} + {r} + {r}^2 + \\cdots",
            tex_to_color_map={"{r}": BLUE}
        )
        
        tex1cCopy.next_to(tex1b, RIGHT)
        
        
        tex2cMinus =  TexMobject(
            "- {r} - {r}^2  - \\cdots",
            tex_to_color_map={"{r}": BLUE}
        )
        
        
        
        
        

        
        

        #coord2 = DOWN
        self.play(Write(tex1a), Write(tex1b), Write(tex1c))
        self.wait(0.5)
        self.add(tex1aCopy, tex1bCopy, tex1cCopy)
        self.play(ApplyMethod(tex1a.shift, DOWN),ApplyMethod(tex1b.shift, DOWN) ,ApplyMethod(tex1c.shift, DOWN))
        self.wait(1.5)
        self.play(FadeOut(tex1a), FadeOut(tex1b),GrowFromEdge(tex2a, LEFT),GrowFromEdge(tex2b, LEFT),
                  FadeOut(tex1c, LEFT),GrowFromEdge(tex2c, LEFT) )
        self.wait(2.5)
        self.play(ApplyMethod(tex1aCopy.shift, np.array([-.5,-2,0])),FadeOut(tex1bCopy) ) 
        self.wait(.2)
        minus = add_obj(tex1aCopy, color=WHITE)
        self.add(minus)
        self.play(ApplyMethod(tex2a.next_to, minus, RIGHT ),FadeOut(tex2b) )
        self.wait(.2)
        eq = add_obj(tex2a, "=")
        self.add( eq )
        self.play(ApplyMethod(tex1cCopy.next_to, eq , RIGHT )  )
        self.wait(.2)
        self.play(Transform(tex2c,tex2cMinus.next_to(tex1cCopy, DOWN)))
        self.wait(2)
        one=add_obj(eq, "1")
        zero=add_obj(one, "\\ + \\  0")
        self.play(Transform(tex1cCopy, one ) ,Transform(tex2c, zero ))
        self.wait(1)
        self.play(FadeOut(tex2c))
        self.wait(1)
        self.play(ApplyMethod(tex1cCopy.shift, np.array([0,1.5,0])), 
                  ApplyMethod(tex1aCopy.shift, np.array([0,1.5,0])),
                  ApplyMethod(tex2a.shift, np.array([0,1.5,0])),
                  ApplyMethod(minus.shift, np.array([0,1.5,0])),
                  ApplyMethod(eq.shift, np.array([0,1.5,0]))
                  )
                  
        #This very last self.play above is hackish ..
        #I discovered the Group function shortly hereafter thinking
        #there has got to be a better way...
        #This should have been done using Group (as it was below)
        
        self.wait(1.5)


       	group = Group(tex1cCopy, tex1aCopy, tex2a, minus, eq)
       	factor = TexMobject(
       		"S (1-r) \\ = \\ 1",
       		tex_to_color_map = {"S":ORANGE, "r":BLUE}
       		)
        factor.shift(np.array([1,1.5,0]))

       	final = TexMobject(
       		" S \\ = \\ \\frac{1}{1 - {r} }",

       		tex_to_color_map = {"S":ORANGE , "{r}":BLUE}
       		)
       	final.shift(np.array([.7,-.4,0]))
       	

       	self.play(Transform(group, factor))
       	self.wait(1.5)
       	self.play(Transform(factor, final))

        self.wait(2)
        
#To make animation go to terminal and execute
# manim geometric_series.py geoSeries
