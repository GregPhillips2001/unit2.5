#Greg Phillips
#9/26/17
#name.py - prints name in middle with colored background

from ggame import * 

black = Color(0x000000,1)
blackOutline = LineStyle(1,black) #(pixels thick,color)

name = input("Enter your name: ")
color_input = input("Enter a RGB color code: ")
color = Color(color_input, 1)

text = TextAsset(name, fill = black, style="bold 40pt Times")
background = RectangleAsset(1000,1000,blackOutline,color)

Sprite(background)
Sprite(text, (400,250))

App().run()
