#!/bin/bash

# Verifica que se haya pasado un argumento
if [ -z "$1" ]; then
    echo "Uso: $0 <numero>"
    exit 1
fi

# Almacena el número en una variable
num=$1

# Itera desde 1 hasta el número indicado
for i in $(seq 1 $num); do
    # Crea el archivo con el nombre iVerdejoManuel.py
    touch "${i}VerdejoManuel.py"
done
