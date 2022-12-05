import torch
import torch.nn as nn
import torch.nn.functional as F


class FaceRecognizer2(nn.Module):
    def __init__(self, vgg, input_dim=64, output_dim=40, batch_size = 1):
        super().__init__()
        self.batch_size = batch_size
        self.conv1 = nn.Conv2d(in_channels=1, out_channels=3, kernel_size=3, stride=1, padding=1)
        self.vgg = vgg
        self.fc = nn.Linear(1000, 40)

    def forward(self, input_batch):
        step1 = F.relu(self.conv1(input_batch)) 
        step2 = F.relu(self.vgg(step1))
        step3 = self.fc(step2)
        ret = step3
        
        return ret