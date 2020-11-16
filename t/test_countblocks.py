#!/usr/bin/env python3
"""Test parse_args module."""


from countblocks import parse_args


def test_parse_args_defaults() -> None:
    """parse_args defaults."""
    parser = parse_args()
    assert not parser.verbose


def test_verbose() -> None:
    """parse_args understands --verbose."""
    parser = parse_args(["--verbose"])
    assert parser.verbose


def test_max_magnitude() -> None:
    """parse_args understands --max_magnitude."""
    parser = parse_args(["--max_magnitude=10"])
    assert parser.max_magnitude == 10


def test_help() -> None:
    """Test help which throws a SystemExit."""
    # TODO: How do I do this?
