import glob
import os.path

template = "-- [command=python {file}] [slide-contents-exec=source-highlight -s py -i {file} -o STDOUT --outlang-def=./pango.outlang]\n"
for p in glob.glob("*.py"):
    print template.format(file=p)