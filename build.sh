awk -F=  '{if ($1 =="__version__") print substr($0,0, 17    $1=$2}' secretm/__init__.py | awk -F. '{print ++$3}'
rm -rf dist
python3 -m build
python3 -m twine upload dist/*
