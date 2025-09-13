import argparse
from daily_ai_utils.text.wordcount import wordcount_source

def build_parser():
    p = argparse.ArgumentParser(
        prog="daily-ai-utils",
        description="Swiss Army Knife for AI + Data utilities",
    )
    sub = p.add_subparsers(dest="cmd", required=True)

    # wordcount
    wc = sub.add_parser("wordcount", help="Count lines/words/chars from a file or stdin")
    wc.add_argument(
        "path",
        nargs="?",
        default="-",
        help="Path to text file (use '-' or omit to read from stdin)",
    )
    return p

def main():
    parser = build_parser()
    args = parser.parse_args()

    if args.cmd == "wordcount":
        stats = wordcount_source(args.path, stdin=None if args.path != "-" else __import__("sys").stdin)
        print(stats)

if __name__ == "__main__":
    main()
