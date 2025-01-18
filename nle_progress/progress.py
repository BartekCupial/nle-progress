"""
Adapted from BALROG, https://github.com/balrog-ai/BALROG
"""


import importlib.resources
import json
import os
from dataclasses import dataclass, field
from typing import Optional

workspace_dir = os.path.dirname(importlib.resources.files("nle_progress").__str__())

with open(os.path.join(workspace_dir, "nle_progress/achievements.json"), "r") as f:
    ACHIEVEMENTS = json.load(f)


@dataclass
class NLEProgress:
    score: int = 0
    depth: int = 1
    gold: int = 0
    experience_level: int = 1
    time: int = 0
    dlvl_list: list = field(default_factory=list)
    xplvl_list: list = field(default_factory=list)
    highest_achievement: Optional[str] = None
    progression: float = 0.0

    def update(self, blstats):
        """
        Update the progress of the player given stats.

        Returns:
            float: The progression of the player.
        """
        stats = self._update_stats(blstats)

        xp = self._get_xp(stats)
        if xp not in self.xplvl_list and xp in ACHIEVEMENTS.keys():
            self.xplvl_list.append(xp)
            if ACHIEVEMENTS[xp] > self.progression:
                self.progression = ACHIEVEMENTS[xp]
                self.highest_achievement = xp

        dlvl = self._get_dlvl(stats)
        if dlvl not in self.dlvl_list and dlvl in ACHIEVEMENTS.keys():
            self.dlvl_list.append(dlvl)
            if ACHIEVEMENTS[dlvl] > self.progression:
                self.progression = ACHIEVEMENTS[dlvl]
                self.highest_achievement = dlvl

    def _update_stats(self, blstats):
        # see: https://arxiv.org/pdf/2006.13760#page=16
        stats_names = [
            "x_pos",
            "y_pos",
            "strength_percentage",
            "strength",
            "dexterity",
            "constitution",
            "intelligence",
            "wisdom",
            "charisma",
            "score",
            "hitpoints",
            "max_hitpoints",
            "depth",
            "gold",
            "energy",
            "max_energy",
            "armor_class",
            "monster_level",
            "experience_level",
            "experience_points",
            "time",
            "hunger_state",
            "carrying_capacity",
            "dungeon_number",
            "level_number",
        ]
        stats = {name: value for name, value in zip(stats_names, blstats)}

        self.score = int(stats["score"])
        self.depth = int(stats["depth"])
        self.gold = int(stats["gold"])
        self.experience_level = int(stats["experience_level"])
        self.time = int(stats["time"])

        return stats

    def _get_dlvl(self, stats):
        """
        Get the dungeong lvl from the stats string.

        Args:
            string (str): The stats string.
        Returns:
            str: The dungeong lvl
        """
        # dlvl = string.split("$")[0]
        dlvl = f"Dlvl:{stats['depth']}"
        return dlvl

    def _get_xp(self, stats):
        """
        Get the experience points from the stats string.

        Args:
            string (str): The stats string.
        Returns:
            str: The experience points
        """
        xp = f"Xp:{stats['experience_level']}"
        return xp
