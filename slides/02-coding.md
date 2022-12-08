---
marp: true
title: Código seguro - Buenas prácticas de escritura de código
paginate: true
footer: '[Inicio](index.html)'
headingDivider: 2
theme: marp-viu
---

<style>
    /* You can add custom style here. VSCode supports this.
    Other editor might need these custom code in
    the YAML header: section: | */
</style>

# Buenas Prácticas de Escritura de Código
<!-- _class: first-slide -->

Juan Vera del Campo

<juan.vera@campusviu.es>

# Como decíamos ayer...

- El Thread Modeling permite planificar amenazas y tratarlas en el momento del diseño
- ¿Podemos mejorar la seguridad de una aplicación simplemente escribiendo buen código?

# Hoy hablamos de...
<!-- _class: cool-list -->

1. [Diseño seguro](#4)
1. [Programación segura](#9)
2. [GIT](#33)
3. [Referencias y ejercicio](#22)

# Diseño seguro
<!-- _class: lead -->

# Programación segura

# Clean Code

Recetas del libro "Clean Code" de Robert C. Martin. Nota que los ejemplos son Java y las *best practices* de Python son en ocaciones diferentes.

## Nombres de variables

- Usa nombres que tengan sentido: `gameBoard` mejor que `theList`.
- Evita información incorrecta: no uses `accountList` si no es una lista `List`.
- Distingue perfectamente el nombre de las variables. No uses: `getActiveAccount`, `getActiveAccounts` y `getActiveAccountInfo`.
- Usa nombres que sean pronuncialbes
- Usa nombres que puedan buscarse: `i`, `7` no pueden buscarse. `counter`, `MAX_NUMBER` sí.
- Los nombres de clases son sustantivos
- Las funciones son verbos: `get`, `set` and `is`.
- Nomenclatura contante: fetch, retrieve or get? controller or manager?

# Funciones

- No más de 20 líneas
- No más de uno o dos niveles de indentación
- La función debe hacer solo una cosa
- Usa nombres descriptivos
- Evita parámetros "bandera"
- Prefiere excepciones a devolver códigos de error

# Comentarios

- Los comentarios no compensan un mal código. Mejora el código antes que los comentarios
- "Código autoexplicativo" (pero con cuidado)
- Buenos comentarios:
    - comentarios legales autor/licencia
    - informativos sobre las intenciones
    - clarificaciones sobre excepciones o por qué las cosas se hacen de una forma determinada que no es obvia
    - TODO
    - amplificación de la importancia de una línea (probablemente, por malas experiencias)
    - **APIs**
- Malos comentarios:
    - Redundantes
    - Falsos
    - Sobre la historia del código
    - Avisando de dónde acaba una sección: eso es que es demasiado larga
    - Atribuciones: git blame!
    - Código comentado

## Linting

![center](images/code-linting.png)

# GIT

# Referencias
<!-- _class: lead -->

---

- https://owasp.org/
- https://www.sans.org/top25-software-errors/
- https://www.hackerone.com/vulnerability-management/what-vulnerability-scanning-and-how-do-it-right
- https://www.codecademy.com/article/vulnerability-scans

## Ejercicio

- Ejecuta WebGoat y encuentra al menos dos vulnerabilidades

---

<!-- _class: center -->

Continúa en: [Quality Assurance](03-quality.html)

# ¡Gracias!
<!-- _class: last-slide --> 