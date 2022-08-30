nucio=$2
grep -v "#" $1 | awk '{if ($4==$nucio) {print $5}}' | sort | uniq -c