def split_list(lst):
   
    if len(lst) < 3:
        return None  
    first, second, third, *remaining = lst
    
    return first, second, third, remaining

my_list = [1, 2, 3, 4, 5]
var1, var2, var3, rest = split_list(my_list)

print(f"List: {my_list}")
print(f"Variables: var1={var1}, var2={var2}, var3={var3}, rest={rest}")
