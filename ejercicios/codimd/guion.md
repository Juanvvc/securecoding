
Documentación de instalación:https://hackmd.io/c/codimd-documentation/%2Fs%2Fcodimd-docker-deployment

# Threat Modelling

https://awslabs.github.io/threat-composer/

- pueden los usuarios recuperar contraseñas?
- gestión de historial?
- espacios separados para grupos de usuarios?
- servicios externos de imágenes, sí o no?
- control de salud?
- usuarios anónimos?
- caducidad de sesiones?

https://app.diagrams.net/?src=about

# Linters

Observa cómo funcionan en un editor de texto

También: https://labs.watchtowr.com/xortigate-or-cve-2023-27997/

# Registro de nuevo usuario

lib->auth

Observad:

- uso de librería externa passport para gestionar la autenticación de usuario. El uso de librerías especializadas no solo hará tu trabajo más rápido, también más seguro porque:
  - estás usando el conocimiento especializado de una persona
  - permites utilizar múltiples métodos de autenticación sin esfuerzo
- Enlaces:
  - Tutorial; https://blog.logrocket.com/using-passport-authentication-node-js/
  - Librería: http://www.passportjs.org/

lib->auth->email#41

```javascript
    try {
      const [user, created] = await models.User.findOrCreate({
        where: {
          email: req.body.email
        },
        defaults: {
          password: req.body.password
        }
      })

      if (!user) {
        req.flash('error', 'Failed to register your account, please try again.')
        return res.redirect(config.serverURL + '/')
      }

      if (created) {
        logger.debug('user registered: ' + user.id)
        req.flash('info', "You've successfully registered, please signin.")
      } else {
        logger.debug('user found: ' + user.id)
        req.flash('error', 'This email has been used, please try another one.')
      }
      return res.redirect(config.serverURL + '/')
    } catch (err) {
      logger.error('auth callback failed: ' + err)
      return response.errorInternalError(req, res)
    }
```

Observad:

- control de errores
- comprobación de si el usuario existe o no

## Guardado de las contraseñas de los usuarios

lib->models->users.js#48


```javascript
  User.hashPassword = async function (plain) {
    return (await Scrypt.kdf(plain, await Scrypt.pickParams(0.1))).toString('hex')
  }

  User.prototype.verifyPassword = async function (attempt) {
    if (await Scrypt.verify(Buffer.from(this.password, 'hex'), attempt)) {
      return this
    }

    return false
  }

  User.addHook('beforeCreate', async function (user) {
    // only do hash when password is presented
    if (user.password) {
      user.password = await User.hashPassword(user.password)
    }
  })
  User.addHook('beforeUpdate', async function (user) {
    if (user.changed('password')) {
      user.password = await User.hashPassword(user.password)
    }
  })
```

Observad:

- El modelo de programación usando eventos. Aunque esto depende de la librería de bases de datos, es un modelo de programación muy común.
- El uso de scrypt para gestionar contraseñas

```
docker-compose exec -ti database psql codimd -U hackmd

codimd=# select "Users".id,"Users".email,"Users"."accessToken","Users"."refreshToken","Users"."deleteToken","Users".password from public."Users";
```

Observad:

- los tokens usados para autenticar a los usuarios
- La contraseña guardada como scrypt

# Instalación

Observad:

- server secret para los tokens. ¿Qué pasa si no usamos?
- Volúmenes separados para los datos
- Permisos de los ususarios
- Configuración específica para https

https: https://hackmd.io/c/codimd-documentation/%2F%40codimd%2Fweb-server-nginx
nginx: https://stackify.com/how-to-configure-https-for-an-nginx-docker-container/

# Backups

¿Cómo podemos realizarlos?

https://www.howtogeek.com/devops/how-to-back-up-your-docker-volumes/

Código especializado, en tarea cron semanalmente

```bash
#!/bin/bach
# Backups the database
  
MYDIR=$(dirname $(realpath "$0"))
cd $MYDIR

OUTPUT="backup/$(date +%Y%m%d).backup.sql"
docker-compose exec -T database pg_dump codimd -U hackmd  > $OUTPUT
echo "Backup completed at: $MYDIR/$OUTPUT"
```
