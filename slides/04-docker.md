---
marp: true
title: Código seguro - Kubernetes
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

# Orquestación
<!-- _class: first-slide -->

Juan Vera del Campo

<juan.vera@campusviu.es>

# Hoy hablamos de...
<!-- _class: cool-list -->

1. [De aplicaciones a contenedores](#3)
1. [Kubernetes](#10)
1. [Referencias](#29)

# De aplicaciones a contenedores
<!-- _class: lead -->

## Containers: máquinas de usar y tirar

- Los **containers** se crean y se destruyen fácilmente
- Puedes volver a ejecutar la **image** en la que están basados
- Los datos persistentes se guardan en **volúmenes**
- Puedes crear **networks** aisladas (o no) para comunicar los containers entre sí

![bg right w:90%](images/docker-logo.png)

## ¿Cómo organizamos todo esto?

- Aplicaciones simples: docker-compose
- Aplicaciones complejas: Orquestadores


## Orquestadores

- Provisión y despliegue
- Redundancia y escalado
- Elasticidad
- Redes
- Balanceador de carga
- Monitorización de salud
- Gestión centralizado de configuración: compliance, auditability

## Más populares

- Kubernetes:
    - “Núcleo Linux” para sistemas distribuidos
- Docker Swarm:
    - Respuesta de Docker a la orquestación de contenedores
- Mesos
    - Manejador de clúster
    - Frameworks (Marathon) para equiparar con Swarm y Kubernetes

![bg right w:90%](images/Kubernetes-logo.png)


---

![](images/docker-swamp.png)


---

![](images/marathon.png)

# Kubernetes
<!-- _class: lead -->

## Kubernetes / K8s

- Sistema de código libre para la automatización del despliegue, ajuste de escala y manejo de aplicaciones en contenedores
- Originalmente diseñado por Google 
- Actualmente gestionado por la Cloud Native Computing Foundation (parte de la Linux Foundation)
- Soporta diferentes entornos para la ejecución de contenedores
    - docker. Deprecated en la versión 1.24, puede usarse a través de cri-dockerd
    - containerd
    - CRI-O

---

![](images/kubernetes-infra.png)

---

![](images/kubernetes-flow.png)

---

![](images/kubernetes-google.png)

> https://www.youtube.com/watch?v=Rl5M1CzgEH4

## Docker and Kubernetes

![](images/kubernetes-dockerconfig.png)

## Interfaces
<!-- _class: two-columns -->

```
19:32 securecoding $ kubectl cluster-info
Kubernetes control plane is running at
https://kubernetes.docker.internal:6443

CoreDNS is running at
https://kubernetes.docker.internal:6443/api/v1/
namespaces/kube-system/services/kube-dns:dns/proxy

To further debug and diagnose cluster problems, use 'kubectl cluster-info dump'.
19:32 securecoding $ kubectl get pod     
NAME                                  READY   STATUS    RESTARTS       AGE
kubernetes-bootcamp-d9b4bdd78-trhhh   1/1     Running   1 (114s ago)   26h
```

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  selector:
    matchLabels:
      app: nginx
  minReadySeconds: 5
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.14.2
        ports:
        - containerPort: 80
```

---

![center w:35em](images/kubernetes-dashboard.png)

## Control plane

![bg left w:80%](images/kubernetes-controlpane.png)

- kube-apiserver:
    - Punto de interactuación
- etcd:
    - Almacenamiento distribuido interno
    - Sólo accesible por kube-apiserver
- kube-control-manager
    - Director de orquesta
- kube-scheduler
    - Decide dónde se despliegan los “pods”

## Node

- kubelet
    - Agente en cada nodo, incluído el
maestro
- kube-proxy
    - Comuniaciones entre contenedores y sistema
- Motor de contenedores
    - Containerd (Docker)
    - Rkt (CoreOS)
    - y otros

![bg left w:80%](images/kubernetes-node.png)

## Pod

- Unidad mínima de trabajo
- Puede contener uno o más contenedores
- Similar a un solo docker-compose

![bg left w:80%](images/kubernetes-pod.png)

---

![](images/kubernetes-pod2.png)

## Health checks

- Liveness
    - Indica si un pod está vivo y en buenas condiciones
    - Kubernetes reinicia el pod si no este falla
- Readiness
    - Indica si el pod está listo para recibir tráfico
    - Kubernetes no manda tráfico hasta que éste esté listo
- Startup
    - Usado para pods lentos (arranque)
    - Kubernetes no comprueba los otros checks

## Labels y filters

Puedes asignar labels a los pods, para seleccionarlos desde otros pods

- Basados en igualdad
- Basados en expresiones

![bg left w:80%](images/kubernetes-selector.png)

## Redes

- Redes de “pods”
    - Red dentro del clúster para la comunicación entre Pods
    - CNI (Container Network Interface) plugin
- Redes de servicios
    - Red dentro del clúster de IPs virtuales usadas por kube-
proxy para la localización de servicios (Service Discovery)

---

- Todos los contenedores en un Pod se pueden comunicar entre ellos sin ningún tipo de restricción
- Todos los Pods se pueden comunicar entre ellos sin usar NAT
- Todos los nodos se pueden comunicar con todos los Pods y viceversa sin NAT

## Servicios

Forma de acceder a los Pods desde el exterior

- Son “duraderos”
- IP estática y única del clúster
- Nombre de dominio (DNS) estático y único
- Apuntan a los Pods usando selectores de igualdad
- Actúan como simples balanceadores de carga a través de kube-proxy
- kube-proxy se encarga de modificar las iptables de los nodos para crear una entrada local por cada servicio

## Tipos de servicios

- ClusterIP
- NodePort
- LoadBalancer
- ExternalName

---

![](images/kubernetes-balancer.png)

# References
<!-- _class: lead -->

---

- [Kubernetes Tutorial](https://kubernetes.io/es/docs/tutorials/), intereactivo y muy recomendable
- [The Kubernetes Learning Slides](https://docs.google.com/presentation/d/13EQKZSQDounPC1I6EC4PmqaRmdCrpT3qswQJz9KRCyE/edit#slide=id.g7cd09fc403_101_0), con muchos recursos, explicaciones y sobre todo enlaces a documentación más extensa
- [CI/CD Pipelines with Kubernetes | Best Practices and Tools](https://www.containiq.com/post/cicd-pipelines-with-kubernetes)

# ¡Gracias!
<!-- _class: last-slide -->