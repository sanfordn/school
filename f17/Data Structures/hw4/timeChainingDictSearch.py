# timeChainingDictSearch.py
"""Times the searching of the ChainingDict that uses hashing
   with chaining, i.e., UnorderedList objects at each hash table slot."""

from time import clock
from chaining_dictionary import ChainingDict

testSize = 40000                   # Number of items to search consisting of
evensDict = ChainingDict(2**16)
for i in range(0, 2*testSize, 2):  # even numbers from 0 to 2*(testSize-1)
    evensDict[i] = i
print( "Done entering values in ChainingDict -- Begining accesses")
start = clock()
for target in range(2*testSize):
    value = evensDict[target]
# end for
end = clock()
runTime = end - start
print( "Time to use a ChainingDict of %d size to locate targets 0 to %d is %.6f sec." % \
      (2**14, 2*testSize - 1, runTime))




