import gymnasium as gym
from gymnasium.envs.registration import register

from nle_progress.task import NetHackProgress
from nle_progress.wrapper import NLEProgressWrapper

_version = "v0"

entry_point = "nle_progress.task:NetHackProgress"
kwargs = {}

# Gymnasium does not have the OrderEnforcing wrapper issue.
# You generally don't need to disable it.
# But you can still pass kwargs if needed for your environment.

register(
    id=f"NetHackProgress-{_version}",
    entry_point=entry_point,
    kwargs=kwargs,
)

__all__ = [NLEProgressWrapper, NetHackProgress]
