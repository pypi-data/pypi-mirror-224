"""Base agent."""
from typing import Any

from core import Agent, Predictor
from dm_env import TimeStep


class BaseAgent(Agent):
  """Base agent."""

  def __init__(
    self,
    predictor: Predictor,
  ) -> None:
    """Init."""
    self._predictor = predictor

  def reset(self) -> Any:
    """Reset agent."""

  def step(self, time_step: TimeStep) -> Any:
    """Agent step."""
    action, logits, _ = self._predictor.inference(time_step)
    return action, logits
