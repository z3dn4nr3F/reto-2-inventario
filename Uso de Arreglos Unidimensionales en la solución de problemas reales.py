# 
# Sistema de Gestión de Inventario y Pedidos


def registrar(n, c, p):
    """Registra un nuevo elemento"""
    if nom := input("Nombre: ").strip():
        n += [nom]
        c += [int(input("Cantidad: "))]
        p += [float(input("Precio: "))]
        print("¡Registrado!")

def mostrar(n, c, p):
    """Muestra el listado indexado de los elementos."""
    if not n: print("\nSin registros."); return
    print(f"\n{'Índice':<8} | {'Nombre':<20} | {'Cant':<6} | {'Precio':<10}")
    print("-" * 52)
    for i in range(len(n)):
        print(f"{i:<8} | {n[i]:<20} | {c[i]:<6} | ${p[i]:<9.2f}")

def editar(n, c, p):
    """Edita un elemento existente seleccionándolo por su índice."""
    mostrar(n, c, p)
    if not n: return
    try: idx = int(input("\nÍndice a editar: "))
    except ValueError: return print("Índice inválido.")
    
    if 0 <= idx < len(n):
        if nue := input("Nuevo nombre (Enter para omitir): ").strip(): n[idx] = nue
        if cant := input("Nueva cantidad: ").strip(): c[idx] = int(cant)
        if prec := input("Nuevo precio: ").strip(): p[idx] = float(prec)
        print("Actualizado")
    else: print("Índice fuera de rango.")

def eliminar(n, c, p):
    """Elimina un elemento de forma sincronizada"""
    mostrar(n, c, p)
    if not n: return
    try: idx = int(input("\nÍndice a eliminar: "))
    except ValueError: return print("Índice inválido.")
    
    if 0 <= idx < len(n):
        print(f"Eliminado: {n.pop(idx)}")
        c.pop(idx); p.pop(idx)
    else: print("Índice fuera de rango.")

def main():
    """Función principal con menú interactivo."""
    nombres, cantidades, precios = [], [], []
    while (op := input("\n1. Registrar\n2. Mostrar\n3. Editar\n4. Eliminar\n5. Salir\nOpción: ")) != "5":
        if op == "1": registrar(nombres, cantidades, precios)
        elif op == "2": mostrar(nombres, cantidades, precios)
        elif op == "3": editar(nombres, cantidades, precios)
        elif op == "4": eliminar(nombres, cantidades, precios)
        else: print("Opción inválida.")
    print("Salida del sistema")

if __name__ == "__main__":
    main()
    