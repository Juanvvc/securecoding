---
title: "TM: Aplicación gestión de contraseñas"
model: "claude-sonnet-5"
exported: 2026-09-22
---

# Human

Eres un ingeniero de software. Te han encargado el proyecto de una aplicación multiusuario online de gestión de contraseñas. Estamos ahora mismo en la fase de diseño.

# Claude

¡Buena fase para sentar bases! Un gestor de contraseñas multiusuario online tiene un requisito que domina todo lo demás: el servidor nunca debe poder ver las contraseñas en claro (arquitectura zero-knowledge/zero-trust). Todo lo demás se diseña alrededor de esa restricción.

Antes de proponerte una arquitectura concreta, conviene fijar algunas decisiones de diseño que condicionan todo lo posterior:

**1. Modelo de amenaza**
¿Contra qué te proteges principalmente?
- Servidor comprometido / admin malicioso → obliga a zero-knowledge real (cifrado en cliente, servidor solo almacena blobs)
- Solo tráfico en tránsito → TLS + cifrado en reposo del lado servidor sería suficiente, pero es un estándar mucho más débil (tipo LastPass pre-breach)
- Dispositivo del usuario comprometido → esto ningún gestor lo resuelve del todo, pero afecta a decisiones de sesión/timeout

**2. Compartición entre usuarios**
Dices "multiusuario" — ¿te refieres a que cada usuario tiene su bóveda privada, o a que hay bóvedas compartidas (equipos, familias) donde varios usuarios acceden a las mismas credenciales? Esto es importante porque compartir un secreto cifrado con otra persona sin que el servidor lo vea requiere cifrado asimétrico (RSA/ECC) para "envolver" la clave simétrica de cada credencial por cada destinatario.

**3. Recuperación de cuenta**
Si el modelo es zero-knowledge puro (el servidor no conoce la master password), perder la master password significa perder la bóveda irremediablemente, salvo que implementes algo tipo "recovery kit" (clave de recuperación off-line) o un esquema de secret sharing entre contactos de confianza.

**4. Stack técnico**
Como eres de un SOC y trabajas con Python — ¿el backend también va en Python (FastAPI/Django) o eso está abierto? ¿Y el cliente? (web/app de escritorio/CLI/extensión de navegador — cada uno tiene implicaciones de dónde vive el cifrado).

Mientras me dices esto, te dejo el esqueleto de arquitectura que usaría cualquier gestor serio (Bitwarden es la referencia open-source más estudiable):

Antes de dibujar nada, mejor cerremos las decisiones que van a determinar toda la arquitectura — así el primer diagrama que hagamos ya será el bueno, no uno que tiremos a la basura.

**1. Modelo de amenaza**
¿Contra qué diseñamos principalmente?
- Servidor comprometido o admin malicioso → exige zero-knowledge real: el servidor solo almacena blobs cifrados, nunca ve contraseñas en claro ni la master password
- Solo interceptación en tránsito → TLS + cifrado en reposo del lado servidor bastaría, pero es un estándar mucho más débil (el que falló en el breach de LastPass)
- Dispositivo del usuario comprometido → ningún gestor lo resuelve del todo, pero condiciona decisiones de sesión, timeout y clipboard

Dado tu perfil (SOC, threat intel), imagino que vas a querer zero-knowledge por defecto. Lo confirmo porque cambia todo el diseño de auth y storage.

**2. Compartición entre usuarios**
"Multiusuario" puede significar dos cosas muy distintas:
- Cada usuario tiene su bóveda privada, sin relación entre ellas
- Hay bóvedas compartidas (equipos, familias) donde varios usuarios acceden a las mismas credenciales

Si es lo segundo, compartir un secreto cifrado con otra persona sin que el servidor lo vea requiere cifrado asimétrico (RSA-OAEP o ECC) para "envolver" la clave simétrica de cada entrada por cada destinatario — es la parte más compleja del diseño, así que conviene saberlo ya.

