# NetHack Progression Metric

The NetHack Progression Metric, introduced in the [BALROG benchmark](https://arxiv.org/abs/2411.13543), offers a data-driven approach to measuring player progression in NetHack. This metric improves upon the traditional scoring system by providing a more meaningful measure of progress based on empirical player data. It tracks advancement through two primary dimensions: <b>Dungeon Levels (Dlvl)</b> and <b>Experience Levels (XL)</b>, correlating each level with the probability of achieving an ascension (winning).

Progression metric is probability of winning derived from actual human data. The metric normalizes progress where:
- Starting point (Dlvl:1, XL:1) = 0% progression
- Ascension = 100% progression

Example
A character at:
- Dungeon Level 15 (30% progress score)
- XP Level 12 (33% progress score)

Would have a progression score of 33%

### Installation
```bash
pip install git+https://github.com/BartekCupial/nle-progress.git
```

### Usage
To monitor progress as a metric
```bash
import gym
import nle
from nle_progress import NLEProgressWrapper

env = gym.make("NetHackChallenge-v0")
env = NLEProgressWrapper(env, progression_on_done_only=False)
obs = env.reset()
obs, reward, done, info = env.step(env.action_space.sample())
print(info["episode_extra_stats"])
```

To use progress as a reward
```bash
import gym
import nle_progress

env = gym.make("NetHackProgress-v0")
obs = env.reset()
obs, reward, done, info = env.step(env.action_space.sample())
```