# The script of the game goes in this file.

image white = Solid ("#FFF")
image cat = "cat.jpg"
image tail = "tail.png"

image top_text = ParameterizedText(xalign=0.5, yalign=0.0)

init python:

    import time
    import math
    import random

    x = 0
    y = 0
    dx = 1
    dy = 1
    pythonInitString = """{size=-5}
    import time
    import math
    import random

    x = 0
    y = 0
    dx = 1
    dy = 1"""
    #end pythonInitString
    imagesString = """{size=-5}
image white = Solid ("#FFF")
image cat = "cat.jpg"
image tail = "tail.png"
"""
    #end imagesString

    pythonCatTailString = """{size=-6}    def rotationangle (v, factor1, factor2, angle):
      return v * (factor1 +factor2) - factor2*100 +angle
    def rotation(trans, st, at, factor1, factor2=0, n=0, angle=0):
      v=(1+math.sin(time.time()))*50
      trans.rotate = rotationangle (v, factor1, factor2, angle)
      return 0"""
    pythonCatString="""{size=-6}    def translation(trans, st, at):
       global x,y,dx,dy
       trans.xpos = x; trans.ypos = y; x=x+dx; y=y+dy
       if random.random() < 0.2:
          dx = dx * -1
       if random.random() < 0.2:
          dy = dy * -1
       if x < 0:
          x=0
       if x > 1000:
          x = 1000
       if y<0:
          y=0
       if y>700:
          y=700
       return 0"""
    #end pythonString
    def rotationangle (v, factor1, factor2, angle):
      return v * (factor1 +factor2) - factor2*100 +angle
    def rotation(trans, st, at, factor1, factor2=0, n=0, angle=0):
      v=(1+math.sin(time.time()))*50
      trans.rotate = rotationangle (v, factor1, factor2, angle)
      return 0
    def translation(trans, st, at):
       global x,y,dx,dy
       trans.xpos = x
       trans.ypos = y
       x=x+dx
       y=y+dy
       if random.random() < 0.2:
          dx = dx * -1
       if random.random() < 0.2:
          dy = dy * -1
       if x < 0:
          x=0
       if x > 1000:
          x = 1000
       if y<0:
          y=0
       if y>700:
          y=700
       return 0
    renpyAnimString="""{size=-5}
       show white at topleft
       show cattail at translationTransform
       "Press a key to continue"
       hide cattail"""
    renpyString= """{size=-5}
transform rotationTransform (rotx, roty, xpos, ypos, factor1, factor2, n=0, angle=0):
  around (int(rotx), int(roty))
  alignaround (int(rotx), int(roty))
  xalign int(rotx)
  yalign int(roty)
  xpos int(xpos)
  ypos int(ypos)
  transform_anchor True
  function renpy.curry(rotation)(factor1=factor1, factor2=factor2, n=n, angle=angle)
  repeat
transform translationTransform:
  function renpy.curry(translation)()
  repeat
"""
    renpyLayeredString="""{size=-5}
layeredimage cattail:
  always:
    "cat.jpg"
  always:
    "tail.png"
    at rotationTransform (253, 265, 253, 265, 0.2, 0.2)
"""
#end renpyString

transform rotationTransform (rotx, roty, xpos, ypos, factor1, factor2, n=0, angle=0):
  around (int(rotx), int(roty))
  alignaround (int(rotx), int(roty))
  xalign int(rotx)
  yalign int(roty)
  xpos int(xpos)
  ypos int(ypos)
  transform_anchor True
  function renpy.curry(rotation)(factor1=factor1, factor2=factor2, n=n, angle=angle)
  repeat

transform translationTransform:
  function renpy.curry(translation)()
  repeat

layeredimage cattail:
  always:
    "cat.jpg"
  always:
    "tail.png"
    at rotationTransform (253, 265, 253, 265, 0.2, 0.2)

# The game starts here.

label start:
 show white at topleft
 $e = False
 while not e:
  menu:
    "{color=#f00}Example Renpy animation":
       pass
    "Show wandering cat":
       show white at topleft
       show cattail at translationTransform
       "Press a key to continue"
       hide cattail
    "Show python code":
     $p = True
     while p:
      menu:
       "Show python code (init)":
        hide white
        show top_text "[pythonInitString]"
        "Press a key to continue"
        hide top_text
        show white
       "Show python code (transformation function for cat, translation)":
        hide white
        show top_text "[pythonCatString]"
        "Press a key to continue"
        hide top_text
        show white
       "Show python code (transformation function for cat tail, rotation)":
        hide white
        show top_text "[pythonCatTailString]"
        "Press a key to continue"
        hide top_text
        show white
       "Go back":
        $p = False


    "Show renpy code":
     $p = True
     while p:
      menu:
       "Show renpy code (images)":
        hide white
        show top_text "[imagesString]"
        "Press a key to continue"
        hide top_text
        show white
       "Show renpy code (cat animation)":
        hide white
        show top_text "[renpyAnimString]"
        "Press a key to continue"
        hide top_text
        show white

       "Show renpy code (rotation and translation transforms)":
        hide white
        show top_text "[renpyString]" 
        "Press a key to continue"
        hide top_text
        show white
       "Show renpy code (cat transform)":
        hide white
        show top_text "[renpyLayeredString]"
        "Press a key to continue"
        hide top_text
        show white

       "Go back":
        $p = False
    "Finish":
       $e = True
 hide white
 hide cattail
 return
