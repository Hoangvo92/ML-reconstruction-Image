from models.resnet import ResNet, baseBlock


from torch.utils.data import DataLoader
import numpy as np
import torch
from matplotlib import pyplot as plt
import glob
#from functions import transforms as T 
#from functions.subsample import MaskFunc
from PIL import Image
from skimage.metrics import structural_similarity as cmp_ssim 



def reconstructImage( img_gt, noise_image):
    model_dir = f"/models/restnet-model1.pt"
    model = loadResNet(model_dir)
        #noise_image = noise_image.to('cuda:0')
    
    img_gt = img_gt.numpy()
    output = model(noise_image)
   # output = output.squeeze(1).cpu().detach().numpy()
    output = output.squeeze(1).detach().numpy()   #image under numpy form
    output_loss = torch.tensor(ssim(gt, output))  
    image_loss = torch.tensor(ssim(gt, image.squeeze(1).numpy()))
    SSIM_improvement = (output_loss.item()-image_loss.item())
    SSIM_score = output_loss.item()
    np_rescontruct_image = transform_kspace_to_image(output)# image noise numpy array
    im_reconstruct = Image.fromarray(np_rescontruct_image)
    im_reconstruct.save("testing/test.png") #for prediction values
    im_reconstruct.save("pred1.png")

    return im_reconstruct
    

def loadResNet( model_dir):
    #load model on CPU: laptop
    device = torch.device('cpu')
    #model = TheModelClass(*args, **kwargs)
    model = ResNet(baseBlock,[2, 2, 2, 2, 3, 3, 3, 3, 2, 2, 2, 2])
    #model.load_state_dict(torch.load(PATH, map_location=device))
    model.load_state_dict(torch.load(model_dir, map_location=device))
    model.eval()
    return model

def ssim(gt, pred):
    """ Compute Structural Similarity Index Metric (SSIM). """
    return cmp_ssim(
        gt.transpose(1, 2, 0), pred.transpose(1, 2, 0), multichannel=True, data_range=gt.max()
    )