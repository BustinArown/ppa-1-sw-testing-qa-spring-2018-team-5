for  item in *.py
do
        if [ -f $item ]
        then
                 pylint --disable=R --disable=W0141 --disable=C0103 --disable=C -rn $item 
        fi
done
