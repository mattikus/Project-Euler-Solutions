if [ -z $1 ]; then
  echo Requires One Argument
else
  mkdir $1 && sed "s/#/$1/g" Makefile.tmpl > ./$1/Makefile  
  touch $1/$1.py $1/$1.c
fi
