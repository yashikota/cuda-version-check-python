import torch

print(f"{torch.cuda.is_available()=}")
print(f"{torch.version.cuda=}")
print(f"{torch.backends.cudnn.version()=}")
