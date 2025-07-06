ranks = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
print(*ranks[::1],sep="  |  ")

# *: is used for removing the brackets
# sep can be added to separate the items
# rank in bracket () is a truple, [] is a list, no difference