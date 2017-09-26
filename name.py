#Greg Phillips
#9/26/17
#name.py - prints name in middle with colored background

from ggame import * 

black = Color(0x000000,1)
blackOutline = LineStyle(1,black) #(pixels thick,color)

name = input("Enter your name: ")
color = input("Enter a RGB color code: ")

text = TextAsset(name, style="bold 40pt Times")
background = RectangleAsset(1000, 1000, blacOutline, color)

Sprite(text, (300,300))
Sprite(background)

App().run()
