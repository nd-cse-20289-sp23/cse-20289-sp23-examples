#!/usr/bin/env python3

import concurrent.futures
import os
import re
import sys

import requests

# Constants

BASE = 'https://lofigirl.com/blogs/releases/'

# Functions

def wget(url):
    p = os.path.basename(url.split('?')[0]) # Review: os.path.basename

    print('Downloading {} to {}'.format(url, p))
    r = requests.get(url)
    with open(p, 'wb') as fs:               # Review: Writing to a file, with statement
        fs.write(r.content)

    return p

def flatten(sequence):
    for iterable in sequence:
        yield from iterable

# Main Execution

def main():
    # Download pages of each release of Lofi Girl
    # https://lofigirl.com/blogs/releases
    releases = (requests.get(url) for url in sys.argv[1:])
    assets   = flatten(
        re.findall(r'source src="([^"]+)"', release.text) for release in releases
    )

    # Sequential
    # list(map(wget, assets))           # Discuss: Why list?

    # Parallel                          # Discuss: concurrent.futures
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(wget, assets)      # Discuss: Timing

if __name__ == '__main__':
    main()
