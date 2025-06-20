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

1. [Desarrollo y Operaciones](#3)
1. [Etapas DevOps](#14)
1. [Resumen y referencias](#58)

# Desarrollo y Operaciones
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
- Despliega nuevas version de la aplicación
- Comprueba que el sistema final no tiene problemas de seguridad
- Flexible y adaptable a cambios
- Feedback constante de los usuarios finales
- **Todo de forma automática**

Cada cambio en el código se testea y despliega en producción en minutos

> https://semaphoreci.com/blog/cicd-pipeline

## Exigencias

- Diseña el sistema de manera que admita versiones iterativas
- Trabaja en pequeñas iteraciones. Por ejemplo, si desarrolla en ramas de características, no deberían vivir más de un día
- Desarrollo basado en tests para mantener siempre el código en un estado desplegable
- Monitoreo, registro y tolerancia a fallas por diseño
- Uso de entornos de prueba similares a los de producción
- Si lo desarrollas, lo ejecutas. Los equipos de ingeniería autónomos deben ser responsables de la calidad y la estabilidad del software que construyen
- Los clientes tienen que poder aceptar cambios constantes
- El objetivo es llegar rápido al mercado: puede ser más caro que el sistema tradicional

---

![w:30em center](images/cicd/git-branches.png)

## Buenas prácticas

- Trata la rama "*main*" como si pudiese desplegarse en cualquier momento
- Cada fallo de tests es un bug
- Mejora los tests
- No uses ramas de desarrollo enormes
- Automatiza todo el despliegue:
    - Incluida la creación de infraestructura: terraform, ansible, kubernetes...

---

Y por supuesto, ¡introduce controles de seguridad en todo el proceso!

![center](images/devops/etapas.png)

## Quality Assurance

 "*Quality assurance*" (QA) : conjunto de procesos diseñados para garantizar que el software cumple con ciertos estándares de calidad antes de ser entregado al usuario

 1. **Prevención de errores**, no solo detección, desde etapas tempranas del desarrollo
 1. **Establecimiento de procesos y estándares**: desarrollar, documentar, probar y mantener los productos de software para asegurar calidad de forma consistente.
    - Estándares de codificación y pruebas comunes a todo el equipo
    - Revisión de código y diseño
    - Testeo estático y dinámico
    - Métricas de calidad

## Herramientas

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

# Etapas DevOps
<!-- _class: lead -->

## Etapas

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

- Todo el equipo sigue las mismas reglas
- Aumenta la legibilidad del código
- Corrige algunos errores básicos
- Pueden integrase en tu entorno de desarrollo

Ejemplos: [black](https://black.readthedocs.io/en/stable/), [Pylama](https://klen.github.io/pylama/), [Flake8](https://flake8.pycqa.org/en/latest/), [Ruff](https://docs.astral.sh/ruff/)...

> https://twitter.com/svpino/status/1736037083276263563

---

Ejemplo de linter: black

```bash
$ git clone https://github.com/NetSPI/django.nV ; cd django.nV
$ python3 -m pip install black
$ python3 -m black taskManager/views.py
$ git diff
```

![center](images/devops/example-black.png)

> Black usa una versión estricta de [PEP8](https://peps.python.org/pep-0008/) y admite poca configuración de manera premeditada.
> https://black.readthedocs.io/en/stable/the_black_code_style/current_style.html

---

Ejemplo de linter: pylama

```bash
git clone https://github.com/NetSPI/django.nV ; cd django.nV
python3 -m pip install pylama
python3 -m pylama taskManager/views.py

# Resultados
taskManager/views.py:18:1 W0611 'codecs' imported but unused [pyflakes]
taskManager/views.py:161:9 W0612 local variable 'proj' is assigned to but never used [pyflakes]
taskManager/views.py:821:101 E501 line too long (151 > 100 characters) [pycodestyle]
```

Pueden ignorarse errores determinados:

```bash 
python3 -m pylama -i E501 taskManager/views.py

# Resultados
taskManager/views.py:18:1 W0611 'codecs' imported but unused [pyflakes]
taskManager/views.py:161:9 W0612 local variable 'proj' is assigned to but never used [pyflakes]
```

> Pylama también sigue el estilo [PEP8](https://peps.python.org/pep-0008/)

---

También pueden integrarse en tu entorno de desarrollo para que haga las comprobaciones siempre:

![center w:20em](images/coding/code-linting.png)

## Etapa 1: Build - Análisis estático de código (SAST)

Análisis estático: *Static Application Security Testing*

- Análisis automático del código antes de compilarlo
- Incluye:
  - errores comunes: algoritmos que no deben usarse, estructuras que pueden crear un buffer overflow, variables usadas antes de asignarse...
  - análisis de librerías
  - uso inseguro de "secretos" como contraseñas
- Puede tener falsos positivos
- No encontrará errores en **la lógica** del código como por ejemplo acceso a recursos sin la suficiente autorización

---


Lenguaje|Herramienta SAST
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

![w:30em center](images/devops/ejemplo-bandit.png)

---

Ejemplo: [SonarQube](https://www.sonarsource.com/products/sonarqube/downloads/)

![w:25em center](images/devops/ejemplo-sonarqube.png)

## El fiasco CrowdStrike y SAST

![center w:20em](images/coding/crowdstrike-fiasco.png)

> https://twitter.com/Perpetualmaniac/status/1814376668095754753
> https://www.nytimes.com/2024/07/19/business/microsoft-outage-cause-azure-crowdstrike.html

<!-- El 19 de Julio de 2024, un programador olvidó comprobar si un puntero
era NULL... en un driver de sistema como es CrowdStrike.

El asunto dejó decenas de miles de PCs inservibles

El error se podría haber evitado con herramientas de análisis
de la calidad de código
-->

## Análisis estático - auditoría de librerías
<!-- _class: two-columns -->

- Estas herramientas comprueban en una base de datos si la librería usada tiene alguna vulnerabilidad conocida -> ¡No analizan la librería!
- Decisión: ¿ss posible actualizar la librería o asumimos el riesgo?
- No detectan vulnerabilidades automáticamente: se tiene que analizar periódicamente con bases de datos actualizadas


Lenguaje|Herramienta de análisis de librerías
--|--
JS|[Retirejs](https://retirejs.github.io/retire.js/)/npm audit/AuditJS
Python|[Safety](https://github.com/pyupio/safety)
Ruby|Bundler audit/Chelsea
PHP|Composer
Java|OWASP dependency checker

---

¿Por qué no querríamos actualizar una librerías que es vulnerable?

- El trabajo necesario para actualizar a una versión superior puede ser mayor que el riesgo que crea la vulnerabilidad sobre tu aplicación
- El imacto de la vulnerabilidad podría ser mínimo
- La explotación de la vulnerabilidad podría ser muy difícil

Recuerda: Riesgo = Probabilidad * Impacto

[![center w:30em](images/threatmod/cve-2023-38408.png)](https://www.cvedetails.com/cve/CVE-2023-38408)


> https://www.splunk.com/en_us/blog/learn/vulnerability-vs-threat-vs-risk.html

<!--
En el ejemplo, la cve-2023-38408 que es una vulnerabilidad crítica... con un impacto bajo
-->

---

Ejemplo: [Safety](https://github.com/pyupio/safety) analiza librerías Python

```bash
git clone https://github.com/NetSPI/django.nV ; cd django.nV
python3 -m pip install safety
python3 -m safety check -r requirements.txt --save-json safety-resuls.json
```

![center w:30em](images/devops/ejemplo-safety.png)

---

Fíjate:

- *safety* simplemente examina el archivo de requisitos `requirements.txt`, no entra en el código
- Safety tiene una versión gratuita con vulnerabilidades >30 days, y otra de comercial con vulnerabilidades recientes que también emite recomendaciones

---

Ejemplo: Pip audit

```bash
git clone https://github.com/NetSPI/django.nV
python3 -m pip pip-audit
pip-audit -r ./requirements.txt
```

![center](images/devops/ejemplo-pipaudit.png)

---

Ejemplo: `npm audit` (ya incluido con node)

```bash
git clone https://github.com/SasanLabs/VulnerableApp-facade
cd VulnerableApp-facade/facade-app
npm audit
```

![center](images/devops/example-npmaudit.png)

---

Ejemplo: Github Dependabot

![](images/devops/ejemplo-dependabot.png)

Dependabot es un servicio que puedes activar en la configuración de tu proyecto en GitHub

---

Ejemplos de librerías maliciosas:

- https://socket.dev/npm/package/segment-bundle/files/6.6.9/package.json
- https://socket.dev/npm/package/filebdecoder/files/1.0.0/package.json
- https://socket.dev/npm/package/123rf-ui-core/files/9.849.9/index.js

> https://twitter.com/feross/status/1672401333893365761

## Análisis estático - secretos

Tipos de secretos:

- Archivos de configuración interna que no deberían subirse a un repositorio
- Contraseñas *hardcoded* en el código fuente que está público en GitHub
- Subir la clave privada en vez de la pública
- Claces de conexión a las APIs de otros servicios
- Direcciones IPs de servicios en la intranet
- ...

![bg right:40% w:100%](images/devops/secrets-sourcecode1.png)

> https://www.wiz.io/academy/secret-scanning#scanning-for-secrets-with-wiz-85


<!--
Comic: https://twitter.com/DZoneInc/status/1361420207793659904
-->

---

Ejemplo: secretos en archivos de configuración

![center](images/devops/secrets-configfile.png)

<!-- Ejemplo de: > https://cybenari.com/2024/08/whats-the-worst-place-to-leave-your-secrets/
 -->

---

Ejemplo: secretos en código fuente

![center](images/devops/secrets-sourcecode2.png)

<!-- Ejemplo de: > https://cybenari.com/2024/08/whats-the-worst-place-to-leave-your-secrets/
 -->

---
<!-- _class: with-warning -->

Utiliza detectores de contraseñas/tokens de seguridad:

- Basados en patrones/regex: reconocen errores comunes como poner la contraseña en un parámetro función, o variables llamadas `aws_token`
- Basados en entropía: reconocen "el aspecto" de una contraseña

Ten en cuenta que ambos métodos pueden tener falsos positivos

Recuerda que Git (github, gitlab...) guarda el histórico de un proyecto: una vez que se ha subido un archivo con un secreto, ya no puede eliminarse del histórico ni aunque cambies el archivo. Considera los secretos subidos a git como comprometidos que deben cambiarse inmediatamente.


---

![w:20em center](images/devops/forgotten-tokens.png)

> https://cybenari.com/2024/08/whats-the-worst-place-to-leave-your-secrets/

## Comparación de herramientas para detección de secretos
<!-- _class: smaller-font -->

Tool|History|Regex/entropy|FP handling|Custom regex|Language|CI/CD|Comments
--|--|--|--|--|--|--|--
git-secrets|No|regex|yes|yes|shell scripts|No|-|Git hook
Trufflehog|yes|both|-|yes|python|yes|no|-
gitrob|yes|regex|no|yes|ruby|no|no|standalone
repo-security-scanner|yes|regex@yes|yes|golang|yes|-|-
git-hound|-|regex|no|yes|golang|-|-|-
surch|yes|regex|no|yes|python|no|-|-

---

Ejemplo: trufflehog

```bash
git clone https://github.com/dustin-decker/secretsandstuff
wget https://github.com/trufflesecurity/trufflehog/releases/download/v3.81.8/trufflehog_3.81.8_linux_amd64.tar.gz
tar -xvf trufflehog_3.81.8_linux_amd64.tar.gz trufflehog
chmod +x trufflehog

# Análisis local
./trufflehog filesystem secretsandstuff

# Análisis remoto
./trufflehog github --repo=https://github.com/dustin-decker/secretsandstuff
```

![center w:15em](images/devops/trufflehog.png)

<!-- Observa que trufflehog tiene diferentes detectores filesystem gitlab, token...

trufflehog --help
trufflehog filesystem --help
trufflehog filesystem --directory=mydir

-->

---

Ejemplo: deepfence

```bash
git clone https://github.com/dustin-decker/secretsandstuff
docker run --rm -v $PWD/secretsandstuff:/source deepfenceio/deepfence_secret_scanner --local /source --output json
```

![center w:20em](images/devops/deepfence.png)

Con este ejemplo vemos también que podemos ejecutar algunas de las herramientas con docker. Veremos en la siguiente sesión que esto es muy deseable

# Ejemplo: Github

Servicios ofrecidos por Github en sus repositorios

- *Dependabot*: análisis de librerías
- *Code scanning*: SAST para errores comunes
- *Secret scanning*: [patterns](https://docs.github.com/en/code-security/secret-scanning/introduction/supported-secret-scanning-patterns)

Ejemplo: <https://github.com/Juanvvc/sMSD/security> (Nota: necesitas permisos)

![bg right w:100%](images/devops/github-services.png)

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

## Tests unitarios

```python
import unittest
from code.my_calculations import Calculations

class TestCalculations(unittest.TestCase):

    def test_sum(self):
        calculation = Calculations(8, 2)
        self.assertEqual(calculation.get_sum(), 10, 'The sum is wrong.')

    def test_diff(self):
        calculation = Calculations(8, 2)
        self.assertEqual(calculation.get_difference(), 6, 'The difference is wrong.')

    def test_product(self):
        calculation = Calculations(8, 2)
        self.assertEqual(calculation.get_product(), 16, 'The product is wrong.')

    def test_quotient(self):
        calculation = Calculations(8, 2)
        self.assertEqual(calculation.get_quotient(), 4, 'The quotient is wrong.')

if __name__ == '__main__':
    unittest.main() 
```

> https://www.dataquest.io/blog/unit-tests-python/

## Test Coverage

![center 10em](images/devops/coverage.png)

> https://artoftesting.com/test-coverage

---

- ¿Qué porcentaje del código cubren nuestros tests? Ejemplo: <https://coverage.readthedocs.io/en/7.5.3/>
- ¿Qué porcentaje de las amenazas detectadas durante el diseño cubren los tests?
- ¿Se testean todos los casos de uso de la aplicación?



---

![center](images/devops/Code-Based-Testing.png)

## Etapa 4: Dynamic Application Security Testing DAST

- Explora vulnerabilidades conocidas de las aplicación en ejecución
- Ejemplos:
  - uso de protocolos http en vez de https
  - configuración inadecuada del servidor
  - puertos abiertos
  - Compliance

> https://about.gitlab.com/blog/2019/08/12/developer-intro-sast-dast/
> https://realm3ter.medium.com/analyzing-javascript-files-to-find-bugs-820167476ffe
> https://www.gb-advisors.com/es/pruebas-de-seguridad-de-aplicaciones-ast-sast-dast-e-iast/

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

## Infrastructure-as-a-code

1. Ejecuta *terraform* para desplegar dockers/máquinas virtuales
1. Ejecuta *ansible* para configurar las máquinas desplegadas
2. Ejecuta testeos con *inspec*

## Terraform
<!-- _class: two-columns -->

- Terraform: https://www.terraform.io/
- Crea la infrastructura de máquinas virtuales / docker que necesites
- SAST con [Checkov](https://www.checkov.io/)

```
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

  required_version = ">= 1.2.0"
}

provider "aws" {
  region  = "us-west-2"
}

resource "aws_instance" "app_server" {
  ami           = "ami-830c94e3"
  instance_type = "t2.micro"

  tags = {
    Name = "ExampleAppServerInstance"
  }
}
```

## Ansible
<!-- _class: two-columns -->

- [Ansible](https://docs.ansible.com/ansible/latest/index.html): Application deployment + configuration management
- https://github.com/dev-sec/ansible-collection-hardening
- Prepara y configura los sistemas a tu gusto: *hardening*
- Utiliza ssh para conectarse a los sistemas

```
- name: Playbook to install nginx
  hosts: sandbox
  remote_user: root
  become: yes

  # We are checking avaibility of nginx binary at a specific location
  tasks:
    - name: check if nginx installed
      stat:
        path: /usr/sbin/nginx
      register: stat_nginx

    - name: get nginx version
      command: nginx -v
      register: nginx_version
      when: stat_nginx.stat.exists

    - name: Print version
      debug:
        msg: "{{ nginx_version.stderr }}"
      when:
        - nginx_version is defined
        - stat_nginx.stat.exists

    - name: install nginx if not exist
      apt:
        name: nginx
        state: present
        update_cache: true
      when: not stat_nginx.stat.exists
```

> https://www.redhat.com/sysadmin/harden-new-system-ansible

## Inspec
<!-- _class: two-columns -->

- Inspec: <https://github.com/inspec/inspec>
- Test de infrastructura para compliance y seguridad
- Guía: https://www.chef.io/docs/cheflibraries/whitepapers/guidetopcidsscompliance.pdf

```
describe file('/etc/ssh/sshd_config') do
    it { should exist }
    it { should be_file }
    it { should be_owned_by 'root' }
    its('content') { should match 'PasswordAuthentication no' }
end

describe file('/etc/pam.d/password-auth') do
  its('content') { 
      should match(/^\s*password\s+requisite\s+
        pam_pwquality\.so\s+(\S+\s+)*try_first_pass/)
  }
  its('content') {
      should match(/^\s*password\s+requisite\s+
        pam_pwquality\.so\s+(\S+\s+)*retry=[3210]/)
  }
end
```



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