**3. Recuperación de cuenta**
Si el servidor nunca conoce la master password (zero-knowledge puro), perder esa contraseña significa perder la bóveda sin remedio, salvo que implementes algo como:
- Recovery kit off-line (clave de recuperación que el usuario guarda aparte)
- Secret sharing (Shamir) entre contactos de confianza
- Renunciar a parte del zero-knowledge para permitir reset (trade-off real, hay que decidirlo conscientemente)

**4. Stack**
¿Backend en Python (FastAPI/Django + PostgreSQL, por ejemplo)? ¿Y el cliente — web, extensión de navegador, CLI, app de escritorio? Cada cliente implica dónde vive literalmente el código de cifrado, porque ese código nunca puede pasar por el servidor sin invalidar el modelo.

Con esas cuatro respuestas te preparo la arquitectura completa: derivación de claves (Argon2id habitualmente), esquema de cifrado (AES-256-GCM para las entradas, envelope encryption para compartición), modelo de datos, flujo de autenticación (algo tipo SRP o al menos evitar que el servidor vea ni siquiera un hash reutilizable de la master password), y APIs. ¿Empezamos por ahí?

# Human

1. Modelo a amenaza: servidor comprometido
2. Cada usuario tiene una bóveda individual
3. zero-knowledge puro, el servidor no conoce la master password. La clave de recuperación está offline
4. FastAPI+PostgreSQL


Crea una lista con los componentes principales de esta aplicación

# Claude

Con esas cuatro decisiones, esta es la lista de componentes principales, agrupados por dónde viven (cliente vs servidor) porque en zero-knowledge esa frontera es la más importante del diseño.

**Cliente (donde vive todo el cifrado — nunca cruza al servidor sin cifrar)**

- **Derivación de clave maestra**: Argon2id sobre la master password + salt único por usuario → genera la clave simétrica que nunca sale del dispositivo
- **Motor de cifrado de entradas**: AES-256-GCM (o XChaCha20-Poly1305) para cifrar/descifrar cada credencial individualmente
- **Cliente de autenticación**: implementa el protocolo de login sin exponer la master password ni un hash reutilizable de ella (ver más abajo — esto es la pieza más delicada)
- **Gestor de sesión local**: guarda la clave derivada solo en memoria, con timeout/lock automático
- **Generador de contraseñas**: local, sin llamada al servidor
- **Módulo de recovery kit**: genera y muestra una sola vez la clave de recuperación offline (idealmente derivada de una segunda clave maestra independiente, no de la primera)

**Servidor (FastAPI — solo maneja blobs opacos)**

- **API de autenticación**: valida la identidad del usuario sin nunca recibir ni poder derivar la master password. Con zero-knowledge puro esto normalmente significa un protocolo tipo **SRP (Secure Remote Password)** o, más simple de implementar bien, un esquema de "verificador" separado de la clave de cifrado (nunca uses el mismo hash para autenticar y para derivar la clave — si el server ve el verificador de auth, no debe poder usarlo para descifrar nada)
- **API de bóveda (CRUD de entradas cifradas)**: recibe y devuelve blobs opacos, sin lógica de negocio sobre el contenido
- **Gestor de metadatos**: lo mínimo que el servidor sí necesita ver en claro (timestamps, IDs, quizás nombres de carpeta si decides no cifrarlos — decisión de UX vs privacidad a tomar)
- **Rate limiting / anti brute-force**: crítico dado el modelo de amenaza — protege contra intentos masivos de login incluso sin conocer la password
- **Auditoría/logging de eventos de seguridad**: logins, cambios de password, exportaciones — dato interesante para ti dado tu perfil de SOC
- **Gestor de sesiones/tokens**: JWT o tokens opacos con expiración corta + refresh

**Base de datos (PostgreSQL)**

- Tabla `users`: email, verificador de auth (no la password ni su hash directo), salt, metadatos de cuenta
- Tabla `vault_entries`: blob cifrado, IV/nonce, user_id, timestamps — nada más
- Tabla `recovery` (opcional): datos del recovery kit si decides que el servidor guarde algo del lado de recuperación (evalúa si esto compromete el zero-knowledge)
- Tabla `sessions`/`audit_log`

