import re
import json

from utils.logger import LOGGER

_STYLESHEET = None

def _cleanElementString(elementString):
    _elementString =  re.sub('/\*.*\*/', '', elementString) # remove comme (/* comment */ like)
    _elementString = _elementString.replace(' ', '').replace('\n','').replace('\t','') # removing spaces
    _elementString = _elementString.replace(':', '":"').replace(';','","').replace('{', '{"') # adding quotes
    _elementString = _elementString[:-2] + '}' # remove ", and add }
    
    
    
    return _elementString

def _transformCSSToDict(cssElements):
    
    _keysValues = re.compile(r"([a-zA-Z0-9(\);\s\#\"\-\.\_]+):([a-zA-Z0-9:\(\)\s\#\"\-\.\_]*)")
   
    _jsonElementItems= {}
        
    for _keyValue in _keysValues.finditer(cssElements):
        _jsonElementItems[_keyValue.group(1).strip()] = _keyValue.group(2).strip()
    
    return(_jsonElementItems)
    

def _substituteVar(cssStyleSheet, styleSheetVar):

    _cssStyleSheet = cssStyleSheet
    
    for var  in styleSheetVar:
        _cssStyleSheet = re.sub('var\s*\(\s*\-\-'+var+'\s*\)', styleSheetVar[var], _cssStyleSheet)
    
    return _cssStyleSheet
    

def _loadElementsStyle(cssStyleSheet, styleSheetVar):
    
    _cssStyleSheet = re.sub('/\*.*\*/', '',  cssStyleSheet)                            # remove comme (/* comment */ like)        
    _cssStyleSheet = _substituteVar(_cssStyleSheet, styleSheetVar)
    
    _elementPattern = re.compile(r"\.([a-zA-Z0-9:\(\);\s\#\"\-\.\_]+)[\s]*{\s*([a-zA-Z0-9(\);\s\#\"\-\.\_]+:[a-zA-Z0-9:\(\);\s\#\"\-\.\_]*)}")
    
    _elementStyle = {}
    
    for _element in _elementPattern.finditer(_cssStyleSheet):
        _elementStyle[_element.group(1).strip()] = _transformCSSToDict(_element.group(2))
    
    return _elementStyle

def _listVars(cssStyleSheet):
    _styleSheetVars = {}

    _cssStyleSheet = re.sub('/\*.*\*/', '',  cssStyleSheet)                            # remove comme (/* comment */ like)    
    
    _varPattern = re.compile(r"\-\-([a-zA-Z0-9\s\-]+:[a-zA-Z0-9\s\#\"\-]+);")

    for _var in _varPattern.finditer(_cssStyleSheet):
        tmp = _var.group(1).split(":")
        _styleSheetVars[tmp[0].strip()] = tmp[1].replace('"','').strip()
        
    return _styleSheetVars


def loadFromCSSStyleSheet(cssStyleSheet):
    _styleSheetVars = _listVars(cssStyleSheet)
    
    global _STYLESHEET
    _STYLESHEET = _loadElementsStyle(cssStyleSheet, _styleSheetVars) 
    
def getStyleSheet():
    return _STYLESHEET

    