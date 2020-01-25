# https://codeyarns.com/2017/12/11/how-to-discover-type-hierarchy-in-python/
"""Print hierarchy of types present in Python."""

import argparse
import sys


def is_builtin(t):
    """Check if type is builtin."""
    builtin_s = "__builtin__" if sys.version_info.major <= 2 else "builtins"
    return t.__module__ == builtin_s


def process_a_type(t, level, options):
    # Not a builtin type
    if options.only_builtins and not is_builtin(t):
        return

    # Print type
    s = ""
    if level > 0:
        s += "    " * (level - 1)
        s += "+-- "
    s += t.__name__
    if options.show_module:
        s += " ({})".format(t.__module__)
    print(s)

    # -type- has no subclasses
    if t.__name__ == "type":
        return

    # Recurse through child types
    for st in t.__subclasses__():
        process_a_type(
            st,
            level + 1,
            options,
        )


def get_args():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    ap.add_argument("--only_builtins", default=False, action="store_true", help="Only show builtin types")
    ap.add_argument("--show_module", default=False, action="store_true", help="Show module name beside type")
    ap.add_argument("--import_module", default="", type=str, help="Import this module to get its types")
    args = ap.parse_args()
    return args


def main():
    args = get_args()

    # Import module wanted by user
    if args.import_module:
        __import__(args.import_module)

    # -object- type is root
    process_a_type(
        object,
        0,
        args,
    )


if __name__ == "__main__":
    main()
