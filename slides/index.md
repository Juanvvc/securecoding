---
marp: true
title: Código seguro - Índice
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

# Código seguro y *quality assurance*
<!-- _class: first-slide -->

**Presentación**
Juan Vera del Campo

<juan.vera@campusviu.es>


## Temario
<!-- _class: cool-list -->

1. [Modelado de amenazas](01-threatmodeling.html)
2. [Buenas prácticas en la escritura de código](02-coding.html)
3. [Open Web Application Security Project](03-quality.html)
4. [SecDevOps](04-devsecops.pdf)
5. [Docker](05-docker.pdf)
6. [Análisis de un ejemplo real](07-ejemplo.html)

# Presentación
<!-- _class: lead -->

## Objetivos

1. seguridad en la creación de aplicaciones de software
1. Identificar problemas de seguridad durante el diseño
1. Despliegue seguro de aplicaciones
1. Quality Assurance Testing

En resumen: gestión de la seguridad durante todo el ciclo de vida de la aplicación

> https://www.packetlabs.net/posts/devsecops-replace-agile/
> https://www.packetlabs.net/posts/security-qa-testing/

## Sobre mí

![bg left:45%](images/juanvi.jpg)

Dr. Juan Vera (Juanvi)

juan.vera@campusviu.es

Intereses:

- DFIR: Análisis forense e *Incident Response*
- Miembro del Cyber Incident Response Team de [Valeo](https://es.wikipedia.org/wiki/Valeo)
- Cualquier cosa que vuele

## Intrucciones de uso de las transparencias
<!-- _class: smaller-font -->

Versión más actualizada:

- Acceso directo HTML: <http://juanvvc.github.io/securecoding/slides>
    - Puedes pulsar `p` para ver las notas de presentación
    - Con "Inicio" (en pie de cada transparencia) puedes venir a esta presentación, con el índice global de contenidos
    - Encontrarás la versión en PDF entre los recursos de la asignatura
- Código Markdown: <https://github.com/juanvvc/securecoding>

Durante el estudio personal es muy recomendable seguir los enlaces que aparecen en las transparencias para completar el tema.

[![Licencia de Creative Commons](https://i.creativecommons.org/l/by/4.0/88x31.png)](http://creativecommons.org/licenses/by/4.0/) Esta obra esta sujeta a una licencia de [Atribución 4.0 Internacional de Creative Commons](http://creativecommons.org/licenses/by/4.0/)

## Evaluación

- Ejercicios, a entregar antes del examen final
- 50% examen final "tipo test" de 20 preguntas

## Conocimientos necesarios

- Algo de programación
- Algo de sistemas
- Algo de gestión de sistemas operativos

## Descripción del escenario

Tecnología:

- Dispositivo Bluetooth BLE en el tobillo
- Aplicación en el teléfono móvil que envía datos al servidor
- AMPSCS: servidor que recibe los datos
    - API paa el móvil
    - Backend
- Frontend para doctores
- Frontend para ATS
- Compartición de datos para estudios

## Ejercicio de la sesión de hoy

Utilizaremos docker en varias de las sesiones de la asignatura. Como ejercicio de hoy, instaladlo en vuestros PCs y probad que se ha instalado correctamente (Windows, Linux, Mac)

- Instalación de docker en vuestros PCs
- Ejecución de imagen "Hola mundo": https://hub.docker.com/_/hello-world/
- Entrega: "pantallazo" de que se todo ha ejecutado correctamente


