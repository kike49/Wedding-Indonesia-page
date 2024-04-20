import sys
path = '/home/kike49/Wedding-Indonesia-page/'
if path not in sys.path:
    sys.path.insert(0, path)
from yourapp import app as application
