def sum_all(*args):
   return sum(args)

print(sum_all(1,2,3,4))
print(sum_all(1,2,4))
print(sum_all(1,2,4,5,6))


#kw_args 

def print_kwargs( **kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name="Shaktiman",power="lazer",enemy="dr. Jackaal")
