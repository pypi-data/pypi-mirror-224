import tkinter as Tkinter
import tkinter.font as tkFont

import re

from utils.logger import LOGGER

from stylesheet import getStyleSheet


class Text:
    
    _TK_ROOT = Tkinter.Tk() 
        
    def __init__(self, x=None, y=None, text=None):
        self.__x = x
        self.__y = y
        self.__text = text


    @staticmethod
    def __handleFontSize(font_size):
        _font_size = re.sub(r'[^0-9]', '', font_size) 
        _font_units = re.sub(r'[^a-zA-Z]', '', font_size) 
        
        if(_font_units == 'px'):
            _font_size = 0 - int(_font_size)
            
        return _font_size        

    @staticmethod
    def __handleFontWeight(font_weight):
        if(font_weight is None or font_weight != 'bold'):
            return Tkinter.font.NORMAL
        return Tkinter.font.BOLD
    
    @staticmethod    
    def __handleFontWeight(font_weight):
        if(font_weight is None or font_weight != 'bold'):
            return Tkinter.font.NORMAL
        return Tkinter.font.BOLD    
    
    @staticmethod
    def __handleFontStyle(font_style):
        if(font_style is None or font_style != 'italic'):
            return Tkinter.font.ROMAN
        return Tkinter.font.ITALIC    
    
    @staticmethod
    def __handleFontDecoration(font_decoration):
        _font_decoration = {}
        _font_decoration['overstrike'] = 0
        _font_decoration['underline'] = 0     
        
        if(font_decoration is not None) :        
            if('line-through' in font_decoration.lower()):
                _font_decoration['overstrike'] = 1          
            if('underline' in font_decoration.lower()):
                _font_decoration['underline'] = 1      
        
        return _font_decoration    
    
    @staticmethod
    def __getTextMetrics(text, fontFamily, fontSize, fontStyle=None, fontWeight=None, fontDecoration=None):

        font = None
        
        _fontSize = Text.__handleFontSize(fontSize)
        _fontWeight = Text.__handleFontWeight(fontWeight)
        _fontStyle = Text.__handleFontStyle(fontStyle)
        _fontDecoration = Text.__handleFontDecoration(fontDecoration)
        
        """
        print("family= "+str(fontFamily)) 
        print("size= "+str(_fontSize))
        print("weight= "+str(_fontWeight)) 
        print("slant= "+str(_fontStyle))
        print("overstrike= "+str(_fontDecoration['overstrike']))
        print("underline= "+str(_fontDecoration['underline'] ))
        """
        
        font = tkFont.Font( family=fontFamily, 
                            size=_fontSize, 
                            weight=_fontWeight, 
                            slant=_fontStyle, 
                            overstrike=_fontDecoration['overstrike'],
                            underline=_fontDecoration['underline'] )
        
        if (font is not None) :
            _text_metrics = {}
            _text_metrics['width'] = font.measure(text)
            _text_metrics['height'] = font.metrics('linespace')
            return _text_metrics
        
        return None    
    
    @staticmethod  
    def getTextMetrics(text, styleClass):
        
        _textFontFamily = 'Open Sans'
        _textFontSize = '10px'
        _textFontStyle = None
        _textFontWeight = None 
        _textFontDecoration = None       
        
        _textStyle = getStyleSheet()[styleClass]
        
        
        try: 
            _textFontFamily = _textStyle['font-family']
        except:
            pass
        
        try: 
            _textFontSize = _textStyle['font-size']
        except:
            pass    
        
        try: 
            _textFontStyle = _textStyle['font-style']
        except:
            pass
        
        try: 
            _textFontWeight = _textStyle['font-weight']
        except:
            pass

        try: 
            _textFontDecoration = _textStyle['text-decoration']
        except:
            pass
        
        return Text.__getTextMetrics(text, _textFontFamily, _textFontSize, fontStyle=_textFontStyle, fontWeight=_textFontWeight, fontDecoration=_textFontDecoration)        
  