import torch
import torch.nn as rizz
import numpy as np

def convert(flagz):
	flag = [float(ord(i)) for i in flagz]
	output = torch.tensor([flag], dtype=torch.float32)
	return output

def init(_in, _out):
  weight = np.round(np.random.uniform(-1, 1, (_out, _in)).astype(np.float32),2)
  bias = np.round(np.random.uniform(-1, 1, _out).astype(np.float32),2)
  return torch.from_numpy(weight), torch.from_numpy(bias)


sigma = rizz.Sequential(
    rizz.Linear(40, 222),
    rizz.Linear(222, 100),
    rizz.Linear(100, 33)
)

layer_shapes = [(40, 222), (222, 100), (100, 33)]

for i, (input_dim, output_dim) in enumerate(layer_shapes):
  weight, bias = init(input_dim, output_dim)
  sigma[i].weight.data = weight
  sigma[i].bias.data = bias

np.random.seed(0x2019)
flag = "PETIR{REDACTED}"
print([i.detach().numpy().tolist() for i in sigma(convert(flag))])

# Output
# [22847.716796875, -21964.810546875, -14513.71875, -3790.312744140625, -8359.19921875, -950.1218872070312, -25765.904296875, 33915.84765625, 25927.662109375, 2029.1702880859375, 20599.05859375, -22778.146484375, 23582.5546875, -33654.6640625, -10178.52734375, 10646.5927734375, 18819.64453125, -8857.6650390625, 2287.3623046875, 22975.994140625, 8632.626953125, 1591.319580078125, -3773.903564453125, 6465.8408203125, -14653.0146484375, 7569.791015625, -5770.65673828125, -34205.97265625, -16681.216796875, -3415.234375, 5391.5654296875, -12609.5859375, 4626.630859375]