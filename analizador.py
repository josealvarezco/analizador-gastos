# analizador.py
import csv
import sys
from datetime import datetime
from pathlib import Path

RUTA_POR_DEFECTO = Path("gastos.csv")


def leer_gastos(ruta):
    gastos = []
    with open(ruta, "r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for numero_fila, fila in enumerate(lector, start=2):
            try:
                float(fila["monto"])
            except ValueError:
                print(f"Aviso: se ignora la fila {numero_fila} (monto invalido: '{fila['monto']}')")
                continue
            gastos.append(fila)
    return gastos


def totales_por_categoria(gastos):
    totales = {}
    for gasto in gastos:
        categoria = gasto["categoria"]
        monto = float(gasto["monto"])
        totales[categoria] = totales.get(categoria, 0) + monto
    return totales


def totales_por_mes(gastos):
    totales = {}
    for gasto in gastos:
        fecha = datetime.strptime(gasto["fecha"], "%Y-%m-%d")
        clave_mes = fecha.strftime("%Y-%m")
        monto = float(gasto["monto"])
        totales[clave_mes] = totales.get(clave_mes, 0) + monto
    return totales


def mayor_gasto(gastos):
    return max(gastos, key=lambda g: float(g["monto"]))


def totales_ordenados(totales):
    return sorted(totales.items(), key=lambda item: item[1], reverse=True)


def barra_ascii(valor, maximo, ancho=40):
    if maximo == 0:
        return ""
    largo = int((valor / maximo) * ancho)
    return "█" * largo


def imprimir_reporte(gastos):
    if not gastos:
        print("No hay gastos para analizar.")
        return

    totales_cat = totales_por_categoria(gastos)
    totales_mes = totales_por_mes(gastos)
    mayor = mayor_gasto(gastos)
    maximo_cat = max(totales_cat.values())
    total_general = sum(totales_cat.values())

    print(f"Analizando {len(gastos)} gastos")

    print("Total por categoria:")
    for categoria, total in totales_ordenados(totales_cat):
        barra = barra_ascii(total, maximo_cat)
        print(f"  {categoria:<16} {barra} {total:,.0f}")

    print("Total por mes:")
    for mes, total in sorted(totales_mes.items()):
        print(f"  {mes}: {total:,.0f}")

    print("Mayor gasto individual:")
    print(f"  {mayor['descripcion']} ({mayor['categoria']}) - {float(mayor['monto']):,.0f} el {mayor['fecha']}")

    print(f"Total general: {total_general:,.0f}")


def main():
    ruta = Path(sys.argv[1]) if len(sys.argv) > 1 else RUTA_POR_DEFECTO

    if not ruta.exists():
        print(f"Error: no se encontro el archivo '{ruta}'")
        sys.exit(1)

    gastos = leer_gastos(ruta)
    imprimir_reporte(gastos)


if __name__ == "__main__":
    main()
