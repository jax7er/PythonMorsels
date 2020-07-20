import argparse
import csv
import string

parser = argparse.ArgumentParser(description="process a csv file")
parser.add_argument("filename_orig", type=str)
parser.add_argument("filename_new", type=str)
parser.add_argument("--in-delimiter", dest="delimiter_orig", nargs="?", type=str)
parser.add_argument("--in-quote", dest="quote", nargs="?", type=str)
args = parser.parse_args()

delimiter_orig = args.delimiter_orig
quote = args.quote

delimiter_new = ","

with open(args.filename_orig, "r", newline="") as orig_f:
    if None in [delimiter_orig, quote]:
        delim_count = {}
        quote_count = {}

        for line in orig_f:
            for c in set(line):
                if c in ["\"", "'"]:
                    quote_count[c] = quote_count.get(c, 0) + 1
                elif c in string.punctuation:
                    delim_count[c] = delim_count.get(c, 0) + 1
        
        if delimiter_orig is None:
            delim_count_sorted = sorted(delim_count.items(), key=lambda t: t[1], reverse=True)
            delimiter_orig = delim_count_sorted[0][0]
            
        if quote is None:
            if quote_count:
                quote_count_sorted = sorted(quote_count.items(), key=lambda t: t[1], reverse=True)
                quote = quote_count_sorted[0][0]
            else:
                quote = "\""

        orig_f.seek(0)

    reader = csv.reader(orig_f, delimiter=delimiter_orig, quotechar=quote)

    with open(args.filename_new, "w", newline="") as new_f:
        writer = csv.writer(new_f, delimiter=delimiter_new, quotechar=quote, quoting=csv.QUOTE_MINIMAL)

        writer.writerows(reader)
