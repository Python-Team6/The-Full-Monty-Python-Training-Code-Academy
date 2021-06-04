#!/usr/bin/env python3

import argparse
import module  # This will not link correctly if you use from imports


def some_helper(argument):
    """Some echo-like helper function.

    Returns a string that contains the input argument.

    :param argument: the argument to print in the return string
    :type argument: any
    :returns: "I repeat: " followed by the input argument
    :rtype: str"""
    return f"I repeat: {argument}"


def parse_args():  # pragma: no cover
    """Parse the input args."""
    parser = argparse.ArgumentParser(
        description="Blueprint executable. <To be updated by developer>"
    )
    return parser.parse_args()


def main(args):  # pragma: no cover
    """Main."""
    print(f"args: {args}")
    print(f"example function result: {module.example_function()}")

    example_inst = module.Example()
    print(
        f"example class result:"
        f"\n - instance: {example_inst}"
        f"\n - member:   {example_inst.example}"
    )


if __name__ == "__main__":
    args = parse_args()
    main(args)