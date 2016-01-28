#!/usr/bin/env python

import sys

from wordcount import load_word_counts

def plot_word_counts(counts, limit=10):
    """
    Given a list of (word, count, percentage) tuples, generate a crude
    plot of the counts made from asterisks. Only the first limit tuples
    are plotted.
    """
    text = "Word Counts\n"
    limited_counts = counts[0:limit]
    word_field_width = max(len(w) for w, _, _ in limited_counts)
    max_number_asterisks = 75 - word_field_width
    scale_factor = float(max_number_asterisks) / float(limited_counts[0][1])
    for word, count, _ in limited_counts:
        number_asterisks = int(scale_factor * count)
        text += "%s %s\n" % (word.ljust(word_field_width), number_asterisks*'*')
    return text

if __name__ == '__main__':
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    limit = 10
    if len(sys.argv) > 3:
        limit = int(sys.argv[3])
    counts = load_word_counts(input_file)
    text = plot_word_counts(counts, limit)
    if output_file == "show":
        print text
    else:
        with open(output_file, 'w') as output:
            output.write(text)
