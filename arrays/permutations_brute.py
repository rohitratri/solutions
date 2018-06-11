def permutations(ar):
    if len(ar) == 1:
        return [ar,]
    perms = []
    for perm in permutations(ar[1:]):
        for pos in xrange(len(perm)+1):
            temp_perm = perm[:]
            temp_perm.insert(pos, ar[0])
            perms.append(temp_perm)
        print perms
    return perms

permutations([1,2,3])
