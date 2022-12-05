import torch
import torch.nn as nn
import torch.nn.functional as F

def Decoder(feature_dim=64):
    return nn.Sequential(
        nn.Linear(feature_dim, 128),
        nn.ReLU(),
        nn.Linear(128, 8*8),
        nn.ReLU(),
        nn.Unflatten(-1, (1, 8, 8)), 
        nn.ConvTranspose2d(1, 32, 4, stride=2, padding=1),
        nn.ReLU(),
        nn.ConvTranspose2d(32, 64, 4, stride=2, padding=1),
        nn.ReLU(),
        nn.ConvTranspose2d(64, 1, 4, stride=2, padding=1),
        nn.Tanh()
    )