#Greg Phillips
#9/20/17
#graphicsDemo.py - intro to graphics 

from ggame import * 

red = Color(0xff0000,1)
green = Color(0x00ff00,1)
blue = Color(0x0000ff,1)
black = Color(0x000000,1)

blackOutline = LineStyle(1,black) #(pixels thick,color)

redRectangle = RectangleAsset(200,100,blackOutline,red) #(width,height,outline,fill)
blueCircle = CircleAsset(50,blackOutline,blue) #(radius,outline,fill)
greenEllipse = EllipseAsset(100,50,blackOutline,green) #(horizontal radius, verticle radius, outline, fill)
blackLine = LineAsset(50,160,blackOutline) #(x endpoint, y endpoint, lineStyle)
redTriangle = PolygonAsset([(0,0), (120,180), (60,300)],blackOutline,red) #list of endpoints
text = TextAsset("Greg",fill=green,style="bold 40pt Times") 

Sprite(redRectangle)
Sprite(blueCircle,(50,50)) #(num of pixels right, num of pixels down)
Sprite(greenEllipse,(200,400))
Sprite(blackLine)
Sprite(redTriangle)
Sprite(text,(300,200))
App().run()
