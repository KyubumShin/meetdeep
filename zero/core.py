import numpy as np


class Tensor:
    def __init__(self, data):
        self.data = data


class Function:
    def __call__(self, input: Tensor):
        x = input.data
        y = self.forward(x)
        output = Tensor(y)
        return output

    def forward(self, x):
        raise NotImplementedError()
