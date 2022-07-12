## final version with head included

def hairpin(primer,head):
    pl = len(primer)

    match = ({"A", "T"},{"C", "G"})
    c_max = 0

    for n in range(head+1,pl-head):

        s = abs(2*n-pl)

        if n <= head or pl - n <= head:
            return -1
        else:
            pr_1 = "*" * s*(n>10) + primer[:pl-n-head] + "-"*(head != 0) + primer[pl-n-head:pl-n]
            pr_2 = "*" * s*(not n>10) +primer[-n:][::-1][:n-head] + "-"*(head != 0) + primer[-n:][::-1][n-head:n]
#            print(pr_1[s:-(head+1)])
#            print(pr_2[s:-(head+1)])
            c = 0
            for i,j in zip(pr_1[s:-(head+1)], pr_2[s:-(head+1)]):
                if {i,j} in match: c+=1
                if c_max < c: c_max = c    
    return c_max