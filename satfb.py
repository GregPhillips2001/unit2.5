#Greg Phillips
#9/27/17
#satfb.py

from ggame import * 

red = Color(0xcc0000,1)
blue = Color(0x000099,1)
white = Color(0xffffff,1)
black = Color(0x000000,1)

blackOutline = LineStyle(1,black) #(pixels thick,color)

redRectangle = RectangleAsset(500,100,blackOutline,red) #(width,height,outline,fill)
whiteRectangle = RectangleAsset(500,100,blackOutline,white) #(width,height,outline,fill)
blueRectangle = RectangleAsset(500,100,blackOutline,blue) #(width,height,outline,fill)
text = TextAsset("SATURDAYS", fill=white, style="bold 50pt Times")
text2 = TextAsset("ARE_FOR", fill=blue, style="bold 50pt Times")
text3 = TextAsset("THE_BOYS", fill=white, style="bold 50pt Times")

Sprite(redRectangle)
Sprite(whiteRectangle, (0,100))
Sprite(blueRectangle, (0,200))
Sprite(text, (50,17))
Sprite(text2, (90,117))
Sprite(text3, (70,217))
App().run()
