# programa sobre el metodo de busqueda merge sort

def merge(l1, l2):
    
    
    l3 = []
    
    while (len(l1) > 0 and len(l2) > 0):
        if l1[0] < l2[0]:
            l3.append(l1[0])
            l1 = l1[1:]
        else:
            l3.append(l2[0])
            l2 = l2[1:]
    
    
    if len(l1) > 0:
        l3 = l3 + l1
    
    if len(l2) > 0:
        l3 = l3 + l2
    
    return l3



def mergesort(L):
        if len(L) == 1:
            return L
        
        li = L[:len(L) // 2]
        ld = L[len(L) // 2:]
        
        li = mergesort(li)
        ld = mergesort(ld)
        
        return merge(li, ld)
    


lista = [20, 19, 5, 6, 15, -4, 0,18, 7, 3]

print(lista)
print(mergesort(lista))