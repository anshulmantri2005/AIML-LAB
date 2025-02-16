import numpy as np
arr_1d = np.array([4, 9, 6, 5,10])
print("1D Array:\n", arr_1d)
arr_arange = np.arange(10)
print("Array using arange:\n", arr_arange)
arr_linspace = np.linspace(0, 2, 5)
print("Array using linspace:\n", arr_linspace)
arr_2d = np.array([[9, 8, 7], [6, 5, 4]])
print("2D Array:\n", arr_2d)
arr_2d_reshaped = np.arange(6).reshape(2, 3)
print("2D Array using arange and reshape:\n", arr_2d_reshaped)
arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("3D Array:\n", arr_3d)
element = arr_1d[4]
print("Element at index 4:", element)
slice_arr = arr_2d[:, 1:3]
print("Sliced Array:\n", slice_arr)
reshaped_arr = arr_1d.reshape(5, 1)
print("Reshaped Array:\n", reshaped_arr)
concat_arr = np.concatenate((arr_1d, np.array([6, 7, 8])))
print("Concatenated Array:\n", concat_arr)
print("Shape of 2D Array:", arr_2d.shape)
print("Size of 2D Array:", arr_2d.size)
print("Data Type of 2D Array:", arr_2d.dtype)
print("Number of Dimensions in 3D Array:", arr_3d.ndim)
reshaped_arr = arr_1d.reshape(1, 5)
print("Reshaped Array:\n", reshaped_arr)
resized_arr = np.resize(arr_1d, (2, 3))
print("Resized Array:\n", arr_1d)
flattened_arr = arr_3d.flatten()
print("Flattened Array:\n", flattened_arr)
