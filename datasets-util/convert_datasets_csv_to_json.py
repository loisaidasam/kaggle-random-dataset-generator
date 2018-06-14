
import json

import unicodecsv


def convert_csv_to_json(filename_csv='datasets.csv',
                        filename_json='datasets.json',
                        encoding='latin-1'):
    num_rows = 0
    with open(filename_csv, 'r') as fp_read, open(filename_json, 'w') as fp_write:
        fp_write.write(u'{\n\t"datasets": [\n')
        reader = unicodecsv.DictReader(fp_read, encoding=encoding)
        for num_rows, row in enumerate(reader, start=1):
            fp_write.write(u"\t\t%s,\n" % json.dumps(row))
        # We need to back up a couple of spaces to delete the last comma.
        # from the seek() docs:
        #   To change the file object's position, use f.seek(offset, from_what).
        #   The position is computed from adding offset to a reference point;
        #   the reference point is selected by the from_what argument. A
        #   from_what value of 0 measures from the beginning of the file, 1 uses
        #   the current file position, and 2 uses the end of the file as the
        #   reference point. from_what can be omitted and defaults to 0, using
        #   the beginning of the file as the reference point.
        # via https://docs.python.org/2/tutorial/inputoutput.html
        fp_write.seek(-2, 1)
        fp_write.write(u'\n]}')
    return num_rows


if __name__ == '__main__':
    print "Converting CSV to JSON"
    num_rows = convert_csv_to_json()
    print "Converted %s rows" % num_rows
