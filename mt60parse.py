from demjson import decode
from typing import (
    List,
    cast,
)
from re import compile
from mt60types import MT60PlaylistEntry


def parse(file_contents: List[str]) -> List[MT60PlaylistEntry]:
    """
    We want to get lines like this.
    playList.push({ videoId : '5yt849wJyVk', start : 104.621, end : 164.62099999999998, title : 'Ludacris - Get Back' });
    """
    lines = [l for l in file_contents if "playList.push" in l]
    lines = [get_json(l) for l in lines]
    return lines

#                                     $1
regex = compile("^\s*playList\.push\((.*)\);$")
def get_json(line: str) -> MT60PlaylistEntry:
    match = regex.match(line)[1]
    return cast(MT60PlaylistEntry, decode(match))

def parse_from_file(filepath: str) -> List[MT60PlaylistEntry]:
    with open(filepath, 'r') as f:
        contents = f.readlines()

    return parse(contents)

