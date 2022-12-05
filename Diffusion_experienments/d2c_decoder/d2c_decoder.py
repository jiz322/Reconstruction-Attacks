import torch
import torch.nn as nn
import torch.nn.functional as F

# imput: 16*8*8
def D2CDecoder(feature_dim=64):
    return nn.Sequential(
        nn.Conv2d(in_channels=16, out_channels=32, kernel_size=3, stride=1, padding=1),
        nn.ReLU(),
        nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3, stride=1, padding=1),
        nn.ReLU(),
#         nn.ConvTranspose2d(16, 64, 4, stride=2, padding=1),
#         nn.ReLU(),
#         nn.ConvTranspose2d(64, 64, 4, stride=2, padding=1),
#         nn.ReLU(),
        nn.ConvTranspose2d(64, 1, 4, stride=2, padding=1),
        nn.Tanh()
    )