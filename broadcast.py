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


#Output

#+------------------+--------------------+
#|   census_division|count(census_region)|
#+------------------+--------------------+
#|   Middle Atlantic|                  45|
#|East South Central|                  12|
#|East North Central|                  43|
#|    South Atlantic|                  74|
#|           Pacific|                 174|
#|          Mountain|                  48|
#|West South Central|                  31|
#|West North Central|                  21|
#|                  |                   6|
#|       New England|                  21|
#+------------------+--------------------+
