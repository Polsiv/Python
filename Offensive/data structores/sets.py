#!/usr/bin/env python3

#enumerated data structure
my_list = ["silv", "elpepe", "la pepa"]

#becuase of this
my_list[1]


#sets dont work like this (also unique elements, ik shit basic asf)

my_set = {1, 2, 3, 4}
print(my_set)
print(type(my_set))

#add new elements=====================

#because of optimization, we adding new elements, order may vary
my_set.add(19)
print(my_set)


# add another set ==================

my_set.update({4, 5, 6, 7})
print(my_set)

# remove element =========
my_set.remove(4)
print(my_set)

#remove element w/o getting an error if its not present
my_set.discard(9)




#Basic operations ==================================

#intersection
another_set = {10, 7, 4, 1, 2}

intersection_set = my_set.intersection(another_set)
print(intersection_set)

#union
union_set = my_set.union(another_set)
print(union_set)


#Sub sets

sub_set = {7, 10}

#returns false if theres another element not present in the main set
print(sub_set.issubset(another_set))



#casting list to set====================

my_list2 = [1, 23, 3, 3, 1, 2, 45]

set_list2 = set(my_list2)

#casting back to list lol
print(list(set_list2))


#iterate =====================

new_set = set(range(5))

for i in new_set:
    print(i, end = ' ')


#if element is presnet ===========

#true/false
print(999 in new_set)
 

#USE CASE EXAMPLE ==============


fb_users = {"silv", "elpepe", "la pepa", "los pepes"}
twt_users = {"silv", "Jdlmao", "la pepa", "Manolito", "lucy"}

user_in_both = fb_users.intersection(twt_users)
all_users = twt_users.union(fb_users)

#users present in facebook but not in twitter
diff = fb_users.difference(twt_users)

print(user_in_both)
print(all_users)
print(diff)