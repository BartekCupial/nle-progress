from nle.env.tasks import NetHackScore

from nle_progress.progress import NLEProgress


class NetHackProgress(NetHackScore):
    """Environment for the "progress" task.

    The task is similar to the one defined by `NetHackScore`, but the score is
    defined by the progress metric.
    """

    def reset(self, **kwargs):
        self.progress = NLEProgress()
        return super().reset(**kwargs)

    def _reward_fn(self, last_observation, action, observation, end_status):
        if not self.nethack.in_normal_game():
            # Before game started and after it ended blstats are zero.
            return 0.0

        last_progress = self.progress.progression
        self.progress.update(observation[self._blstats_index])
        reward = self.progress.progression - last_progress

        time_penalty = self._get_time_penalty(last_observation, observation)

        return reward + time_penalty
