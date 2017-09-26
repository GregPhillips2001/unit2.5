#Greg Phillips
#9/26/17
#warmup5.py - yellow diamond with bame inside in blue

from ggame import * 

black = Color(0x000000,1)
yellow = Color(0xffff00,1)
blue = Color(0x0000ff,1)

blackOutline = LineStyle(1,black) #(pixels thick,color)

yellowDiamond = PolygonAsset([(50,0), (0,50), (50,100), (100,50)], blackOutline, yellow)
text = TextAsset("Greg", fill=blue, style="bold 10pt Times")

Sprite(yellowDiamond)
Sprite(text, (25,50))

App().run()

