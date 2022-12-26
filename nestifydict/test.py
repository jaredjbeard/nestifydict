from copy import deepcopy
from nestifydict import *

## Test Merge ------------------------------------
print("------ Test Merge ------")
a = {"a": {"a1": 1}, "b": 2}
b = {"a": {"a2": 3}, "b": 2}
c = {"a": {"a1": {"a1a": 4}}, "b": {"b1":{"b1a":5}}, "c":6}

print("a", a)
print("b", b)
print("c", c)
print("a <- b", merge(a,b))
print("b <- c", merge(b,c))
print("a <- c", merge(a,c))
print("b <- a", merge(b,a))
print("c <- b", merge(c,b))
print("c <- a", merge(c,a))

## Test Unstructure ------------------------------
print("\n------ Unstructure ------")

cflat = unstructure(c)
print("c flat", cflat)

d = {"a": {"a1": {"a1a": 4, "a1b": 8}}, "b": {"b1":{"b1a":5, "a1a": 7}}, "c":6}
print("d", d)
dflat = unstructure(d)
print("d flat", dflat)
    
## Test structure --------------------------------
print("\n------ Structure ------")

# cflattemp = deepcopy(cflat)
print("c flat -> c | reject", structure(cflat,c))
print("c flat", cflat)
# dflattemp = deepcopy(dflat)
print("d flat -> c | no reject", structure(dflat,c, False))

## Test Find Key ---------------------------------
print("\n------ Find Key ------")

a1akey = find_key(d,"a1a")
print("a1a in d", a1akey)
print("a1 in d", find_key(d,"a1"))
print("c2a in d", find_key(d,"c2a"))

## Test Recursive Set ----------------------------
print("\n------ Recurcsive Set ------")

recursive_set(a,a1akey,"hi")
print("set a1a1 full key", a)
recursive_set(a,["a1a"],"bye", True)
print("set a1a1 as hint", a)