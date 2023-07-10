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

Juan Vera del Campo

<juan.vera@campusviu.es>

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

![center width:40em](images/devops/WaterFall-Model-Challenges-DevOps-Tutorial-Edureka-4.png)

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

---

![center](images/devops/digiwiseacademy-devops.jpeg)

## Fases

- **Build**: en esta etapa se realiza la compilación de las unidades de código. Herramientas: Maven, Gradle...
- **Tests**: la prueba de todas las unidades se realiza en esta etapa. Entonces, sabremos dónde exactamente el código tiene errores y, si se encuentran errores, no se continúa a las siguientes etapas. Herramientas: linters, Selenium, PYtest...
- **Integrar**: en esta etapa, se integran todas las unidades de los códigos. Herramientas: Jenkins.
- **Despliegue**: en esta etapa, el código se despliega en el entorno del cliente. AlEjemplos: AWS, Docker...
- **Operar**: las operaciones se realizan en el código si es necesario.Herramienta: Kubernetes, OpenShift...
- **Monitor**: en esta etapa, el monitoreo de la aplicación se realiza aquí en el entorno del cliente. Herramientas: Nagios, ELK, Splunk, Grafana...

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
- Cada fallo de tests es un big
- Mejora los tests
- No uses ramas de desarrollo enormes
- Automatiza todo el deployment
    - Incluida la creación de infraestructura: terraform, ansible, kubernetes...

---

![center](images/devops/etapas.png)

# Etapas
<!-- _class: lead -->

## Build

![center](images/devops/cicd-simple-1024x241.png)

- Compilación, y errores de compilación
- Linters
- Gestión de librerías, y auditoría de librerías

## Build - librerías

`npm audit`

 Dependabot

Ejemplos:

- https://socket.dev/npm/package/segment-bundle/files/6.6.9/package.json
- https://socket.dev/npm/package/filebdecoder/files/1.0.0/package.json
- https://socket.dev/npm/package/123rf-ui-core/files/9.849.9/index.js

> https://twitter.com/feross/status/1672401333893365761

## Tests
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

---

https://owasp.org/www-community/Source_Code_Analysis_Tools

- Análisis estático: Brakeman (Ruby), SpotBugs+FindSecBugs (Java), Go AST (Go), Bandit (Python), Linters...
- Test de contenedores: https://testcontainers.com/
- Análisis dinámico: Nikto, sqlmap, namp, Gauntlt...

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
- https://owasp.org/www-pdf-archive/OWASP_Code_Review_Guide_v2.pdf)

## Application security testing (AST)

Estática y dinámica

https://about.gitlab.com/blog/2019/08/12/developer-intro-sast-dast/

https://realm3ter.medium.com/analyzing-javascript-files-to-find-bugs-820167476ffe

---

![center w:35em](images/devops/sast-dast.png)

> https://blog.51sec.org/2018/12/from-devops-to-devsecops-topics.html

## Despliegue

Manejo de secretos:

- AWS Secret Management
- Azure Key Vault
- Secret Manager (GCP)
- GitHub secret scanning

https://gist.github.com/win3zz/0a1c70589fcbea64dba4588b93095855

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

# Resumen y referencias
<!-- _class: lead -->

## Referencias

- https://semaphoreci.com/blog/cicd-pipeline
- https://www.edureka.co/blog/devops-tutorial
- Tools for testing: https://www.creativebloq.com/features/12-must-have-user-testing-tools
- Courses: https://javarevisited.blogspot.com/2020/07/5-free-courses-to-learn-devops-in-2020.html

---
<!-- _class: center -->

Continúa en: [Ejemplo del curso](07-ejemplo.html)

# ¡Gracias!
<!-- _class: last-slide --> 
