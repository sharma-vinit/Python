def memory_locations_of(value):
    for index, element in enumerate(value):
        print("{: <15}{}".format("index[" + str(index) + "] ", hex(id(element))))
        print("{: <15}{}".format(str(element), hex(id(str(element)))))


python_list = [0, 1, 2]
memory_locations_of(python_list)

# import numpy library
import numpy as np

# Create a numpy array
numpy_list = np.array([0, 1, 2], dtype='int32')
memory_locations_of(numpy_list)