from typing import Union

import torch
import torch.nn as nn
from torch import Tensor
import torch.nn.functional as F

from models.aggregate import select_method
from models.modules import SimpleLinear
from models.tasks.absract import TaskDependentModule


class SimpleClassificationModule(TaskDependentModule):
    def __init__(self, input_dim:int = 768, num_classes:int = 26, head_type='avgpool', **kwargs) -> None:
        super().__init__()
        self.head = select_method(head_type, input_dim=input_dim, **kwargs)
        if kwargs.get('is_concatenated', False):
            print("Connecting Pooling layer concatenating representations, while doubling the input dimensions.")
            self.linear = SimpleLinear(input_dim * 2, num_classes)
        else:
            self.linear = SimpleLinear(input_dim, num_classes)

    def forward(self, inputs, input_lengths, *args) -> Tensor:
        speech_representation = self.head(inputs, input_lengths, *args)
        outputs = self.linear(speech_representation)
        return outputs

    def predict(self, inputs, input_lengths, *args) -> Union[int, Tensor]:
        speech_representation = self.head(inputs, input_lengths, *args)
        outputs = self.linear(speech_representation)
        return outputs.max(-1)
    
    def extract(self, inputs, input_lengths, *args) -> Tensor:
        speech_representation = self.head(inputs, input_lengths, *args)
        return speech_representation