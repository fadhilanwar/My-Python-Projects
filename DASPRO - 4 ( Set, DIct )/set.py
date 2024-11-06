a = {"apel", "jeruk", "mangga", "ceri"}
b = {"strawberry", "blueberry", "apel"}



for item in a :
    print(item)

union = a.union(b)
print(union)

## Mencari item yang sama dari dua buah set
a.intersection_update(b)
intersection = a.intersection(b)

## Mencari item yang dari dua buah set
a.symmetric_difference_update(b)

symmetric_difference = a.symmetric_difference(b)

## Menambah Item dari sebuah LIST
add_from_list = ["CILOK", "BAKSO"]

a.update(add_from_list)
print(a)

## Mengubah Set ke List
convert = list(a)

print(convert)
