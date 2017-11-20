#Accumulator example :(tested in pyspark shell)
#==============================================

from pyspark import Accumulator,AccumulatorParam

heightCount=sc.accumulator(0)

class StringAccumulatorParam(AccumulatorParam):
 def zero(self,initialSize=""):
  return ""
 def addInPlace(self,s1,s2):
  return s1.strip()+" "+s2.strip()
  
heightValues=sc.accumulator("",StringAccumulatorParam())

def validate(x):
 ht=x.height
 if (ht < 15 or ht > 80 ):
  heightCount.add(1)
  heightValues.add(str(ht))

#This will create a dataframe... of key-values from json file  
heightDF=sqlContext.read.json("/dev/datalake/app/gcr/medt/input/heights.json")

heightDF.foreach(lambda x : validate(x))

#Test our accumulators:
#======================
#>>> heightCount.value
#3
#>>> heightValues.value
#'102 85 1'
#>>>
