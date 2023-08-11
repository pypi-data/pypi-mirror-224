from ..interfaces import ReinforcementLearning


class OnlineRL(ReinforcementLearning):
    def improve(self, episode: int) -> None:
        batch_size = len(self)

        self.experience.clear()
