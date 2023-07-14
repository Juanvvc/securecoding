# CodiMD

CodiMD es el editor de texto multiusuario. Hay un pequeño lío de versiones
disposibles:

- HackMD es el nombre original del proyecto. Es un producto cerrado y comercial
  de hackmd.io
- CodiMD es la versión "community" de HackMD, mantenida por hackmd.io
- HedgeDoc es un fork de CodiMD open source. La base de datos de CodiMD 2.4 es
  compatible con la base de datos de HedgeDoc 1.8, pero puede cambiar en el
  futuro

Por ahora, ambos proyectos generan código compatible

# Configuración

El docker-compose está sacado de aquí, con la configuración cambiada:
<https://hackmd.io/c/codimd-documentation/%2Fs%2Fcodimd-docker-deployment>

Esta configuración:

- Guarda las imágenes subidas en el directorio del host `uploads`. Este
  directorio tiene el usuario y permisos requeridos por docker.
- Añade `https://hackmd.mycompany.es` a las URLs de las imágenes subidas.
- Utiliza hackmd como nombre del usuario de la base de datos para poder
  importar la que ya teníamos. La clave es clave aleatoria creada por
  criptografía cuántica: mi gato Roy paseándose por el teclado
- Usa un template propio para las nuevas notas: `default.md`
- Guarda las sesiones entre ejecuciones (parámetro secrete token constante)
- Permite vistas anónimas, para poder descargar el documento desde líneas de
  comandos.

**ATENCIÓN**: permitir vistas anónimas es un problema de seguridad ya que
cualquiera en la red puede ver los documentos.

# Ejecución

El sistema se inicia con `run.sh`, que crea el directorio `uploads` si es
necesario y carga el `docker-compose.yml`.

Inicio:

```
./run.sh
```

Parada:

```
./run.sh down
```

Dado que, en el docker-compose, restart está a always, CodiMD debería iniciarse
automáticamente cuando empieza el sistema.

# Gestión de usuarios

Se ha configurado Codi para que no se puedan crear ni editar notas de forma anónima.
Aún así, cualquier persona puede registrarse en el servidor.
No hace falta que el correo que configuran los usuarios sea real, ya que no se
verifica de ninguna forma. Como no hay servidor de correo, tampoco funciona
el enlace "recuperar contraseña".

Desde línea de comandos se pueden añadir, borrar o cambiar la contraseña
de los usuarios. Desde el directorio de la aplicación:

```
docker-compose exec codimd bin/manage_users --help
```

#  Backups

Hay un script para hacer backups, que se guardan en el directorio `backups`.
Llama a este script una vez a la semana, por ejemplo, poniendo algo parecido a
esto en `/etc/cron.weekly/backup-codimd`

```
#!/bin/bash
# Contenido del archivo /etc/cron.weekly/backup-codimd

# en este servidor, docker-compose está instalado en /user/local/bin, y esa ruta no está
# en el path cuando se ejecuta desde cron. Añadiendo
export PATH=$PATH:/usr/local/bin
cd /home/hackm
./backup.sh
```

Para recuperar un backup, bájalo todo y ejecuta:

```
docker-compose down
docker volume ls
# Apunta el nombre del volumen de la base de datos, DATABASEVOLUME
docker volume rm DATABASEVOLUME
# Empieza solo la base de datos y recupera
docker-compose up --no-deps -d database
cat BACKUPFILE.sql | docker-compose exec -T database psql -U hackmd codimd
# Baja de nuevo la base de datos
docker-compose down
```

Y ya se puede empezar con normalidad el sistema.

# Listado de informes

El script `lista_informes.py` crea una lista de los informes disponibles, con
los enlaces internos. La salida se guarda en el directorio del servidor web.
Ejecútalo una vez al día con crontab:

```
#!/bin/bash
# Contenido del archivo /etc/cron.daily/lista-informes 

cd /home/hackmd

# Crea la lista de informes y la publica en portal
python3 lista_informes.py > /var/www/html/lista_informes.html
chown www-data.www-data /var/www/html/lista_informes.html
```

# Reinicios periódicos

Hemos visto que CodiMD tienda a guardar demasiadas cosas en memoria y se tiene
que reiniciar de vez en cuando:

```
./run.sh restart
```

Esto se puede hacer cada domingo a las 3:00 de la mañana, por ejemplo, poniendo
esto en el crontab:

```
00 3    * * SUN root    /home/hackmd/run.sh restart
```

# Limpieza de control de versiones

La base de datos guarda una enorme cantidad de revisiones de los informes que
después de seis meses probablemente ya no sean importantes. Estas versiones
pueden borrarse con:

```
docker-compose exec database psql -U hackmd codimd
delete from public."Revisions" where public."Revisions"."createdAt" < '2021-01-01';
quit
```

Ajusta la fecha a lo que sea conveniente.

# Exportación de informes concretos

Se incluyen algunos scripts para exportar informes concretos al directorio
actual. La idea de estos scripts es que fuese rápido de programar y que no
necesitasen ninguna dependencia más allá de Python, así que son muy mejorales.

- `list_informes.py`: crea una lista HTML con todos los informes en la base de
  datos
- `extract_informes.py  IDENTIFICADOR1 [IDENTIFICADOR2 IDENTIFICADOR3 ...]`:
  exporta los informes de esos identificadores concretos
- `newer_informes.py 2021-10-01`: lista los informes editados más tarde de una
  fecha.

# Extracción de informes en Markdown

Puede extraerse la última versión de uno o varios informes con:

```
./extract_informes.py ID1 ID2 ID3 ...
```

Los informes se guardarán como `ID1.md`, `ID2.md`...

Los identificadores de pueden sacar de la salida de `lista_informes.py` 

# Configuración para pruebas y HedgeDoc

El docker-compose incluye alguna configuración adicional para pruebas en local
y el uso de HedgeDoc. Antes de cada actualización, prueba en tu ordenador que
nada cambia y que puedes restaurar el sistema.

- HedgeDoc: cambia las líneas de imagen y volúmenes por las comentadas
- Pruebas en local sin SSL: quita la configuración de SSL. El servidor estará
  en <http://localhost:3000>
