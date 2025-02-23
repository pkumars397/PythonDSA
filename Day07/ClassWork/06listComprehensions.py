#List Comprehension -a better way to create list with some condition or without any condition
#syntax [expr for i in iterable if cond]
numbers=[i*i for i in range(1,6)] #will create new list [1,4,9,16,25]
print(numbers)
even_nums=[i for i in range(1,12) if i%2==0] #[2,4,6,8,10]
print(even_nums)