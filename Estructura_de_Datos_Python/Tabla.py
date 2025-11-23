from tabulate import tabulate

v1 = [1,2,3,100]
v2 = ["a","bb","ccc","dddd"]
tabla = list(zip(v1, v2))
print(tabulate(tabla, headers=["Num", "Txt"], tablefmt="github"))
