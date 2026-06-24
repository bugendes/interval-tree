"""Tests for IntervalTree."""

import pytest
from interval_tree import IntervalTree, Interval


class TestIntervalTree:
    def test_insert_query(self):
        t = IntervalTree()
        t.insert(Interval(15, 20))
        t.insert(Interval(10, 30))
        t.insert(Interval(17, 19))
        t.insert(Interval(5, 20))
        t.insert(Interval(12, 15))
        t.insert(Interval(30, 40))

        result = t.query(Interval(14, 16))
        assert result is not None
        assert result.low <= 16 and result.high >= 14

    def test_no_overlap(self):
        t = IntervalTree()
        t.insert(Interval(1, 3))
        t.insert(Interval(5, 7))
        assert t.query(Interval(4, 4)) is None

    def test_query_all(self):
        t = IntervalTree()
        t.insert(Interval(1, 5))
        t.insert(Interval(3, 8))
        t.insert(Interval(10, 15))
        results = t.query_all(Interval(4, 6))
        assert len(results) == 2

    def test_size(self):
        t = IntervalTree()
        t.insert(Interval(1, 2))
        assert t.size == 1
