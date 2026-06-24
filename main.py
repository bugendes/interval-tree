#!/usr/bin/env python3
"""Interval Tree demo."""

from interval_tree import IntervalTree, Interval


def main():
    print("=== Interval Tree Demo ===
")

    t = IntervalTree()
    intervals = [Interval(15,20), Interval(10,30), Interval(17,19),
                 Interval(5,20), Interval(12,15), Interval(30,40)]
    for iv in intervals:
        t.insert(iv)

    q = Interval(14, 16)
    print(f"Query {q}:")
    print(f"  Any overlap: {t.query(q)}")
    print(f"  All overlaps: {t.query_all(q)}")


if __name__ == "__main__":
    main()
