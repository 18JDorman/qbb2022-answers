#nucoi=$2
grep -v "#" $1 | awk '{if ($4=='C') {print $5}}' | sort | uniq -c