# Analizador de Gastos Personales

Script en Python que lee un CSV de gastos y genera un reporte con totales
por categoria, totales por mes, el mayor gasto individual, y barras ASCII
proporcionales al monto de cada categoria. Usa unicamente la libreria
estandar de Python (csv, pathlib, datetime, sys).

## Como correrlo

Necesitas Python 3 instalado. Desde la carpeta del proyecto:

    python analizador.py

Por defecto lee `gastos.csv`. Para usar otro archivo:

    python analizador.py otro-archivo.csv

## Formato del CSV

Columnas: fecha (YYYY-MM-DD), categoria, descripcion, monto
