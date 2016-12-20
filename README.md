# FullGraphDatabase
orientdb database service for full episte's graph

# resources/populate/example.txt:
Cada linea del archivo es un json estandar que representa una revision sistematica en epistemonikos, incluye sus referencias en la key 'references'.

# CREATE 
Crea la base de datos si es que no existe y luego crea todas las revisiones sistematicas en 'example.txt'
```
python create.py resources/populate/example.txt
```

# UPDATE
Busca cada una de las revisiones sistematicas en 'example.txt', para cada una que encuentra primero la elimina y luego la vuelve a crear.
```
python update.py resources/populate/example.txt
```

# DESTROY
Elimina la base de datos
```
python destroy.py
```
