#27.09.21
#Config(json) utils by LEDShack
import json
from os import path

#GET
def get(name):
    if(path.exists(name) == True):
        with open(name, 'r') as f:
            return(json.load(f))
    else:
        return({'a': 3})
#SET
def set(name, index, data):
    stock = get(name)
    if(stock.get(index) == None):
        stock[index] = data
        with open(name, 'w') as f:
            json.dump(stock, f, indent = 4)
#REM
def rem(name, index):
    stock = get(name)
    if(not (stock.get(index) == None)):
        del stock[index]
        with open(name, 'w') as f:
            json.dump(stock, f, indent = 4)
