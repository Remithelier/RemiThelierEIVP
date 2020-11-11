def is_palindrome(a):
    b=list(a)
    b.reverse()
    n=len(a)
    err=0
    for i in range(n):
        if a[i]!=b[i]:
            err=err+1
    if err==0:
        return True
    else:
        return False

def is_palindrome2():
    for i in range(len(a)//2):
        if a[i]!=a[-1-i]:
            return False


def bubble_sort(liste):
    n=len(liste)
    for j in range(n):
        for i in range(n-j-1):
            a=liste[i]
            b=liste[i+1]
            if b<=a:
                liste[i]=b
                liste[i+1]=a
    return liste

def insertion_sort(liste):
    n=len(liste)
    for i in range(n-1):
        var=liste[i+1]
        if liste[i]>liste[i+1]:
            var=liste[i]
            liste[i]=liste[i+1]
    return liste


def tri_rapide(liste):
    n=len(liste)












