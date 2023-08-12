
from torch.nn import Module, Conv2d, Linear, MaxPool2d, AvgPool2d, Sequential, BatchNorm2d, Dropout, AdaptiveAvgPool2d, AdaptiveMaxPool2d, Dropout2d, LPPool2d
from torch.nn import BatchNorm2d, GroupNorm, LazyLinear, Identity, Sigmoid, Flatten, Unflatten
from torch.nn import Mish, ReLU, LeakyReLU, PReLU, SELU
from torch import mul

from torchvision.ops import DropBlock2d

from kornia.augmentation import Resize
import torch

#------------------------------
from .AttentionBlocks import SE_Block

# from custom_blocks import AFF,MSCAM, SAM, iAFF, ECA
#------------------------------

torch.manual_seed(43)

def ResBlock(args):

    """

    args: [flavor, channels, squeeze, downsample]

    """

    flavor, channels, squeeze, downsample = args
    
    if flavor == 'basic':
        return Basic_Block(channels, squeeze, downsample)
    
    elif flavor == 'bottleneck':
        return Bottleneck_Block(channels, squeeze, downsample)
    
    # elif flavor == 'radon':
    #     return


class ConvBlock(Module):
    def __init__(self, in_channels, out_channels, kernel_size = 3, stride = 1, padding = 1):
        super(ConvBlock, self).__init__()

        self.bn = BatchNorm2d(in_channels)
        self.activation = Mish(inplace = True)
        self.conv = Conv2d(in_channels, out_channels, kernel_size, stride, padding)
        
    def forward(self, x):

        x = self.bn(x)
        x = self.activation(x)
        x = self.conv(x)

        return x

#--------------------------------------------------------------------------------- Basic

class Basic_Block(Module):
    def __init__(self, channels, squeeze, downsample = False):
        super(Basic_Block, self).__init__()

        if downsample:
            stride = 2
            i_channels = channels // 2
            o_channels = channels 
        else:
            stride = 1
            i_channels = channels
            o_channels = channels

        self.BasicBlock = Sequential(
            ConvBlock(i_channels, o_channels, stride = stride),
            ConvBlock(o_channels, o_channels),
        )

        self.downsample = Sequential(
            AvgPool2d(stride, stride),
            ConvBlock(i_channels, o_channels, 1, 1, 0),
        )

        if squeeze:
            self.attention = SE_Block(o_channels, 16)

    def forward(self, x):

        identity = x

        x = self.BasicBlock(x)
        identity = self.downsample(identity)

        try:
            x = self.attention(x)
        except:
            pass

        x += identity

        return x

#--------------------------------------------------------------------------------- Basic

#--------------------------------------------------------------------------------- Bottleneck

class Bottleneck_Block(Module):
    def __init__(self, channels, squeeze, downsample = False):
        super(Bottleneck_Block, self).__init__()

        if downsample:
            stride = 2
            i_channels = channels * 2
            m_channels = channels
            o_channels = channels * 4
        else:
            stride = 1
            i_channels = channels * 4
            m_channels = channels
            o_channels = channels * 4

        self.BottleneckBlock = Sequential(
            ConvBlock(i_channels, m_channels, kernel_size = 1, padding = 0),
            ConvBlock(m_channels, m_channels, stride = stride),
            ConvBlock(m_channels, o_channels, kernel_size = 1, padding = 0),
        )

        self.downsample = Sequential(
            AvgPool2d(stride, stride),
            ConvBlock(i_channels, o_channels, 1, 1, 0),
        )

    def forward(self, x):

        identity = x

        x = self.BottleneckBlock(x)
        identity = self.downsample(identity)

        print(x.size())
        print(identity.size())

        x += identity

        return x