**Infraestructura transversal**

- TLS obligatorio en todo el tráfico (defensa en profundidad, aunque el modelo de amenaza ya asume servidor comprometido)
- Gestión de secretos del servidor (nunca claves de usuario, pero sí claves de firma de tokens, etc.)
- Backups cifrados de la base de datos (los blobs ya van cifrados, pero conviene cifrar también en reposo a nivel de disco)

El punto que más cuidado va a requerir es el protocolo de autenticación (SRP vs esquema propio) porque es donde más gestores de contraseñas fallan — ahí es fácil acabar filtrando indirectamente información que permite un ataque offline contra la master password. ¿Quieres que profundicemos en esa pieza primero, o prefieres ver el modelo de datos completo (esquema de tablas) antes?

# Human

Haz un análisis de amenazas STRIDE. Lista al menos 3 amenazas para cada una de las categorías STRIDE

# Claude

Análisis STRIDE aplicado a la arquitectura que hemos definido (zero-knowledge, bóvedas individuales, FastAPI + PostgreSQL, servidor comprometido como amenaza principal).

## Spoofing (suplantación de identidad)

1. **Suplantación de usuario mediante robo de credenciales de sesión** — si un token JWT/sesión es robado (XSS en cliente web, malware en el dispositivo), el atacante actúa como el usuario sin necesitar la master password.
2. **Suplantación del servidor (man-in-the-middle)** — un atacante que intercepta la conexión podría hacerse pasar por el backend legítimo y capturar el verificador de autenticación o inyectar respuestas maliciosas al cliente.
3. **Registro de cuenta con email ajeno** — si no se verifica la propiedad del email en el registro, un atacante podría crear una cuenta a nombre de la víctima para intentar phishing posterior o confundir el proceso de recuperación.
4. **Replay de credenciales de autenticación** — si el protocolo de login no usa nonces/challenges únicos, un atacante que capture el tráfico de auth podría reproducirlo para autenticarse sin conocer la master password.

## Tampering (manipulación de datos)

1. **Modificación de blobs cifrados en tránsito o en la base de datos** — un servidor comprometido podría alterar un blob cifrado antes de devolverlo; sin autenticación del ciphertext (AEAD), el cliente podría no detectarlo y descifrar datos corruptos o inyectados.
2. **Manipulación de metadatos no cifrados** (timestamps, nombres de carpeta si van en claro) — permite a un atacante reordenar, ocultar o confundir entradas sin tocar el contenido cifrado.
3. **Alteración del recovery kit o su flujo de generación** — si el proceso de generación del recovery kit se ejecuta en un cliente comprometido, el atacante podría sustituir la clave de recuperación mostrada al usuario por una controlada por él.
4. **Modificación del código cliente servido al usuario** (para la versión web) — un servidor o CDN comprometido podría alterar el JavaScript que hace el cifrado, capturando la master password directamente en el navegador antes de que se derive la clave.

## Repudiation (repudio)

1. **Usuario niega haber realizado un cambio o eliminación de una entrada** — sin logs de auditoría con integridad garantizada, no hay forma de demostrar que fue el usuario (o su sesión) quien hizo el cambio.
2. **Falta de trazabilidad de accesos a la bóveda** — sin registro de "cuándo y desde dónde se accedió", no se puede reconstruir un incidente ni distinguir acceso legítimo de uno comprometido.
3. **Administrador del sistema niega haber accedido a la base de datos** — dado el modelo de amenaza (servidor comprometido/admin malicioso), conviene tener logs de acceso a nivel de infraestructura que ni el propio admin pueda alterar retroactivamente (write-once o enviados a sistema externo).
4. **Ausencia de logs firmados/con integridad** — si los logs se pueden editar tras el hecho, cualquier repudio es imposible de refutar.

## Information Disclosure (divulgación de información)

