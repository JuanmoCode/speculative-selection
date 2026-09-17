# Ejemplos de Selección Especulativa

Este proyecto contiene dos ejemplos en Python para comparar una estrategia **secuencial** con una estrategia de **selección especulativa**.

## Ejemplos

### 1. Selección secuencial

El programa consulta los servidores uno por uno y selecciona el primero que responde correctamente.


### 2. Selección especulativa

El programa consulta los tres servidores **simultáneamente** utilizando `ThreadPoolExecutor`.

Cuando llega la primera respuesta válida, ese servidor es seleccionado. La idea es reducir el **tiempo de espera**, aunque se utilicen más recursos al realizar varias consultas al mismo tiempo.



Los servidores utilizados (`httpbin.org/delay`) simulan diferentes tiempos de respuesta para observar la diferencia entre ambas estrategias.

## Requisitos

* Python 3
* `requests`

Instalar la dependencia:

```bash
pip install requests
```

## Ejecución

```bash
python secuencial.py
```

```bash
python especulativa.py
```

