# varios_python

Repositorio con pequeños ejercicios sobre temas matemáticos trabajables en Python.

## 1. Tablas de verdad

### Descripción

¿Cómo ilustrar un uso concreto de conceptos relacionados con los temas de *gramáticas* y *recursión*? Éste es un proyecto sencillo pero requiere de un número importante de herramientas teóricas y técnicas. Se puede dividir en las siguientes tareas:

1. Dada una fórmula de la lógica proposicional (sintácticamente correcta o *bien escrita*), generar la tabla de verdad correspondiente.
2. Comprobar que la fórmula que ha introducido el usuario sea sintácticamente correcta. Por ejemplo, correcta: **p v ¬(q v ¬r)**, incorrecta: **¬((pq**. (Ésta es la parte más interesante).

### Para seguir trabajando

- [ ] Ampliar los conectivos lógicos aceptables a: &, ->, <->, etc.
- [ ] Analizar la fórmula ingresada por el usuario identificando subfórmulas (árbol de la fórmula).
- [ ] Incluir subfórmulas en la tabla de verdad que se imprime.
- [ ] ¿Hay un error de sintaxis? Decir cuál ha sido.
- [ ] ¡Hacer pruebas!

### Demo

[demo_log.gif]
[demo_log_1.gif]

### Código

tabla_de_verdad.py
