---
marp: true
title: Código seguro - DevSecOps
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

# DevSecOps 
<!-- _class: first-slide -->

Juan Vera del Campo - <juan.vera@professor.universidadviu.com>

# Hoy hablamos de...
<!-- _class: cool-list toc -->

1. [DevOps](#3)
1. [Etapas](#13)
1. [Resumen y referencias](#24)

# DevOps
<!-- _class: lead -->

## El problema

El código debe ser dinámico dinámico: los desarrolladores están constamentemente añadiendo funcionalidad y arreglando errores

- ¿Cómo podemos automatizar el proceso de analizar la calidad del código?
- ¿Cómo podemos reducir el tiempo de entrega de la nueva versión del código?
- ¿Podemos hacer el código más seguro en esta etapa?

DevOps: metodología para que desarrollo, operaciones y seguridad colaboren desde las primeras etapas para automatizar el proceso que lleva desde la programación hasta la entrega derl código

> https://www.edureka.co/blog/devops-tutorial


## Problemas de los modelos tradicionales

![center width:100%em](images/devops/WaterFall-Model-Challenges-DevOps-Tutorial-Edureka-4.png)

- Demasiado tiempo entre desarrollo y despliegue
- Tareas manuales no automatizadas
- Varios equipos tienen que aceptas los cambios

## Nuevo paradigma

![center](images/devops/cicd-pipeline-introduction-1024x422-1.jpg)

## CI/CD Continuous Integration / Continous Development
<!-- _class: with-success -->

- Compila código
- Ejecuta tests
- Despliega nuevas versiones de la aplicación frecuentemente
- Flexible y adaptable a cambios
- Feedback constante de los usuarios finales
- Todo de forma automática

Cada cambio en el código se testea y despliega en producción en minutos

> https://semaphoreci.com/blog/cicd-pipeline

## Exigencias

- Diseña el sistema de manera que admita versiones iterativas.
- Métricas que ayuden a detectar problemas en tiempo real.
- Desarrollo basado en tests para mantener siempre el código en un estado desplegable.
- Monitoreo, registro y tolerancia a fallas por diseño.
- Trabaja en pequeñas iteraciones. Por ejemplo, si desarrolla en ramas de características, no deberían vivir más de un día.
- Uso de entornos de prueba similares a los de producción
- Si lo desarrollas, lo ejecutas. Los equipos de ingeniería autónomos deben ser responsables de la calidad y la estabilidad del software que construyen
- Los clientes tienen que poder aceptar cambios contantes
- El desarrollo Ci/CD puede ser más caro que el tradicional

## Buenas prácticas

- Trata la rama "main" como si pudiese desplegarse en cualquier momento
- Cada fallo de tests es un bug
- Mejora los tests
- No uses ramas de desarrollo enormes
- Automatiza todo el deployment
    - Incluida la creación de infraestructura: terraform, ansible, kubernetes...

---

![center](images/devops/etapas.png)

## DevOps: herramientas

- Repositorios de código (Github, Gitlab, Bitbucket, etc)
- Infraestructura (Terraform, CloudFormation, etc)
- CI/CD (Jenkins, Bamboo, CircleCI, TravisCI, etc)
- Builds (Maven, Gradle, make, rake, etc)
- Test (*unit, cucumber, protractor, etc)
- Repositorio de artefactos (Nexus, Artifactory, Docker Hub,
S3, etc)
- Despliegue (Ansible, Puppet, Chef, etc)
- Monitorización (NewRelic, AppDynamics, Sysdig, etc)
- Logging (Splunk, ELK, etc)
- Comunicación (Slack, HipChat, etc)

# Etapas
<!-- _class: lead -->

## Fases

- **Build**: en esta etapa se realiza la compilación de las unidades de código. Herramientas: Maven, Gradle...
- **Tests**: la prueba de todas las unidades se realiza en esta etapa. Entonces, sabremos dónde exactamente el código tiene errores y, si se encuentran errores, no se continúa a las siguientes etapas. Herramientas: linters, Selenium, PYtest...
- **Integrar**: en esta etapa, se integran todas las unidades de los códigos. Herramientas: Jenkins.
- **Despliegue**: en esta etapa, el código se despliega en el entorno del cliente. AlEjemplos: AWS, Docker...
- **Operar**: las operaciones se realizan en el código si es necesario.Herramienta: Kubernetes, OpenShift...
- **Monitor**: en esta etapa, el monitoreo de la aplicación se realiza aquí en el entorno del cliente. Herramientas: Nagios, ELK, Splunk, Grafana...

---

![center](images/devops/digiwiseacademy-devops.jpeg)


## Etapa 1: Build

Análisis estático de código: Static application security testing (SAST)

- Linters
- Compilación y gestión de errores de compilación
- Detección de errores comunes de seguridad
- Auditoría de librerías
- Gestión de secretos
- Herramientas: Brakeman (Ruby), SpotBugs+FindSecBugs (Java), Go AST (Go), Bandit (Python), Linters... 

> https://seguridad.prestigia.es/que-son-las-herramientas-sast-y-dast/
> https://owasp.org/www-community/Source_Code_Analysis_Tools

## Etapa 1: Build - linters

No corrigen errores, sino que usan formatos estandarizados para el código

Ejemplos: [black](https://black.readthedocs.io/en/stable/), [Pylama](https://klen.github.io/pylama/)

```bash
git clone https://github.com/NetSPI/django.nV
python3 -m pip install black
python3 -m black taskManager/views.py
```

![center](images/example-black.png)


## Etapa 1: Build - Análisis de código

Lenguaje|SAST tool
--|--
Python|[bandit](https://bandit.readthedocs.io/en/latest/)
Ruby|Brakeman
Comerciales|[SonarQube](https://www.sonarsource.com/products/sonarqube/downloads/)
Secretos|Github secrets, Trufflehog, git-secrets, detect-secrets...

---

Ejemplo: [bandit](https://bandit.readthedocs.io/en/latest/) analiza errores comunes en Python

```bash
git clone https://github.com/NetSPI/django.nV ; cd django.nV
python3 -m pip install bandit
bandit -r .
```

![w:30em center](images/ejemplo-bandit.png)

---

Ejemplo: [SonarQube](https://www.sonarsource.com/products/sonarqube/downloads/)

![w:25em center](images/ejemplo-sonarqube.png)

## Etapa 1: Build - Auditoría de librerías

Lenguaje|SAST tool
--|--
JS|[Retirejs](https://retirejs.github.io/retire.js/)/npm audit/AuditJS
Python|[Safety](https://github.com/pyupio/safety)
Ruby|Bundler audit/Chelsea
PHP|Composer
Java|OWASP dependency checker

- Estas herramientas comprueban en una base de datos si la librería usada tiene alguna vulnerabilidad conocida
- ¿Es posible actualizar la librería o asumimos el riesgo?
- No detectan vulnerabilidades automáticamente: se tiene que analizar periódicamente con bases de datos actualizadas

---

Ejemplo: [Safety](https://github.com/pyupio/safety) analiza librerías Python

```bash
git clone https://github.com/NetSPI/django.nV ; cd django.nV
python3 -m pip install safety
python3 -m safety check -r requirements.txt --save-json safety-resuls.json
```

![center](images/ejemplo-safety.png)

---

Ejemplo: Pip audit

```bash
git clone https://github.com/NetSPI/django.nV
python3 -m pip pip-audit
pip-audit -r ./requirements.txt
```

![center](images/ejemplo-pipaudit.png)

---

Ejemplo: npm audit (ya incluido con node)

```
https://github.com/SasanLabs/VulnerableApp-facade
cd VulnerableApp-facade/facade-app
npm audit
```

![center](images/example-npmaudit.png)

---

Ejemplo: Github Dependabot

![](images/ejemplo-dependabot.png)

Dependabot es un servicio que puedes activar en la configuración de tu proyecto en GitHub

---

Ejemplos de librerías maliciosas:

- https://socket.dev/npm/package/segment-bundle/files/6.6.9/package.json
- https://socket.dev/npm/package/filebdecoder/files/1.0.0/package.json
- https://socket.dev/npm/package/123rf-ui-core/files/9.849.9/index.js

> https://twitter.com/feross/status/1672401333893365761

## Etapa 2: Tests
<!-- _class: smallest-font -->

- ¿Cuál es tu input?
  - ¿Qué pasa si algunos de los parámetros no esá presente, o tiene un tipo no esperado, o está fuera de rango?
- ¿Cuál es la lógica?
  - Modificación de la entrada por otros elementos
  - Código esperando entrada del usaurio
  - Salidas sin control, o nulas
  - Timeouts para las salida
  - ¿Están todos los posibles casos cubiertos?
  - ¿Son relevantes todos los casos?
- Interacciones con los datos: CRUD
  - ¿Autorización para las acciones?
  - ¿Puedes distinguir entre no autorizado, errores o datos que no existen?
- Bucles
  - ¿Siempre acaban?
  - ¿Salen bien en caso de error?

![bg right:40%](images/common/computer-code-text-programming.jpg)

> [Hris Koleva en twitter](https://twitter.com/hrisKoleva)

---

![center](images/devops/Code-Based-Testing.png)

## Etapa 4: despliegue Application security testing (AST)

Estática y dinámica

https://about.gitlab.com/blog/2019/08/12/developer-intro-sast-dast/

https://realm3ter.medium.com/analyzing-javascript-files-to-find-bugs-820167476ffe

---

![center w:35em](images/devops/sast-dast.png)

> https://blog.51sec.org/2018/12/from-devops-to-devsecops-topics.html

## Etapa 4: despliegue

Manejo de secretos:

- AWS Secret Management
- Azure Key Vault
- Secret Manager (GCP)
- GitHub secret scanning

https://gist.github.com/win3zz/0a1c70589fcbea64dba4588b93095855

## Etapa 4: despliegue: análisis dinámico de código

- Analiza vulnerabilidades de las aplicaciones en funcionamiento
- Ejemplos: puertos cerrados, protocolos HTTPS para todo, configuraciones correctas...

---

Algunas herramientas:

- NMAP
- SSLyze
- [Nikto](https://cirt.net/Nikto2)
- [Zed Attack Proxy (ZAP)](https://www.zaproxy.org/): web vulnerability scanner, OWASP Top 10.
- [Dastarly](https://portswigger.net/burp/dastardly) similar a ZAP, pero de la empresa Burp
- [Nuclei](https://github.com/projectdiscovery/nuclei)
- Infrastructura y compliance: [Inspec](https://github.com/inspec/inspec), [Ansible](https://www.ansible.com/), [checkov](https://github.com/bridgecrewio/checkov)
  - Ejemplo: [Linux baseline en inspec](https://github.com/dev-sec/linux-baseline/blob/master/controls/os_spec.rb)
- Bases de datos de vulnerabilidades a través de agentes: Qualys


# Resumen y referencias
<!-- _class: lead -->

## Referencias

- https://semaphoreci.com/blog/cicd-pipeline
- https://www.edureka.co/blog/devops-tutorial
- Tools for testing: https://www.creativebloq.com/features/12-must-have-user-testing-tools
- Courses: https://javarevisited.blogspot.com/2020/07/5-free-courses-to-learn-devops-in-2020.html

--- 


- https://docs.github.com/en/code-security/code-scanning
- https://github.com/kaiiyer/awesome-vulnerable
- https://github.com/appsecco/dvna
- https://github.com/analysis-tools-dev/static-analysis#javascript
- https://deepscan.io/pricing/
- https://www.sonarsource.com/products/sonarlint/
- https://github.com/designsecurity/progpilot
- https://github.com/duo-labs/dlinto
- https://snyk.io/learn/code-security-audit/
- https://www.sonarsource.com/solutions/security/
- https://www.codementor.io/learn-programming/performing-security-audit-for-your-code-the-basics
- https://owasp.org/www-pdf-archive/OWASP_Code_Review_Guide_v2.pdf

# ¡Gracias!
<!-- _class: last-slide --> 
