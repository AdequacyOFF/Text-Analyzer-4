import torch.nn as nn

class MLP(nn.Module):
  def __init__(self, in_channels, class_amount):
    super().__init__()

    self.in_channels = in_channels
    self.class_amount = class_amount
    
    self.fc1 = nn.Linear(self.in_channels, 100)
    self.fc2 = nn.Linear(100, self.class_amount)
    self.ln = nn.LayerNorm(100)
    
    self.act = nn.LeakyReLU(0.2, inplace=True)

  def forward(self, x):
    out = self.fc1(x) 
    out = self.ln(out)
    out = self.act(out)
    out = self.fc2(out)

    return out