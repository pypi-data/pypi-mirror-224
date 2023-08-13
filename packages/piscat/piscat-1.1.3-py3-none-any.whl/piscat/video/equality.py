from __future__ import annotations

from piscat.video import Video

class Video_equality(Video):
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Video_equality):
            return False
        if self.shape != other.shape:
            return False
        if self.precision != other.precision:
            return False
        return False
