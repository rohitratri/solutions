def generate_permutations(num_pairs):
    if num_pairs == 1:
        return ['()']
    perms = []
    prev_perms = generate_permutations(num_pairs-1)
    for _perm in prev_perms:
        if not _perm.startswith('()'):
          perms.append(_perm + '()')
        perms.append('()' + _perm)
        perms.append('(' + _perm + ')')
    return perms

print generate_permutations(16)


    
    
