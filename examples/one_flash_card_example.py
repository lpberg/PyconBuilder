import sys, os
#add parent direction to module search path (so we can load PyconBuilder)
sys.path.append('../')
from PyconBuilder import createImageFromText

# EXAMPLE USE:
createImageFromText("have*had*have had","../images/flash_base.png","../fonts/Arimo-Bold.ttf")

