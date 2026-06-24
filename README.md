# Interval Tree

A BST-based data structure for efficiently finding all intervals that overlap a given point or range.

## How It Works

An interval tree augments a BST with one extra field per node: `max_end`, the maximum high endpoint in that subtree. Intervals are keyed by their `low` endpoint.

**Search for overlap with query [lo, hi]:**
1. At each node, check if its interval overlaps the query.
2. If left child exists and `left.max_end >= lo`, recurse left (there might be overlaps there).
3. Always recurse right if needed.

The `max_end` prune is what makes it efficient — if `left.max_end < lo`, no interval in the left subtree can overlap the query.

## Complexity

| Operation | Time | Notes |
|-----------|------|-------|
| insert    | O(log n) | BST insert + max_end update |
| query (any) | O(log n) | Single path with prune |
| query (all) | O(log n + k) | k = number of results |

Space: O(n) for the tree.

## Applications

**Computational Geometry:** Finding all line segments that intersect a vertical ray, or all rectangles overlapping a region.

**Meeting Room Booking:** Check if a proposed time slot overlaps any existing booking. Insert: O(log n), check: O(log n).

**Genomics:** Gene annotations on chromosomes are intervals. Finding which genes overlap a query region is a classic interval tree application.

**Network Scheduling:** Finding overlapping time ranges in packet scheduling, bandwidth reservation, or QoS policies.
