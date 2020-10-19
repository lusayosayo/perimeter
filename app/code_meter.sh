#!/bin/bash
echo '' > count.txt

find -type f -exec wc -l {} >> count.txt \;

python3 -c "file = open('count.txt'); counts = [ int(line.split()[0]) for line in file.readlines()[1:] ]; print(sum(counts)); file.close();"

