import torch
import torch.nn as nn
import torch.nn.functional as F

# Encode the image to 16*8*8
class D2CEncoder(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(in_channels=1, out_channels=4, kernel_size=3, stride=1, padding=1)
        self.conv2 = nn.Conv2d(in_channels=4, out_channels=8, kernel_size=3, stride=2, padding=1)
        self.conv3 = nn.Conv2d(in_channels=8, out_channels=16, kernel_size=3, stride=1, padding=1)
#         self.conv4 = nn.Conv2d(in_channels=16, out_channels=16, kernel_size=3, stride=2, padding=1)
        
        # 16*8*8


    def forward(self, input_batch):
        step1 = F.relu(self.conv1(input_batch)) 
        step2 = F.relu(self.conv2(step1)) 
        step3 = F.relu(self.conv3(step2))
#         step4 = self.conv4(step3)

        ret = step3
        
        return ret