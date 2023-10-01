# Copyright 2021 The NetKet Authors - All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import Any

from netket.operator import AbstractOperator, AbstractSuperOperator

from netket.vqs import expect_and_forces

from .state import MCMixedState


# If batch_size is None, ignore it and remove it from signature
@expect_and_forces.dispatch
def expect_and_forces_operators(
    vstate: MCMixedState,
    operator: AbstractOperator,
    chunk_size: Any,
    *args,
    **kwargs,
):
    raise NotImplementedError("Gradients for operators are not implemented yet")


@expect_and_forces.dispatch
def expect_and_forces_nochunking(
    vstate: MCMixedState,
    operator: AbstractSuperOperator,
    chunk_size: None,
    *args,
    **kwargs,
):
    return expect_and_forces(vstate, operator, *args, **kwargs)
