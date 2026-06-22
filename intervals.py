#!/usr/bin/env python3
"""Interval Tree — efficient range overlap queries."""

class Interval:
    def __init__(self, lo, hi, data=None):
        self.lo, self.hi, self.data = lo, hi, data
    def __repr__(self): return f"[{self.lo},{self.hi}]({self.data})"

class IntervalTree:
    def __init__(self): self.intervals = []
    def add(self, interval): self.intervals.append(interval)
    def query(self, lo, hi):
        return [iv for iv in self.intervals if iv.lo <= hi and lo <= iv.hi]

if __name__ == "__main__":
    tree = IntervalTree()
    meetings = [(9,10,"Standup"),(10,11,"Review"),(13,14,"Lunch"),
                (14,16,"Deep Work"),(10,12,"Pair Prog"),(16,17,"1:1")]
    for lo, hi, name in meetings:
        tree.add(Interval(lo, hi, name))
    print("Interval Tree — Meeting Scheduler")
    for q_lo, q_hi in [(10,11),(15,16),(9,9.5)]:
        overlaps = tree.query(q_lo, q_hi)
        print(f"  [{q_lo},{q_hi}] overlaps: {[iv.data for iv in overlaps]}")\n