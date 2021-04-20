import cv2
import matplotlib
import numpy as np
from copy import copy


def calculate_single_dim_conv_output(h_in, padding, kernel_size, stride):
    return #Your Code


def calculate_conv_output_hw(h_in, w_in, padding, kernel_size, stride):
    return calculate_single_dim_conv_output(h_in, padding[0], kernel_size[0], stride), \
           calculate_single_dim_conv_output(w_in, padding[1], kernel_size[1], stride)


class MyConv2D:

    def __init__(self, img, kernel, pad, stride=1, flip=True):

        self.img = copy(img)
        self.img_ndim = img.ndim

        self.kernel = kernel
        self.set_kernel(kernel, flip)

        self.stride = stride

        self.padding = pad
        self.set_padding(pad)

        self.ndim = img.ndim
        self.h_out, self.w_out = calculate_conv_output_hw(self.get_h_in(), self.get_w_in(), self.padding,
                                                          self.get_kernel_size(), self.stride)

    def get_kernel_size(self):
        return self.kernel.shape

    def get_h_in(self):
        return int(self.img.shape[0])

    def get_w_in(self):
        return int(self.img.shape[1])

    def get_channels_in(self):
        if self.ndim == 3:
            return self.img.shape[2]
        else:
            return 1

    def get_input_image_dim(self):
        return self.get_h_in(), self.get_w_in()

    def set_padding(self, pad):
        if isinstance(pad, int):
            self.padding = pad
        if isinstance(pad, str):
            self.padding = self.calculate_padding(self.get_h_in(), self.get_w_in(), self.get_kernel_size(),
                                                  self.stride, padding=pad)

    def set_kernel(self, kernel, flip):
        if flip:
            #self. kernel =  Your code here 
        else:
            #self. kernel = Your code here

    
    @staticmethod
    def calculate_padding(h_in, w_in, kernel_size, stride=1, padding='same'):
        if padding.lower() == 'same':
            return calculate_padding_single_dim(h_in, h_in, kernel_size[0], stride), \
                   calculate_padding_single_dim(w_in, w_in, kernel_size[1], stride)

        if padding.lower() != 'full':
            assert 'invalid padding specified'
        else:  
            return # Your code here 

    def my_conv_single_channel(self, single_channel_image=None):
        # Your code
        pass

    def my_conv_multi_channel(self):
        # Your code
        pass


def calculate_padding_single_dim(dim_in, dim_out, kernel_size, stride=1):
    # https://pytorch.org/docs/stable/generated/torch.nn.Conv2d.html#torch.nn.Conv2d
    return # Your Code 



