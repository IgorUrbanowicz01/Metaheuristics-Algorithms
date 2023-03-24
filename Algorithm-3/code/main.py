from Select import *
from Importing import *


distance_matrix = askUserForFilename()
paths = initial_select(distance_matrix, 100, 2)
select(10, paths)
