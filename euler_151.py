import functools
import copy
import sys
import pytest


@functools.lru_cache(maxsize=None)
def expect_single_times(*args):
	papers = list(args)
	expected = 0
	if len(papers) == 1:
		expected = 1
	for paper in papers:
		new_papers = copy.copy(papers)
		new_papers.remove(paper)
		for n in range(5 - paper):
			new_papers.append(paper + n + 1)
		expected += expect_single_times(*new_papers) / len(papers)
	return expected


def test_expect_single_times():
	assert expect_single_times(5) == 1
	assert expect_single_times(4) == 2
	assert expect_single_times(4, 5) == 1.5
	assert expect_single_times(4, 4) == 1.5


if __name__ == "__main__":
	if "-test" in sys.argv:
		pytest.main([__file__])
	else:
		print(expect_single_times(1) - 2)