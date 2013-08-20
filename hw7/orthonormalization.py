def orthonormalize(L):
    '''
    Input: a list L of linearly independent Vecs
    Output: A list T of orthonormal Vecs such that for all i in [1, len(L)],
            Span L[:i] == Span T[:i]
    '''
    from math import sqrt
    from orthogonalization import orthogonalize
    import copy
    L_local = copy.deepcopy(L)
    vstarlist = orthogonalize(L_local)
    for vstar in vstarlist:
        d = 0
        for key in vstar.D:
            d = d + vstar[key] * vstar[key]
        d = sqrt(d)
        for key in vstar.D:
            vstar[key] = vstar[key] / d
    return vstarlist


def aug_orthonormalize(L):
    '''
    Input:
        - L: a list of Vecs
    Output:
        - A pair Qlist, Rlist such that:
            * coldict2mat(L) == coldict2mat(Qlist) * coldict2mat(Rlist)
            * Qlist = orthonormalize(L)
    '''
    from orthogonalization import aug_orthogonalize
    from matutil import mat2coldict, coldict2mat
    Qlist = orthonormalize(L)
    Rlist = mat2coldict(coldict2mat(Qlist).transpose() * coldict2mat(L))
    return Qlist, list(Rlist.values())
