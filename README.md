# Humberto's Negotiation Project

Esta aplicación es una herramienta de despliegue para el Test de Thomas-Kilmann, construida sobre **Streamlit** y conectada a una base de datos **PostgreSQL en Supabase**.

## Arquitectura Técnica

### 1. Conexión a Base de Datos

La aplicación utiliza `psycopg2` para establecer conexiones con PostgreSQL. Se utiliza un **Session Pooler** para evitar problemas de compatibilidad de red entre entornos IPv4/IPv6.

* **Función clave:** `get_db_connection()` utiliza credenciales inyectadas mediante `st.secrets`.
* **Configuración de red:** Se utiliza el puerto **6543** (Transaction Pooler) en lugar del 5432 estándar.

### 2. Lógica de Persistencia

* **Insertions:** Los datos se registran mediante comandos SQL parametrizados (`%s`), evitando inyecciones SQL. Las columnas se envuelven en comillas dobles (`" "`) para asegurar que el motor de PostgreSQL respete la nomenclatura de las columnas (ej: `"Fecha"`, `"Nombre"`).
* **Queries:** La lectura de datos se realiza mediante `pd.read_sql_query`, permitiendo cargar los resultados directamente en estructuras de datos (`DataFrames`) de `pandas`.

### 3. Componentes de Interfaz

* **Navegación:** Gestión de estado mediante `st.radio` y `st.tabs`.
* **Validación:** El cuestionario utiliza `st.form` y `st.session_state` para verificar la completitud de las respuestas (`sin_responder`) antes de habilitar el botón de envío.
* **Visualización:** Integración con `Plotly` para generar gráficos de barras y diagramas polares basados en los datos procesados del `DataFrame`.

## Configuración del Entorno (Variables de Entorno)

La aplicación requiere un archivo `secrets.toml` ubicado en el directorio `.streamlit/` con la siguiente estructura:

```toml
DB_HOST = "tu-host.supabase.co"
DB_NAME = "nombre-base-datos"
DB_USER = "usuario-db"
DB_PASSWORD = "password-db"

```

## Protocolos de Seguridad

* **Ignorancia de archivos:** El archivo `.gitignore` excluye explícitamente `.streamlit/secrets.toml`, directorios de entorno virtual (`.venv/`), cachés de compilación (`__pycache__/`) y archivos de sistema.

---
Gracias al apoyo de Google Gemini y la documentación de streamlit.
