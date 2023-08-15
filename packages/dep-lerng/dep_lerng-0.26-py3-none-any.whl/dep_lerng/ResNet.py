
from torch.nn import Module, Conv2d, Linear, MaxPool2d, AvgPool2d, Sequential, BatchNorm2d, Dropout, AdaptiveAvgPool2d, LazyConv2d, AlphaDropout, Bilinear
from torch.nn import BatchNorm1d, BatchNorm2d, GroupNorm, LazyLinear, LazyBatchNorm1d, LogSoftmax
from torch.nn import Mish, ReLU, LeakyReLU, PReLU, SELU, Tanh
from torch import flatten, unsqueeze

import torch

torch.manual_seed(43)

#------------------------------
from .ResBlock import ResBlock
from .UtilityBlocks import FastGlobalAvgPool2d, SpaceToDepth
from .ClassifierNet import ClassifierNet
#------------------------------
  
# torch.set_float32_matmul_precision("high")
# acti = PReLU()

def make_layers(args, init_channels):

    stages = args.pop(0)

    res_stages = []

    for s, stage in enumerate(stages):
        for l in range(stage):

            if l == 0 and s != 0:
                downsample = True
            else:
                downsample = False
            
            channels = init_channels * (2 ** s)

            block = ResBlock((channels, args, downsample))
            
            res_stages.append(block)

    return Sequential(*res_stages)

class Resnet(Module):
    def __init__(self, variant, flavor, head, attention, ratio, init_channels):

        """
        Accepted Variants:
        18 : [2, 2, 2, 2] -- Vanilla Block
        34 : [3, 4, 6, 3] -- Vanilla Block
        50 : [3, 4, 6, 3] -- Bottleneck Block
        101 : [3, 4, 6, 3] -- Bottleneck Block
        152 : [3, 4, 6, 3] -- Bottleneck Block

        Accepted Augments:
        None : No Augmenting
        V1 : Augmented data goes through shallow NN first, outputting a single digit ## DEPRECATED ##

        V1_A : Only Augment 1 ## DEPRECATED ##
        V1_B : Only Augment 2 ## DEPRECATED ##


        V2 : Augmented is concated directly with original data ## DEPRECATED ##

        
        V3 : Augmented data is SE'd then chosen     by a NN to directly augment original wafer ## DEPRECATED ##
        V3-Kai   : Combines V3 and V1 together ## DEPRECATED ##
        V3-Kai A : Only Augment 1 ## DEPRECATED ## 
        V4-Kai B : Only Augment 2 ## DEPRECATED ##

        V4 
       
        """
        variants = {

            '18' : [[2, 2, 2, 2], flavor, attention, ratio],
            '34' : [[3, 4, 6, 3], flavor, attention, ratio],

            # 'radon' : [[2, 2, 2], 'vanilla'],

            # '25_v2' : [[2, 4, 6, 2], 'bottleneck'],
            # 'custom' : [[2, 2, 2, 3], 'vanilla'],

            # '18'  : [[2, 2, 2, 2], 'vanilla'],
            # '34'  : [[3, 4, 6, 3], 'vanilla'],

            # '50'  : [[3 ,4, 6, 3], 'bottleneck'],
            # '101' : [[3 ,4, 23, 3], 'bottleneck'], 
            # '152' : [[3, 8, 36, 3], 'bottleneck'],
        }

        super(Resnet, self).__init__()

        if flavor == 'basic':
            channels = init_channels
        elif flavor == 'bottleneck':
            channels = init_channels * 4

        #---------------------------------------------------------------------------------- HEAD

        if head == 'bad':
            
            self.Head = Sequential(

                Conv2d(1, channels // 2, 3, 2, 1, bias = False),
                BatchNorm2d(channels // 2),
                Mish(inplace = True),

                Conv2d(channels // 2, channels // 2, 3, 1, 1, bias = False),
                BatchNorm2d(channels // 2),
                Mish(inplace = True),

                Conv2d(channels // 2, channels, 3, 1, 1, bias = False),
                BatchNorm2d(channels),
                Mish(inplace = True),

                MaxPool2d(3, 2, 1),
            )

        elif head == 'good':
            self.Head = Sequential(

                SpaceToDepth(),

                Conv2d(16, channels, 3, 1, 1, bias = False),
                BatchNorm2d(channels),
                Mish(inplace = True),
            )

        #---------------------------------------------------------------------------------- RESBLOCKS


        self.ResBlocks = make_layers(variants[variant], init_channels)

        #---------------------------------------------------------------------------------- EXTRA FEATURES


        #-------------------------------------------------------------- HEAD

        # self.feature_attention_head = Sequential(
        #     # Conv2d(in_channels = 1, out_channels = 32, kernel_size = 7, stride = 2, padding = 3, bias = False),
        #     # BatchNorm2d(32),
        #     # acti,

        #     Conv2d(in_channels = 1, out_channels = c, kernel_size = 3, stride = 1, padding = 1, bias = False),
        #     BatchNorm2d(c, momentum = self.moment),
        #     acti,

        #     Conv2d(in_channels = c, out_channels = c, kernel_size = 3, stride = 1, padding = 1, bias = False),
        #     BatchNorm2d(c, momentum = self.moment),
        #     acti,

        #     Conv2d(in_channels = c, out_channels = c, kernel_size = 3, stride = 1, padding = 1, bias = False),
        #     BatchNorm2d(c, momentum = self.moment),
        #     acti,

        #     # MaxPool2d(kernel_size = 3, stride = 2, padding = 1),
        # )

        #-------------------------------------------------------------- RESBLOCKS

        # self.feature_attention = make_layers('radon', variants['radon'], self.squeeze, self.moment)

        #---------------------------------------------------------------------------------- FULLY CONNECTED

        self.AvgPool = FastGlobalAvgPool2d(flatten = False)

        self.fc = ClassifierNet(flavor, init_channels)

    def forward(self, x):

        # print(torch.cuda.memory_summary(device=None, abbreviated=False))

        x1, x2 = x

        #--------------------------------------- HEAD
 
        # print(torch.cuda.memory_summary(device=None, abbreviated=False))

        x1 = self.Head(x1)

        #--------------------------------------- RESBLOCKS

        # print(torch.cuda.memory_summary(device=None, abbreviated=False))

        x1 = self.ResBlocks(x1)
        x1 = self.AvgPool(x1)

        #-------------------- RESBLOCKS -- EXTRA FEATURES

        # print(torch.cuda.memory_summary(device=None, abbreviated=False))

        # x2 = self.feature_attention_head(x2)
        # # print(torch.cuda.memory_summary(device=None, abbreviated=False))
        # x2 = self.feature_attention(x2)
        # # print(torch.cuda.memory_summary(device=None, abbreviated=False))
        # x2 = self.AvgPool(x2)
        # # print(torch.cuda.memory_summary(device=None, abbreviated=False))

        # # x1 = (x1, x2, x3)
        # x = (x1, x2)

        #--------------------------------------- FULLY CONNECTED

        # print(torch.cuda.memory_summary(device=None, abbreviated=False))
        
        x = self.fc(x1)

        return x
    