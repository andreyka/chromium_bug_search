#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
from commit_search import CommitSearch


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-b', '--bug', help='Bug ID from Chromium issue tracker or release report', type=str,
                        required=True)
    parser.add_argument('-r', '--rel', help='Release version', type=str, required=True)
    parser.add_argument('-p', '--prod', help='Specify "chromium" or "v8" search, default value is "chromium" ',
                        type=str, default='chromium', required=False)
    parser.add_argument('-mp', '--maxpages', help='Specify log pages limit, default vaule is 500',
                        type=int, default=500, required=False)
    args = parser.parse_args()
    search = CommitSearch(args.rel, args.bug, args.prod, args.maxpages)
    commits = search.find_bug_commit()
    if not commits:
        print('[-] Nothing was found')
        exit()

    else:
        print('[+] Commits found:')
        for item in commits:
            print(item)
