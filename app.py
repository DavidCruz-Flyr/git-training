with open("./data.txt", "r", encoding="utf-8") as file:
    data = [line.split(",")[0] for line in file.read().splitlines() if line.strip()]

numeros = list(map(float, data))

promedio = numeros[-1]

resultados = [str(num - promedio) for num in numeros[:-1]]

lineas_modificadas = [f"{numeros[i]},{resultados[i]}" for i in range(len(resultados))]

with open("./data.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(lineas_modificadas))

with open("./data.txt", "r", encoding="utf-8") as file:
    data = file.read().splitlines()

for num in data:
    print(num)
