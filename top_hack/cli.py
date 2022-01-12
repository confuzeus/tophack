"""Console script for top_hack."""
import argparse
import sys
import webbrowser
from .top_hack import TopHack


def main():
    """Console script for top_hack."""
    parser = argparse.ArgumentParser()
    parser.add_argument('-ms',
                        '--min-score',
                        metavar='N',
                        type=int,
                        default=100,
                        help="Minimum score to fetch.")
    parser.add_argument('-n',
                        '--amount',
                        metavar='N',
                        type=int,
                        default=10,
                        help="Amount of results to fetch.")
    args = parser.parse_args()

    app = TopHack(args.amount, args.min_score)
    results = app.run()

    presentation = ''

    for idx, result in enumerate(results):
        presentation += f"[{idx}] {result['title']} ({result['score']})\n"

    print(presentation)

    while True:
        try:
            chosen = int(input("Which number? <C-c> to quit."))
        except Exception:
            continue
        webbrowser.open(results[chosen]['url'], new=2)
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
