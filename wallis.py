from manimlib.imports import *


class Wallis(Scene):
    def construct(self):
        color = BLACK
        
        sc = 1
        sep = 2
        
        π = TexMobject('{\\pi} \\over 2', substrings_to_isolate=['{\\pi}'] ,color=color).shift(4*LEFT)
        
        
        eq = TexMobject(' = ', color=color ).next_to(π, RIGHT)
        two = TexMobject('2^{ \\phantom{ \\frac{1}{2} }  }', color=color, 
                         substrings_to_isolate=['{ \\phantom{ \\frac{1}{2} }  }']).next_to(eq, RIGHT)
        dot1 = TexMobject('\\cdot', color=color).next_to(two, 1.5*RIGHT)
        t2 = TexMobject('\\left( \\frac{2\\cdot 4}{3\\cdot 3} \\right)^{ \\phantom{ \\left( \\frac{1}{2}  \\right)^2  } }  ', 
                        color=color, substrings_to_isolate=['{ \\phantom{ \\left( \\frac{1}{2}  \\right)^2  } }'])
        t2.next_to(two,3*RIGHT)
        dot2 = TexMobject('\\cdot', color=color).next_to(t2, 1.5*RIGHT)
        t3 = TexMobject('\\left( \\frac{4\\cdot 6 \\cdot 6 \\cdot 8}{5\\cdot 5 \\cdot 7 \\cdot 7} \\right)^{ \\phantom{ \\left( \\frac{1}{2}  \\right)^3  } }', 
                        color=color, substrings_to_isolate=['{ \\phantom{ \\left( \\frac{1}{2}  \\right)^3  } }'])                
        t3.next_to(t2, 3.5*RIGHT)
        
        cdots = TexMobject('\\cdots', color=color).next_to(t3,1.5*RIGHT)
        
        terms = [π, eq, two, t2, t3, dot1, dot2,cdots]
        sc1 = Group(*terms)
        
        
        self.add(sc1)
            
            
        twoPos = two.get_part_by_tex('{ \\phantom{ \\frac{1}{2} }  }')
        t2Pos = t2.get_part_by_tex('{ \\phantom{ \\left( \\frac{1}{2}  \\right)^2  } }')
        t3Pos = t3.get_part_by_tex('{ \\phantom{ \\left( \\frac{1}{2}  \\right)^3  } }')
        
        firstPow = TexMobject('{}^{  \\frac{1}{2}   }', color='#0247FE').move_to(twoPos).scale(1)
        firstPow.shift(.15*RIGHT + .2*UP)

        t2Pow = TexMobject('{}^{ \\left(\\frac{1}{2}\\right)^2 }', color='#0247FE').move_to(t2Pos).scale(1)
        t2Pow.shift(.4*RIGHT + .6*UP)
        
        t3Pow = TexMobject('{}^{ \\left(\\frac{1}{2}\\right)^3 }', color='#0247FE').move_to(t3Pos).scale(1)
        t3Pow.shift(.4*RIGHT + .6*UP)
        
        πPos = π.get_part_by_tex('{\\pi}')
        e = TexMobject('e', color='#0247FE').move_to(πPos)
        
        rt=3
        self.play(GrowFromCenter(firstPow, run_time=rt), GrowFromCenter(t2Pow, run_time=rt), 
                  GrowFromCenter(t3Pow, run_time=rt),
                  GrowFromCenter(e, run_time=rt), ShrinkToCenter(πPos, run_time=rt))
        
