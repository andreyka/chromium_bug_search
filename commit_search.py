#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import re
import requests


class CommitSearch(object):
    src_url = 'https://chromium.googlesource.com'
    cr_log_path = '/chromium/src/+log/'
    cr_commit_path = '/chromium/src/+/'
    v8_log_path = '/v8/v8/+log/'
    v8_commit_path = '/v8/v8/+/'

    def __init__(self, version, bug, product, max_pages):
        self.page_counter = max_pages
        self.found = False
        self.commits = set()
        self.id = bug
        if product == 'chromium':
            self.rel_url = self.src_url + self.cr_log_path + version
            self.commit_url = self.src_url + self.cr_commit_path

        if product == 'v8':
            self.rel_url = self.src_url + self.v8_log_path + version
            self.commit_url = self.src_url + self.v8_commit_path

        self.bug_re = re.compile(self.id)

    def _find_bug_id(self, commits):
        for commit in commits:
            message = commit.get('message')
            if not message:
                continue

            matched = re.findall(self.bug_re, message)
            if not matched:
                continue

            sha1 = commit.get('commit')
            self.commits.add(self.commit_url + sha1)
            self.found = True

    def _parse_changelog(self, log):
        if self.found:
            return

        self.page_counter -= 1
        next_id = log.get('next')
        commits = log.get('log')
        if commits:
            self._find_bug_id(commits)

        if next_id:
            next_changelog_url = self.rel_url + '?s=' + next_id + '&format=JSON'
            next_log = json.loads(requests.get(next_changelog_url).content[4:])
            if self.page_counter > 0:
                try:
                    self._parse_changelog(next_log)

                except RuntimeError:
                    return

    def find_bug_commit(self):
        changelog_url = self.rel_url + '/?format=JSON'
        log = json.loads(requests.get(changelog_url).content[4:])
        self._parse_changelog(log)
        return self.commits
