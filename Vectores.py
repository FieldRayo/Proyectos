import math

def procesar_vector(vectores):
    Rx, Ry = 0, 0
    #Obtiene la resultante de los vectores
    for n, v in enumerate(vectores):
        Rx += -((math.cos((math.radians(v[f"grados_v{n}"])))) * v[f"unidades_v{n}"]) if "w" in v[f"orientacion_v{n}"] else ((math.cos((math.radians(v[f"grados_v{n}"])))) * v[f"unidades_v{n}"]) #cos(grados) * unidad = Vx
        Ry += -((math.sin((math.radians(v[f"grados_v{n}"])))) * v[f"unidades_v{n}"]) if "s" in v[f"orientacion_v{n}"] else ((math.sin((math.radians(v[f"grados_v{n}"])))) * v[f"unidades_v{n}"]) #sen(grados) * unidad = Vy
        print(Rx, Ry, math.cos((math.radians(v[f"grados_v{n}"]))) * v[f"unidades_v{n}"], math.sin((math.radians(v[f"grados_v{n}"]))) * v[f"unidades_v{n}"])
    #Saca el desplasamiento de los vectores
    R = ((Rx**2) + (Ry**2))**0.5 # c² = a² + b²
    grados = math.degrees(math.atan(Ry/Rx)) #arctan(y/x) = grados

    return R, grados

def get_vector():
    vectores = []
    cant_vectores = int(input("Cual es la cantidad de vectores?\n>>> "))
    for i in range(cant_vectores):
        print(f"Vector {i+1}")
        vectores.append({f"unidades_v{i}": int(input('Inserta las unidades\n>>> ')),
                         f"grados_v{i}": int(input(f'Inserta los grados\n>>> ')),
                         f"orientacion_v{i}": (input('Inserta la orientacion\n>>> ').lower())}
        )
        #Establecer complemento
        if vectores[i][f"orientacion_v{i}"][0] in ["n", "s"] and len(vectores[i][f"orientacion_v{i}"]) > 1:
            vectores[i][f"grados_v{i}"] = 90 - vectores[i][f"grados_v{i}"]
    return vectores
vectores = get_vector()
print(procesar_vector(vectores))
