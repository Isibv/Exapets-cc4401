# ExaPets

Aplicación web para la gestión del historial de salud y cuidados de mascotas.

Proyecto desarrollado para **CC4401 - Ingeniería de Software**, Universidad de Chile.

## Sprint 1

El objetivo inicial es implementar una primera versión que permita gestionar mascotas y centralizar información básica de salud, incluyendo vacunas, antecedentes y exámenes, medicamentos y tratamientos, y próximas fechas relevantes.

## Equipo

Equipo de 6 integrantes.

> Este repositorio se está preparando de forma temporal antes de migrar el trabajo al repositorio oficial del curso.

## Configuración del entorno local

### 1. Clonar el repositorio

```bash
git clone https://github.com/Isibv/Exapets-cc4401.git
cd Exapets-cc4401
```

### 2. Crear y activar el entorno virtual

En Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

En macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar las dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar las variables de entorno

Crear un archivo `.env` en la raíz del proyecto, junto a `manage.py`.

Solicitar la `SECRET_KEY` a un administrador del repositorio y configurar:

```text
SECRET_KEY=la_clave_que_te_envien
DEBUG=True
```

El archivo `.env` no debe subirse al repositorio.

### 5. Aplicar las migraciones

```bash
python manage.py migrate
```

Esto creará la base de datos local `db.sqlite3`.

Opcionalmente, se puede crear un usuario administrador:

```bash
python manage.py createsuperuser
```

### 6. Iniciar el servidor

```bash
python manage.py runserver
```