import pytest
from um import count

def main():
    test()


def test():
    assert count("um") == 1
    assert count("um?") == 1
    assert count("Um, I got stuck on my way, come home later") == 1
    assert count("Um, sorry, um...") == 2