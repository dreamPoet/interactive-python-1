lists can contain different types # but keep same types in one list as a habit
list can nest lists
len(list)


chr() use a range(256) as para return a corresponding char.


a = [xxxx]
b = a
change elem. in b equals to change in a
b = list(a) # create a copy
change elem. in b will not change a

without global:
if we change an elem of a list in a func, then it will be changed;
if we set it directly, it will create a local same name var.


is: mutable or not
int float bool **string** are not mutable
list is mutable
so, list is list : False


tuple: ()
tuple is not mutable; it support same non-mutation operations with lists.(like loop)
tuple[1] = 1 X cannot
can be used to protect data

list + = combine two lists