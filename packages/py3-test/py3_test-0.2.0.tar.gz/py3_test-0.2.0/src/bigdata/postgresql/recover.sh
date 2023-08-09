#参数是日期
cd /data/file/databak/$1
for file in ./*
do
    echo $file
    gunzip -c $file  |mysql -ubiuser -p@biuser123
done
