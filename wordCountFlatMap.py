wiki=sc.textFile("/dev/datalake/app/gcr/medt/input/wiki.txt")
wiki.flatMap(lambda x : x.split()).map(lambda x : 1)
