BOARD = 1
OUT = 1
IN = 1
BCM = 1
HIGH = 1
LOW = 0

def setmode(a):
   print (f"Setting up mode: {a}")

def setup(a, b):
   print (f"Setting up: {a}, {b}")

def output(a, b):
   print (f"Setting Output: {a}, {b}")
   
def cleanup():
   print (f"Cleaning up")

def setwarnings(flag):
   print (f"Setting up warnings: {flag}")
