from itertools import groupby
from operator import itemgetter


def solution(l):
    return sort_releases(l)


def sort_releases(list):
    # List is sorted by each value of the split release numbers in order
    return sorted(list, key=lambda release: map(int, release.split('.')))


if __name__ == '__main__':
    revisions = ["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]
    sorted_revisions = solution(revisions)
    print(sorted_revisions)