1. **Filtración de metadatos en claro** — incluso con el contenido cifrado, exponer dominios, timestamps o estructura de carpetas puede revelar patrones de uso significativos (qué servicios usa el usuario, cuándo, con qué frecuencia).
2. **Side-channel a través de tamaño de los blobs cifrados** — el tamaño de un ciphertext puede filtrar información sobre la longitud de la contraseña o el contenido, si no se aplica padding.
3. **Exposición de la clave derivada en memoria del cliente** — malware o un volcado de memoria podría capturar la clave simétrica mientras está en uso, incluso sin comprometer el servidor.
4. **Logs del servidor con información sensible accidental** — errores mal gestionados en FastAPI podrían loggear payloads completos (incluyendo blobs cifrados o metadatos) en logs de debug accesibles a más personal del que debería.
5. **Enumeración de usuarios vía el endpoint de login o registro** — si las respuestas de error difieren entre "usuario no existe" y "contraseña incorrecta", un atacante puede enumerar emails registrados.

## Denial of Service (denegación de servicio)

1. **Fuerza bruta contra el endpoint de autenticación sin rate limiting adecuado** — agota recursos del servidor y facilita ataques offline si además se filtra el verificador.
2. **Ataque de agotamiento de recursos vía Argon2id en el lado servidor** (si el servidor participa en algún cálculo de verificación costoso) — un atacante podría enviar muchas solicitudes de login simultáneas para saturar CPU.
3. **Bloqueo de cuenta por abuso del mecanismo anti-brute-force** — paradójicamente, un atacante podría bloquear intencionadamente la cuenta de la víctima enviando intentos fallidos repetidos (DoS dirigido a un usuario concreto).
4. **Saturación de la base de datos con escrituras masivas** — un usuario malicioso o cuenta comprometida podría generar miles de entradas de bóveda para agotar almacenamiento o degradar rendimiento para otros usuarios (multi-tenancy).

## Elevation of Privilege (elevación de privilegios)

1. **Acceso de un usuario a la bóveda de otro usuario mediante fallo de autorización** (IDOR) — si los endpoints de la API no verifican correctamente que el `user_id` del token coincide con el recurso solicitado, un usuario autenticado podría leer blobs cifrados de otro (aunque no pueda descifrarlos, ya es una violación grave).
2. **Escalada desde cuenta de servicio de la aplicación a acceso administrativo de la base de datos** — si la app usa credenciales de BD con privilegios excesivos, comprometer la API expone toda la base de datos, no solo la lógica de negocio.
3. **Bypass del flujo de recuperación para tomar control de una cuenta ajena** — si el proceso de recovery kit no está bien aislado, un atacante podría intentar iniciar una recuperación no autorizada y obtener acceso sin la master password original.
4. **Abuso de un panel de administración interno** (si existe) para acceder a funciones reservadas a operadores, saltándose los límites de "el servidor no debería poder hacer X".

Los puntos que yo priorizaría dado tu modelo de amenaza (servidor comprometido) son: **Tampering #1 y #4** (AEAD + integridad del código cliente) y **Elevation of Privilege #1** (IDOR), porque son los que un servidor comprometido puede explotar más directamente incluso sin romper el cifrado. ¿Quieres que profundicemos en mitigaciones concretas para alguno de estos, o seguimos con el modelo de datos?

# Human

Crea una tabla con el riesgo (probabilidad e impacto) de cada una de estas amenazas

# Claude

Aquí tienes la valoración de riesgo para las 24 amenazas identificadas, usando escala Alto/Medio/Bajo para probabilidad e impacto, y un riesgo resultante (combinación de ambos). La probabilidad está calibrada asumiendo tu modelo de amenaza específico (servidor comprometido) y la arquitectura zero-knowledge ya definida.

