from svgwrite import cm, mm, px  

import utils.config as config

from utils.logger import LOGGER

from classes.Text import Text


class Block: 
        
    def __init__(self, x, y, width, height, name):
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height
        self.__name = name
        
        self.__group = config.DWG.g(id=name, 
                                    stroke='green',
                                    stroke_width=1*px,
                                    fill='white'       )
        config.DWG.add(self.__group)
    
        self.__block = config.DWG.rect( insert=(x * px, y * px), 
                                        size=(width * px, height * px),
                                        rx = 10 * px,
                                        ry = 10 *px                      )
        self.__block['class'] = 'eteven'
    
        self.__group.add(self.__block)
    
        _text = Text(x, y, 'TITLÉ of thç blockuoeuepe', 'etname')
        _text.addToGroup(self.__group)