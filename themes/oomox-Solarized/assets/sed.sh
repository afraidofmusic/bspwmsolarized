#!/bin/sh
sed -i \
         -e 's/#002b36/rgb(0%,0%,0%)/g' \
         -e 's/#839496/rgb(100%,100%,100%)/g' \
    -e 's/#002b36/rgb(50%,0%,0%)/g' \
     -e 's/#073642/rgb(0%,50%,0%)/g' \
     -e 's/#00303d/rgb(50%,0%,50%)/g' \
     -e 's/#839496/rgb(0%,0%,50%)/g' \
	$@
