import torch

class ModeloLinear(torch.nn.Module):
    def __init__(self, n_inputs, n_outputs):
        super(ModeloLinear, self).__init__()
        # Definindo uma camada linear
        self.linear = torch.nn.Linear(n_inputs, n_outputs)

    def forward(self, x):
        return self.linear(x)