import board
import pulseio
from adafruit_slideshow import PlayBackOrder, SlideShow

# Create the slideshow object that plays through once alphabetically.
#pylint: disable=no-member
slideshow = SlideShow(board.DISPLAY, pulseio.PWMOut(board.TFT_BACKLIGHT), folder="/",
                      loop=False, order=PlayBackOrder.ALPHABETICAL)
#pylint: enable=no-member

while slideshow.update():
    pass
