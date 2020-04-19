from typing import *
from typing_extensions import *

MT60PlaylistEntry = TypedDict("PlaylistEntry", {
    "videoId": Text,
    "start": float,
    "end": float,
    "title": Text
})

