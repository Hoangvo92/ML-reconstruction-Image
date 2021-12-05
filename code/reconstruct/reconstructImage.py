from models.resnet import ResNet, baseBlock


from torch.utils.data import DataLoader
import numpy as np
import torch
from PIL import Image
from skimage.metrics import structural_similarity as cmp_ssim 
import torchvision.transforms as T



def reconstructImage( img_gt, noise_image):
    model_dir = f"/models/restnet-model1.pt"
    model = loadResNet(model_dir)
        #noise_image = noise_image.to('cuda:0')

    
    img_gt = img_gt.unsqueeze(0).numpy()
    noise_image = noise_image.unsqueeze(0)
    noise_image = noise_image.unsqueeze(0)
    output = model(noise_image)
   # output = output.squeeze(1).cpu().detach().numpy()
    output = output.squeeze(1).detach()
    
    output_np = output.numpy()   #image under numpy form
    img_gt =  np.squeeze(img_gt)
    output_np =  np.squeeze(output_np)
    output_loss = torch.tensor(ssim(img_gt, output_np))  
    SSIM_score = output_loss.item()
    print(SSIM_score)
    
    #np_rescontruct_image =  output # np.reshape(output, (64, 64))# image noise numpy array
    #np_rescontruct_image = transform_kspace_to_image(output)# image noise numpy array
    im_reconstruct = T.ToPILImage()(output)
    im_reconstruct.save("testing/test.png") #for prediction values
    im_reconstruct.save("pred1.png")

    return im_reconstruct
    

    
    
        image = image.unsqueeze(0)
    image = image.unsqueeze(0)
    gt = gt.unsqueeze(0).numpy()
    output = model(image)
  #  output = output.squeeze(1).cpu().detach().numpy()
    output = output.squeeze(1).detach().numpy()
    image = image.squeeze(1).numpy()
    gt =  np.squeeze(gt)
    output =  np.squeeze(output)
    image =  np.squeeze(image)
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