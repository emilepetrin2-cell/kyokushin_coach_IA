### testing cuba and the link with the graphic card
import torch

if torch.cuda.is_available() == False:
    raise ValueError("CUDA not available")


if torch.cuda.device_count() <1:
    raise ValueError("No GPU found")
device = torch.cuda.get_device_name(0)
print (device)
test = torch.rand (3, 3)
print  (test.device)
test = test.to("cuda:0")
print (test.device)

mat1 = torch.randn ((5000, 5000), device = "cuda:0")
mat2 = torch.randn ((5000, 5000), device = "cuda:0")
result = torch.matmul(mat1, mat2)
torch.cuda.memory_allocated(0) / (1024 ** 2)
print(result)
=======================================================================
