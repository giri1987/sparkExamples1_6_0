acc=sc.accumulator(0)
wiki=sc.textFile("/dev/datalake/app/gcr/medt/input/wiki.txt")
wiki.flatMap(lambda x : x.split()).map(lambda x: acc.add(1)).collect()
print("Total words : ",acc.value)
