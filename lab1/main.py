import requiment1
import requiment2
import requiment3

# Call requiment 1
requiment1.load("Kennedy.jpeg")

# Call requiment 2
requiment2.convert_to_grayscale("Huseein.jpeg")
requiment2.contrast_adjustment("Huseein.jpeg")

# Call requiment 3

requiment3.global_equalization("Stalin.jpeg")
requiment3.adaptive_equalization("Stalin.jpeg")
requiment3.kernel_equalization("Stalin.jpeg")