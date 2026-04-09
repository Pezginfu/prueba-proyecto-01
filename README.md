# Tienda Online (Django)

Esta es una tienda online completamente funcional construida con el framework Django. Incluye un catálogo de productos, carrito de compras, sistema de órdenes y pagos integrados mediante **Stripe**.

## Requisitos Previos

- Python 3.10 o superior.
- Una cuenta de Stripe (para obtener las claves de la API).

## Instalación Paso a Paso

1. **Clonar o descargar el código base.**

2. **Crear el entorno virtual**
   ```bash
   # En Windows:
   python -m venv venv
   # En Mac/Linux:
   python3 -m venv venv
   ```

3. **Activar el entorno virtual**
   ```bash
   # En Windows:
   venv\Scripts\activate
   # En Mac/Linux:
   source venv/bin/activate
   ```

4. **Instalar las dependencias**
   ```bash
   pip install -r requirements.txt
   ```

5. **Configurar las Variables de Entorno**
   - Renombra el archivo `.env.example` a `.env` o crea uno nuevo llamado `.env`.
   - Abre el archivo `.env` y rellena las variables de configuración con tus claves de Stripe y una clave secreta para Django:
   ```env
   SECRET_KEY=escribe-una-clave-secreta-larga-aqui
   DEBUG=True
   ALLOWED_HOSTS=127.0.0.1,localhost
   STRIPE_PUBLISHABLE_KEY=tu_clave_publica_de_stripe
   STRIPE_SECRET_KEY=tu_clave_secreta_de_stripe
   STRIPE_API_VERSION=2023-10-16
   ```

6. **Aplicar las Migraciones y crear la Base de Datos**
   ```bash
   python manage.py migrate
   ```

7. **Crear un Superusuario (Opcional, para el panel de administración)**
   ```bash
   python manage.py createsuperuser
   ```

8. **Levantar el Servidor Inicial**
   ```bash
   python manage.py runserver
   ```
   Abre [http://127.0.0.1:8000](http://127.0.0.1:8000) en tu navegador para ver la tienda funcionando.

---

## Publicación en Producción y Dominios Personalizados

Esta tienda está arquitecturada para ser agnóstica de la nube. Aunque puedes subirla instantáneamente a plataformas "Serverless" como **Vercel** (gracias al archivo `vercel.json` autoincluido), el software funcionará impecablemente en cualquier servidor tradicional moderno (Render, Heroku, AWS, Hostinger, DigitalOcean, etc).

Si decides subir el código a otro proveedor o vincular tu **propio nombre de dominio** (ej: `mitienda.com`), únicamente debes autorizar el tráfico modificando tu archivo `.env`:

1.  Abre el archivo `.env`.
2.  Busca la declaración de `ALLOWED_HOSTS`.
3.  Escribe tu nuevo dominio separado por comas (sin el `https://`):
    ```env
    ALLOWED_HOSTS=mitienda.com,www.mitienda.com,127.0.0.1
    ```
*Por qué hacemos esto:* Es un protocolo de ciberseguridad exigido por el robusto núcleo de Django que previene ataques severos como el *Host Header Poisoning*. Al listar tu dominio ahí, ¡tu tienda quedará sellada, protegida y operativa bajo tu propia marca en todo el mundo!

---
**Nota:** Por diseño para desarrollo ágil, tu instalación local arranca predefinida usando la base de datos `db.sqlite3`. Cuando subas a entornos de Producción (como Vercel o Render), simplemente inyecta una variable llamada `DATABASE_URL` en tu servidor y Django la conectará al instante a bases de datos ultrarrápidas de PostgreSQL en la nube, sin tener que borrar ninguna línea de código.
