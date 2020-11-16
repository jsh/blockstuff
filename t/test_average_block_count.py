#!/usr/bin/env python3
"""Test parse_args() function."""


from average_block_count import parse_args


def test_parse_args_defaults() -> None:
    """parse_args defaults."""
    parser = parse_args()
    assert not parser.verbose


def test_verbose() -> None:
    """parse_args understands --verbose."""
    parser = parse_args(["--verbose"])
    assert parser.verbose


def test_length() -> None:
    """parse_args understands --length."""
    parser = parse_args(["--length=8"])
    assert parser.length == 8


def test_trials() -> None:
    """parse_args understands --trials."""
    parser = parse_args(["--trials=200"])
    assert parser.trials == 200


def test_help() -> None:
    """Test help which throws a SystemExit."""
    # TODO: How do I do this?
