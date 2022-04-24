FILE_ROW_COUNT=$(git log --since "6am" | grep "commit" | wc -l)

echo ${FILE_ROW_COUNT}