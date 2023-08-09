# Copyright 2023 The Flax Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import jax
from jax import numpy as jnp, random, lax
from flax.linen import initializers
from typing import Callable
from flax.linen import Module, compact


class Dense(Module):
  features: int
  kernel_init: Callable = initializers.lecun_normal()
  bias_init: Callable = initializers.zeros_init()
  use_bias: bool = True

  @compact
  def __call__(self, inputs):
    kernel = self.param(
        'kernel', self.kernel_init, (inputs.shape[-1], self.features)
    )
    y = lax.dot_general(
        inputs,
        kernel,
        (((inputs.ndim - 1,), (0,)), ((), ())),
    )
    if self.use_bias:
      bias = self.param('bias', self.bias_init, (self.features,))
      y = y + bias
    return y
