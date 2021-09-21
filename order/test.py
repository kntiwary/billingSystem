l = [[1, 2, 3], [[4, 5], [6, 7]], 8, [9], 10]
final_list = [1,2,3,4,5,6,7,8,9,10]


# final_l = []
# for itemlist in l:
#     for item in itemlist:
#         final_l.append(item)


import itertools

final_items  = list(itertools.chain.from_iterable(l))
# print(final_items)from_iterable