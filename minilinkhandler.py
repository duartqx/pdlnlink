#!/usr/bin/env python
from sys import argv, exit as _exit

def youtube_to_yewtube(url: str) -> str:
    ''' Converts youtube.com to yewtu.be url '''
    return f'https://yewtu.be/{url.split("/")[-1]}'


def main() -> None:

    url = ''
    if len(argv) > 1:
        url: str = argv[1]

    if 'youtu' in url:
        print(youtube_to_yewtube(url))
    else:
        print('You need to pass an youtube link as first argument!')
        _exit(1)
