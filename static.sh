for  item in *.py
do
        if [ -f $item ]
        then
                 pylint --disable=C --disable=W --disable=R  $item 
        fi
done
