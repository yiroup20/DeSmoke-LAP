import cv2
# from PIL import Image
# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg
import numpy as np
# import torch
import torch.nn as nn
# from torch.nn import init
# import functools
# from torch.optim import lr_scheduler


class DCLoss(nn.Module):

    def compute_dc(self, im, sz):
        r = im[0]
        g = im[1]
        b = im[2]
        min_dc = cv2.min(cv2.min(r,g),b);
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(sz,sz))
        dark = cv2.erode(min_dc,kernel)
        
        return dark, min_dc

    def apply_guided_filter(self, im, p, r, eps):
        mean_I = cv2.boxFilter(im,cv2.CV_64F,(r,r));
        mean_p = cv2.boxFilter(p, cv2.CV_64F,(r,r));
        mean_Ip = cv2.boxFilter(im*p,cv2.CV_64F,(r,r));
        cov_Ip = mean_Ip - mean_I*mean_p;

        mean_II = cv2.boxFilter(im*im,cv2.CV_64F,(r,r));
        var_I   = mean_II - mean_I*mean_I;

        a = cov_Ip/(var_I + eps);
        b = mean_p - a*mean_I;

        mean_a = cv2.boxFilter(a,cv2.CV_64F,(r,r));
        mean_b = cv2.boxFilter(b,cv2.CV_64F,(r,r));

        q = mean_a*im + mean_b;

        return q;

    def refine_dc(self, im, dc, min_dc):
        r = 15;
        eps = 0.0001;
        dc_rfd = self.apply_guided_filter(min_dc,dc,r,eps);

        return min_dc;

    def get_refined_dc(self, input_img):
        # input_img = cv2.imread(path_image);
        dc, min_dc = self.compute_dc(input_img.cpu().data.numpy(), 15)
        dc = self.refine_dc(input_img,dc,min_dc)*255
        dc[dc < 0] = 0
        dc[dc > 255] = 255

        return np.uint8(dc)

    def __call__(self, hazy_image):
        batch_size, channels, height, width = hazy_image.size()
        index = np.random.randint(batch_size)
        input_img = hazy_image[index]
        refined_dc = self.get_refined_dc(input_img)
        loss = refined_dc.mean()*0.05

        return loss