| # | Categoría | Amenaza | Probabilidad | Impacto | Riesgo |
|---|-----------|---------|:---:|:---:|:---:|
| S1 | Spoofing | Robo de token de sesión (XSS/malware) | Medio | Alto | **Alto** |
| S2 | Spoofing | Suplantación del servidor (MITM) | Bajo | Alto | Medio |
| S3 | Spoofing | Registro con email ajeno sin verificar | Medio | Bajo | Bajo |
| S4 | Spoofing | Replay de credenciales de autenticación | Bajo | Alto | Medio |
| T1 | Tampering | Modificación de blobs cifrados sin AEAD | Medio | Alto | **Alto** |
| T2 | Tampering | Manipulación de metadatos en claro | Medio | Medio | Medio |
| T3 | Tampering | Alteración del flujo de generación del recovery kit | Bajo | Alto | Medio |
| T4 | Tampering | Modificación del código cliente servido (web) | Medio | Alto | **Alto** |
| R1 | Repudiation | Usuario niega cambio/eliminación de entrada | Medio | Bajo | Bajo |
| R2 | Repudiation | Falta de trazabilidad de accesos | Alto | Medio | Medio |
| R3 | Repudiation | Admin niega acceso no autorizado a BD | Medio | Medio | Medio |
| R4 | Repudiation | Logs sin integridad (editables a posteriori) | Alto | Medio | Medio |
| I1 | Info Disclosure | Filtración de metadatos en claro | Alto | Medio | Medio |
| I2 | Info Disclosure | Side-channel vía tamaño de ciphertext | Medio | Bajo | Bajo |
| I3 | Info Disclosure | Exposición de clave derivada en memoria del cliente | Bajo | Alto | Medio |
| I4 | Info Disclosure | Logs de servidor con datos sensibles por error de debug | Medio | Medio | Medio |
| I5 | Info Disclosure | Enumeración de usuarios vía login/registro | Alto | Bajo | Medio |
| D1 | DoS | Fuerza bruta contra autenticación sin rate limiting | Alto | Medio | **Alto** |
| D2 | DoS | Agotamiento de recursos vía cómputo de verificación | Bajo | Medio | Bajo |
| D3 | DoS | Bloqueo de cuenta ajena vía anti-brute-force | Medio | Bajo | Bajo |
| D4 | DoS | Saturación de BD con escrituras masivas | Bajo | Medio | Bajo |
| E1 | Elevation | IDOR — acceso a bóveda de otro usuario | Medio | Alto | **Alto** |
| E2 | Elevation | Escalada de app a acceso admin de BD | Bajo | Alto | Medio |
| E3 | Elevation | Bypass del flujo de recuperación | Bajo | Alto | Medio |
| E4 | Elevation | Abuso de panel de administración interno | Bajo | Alto | Medio |

**Riesgo Alto (prioridad de mitigación inmediata):** S1, T1, T4, D1, E1 — coinciden con lo que ya intuíamos: integridad del ciphertext (AEAD), integridad del código cliente, control de sesión, rate limiting y aislamiento estricto por usuario (anti-IDOR) son los cinco frentes que hay que blindar primero.

Nota sobre la calibración: en tu modelo de amenaza (servidor comprometido), varias probabilidades subirían si el atacante fuera precisamente el operador del servidor en vez de un externo — por ejemplo T4 (modificación del código cliente web) pasaría a ser prácticamente garantizada si el propio proveedor de hosting o CDN está comprometido, lo cual es un argumento fuerte a favor de subresource integrity (SRI) o, mejor aún, de una app de escritorio/CLI en vez de solo cliente web para los casos de uso más sensibles.

¿Seguimos con mitigaciones concretas para los cinco de riesgo Alto, o prefieres primero cerrar el modelo de datos?

# Human

Mitigaciones concretas para las cinco de riesgo alto

# Claude

## S1 — Robo de token de sesión (XSS/malware)

