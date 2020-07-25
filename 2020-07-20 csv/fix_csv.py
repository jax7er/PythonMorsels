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

with open(args.filename_orig, "r", newline="") as orig_f:
    if delimiter_orig or quote:
        reader_kwargs = {k: v 
            for k, v 
            in zip(["delimiter", "quotechar"], [delimiter_orig, quote])
            if v}
    else:
        reader_kwargs = {"dialect": csv.Sniffer().sniff(orig_f.read())}
        orig_f.seek(0)
    
    reader = csv.reader(orig_f, **reader_kwargs)

    with open(args.filename_new, "w", newline="") as new_f:
        csv.writer(new_f).writerows(reader)
