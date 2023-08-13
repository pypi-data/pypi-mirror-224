from svgwrite import cm, mm, px  

import tkinter as Tkinter
import tkinter.font as tkFont

import re

import utils.config as config

from utils.logger import LOGGER



class Text:
    
    _TK_ROOT = Tkinter.Tk() 
        
    def __init__(self, x=None, y=None, text=None, styleClass=None):

        self.__x = x + 10 # 10 = margin. TODO: handles margin with CSS
        self.__y = y + 10 # 10 = margin. TODO: handles margin with CSS
        self.__text = text
        self.__styleClass = styleClass
        
        self.__size = Text.getTextMetrics(self.__text, self.__styleClass)        
        print(self.__size)    
        
        self.__entityBlock = config.DWG.rect(insert=( (self.__x) * px, (self.__y) * px), 
                                            size=((self.__size['width']) * px, self.__size['height'] * px),
                                            stroke_width=0)        
        
        self.__entity = config.DWG.text(self.__text, 
                                        insert=( (self.__x) * px, 
                                        (self.__y + self.__size['height']*0.75) * px))
        self.__entity['class'] = "defaulttext " + self.__styleClass

    def addToGroup(self, group):
        group.add(self.__entityBlock)  
        group.add(self.__entity)
        


    @classmethod
    def __handleFontSize(cls, font_size):
        _font_size = re.sub(r'[^0-9]', '', font_size) 
        _font_units = re.sub(r'[^a-zA-Z]', '', font_size) 
        
        if(_font_units == 'px'):
            _font_size = 0 - int(_font_size)
            
        return _font_size        

    @classmethod
    def __handleFontWeight(cls, font_weight):
        if(font_weight is None or font_weight != 'bold'):
            return Tkinter.font.NORMAL
        return Tkinter.font.BOLD
    
    @classmethod    
    def __handleFontWeight(cls, font_weight):
        if(font_weight is None or font_weight != 'bold'):
            return Tkinter.font.NORMAL
        return Tkinter.font.BOLD    
    
    @classmethod
    def __handleFontStyle(cls, font_style):
        if(font_style is None or font_style != 'italic'):
            return Tkinter.font.ROMAN
        return Tkinter.font.ITALIC    
    
    @classmethod
    def __handleFontDecoration(cls, font_decoration):
        _font_decoration = {}
        _font_decoration['overstrike'] = 0
        _font_decoration['underline'] = 0     
        
        if(font_decoration is not None) :        
            if('line-through' in font_decoration.lower()):
                _font_decoration['overstrike'] = 1          
            if('underline' in font_decoration.lower()):
                _font_decoration['underline'] = 1      
        
        return _font_decoration    
    
    @classmethod
    def __getTextMetrics(cls, text, fontFamily, fontSize, fontStyle=None, fontWeight=None, fontDecoration=None):

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
    
    @classmethod  
    def getTextMetrics(cls, text, styleClass):
        
        _textFontFamily = config.DEFAULTFONTFAMILY
        _textFontSize = config.DEFAULTFONTSIZE
        _textFontStyle = config.DEFAULTFONTSTYLE
        _textFontWeight = config.DEFAULTFONTWEIGHT 
        _textFontDecoration = config.DEFAULTFONTDECORATION       
        
        _textStyle = config.STYLESHEET['defaulttext']       
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
        
        _textStyle = config.STYLESHEET[styleClass]       
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
  