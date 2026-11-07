#!/usr/bin/env python3
"""Compute Fibonacci numbers.

This module provides an iterative implementation of the Fibonacci
sequence that works for large inputs without deep recursion, plus a
small command-line interface to print the first N terms.
"""

from __future__ import annotations

import sys


def fibonacci(n: int) -> int:
    """Return the n-th Fibonacci number (0-indexed).

    F(0) = 0, F(1) = 1, and F(n) = F(n-1) + F(n-2) for n >= 2.

    Raises:
        ValueError: if n is negative.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")

    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def fibonacci_sequence(count: int):
    """Yield the first `count` Fibonacci numbers."""
    if count < 0:
        raise ValueError("count must be a non-negative integer")

    a, b = 0, 1
    for _ in range(count):
        yield a
        a, b = b, a + b


def main(argv: list[str] | None = None) -> int:
    """Print the first N Fibonacci numbers and return an exit code."""
    args = sys.argv[1:] if argv is None else argv

    if len(args) > 1:
        print("Usage: python fibonacci.py [count]", file=sys.stderr)
        return 2

    count = 10
    if args:
        try:
            count = int(args[0])
        except ValueError:
            print(f"Invalid count: {args[0]!r}", file=sys.stderr)
            print("Usage: python fibonacci.py [count]", file=sys.stderr)
            return 2

    try:
        terms = list(fibonacci_sequence(count))
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 2

    print(" ".join(map(str, terms)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
