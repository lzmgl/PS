FILE_ROW_COUNT=$(git log --since "6am" | grep "commit" | wc -l)
git cmp $FILE_ROW_COUNT