- **Tokens de corta duración + refresh rotativo**: access token de vida corta (10-15 min), refresh token de vida más larga pero con **rotación en cada uso** (refresh token reuse detection) — si el mismo refresh token se usa dos veces, se invalidan todas las sesiones del usuario, señal de robo.
- **HttpOnly + Secure + SameSite=Strict en cookies** si usas cookies para el token — nunca en `localStorage`, que es directamente legible por cualquier XSS.
- **Content Security Policy (CSP) estricta** en el cliente web para reducir la superficie de XSS (sin `unsafe-inline`, sin `unsafe-eval`).
- **Binding del token al contexto del dispositivo** (fingerprint ligero, no intrusivo) para detectar uso desde un contexto radicalmente distinto y forzar re-autenticación.
- **Revocación activa**: endpoint de "cerrar todas las sesiones" accesible al usuario, y lista de tokens revocados consultable en cada request (Redis con TTL, no solo confiar en expiración del JWT).
- La clave derivada de cifrado **nunca debe viajar en el token de sesión** — el token de sesión solo debe servir para autorizar llamadas API, no para descifrar nada. Así, aunque roben el token, solo acceden a blobs cifrados, no a contenido en claro.

## T1 — Modificación de blobs cifrados sin AEAD

- Usa **AES-256-GCM** o **XChaCha20-Poly1305** (AEAD real) para cada entrada — nunca AES-CBC sin HMAC separado. El tag de autenticación garantiza que cualquier modificación del ciphertext hace fallar el descifrado en vez de producir datos corruptos silenciosamente.
- **Additional Authenticated Data (AAD)**: incluye el `entry_id` y el `user_id` como AAD en el cifrado. Así, aunque alguien copie un blob cifrado válido de una entrada a otra fila de la base de datos (ataque de sustitución), el descifrado fallará porque el AAD no coincide.
- **Nonce/IV único por operación de cifrado**, generado con CSPRNG, nunca reutilizado — la reutilización de nonce en GCM es catastrófica (permite recuperar el keystream).
- Verifica el tag de autenticación **antes** de exponer cualquier dato descifrado a la UI; si falla, trata la entrada como potencialmente manipulada y avisa al usuario en vez de fallar silenciosamente.

```python
# Ejemplo conceptual del lado cliente (pseudocódigo Python con cryptography)
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

def encrypt_entry(key: bytes, plaintext: bytes, entry_id: str, user_id: str) -> tuple[bytes, bytes]:
    nonce = os.urandom(12)
    aad = f"{user_id}:{entry_id}".encode()
    ciphertext = AESGCM(key).encrypt(nonce, plaintext, aad)
    return nonce, ciphertext  # el tag va incluido al final de ciphertext
```

## T4 — Modificación del código cliente servido (web)

- **Subresource Integrity (SRI)** en cualquier script/asset servido desde CDN, con hashes verificados por el navegador.
- **Certificate/Public Key Pinning** para la conexión entre cliente y servidor propio, si el modelo de amenaza lo justifica (mitiga MITM incluso con CA comprometida).
- **Firma de builds**: pipeline de CI/CD que firma criptográficamente cada release del frontend; idealmente reproducible builds para que terceros puedan verificar que el código servido coincide con el código fuente auditado.
- Para los casos de uso más sensibles, **prioriza cliente de escritorio o extensión de navegador** sobre webapp pura — reduce la ventana de ataque porque el código no se re-descarga en cada sesión desde un servidor potencialmente comprometido.
- **Auditoría pública del código de cifrado** (aunque sea closed-source el resto de la app) — es lo que hace Bitwarden y genera confianza verificable, no solo declarada.
- Considera **Trusted Types API** en el navegador para mitigar inyección de DOM incluso si algo se cuela.

## D1 — Fuerza bruta contra autenticación

- **Rate limiting por IP y por cuenta** (no solo uno de los dos) — ej. `slowapi` en FastAPI, o un middleware con Redis para ventanas deslizantes.
- **Backoff exponencial progresivo** tras intentos fallidos, en vez de bloqueo binario (mitiga el DoS dirigido de D3 que vimos antes — bloquear cuentas ajenas a propósito).
- **CAPTCHA adaptativo** (solo se activa tras N intentos fallidos, no en el primer login, para no dañar UX).
- **Costo computacional intrínseco del lado cliente** vía Argon2id con parámetros suficientemente altos — ralentiza brute-force offline incluso si el atacante ya tiene el verificador.
- **Alertas de seguridad al usuario** ante múltiples intentos fallidos desde ubicaciones/IPs distintas — coherente con tu perfil de SOC, esto es terreno conocido.
- **WAF o proxy con detección de patrones de bot** delante de la API (Cloudflare, AWS WAF) como capa adicional, no como sustituto del rate limiting a nivel de aplicación.

