import torch


class MLP(torch.nn.Module):
    def __init__(self, n_inputs, n_outputs, n_layers, n_hidden):
        super(MLP, self).__init__()
        self.n_layers = n_layers
        self.layers = torch.nn.ModuleList()
        for i in range(self.n_layers-1):
            if i == 0:
                self.layers.append(torch.nn.Linear(n_inputs, n_hidden))
            else:
                self.layers.append(torch.nn.Linear(n_hidden, n_hidden))

        self.layers.append(torch.nn.Linear(n_hidden, n_outputs))

    def forward(self, x):
        for i in range(self.n_layers-1):
            x = self.layers[i](x)
            x = torch.relu(x)
        x = self.layers[-1](x)
        return x