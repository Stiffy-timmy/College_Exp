def t_ls(lst):
    new_lst = []
    for idx in range(len(lst)):
        if lst[idx] % 2 == 0:
            new_lst.append(lst[idx])
    return new_lst

lst = [item for item in range(1, 11)]
result = t_ls(lst)
print("New List: ", result)
