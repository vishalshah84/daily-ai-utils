import argparse
import sys
from daily_ai_utils.text.wordcount import wordcount_source


__VERSION__ = "0.1.0"


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="daily-ai-utils",
        description="Swiss Army Knife for AI + Data utilities",
    )
    p.add_argument("--version", action="version", version=__VERSION__)

    sub = p.add_subparsers(dest="cmd", required=True)

    # --- wordcount ---
    wc = sub.add_parser("wordcount", help="Count lines/words/chars from a file or stdin")
    wc.add_argument(
        "path",
        nargs="?",
        default="-",
        help="Path to text file (use '-' or omit to read from stdin)",
    )

    # --- clean-csv ---
    cc = sub.add_parser(
        "clean-csv",
        help="Clean a CSV by dropping empty rows and duplicates; writes <name>_clean.csv by default",
    )
    cc.add_argument("input_path", help="Path to input CSV file")
    cc.add_argument(
        "-o",
        "--output",
        dest="output",
        default=None,
        help="Optional output path (default: <input_name>_clean.csv)",
    )

    return p


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.cmd == "wordcount":
        # Read from file or stdin based on the path argument
        stdin = None if args.path != "-" else sys.stdin
        stats = wordcount_source(args.path, stdin=stdin)
        print(stats)
        return

    if args.cmd == "clean-csv":
        # Lazy import so --help works even if pandas isn't installed yet
        try:
            from daily_ai_utils.data.clean_csv import clean_csv  # type: ignore
        except Exception as e:
            print(
                "❌ 'clean-csv' requires pandas. Install dependencies then retry:\n"
                "   pip install -e .",
                file=sys.stderr,
            )
            raise e

        out_path = clean_csv(args.input_path, args.output)
        print(f"✅ Cleaned CSV saved to {out_path}")
        return


if __name__ == "__main__":
    main()
