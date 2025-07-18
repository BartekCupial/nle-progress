import gymnasium as gym

from nle_progress.progress import NLEProgress


class NLEProgressWrapper(gym.Wrapper):
    def __init__(self, env, progression_on_done_only: bool = True):
        super().__init__(env)
        self.progression_on_done_only = progression_on_done_only

    def reset(self, **kwargs):
        self.progress = NLEProgress()
        return self.env.reset(**kwargs)

    def step(self, action):
        obs, reward, term, trun, info = self.env.step(action)
        self.progress.update(obs["blstats"])

        done = term or trun
        if not self.progression_on_done_only or done:
            info["episode_extra_stats"] = self.episode_extra_stats(info)

        return obs, reward, term, trun, info

    def episode_extra_stats(self, info):
        extra_stats = info.get("episode_extra_stats", {})
        new_extra_stats = {
            "progression": self.progress.progression,
        }

        return {**extra_stats, **new_extra_stats}
