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
text = TextAsset("SATURDAYS", fill=white, style="bold 40pt Times")
text2 = TextAsset("ARE_FOR", fill=blue, style="bold 40pt Times")
text3 = TextAsset("THE BOYS", fill=white, style="bold 40pt Times")

Sprite(redRectangle)
Sprite(whiteRectangle, (0,100))
Sprite(blueRectangle, (0,200))
Sprite(text, (100,25))
Sprite(text2, (130,125))
App().run()
