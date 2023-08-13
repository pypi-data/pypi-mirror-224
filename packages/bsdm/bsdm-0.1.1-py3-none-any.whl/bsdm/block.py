from svgwrite import cm, mm, px  

from utils.logger import LOGGER

from stylesheet import getStyleSheet
from classes.Text import Text

def drawBlock(x, y, width, height, name, dwg):
    
    _group = dwg.g( id=name, 
                    stroke='green',
                    stroke_width=1*px,
                    fill='white'       )
    dwg.add(_group)
    
    _block = dwg.rect(  insert=(x * px, y * px), 
                        size=(width * px, height * px),
                        rx = 10 * px,
                        ry = 10 *px                      )
    _block['class'] = 'eteven'
    
    _group.add(_block)
    
    
    _text = 'TITLÉ of thç block'
    _styleClass = 'etname'   
    _textSize = Text.getTextMetrics(_text, _styleClass)        
    print(_textSize)    
    
    _textX = x + 10  # 10 = margin. TODO: handles margin with CSS  
    _textY = y + 10  # 10 = margin. TODO: handles margin with CSS 
    
    _entityNameBlock = dwg.rect(insert=( (_textX) * px, (_textY) * px), 
                                size=((_textSize['width']) * px, _textSize['height'] * px),
                                stroke_width=0)
    

    _entityName = dwg.text(_text, insert=( (_textX) * px, (_textY + _textSize['height']*0.75) * px))
    _entityName['class'] = "defaulttext "+_styleClass
    
    _group.add(_entityNameBlock)  
    _group.add(_entityName)
  
    
