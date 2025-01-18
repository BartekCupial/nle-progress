import gym
from gym.envs import registration

from nle_progress.task import NetHackProgress
from nle_progress.wrapper import NLEProgressWrapper

_version = "v0"

entry_point = "nle_progress.task:NetHackProgress"
kwargs = {}
if gym.__version__ >= "0.21":
    # Starting with version 0.21, gym wraps everything by the
    # OrderEnforcing wrapper by default (which isn't in gym.wrappers).
    # This breaks our seed() calls and some other code. Disable.
    kwargs["order_enforce"] = False
registration.register(id="%s-%s" % ("NetHackProgress", _version), entry_point=entry_point, **kwargs)

__all__ = [NLEProgressWrapper, NetHackProgress]
