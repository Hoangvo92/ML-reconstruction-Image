import numpy as np
import torch
import torchvision.transforms as T
import PIL
from PIL import Image
#import random
import numpy as np
from numpy.fft import fftshift, ifftshift, fftn, ifftn
#import cmath

def noise_and_kspace(image):
    #change to k-space
    img_fft = fftshift(fftn(image))
    #add noise
    size_img = img_fft.shape
     #np.random.uniform, np.random.normal
    std = np.random.normal(0.000, 0.005) * np.amax(img_fft)
    noise = fftshift(std * np.random.standard_normal(size_img) + std * 1j * np.random.standard_normal(size_img));     #This generates a complex noise signal.
    img_fft_noise = img_fft + noise # noise image in k-space form
    img_noise = ifftn(ifftshift(img_fft_noise))# revert k-space back to noise
    return img_noise

def to_k_space(image):
    # create k-space image by using fourier transform
    # input: image in Image form
    # output: return k-space image
    return fftshift(fftn(image))

def to_Pil_image(noise_image):
    #using this function after noise_and_kspace to show noise image
    return Image.fromarray(np.uint8(noise_image)).convert('L')


def preprocessImage(image, noise_image):
    preprocess = T.Compose([
                           T.Resize(128),    #128 as maximum
                           T.CenterCrop(128),
                           T.ToTensor()
                            ])
    img_gt = preprocess(Image.fromarray(np.uint8(image)).convert('L'))
    img_und = preprocess(Image.fromarray(np.uint8(noise_image)).convert('L'))
    
    norm = (img_und**2).sum(dim=-1).sqrt().max()
 
    if norm < 1e-6: norm = 1e-6
    
    img_gt, img_und = img_gt/norm , img_und/norm  

    return img_gt, img_und