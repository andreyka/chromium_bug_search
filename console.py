#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
from commit_search import CommitSearch


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-b", "--bug", help="Bug ID from Chromium issue tracker or release report", type=str,
                        required=True)
    parser.add_argument("-r", "--rel", help="Chromium release for bug search", type=str, required=True)
    args = parser.parse_args()
    search = CommitSearch(args.rel, args.bug)
    commits = search.find_bug_commit()
    if not commits:
        print('[-] Nothing was found')
        exit()

    else:
        print('Commit found:')
        for item in commits:
            print(item)
