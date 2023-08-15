
from torch.nn import Module, Conv2d, Linear, MaxPool2d, AvgPool2d, Sequential, BatchNorm2d, Dropout, AdaptiveAvgPool2d, AdaptiveMaxPool2d, Conv1d
from torch.nn import BatchNorm1d, GroupNorm, LazyLinear, Identity, Sigmoid, Flatten, Unflatten, Tanh, Hardsigmoid, Hardtanh, Softmax
from torch.nn import Mish, ReLU, LeakyReLU, PReLU, SELU
from torch import mul

import torch.nn.functional as F

import torch

from torchvision.ops import DropBlock2d

from kornia.augmentation import Resize

acti = Mish(inplace = True)
# acti = PReLU()

moment = 1E-1

class FastGlobalAvgPool2d():
    def __init__ (self, flatten=False):
        self.flatten = flatten
    
    def __call__ (self, x):
        if self.flatten:
            in_size = x.size()
            return x.view(( in_size [0], in_size [1], -1)).mean(dim=2)
                           
        else:
            return x.view(x.size(0), x.size(1), -1).mean(-1).view(x.size(0), x.size(1), 1, 1)
        

class ChannelPool(Module):
    def forward(self, x):
        return torch.cat( (torch.max(x,1)[0].unsqueeze(1), torch.mean(x,1).unsqueeze(1)), dim=1 )
    
class SpaceToDepth(Module):
    def __init__(self, block_size=4):
        super().__init__()
        assert block_size == 4
        self.bs = block_size

    def forward(self, x):
        N, C, H, W = x.size()
        x = x.view(N, C, H // self.bs, self.bs, W // self.bs, self.bs)  # (N, C, H//bs, bs, W//bs, bs)
        x = x.permute(0, 3, 5, 1, 2, 4).contiguous()  # (N, bs, bs, C, H//bs, W//bs)
        x = x.view(N, C * (self.bs ** 2), H // self.bs, W // self.bs)  # (N, C*bs^2, H//bs, W//bs)
        return x