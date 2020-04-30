import os

from ... import analyze_replay_file
from ..utils import get_replay_path


# All relevant files begin with df_ .

def create_df_docs():
    replay_path = get_replay_path("SHORT_SAMPLE.replay")

    working_dir = os.path.dirname(__file__)

    df_summary_path = os.path.join(working_dir, 'df_summary.md')
    df_methods_path = os.path.join(working_dir, 'df_methods.md')
    df_docs_path = os.path.join(working_dir, "data_frame.md")

    analysis = analyze_replay_file(replay_path, clean=False)

    data_frame = analysis.get_data_frame()

    df_docs = open(df_docs_path, "w")
    df_docs.write("#pandas.DataFrame\n")

    with open(df_summary_path) as summary:
        for line in summary:
            df_docs.write(line)

    df_docs.write("\n")

    with open(df_methods_path) as methods:
        for line in methods:
            df_docs.write(line)

    df_docs.write("\n")

    df_docs.write("## Example (list of columns)\n")
    df_docs.write("Each subheading is the primary column heading, and each row is the secondary column heading."
                  "The 'Player' subheading will be unique for each player in the replay (i.e. for a 3v3 game, there "
                  "will be 6 distinct players)\n")

    current_heading = ""
    for c in data_frame.columns:
        if current_heading != c[0]:
            current_heading = c[0]
            df_docs.write("\n#### " + c[0])

        df_docs.write("\n\t" + c[1])


def benchmark_df_docs(benchmark):
    benchmark(create_df_docs)


if __name__ == '__main__':
    create_df_docs()
