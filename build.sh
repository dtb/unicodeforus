#! /bin/bash -e

git checkout master
jekyll
git checkout gh-pages
find .  -not -path  '*_site*' -not -path '*.git*' -not -path "." -prune -exec rm -rf {} \;
mv _site/* .
rm -rf _site
rm build.sh char.py readme.md symbols
#find . -name "*.html" -exec sed -i '' -e 's/href="\//href="\/unicodeforus\//g' {} \;

echo "Built site"
