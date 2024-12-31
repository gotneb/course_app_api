from dataclasses import dataclass


@dataclass
class Lesson:
    id: int
    title: str
    duration: int # time in secs
    video_url: str = "https://youtu.be/Ah__4g01y_M?si=PbVbDvK1_jPjSRJW"