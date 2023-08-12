#! /bin/bash

msg=$1

# clean notebooks /notebooks/
for f in ./*/*.ipynb 
do
  # # html   # jupyter nbconvert --to html $f
  jupyter nbconvert --clear-output --inplace $f   # clear output
  jupytext --to py:percent $f   # .py
done

# cp src
# clean sandbox /sandbox/
for f in ./notebooks/*.py 
do
  # echo "File -> $f"
  fn=$(basename $f) #   echo "FN => $fn"
  new="./src/"$fn #   echo "new => $new"
  mv $f $new
done

# black
python -m black ./

# git
git add .
git commit -m "update $msg"
git push

