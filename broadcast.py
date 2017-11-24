#Broadcast Variable :
#====================

states=sqlContext.read.json("/dev/datalake/app/gcr/medt/input/us_states.json")
brd_states=sc.broadcast(states.collect())
brd_schema=sc.broadcast(states.schema)
storesDF=sqlContext.read.json("/dev/datalake/app/gcr/medt/input/store_locations.json")

#Creation of dataframe
#---------------------

df=sqlContext.createDataFrame(brd_states.value,brd_schema.value)
f_rdd=storesDF.join(df,"state").groupBy("census_division").agg({"census_division":"count"})
f_rdd.show()
