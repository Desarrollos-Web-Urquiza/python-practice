class TinyIntError(Exception):
    def __init__(self):
        self.message = 'El número no cuenta con las caracteristicas de un número tinyInt'

    def  __str__(self):
        return self.message
    
def tiny_int(val):
    return val >= 0 and val <= 255

def validate_tiny_int(val): #"60"
    return isinstance(val, int)

try:
    numero = 400 
    if tiny_int(numero): 
        print ("El número es correcto")
    else: 
        raise TinyIntError()
except TinyIntError as error:
    print(error)