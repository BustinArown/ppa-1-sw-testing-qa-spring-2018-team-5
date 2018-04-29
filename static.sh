for  item in *.py
do
        if [ -f $item ]
        then
                 pylint $item 
        fi
done
