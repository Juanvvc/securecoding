---
marp: true
title: Código seguro - Quality Assurance
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

# Quality Assurance
<!-- _class: first-slide -->

Juan Vera del Campo

<juan.vera@campusviu.es>

# Como decíamos ayer...

- El Thread Modeling permite planificar amenazas y tratarlas en el momento del diseño
- ¿Podemos seguir comprobando la seguridad en el momento de la ejecución?

# Hoy hablamos de...
<!-- _class: cool-list -->

1. [Quality Assurance](#4)
1. [OWASP](#9)
1. [Otras recomendaciones](#15)
1. [Demos](#33)
1. [Referencias y ejercicio](#22)

# Quality Assurance
<!-- _class: lead -->

## Escaneos de vulnerabilides

- Software especializado en búsqueda de vulnerabilidades
- Software que CONOCE vulnerabilidades y escanea tus sistemas
- Escaneos automáticos

Ejemplos: https://owasp.org/www-community/Vulnerability_Scanning_Tools

---

Problemas:

- Solo se escanea lo que el sofware conoce
- Se conoce el estado de un sistema en un momento concreto del tiempo

## Pentesting

- Externalizar el escaneo: empresas especializadas

![center](https://blogs.getcertifiedgetahead.com/wp-content/uploads/2016/01/black-box-testing-and-more-610x325.jpg)

## CVE: Identify, define, and catalog publicly disclosed cybersecurity vulnerabilities.

![center](images/cves.png)

https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=apache

# OWASP
<!-- _class: lead -->


---

![center](https://owasp.org/assets/images/logo.png)

The Open Web Application Security Project® (OWASP) is a nonprofit foundation that works to improve the security of software.

- Tools and Resources
- Community and Networking
- Education & Training


## OWASP: Top 10

![center w:20em](https://owasp.org/assets/images/content/featured_project_t10.png)

<https://owasp.org/www-project-top-ten/>

---

![center](https://owasp.org/www-project-top-ten/assets/images/mapping.png)

## Otros proyectos

![bg left:40%](https://owasp.org/www-project-mobile-security-testing-guide/assets/images/masvs-mini-cover.png)

OWASP tiene otros proyectos

- API Top 10: https://owasp.org/www-project-api-security/
- Checklist Mobile testing: https://owasp.org/www-project-mobile-security-testing-guide/
- Top 10 en programación de dispositivos móviles <https://owasp.org/www-project-mobile-top-10/>

---

![center](https://owasp.org/www-project-mobile-security-testing-guide/assets/images/checklist_en_filled.png)

# Otras recomendaciones
<!-- _class: lead -->

---

![](images/sans-25.png)

https://www.sans.org/top25-software-errors/

---
<!-- _class: smallest-font -->

Rank|ID|Name|Score|2020 Rank Change
--|--|--|--|--
[1]|CWE-787|	Out-of-bounds Write|	65.93|+1
[2]|CWE-79|	Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')|	46.84|	-1
[3]|CWE-125|	Out-of-bounds Read|	24.9|	+1
[4]|CWE-20|	Improper Input Validation|	20.47|	-1
[5]|CWE-78|	Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection')|	19.55|	+5
[6]|CWE-89|	Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')|	19.54	|0
[7]|CWE-416|	Use After Free|	16.83|	+1
[8]|CWE-22|	Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal')|	14.69	|+4
[9]|CWE-352|	Cross-Site Request Forgery (CSRF)|	14.46	|0
[10]|CWE-434|	Unrestricted Upload of File with Dangerous Type|	8.45|	+5

http://cwe.mitre.org/top25/archive/2021/2021_cwe_top25.html

# Demos
<!-- _class: lead -->

## Bwapp

![bg left:60% w:90%](https://2.bp.blogspot.com/-eLNKbmnOpFg/WwKCa9IBpbI/AAAAAAAADlw/iPv1oX04beInZcDsA57lljJPKz-o1weSACLcBGAs/s640/screenshot-from-2017-01-03-12-39-35-945x531.png)

- Aplicación web con múltiples problemas de seguridad
- ¡No incluye explicaciones!
- Tres niveles de dificultad

http://www.itsecgames.com/

---

1. `docker run --rm -p 80:80 raesene/bwapp`
1. Go to: <http://localhost/install.php> and click on "install"

## WebGoat

![bg left:60% w:90%](https://terokarvinen.com/2020/install-webgoat-web-pentest-practice-target/learning-to-hack_huc9eb25cbfbc872792538337cc9ab52d5_145628_800x800_fit_box_3.png)

- Web de aprendizaje de OWASP
- Incluye lecciones y ejercicios de la lista de OWASP

https://owasp.org/www-project-webgoat/

---

1. `docker run --rm -p 8080:8080 -p 9090:9090 -t -e TZ=Europe/Amsterdam webgoat/goatandwolf`
1. Ve a <http://localhost/WebGoat> y registra un nuevo usuario

<!--
Nota: no he sido capaz de ejecutar WebWolf desde el docker, quizá prefieras hacerlo en tu propio PC
-->


## Exampe: command injection
<!-- _class: two-columns -->

```php
<?php

$command = "ls ".$_GET['modifiers'];

$output = exec($command);
```

![](images/commandinjection.png)

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

Continúa en: [DevSecOps](04-devsecops.pdf)

# ¡Gracias!
<!-- _class: last-slide --> 