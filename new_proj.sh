#!/bin/bash

function tmpl() {
  tmpl=$1
  name=$2
  ext=$(echo $tmpl | sed 's/templates\/\(.*\)\.tmpl/\1/')

  if [[ $ext = "Makefile" ]]; then 
    out="$name/Makefile"
  else
    out="$name/$name.$ext"
  fi

  sed "s/##/$2/g" $tmpl > $out
}

if [ -z $1 ]; then
  echo Requires One Argument
else
  if [[ -d $1 ]]; then
    echo "Problem $1 already exists... Bailing."
    exit 1
  else
    mkdir -p $1 
    for i in templates/*.tmpl; do
      tmpl $i $1
    done
  fi
fi
