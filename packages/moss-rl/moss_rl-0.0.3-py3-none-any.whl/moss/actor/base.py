"""Base Actor."""
from typing import Callable, List, Optional

import jax
import jax.numpy as jnp
from core import Actor, Agent, Buffer
from dm_env import Environment

from moss.types import Transition


class BaseActor(Actor):
  """Base actor."""

  def __init__(
    self,
    buffer: Buffer,
    agent: Agent,
    env_maker: Callable[[], Environment],
    unroll_len: int,
    num_trajs: Optional[int] = None,
  ) -> None:
    """Init."""
    self._buffer = buffer
    self._agent = agent
    self._env_maker = env_maker
    self._unroll_len = unroll_len
    self._num_trajs = num_trajs

  def run(self) -> None:
    """Run actor."""
    env = self._env_maker()
    time_step = env.reset()
    unroll_steps = 0
    num_trajs = 0
    data: List[Transition] = []

    while True:
      if time_step.first():
        self._agent.reset()
      unroll_steps += 1
      action, logits = self._agent.step(time_step)
      time_step = env.step(action)
      transition = Transition(
        step_type=time_step.step_type,
        observation=time_step.observation,
        action=action,
        reward=time_step.reward,
        policy_logits=logits,
      )
      data.append(transition)

      # Add trajectory to replay buffer
      if unroll_steps == self._unroll_len or time_step.last():
        if len(data) < self._unroll_len + 1:
          continue
        trajs = data[-unroll_steps + 1:]
        stacked_traj = jax.tree_util.tree_map(lambda *x: jnp.stack(x), *trajs)
        self._buffer.add(stacked_traj)
        data = data[-unroll_steps:]
        unroll_steps = 0
        num_trajs += 1

      if self._num_trajs and num_trajs > self._num_trajs:
        break