```python
# Ejemplo con slowapi en FastAPI
from slowapi import Limiter
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)

@app.post("/auth/login")
@limiter.limit("5/minute")
async def login(request: Request, credentials: LoginRequest):
    ...
```

## E1 — IDOR (acceso a bóveda de otro usuario)

- **Autorización explícita en cada endpoint**, nunca implícita por el hecho de estar autenticado — cada query a `vault_entries` debe filtrar por `user_id` extraído del token verificado, nunca de un parámetro de la request.
- **Usa el `user_id` del JWT/sesión como única fuente de verdad** para el filtro, ignora cualquier `user_id` que llegue en el body o query params del cliente.
- **Row-Level Security (RLS) en PostgreSQL** como defensa en profundidad — incluso si un bug de aplicación olvida el filtro, la base de datos rechaza el acceso a filas de otro usuario a nivel de motor.
- **IDs no predecibles**: usa UUIDv4 (o ULID) para `entry_id`, nunca autoincrementales — dificulta la enumeración aunque el filtro fallara.
- **Tests de autorización automatizados** en CI: por cada endpoint que devuelve un recurso, un test que verifica explícitamente que el usuario B no puede acceder al recurso del usuario A (401/404), no solo tests de "camino feliz".

```sql
-- Ejemplo de RLS en PostgreSQL
ALTER TABLE vault_entries ENABLE ROW LEVEL SECURITY;

CREATE POLICY vault_isolation ON vault_entries
    USING (user_id = current_setting('app.current_user_id')::uuid);
```

```python
# Y en FastAPI, setear ese contexto por request (con SQLAlchemy, por ejemplo)
async def set_rls_context(db: AsyncSession, user_id: str):
    await db.execute(text("SET LOCAL app.current_user_id = :uid"), {"uid": user_id})
```

Esta combinación (AEAD + AAD para T1, RLS + IDs no predecibles para E1) es la que yo priorizaría primero porque son controles baratos de implementar y con máximo efecto — cierran de raíz las dos amenazas más graves sin depender de configuración externa (CDN, WAF, etc.) que puede fallar o mal configurarse.

¿Seguimos con el modelo de datos completo, o prefieres que detalle el protocolo de autenticación (SRP vs esquema con verificador separado) que dejamos pendiente?

# Human

Crea un diagrama draw.io con la arquitectura

# Claude

Voy a representarlo como tres bloques (cliente, servidor, base de datos), respetando la frontera zero-knowledge que hemos definido — es la que más importa que se vea clara en el diagrama.

El diagrama está listo: separa visualmente las tres capas de la arquitectura zero-knowledge que definimos.

- **Cliente** (izquierda): toda la lógica criptográfica — derivación de clave, cifrado, generador de contraseñas, recovery kit offline marcado en naranja como dato especialmente sensible.
- **Servidor FastAPI** (centro): en verde los componentes que manejan datos opacos o control de acceso; en rojo el rate limiting, resaltado porque mitiga la amenaza D1 (fuerza bruta) que priorizamos antes.
- **PostgreSQL** (derecha): las tres tablas principales como cilindros, coherentes con el modelo de datos que aún no hemos detallado del todo.

Las flechas marcan las dos fronteras de confianza clave: la master password nunca sale del dispositivo (flecha usuario→cliente), y el tráfico cliente-servidor va solo como verificador SRP + blobs cifrados + tokens, nunca contraseñas en claro.

Si quieres, el siguiente paso natural es cerrar el **modelo de datos completo** (esquema de tablas con tipos de columna) o detallar el **protocolo de autenticación SRP** paso a paso — ambos quedaron pendientes en la conversación.

