"""Interval Tree implementation.

Augmented BST where each node stores an interval and the maximum endpoint
in its subtree. Enables efficient overlap queries.

Operations:
  - insert: O(log n)
  - query (find any overlapping): O(log n)
  - query_all (find all overlapping): O(log n + k)

Used in: computational geometry, scheduling, bioinformatics (gene overlap).
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, List, Optional, TypeVar

T = TypeVar("T")


@dataclass
class Interval(Generic[T]):
    low: T
    high: T

    def overlaps(self, other: "Interval[T]") -> bool:
        return self.low <= other.high and other.low <= self.high

    def __repr__(self) -> str:
        return f"[{self.low}, {self.high}]"


class _Node:
    __slots__ = ("interval", "max_end", "left", "right")

    def __init__(self, interval: Interval) -> None:
        self.interval = interval
        self.max_end = interval.high
        self.left: Optional[_Node] = None
        self.right: Optional[_Node] = None


class IntervalTree:
    """BST-based interval tree for overlap queries."""

    def __init__(self) -> None:
        self._root: Optional[_Node] = None
        self._size = 0

    def insert(self, interval: Interval) -> None:
        self._root = self._insert(self._root, interval)
        self._size += 1

    def query(self, interval: Interval) -> Optional[Interval]:
        """Find any interval overlapping the query. Returns None if none."""
        node = self._root
        while node:
            if node.interval.overlaps(interval):
                return node.interval
            if node.left and node.left.max_end >= interval.low:
                node = node.left
            else:
                node = node.right
        return None

    def query_all(self, interval: Interval) -> List[Interval]:
        """Find all intervals overlapping the query."""
        results = []
        self._query_all(self._root, interval, results)
        return results

    def _query_all(self, node, interval, results):
        if not node:
            return
        if node.interval.overlaps(interval):
            results.append(node.interval)
        if node.left and node.left.max_end >= interval.low:
            self._query_all(node.left, interval, results)
        self._query_all(node.right, interval, results)

    def _insert(self, node, interval):
        if not node:
            return _Node(interval)
        if interval.low < node.interval.low:
            node.left = self._insert(node.left, interval)
        else:
            node.right = self._insert(node.right, interval)
        node.max_end = max(node.max_end, interval.high)
        return node

    @property
    def size(self) -> int:
        return self._size

    def __len__(self) -> int:
        return self._size

    def __repr__(self) -> str:
        return f"IntervalTree({self._size} intervals)"
