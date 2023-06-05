# Código seguro

Transparencias en
[juanvvc.github.io/crypto/](https://juanvvc.github.io/securecoding/index.html),
pero puedes acceder directamente a cada capítulo seleccionando los enlaces en
el apartado "Contenido".

## Contenido

1. [Modelado de amenazas](https://juanvvc.github.io/securecoding/01-threatmodeling.html)
2. [Buenas prácticas en la escritura de código](https://juanvvc.github.io/securecoding/02-coding.html)
3. [Open Web Application Security Project](https://juanvvc.github.io/securecoding/03-quality.html)
4. [SecDevOps](https://juanvvc.github.io/securecoding/04-devsecops.html)
5. [Docker](https://juanvvc.github.io/securecoding/05-docker.pdf)
6. (Opcional) [Kubernetes](https://juanvvc.github.io/securecoding/06-kubernetes.html)
7. [Ejemplo](https://juanvvc.github.io/securecoding/07-ejemplo.html)

Recuerda: en Chrome y Edge, **puedes "imprimir a PDF" para obtener las transparencias en PDF**

## Descarga local

Aunque lo más recomendable es acceder a la versión en línea para ver siempre la
versión actualizada, si quieres puedes descargarte las transparencias para
visualizarlas fuera de línea. Simplemente aprieta el botón `Download ZIP` de
arriba.

O si tienes cuenta en GitHub puedes simplemente un `fork` (botón de arriba a la
derecha), aunque no las voy a borrar a medio plazo, con lo que si simplemente
marcas con una estrella tendrás un recordatorio en tu cuenta de donde residen
para cuando las necesites.

O también, puedes clonar el proyecto en tu disco duro local (necesitas un
cliente `git`):

```
$ git clone git@github.com:juanvvc/securecoding.git
```

De esta manera tienes una copia local que siempre puedes mantener al día con:

```
$ git pull
```

Puedes crear las transparencias con:
 
```
# Si no tienes marp instalado, ejecuta esto solo una vez
npm install @marp-team/marp-cli

# Para crear las transparencias en el directorio build
make

# Alternativamente, para crear PDFs en el directorio build
make pdfs
```

# Notas de presentación

Puedes acceder a las notas de presentación, que probablemente contengan
información interesante y extendida, pulsando la tecla `P`

# Licencia

Esta obra esta sujeta a una licencia de [Attribution-ShareAlike 4.0
International (CC BY-SA 4.0) ](https://creativecommons.org/licenses/by-sa/4.0/)

[![Licencia de Creative
Commons](https://licensebuttons.net/l/by-sa/3.0/88x31.png)](https://creativecommons.org/licenses/by-sa/4.0/)

Copyright © 2020-2023 [Juan Vera del Campo](https://github.com/juanvvc)

