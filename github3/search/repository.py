# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ..models import GitHubCore
from ..repos import Repository


class RepositorySearchResult(GitHubCore):
    def __init__(self, data, session=None):
        super(RepositorySearchResult, self).__init__(data, session)
        result = data.copy()
        #: Score of the result
        self.score = result.pop('score')
        #: Text matches
        self.text_matches = result.pop('text_matches', [])
        #: Repository object
        self.repository = Repository(result, self)

    def _repr(self):
        return '<RepositorySearchResult [{0}]>'.format(self.repository)
