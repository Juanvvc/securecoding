---
marp: true
title: Código seguro - Contenedores y docker
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

# Contenedores y docker
<!-- _class: first-slide -->

Juan Vera del Campo - <juan.vera@professor.universidadviu.com>


# Hoy hablamos de...
<!-- _class: cool-list toc -->

1. [Contenedores](#3)

# Contenedores Docker
<!-- _class: lead -->

## ¿Qué es un contenedor?

Es como una máquina virtual... pero no

![center w:40em](images/containers/vm-docker.png)

> https://www.ubuntupit.com/everything-you-need-to-know-about-linux-containers-lxc/

## Ventajas de los contenedores

- Seguridad:
    - Sistema aislado: solo ven la parte del sistema que les dejas ver
    - Pueden conectarse entre ellos
- Portabilidad: arregla "en mi PC funciona":
    - Gestión de "snapshots"
    - Dependencias "autocontenidas"
    - Fácil instalación y compartición
- Auditable:
    - Inicio rápido y consistente
    - Descritos en un archivo de texto que puede auditarse fácilmente
    - Gestión del ciclo de vida

---
<!-- _class: with-success -->

- Escalabilidad:
    - Pueden crearse y destruirse rápidamente
    - PUeden conectarse entre ellos
- Tolerancia a fallos:
    - El gestor de contenedores detecta cuándo uno ha fallado y lo reinicia automáticamente

Los contenedores son ideales para microservicios

## Microservicios

Uso de múltiples componentes de software independientes para crear una aplicación

Ejemplo: contenedores para:

- Base de datos
- Proxy SSL
- Balanceador
- Frontend web
- API

---

![center w:25em](images/kubernetes/microservices.png)

> https://online.visual-paradigm.com/diagrams/templates/ibm-cloud-architecture-diagram/microservices-diagram/

## Terminología

- **Imágenes**: "snapshot" de un sistema. Es el "estado inicial" de un contenedor
- **Contenedor**: un sistema ejecutándose
- **Volumen**: "pendrive" o "carpeta compartida" entre sistemas. Se usa para persistencia y configuraciones

## Ciclo de vida de un contenedor

![center](images/containers/docker-lifecycle.png)

> https://faun.pub/introduction-to-docker-life-cycle-3bf3aeba883

---

Seguimos en:

- https://colab.research.google.com/github/Juanvvc/securecoding/blob/main/ejercicios/04-docker.ipynb
- [Kubernetes](A2-kubernetes.html)

# Referencias

- Tutorial: https://docs.docker.com/get-started/
