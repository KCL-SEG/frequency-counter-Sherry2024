"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for item in items:
        key = item if isinstance (item, str) else str(item)
        if key in frequencies:
            frequencies[key] += 1
        else:
            frequencies[key] = 1
    return frequencies
