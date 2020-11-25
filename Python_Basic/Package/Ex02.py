import inspect
import random
from travel import *

# tells us where the random file is exactly
print(inspect.getfile(random))
# print(inspect.getfile(vietnam))       Doesn't work bc vietname an element in the __all__ list

# if you place the module into the lib folder
# you can import it in any .py file