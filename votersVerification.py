class FaultyEntries(AccumulatorParam):
 def zero(self,initialize=""):
  return ""
 def addInPlace(self,s1,s2):
  return str(s1)+" "+str(s2)

correctEntries=sc.accumulator(0)
 

citizens_dat=sqlContext.read.json("/dev/datalake/app/gcr/medt/input/citizens.json")

def validate(x):
 if x.age >= 18:
  correctEntries.add(1)
 else:
  faultCount.add(x.age)
 return x  
  
citizens_dat.map(lambda x : validate(x)).collect()

correctEntries.value
faultCount.value
