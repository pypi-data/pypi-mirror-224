**Instalar el proyecto**

- Para instalar todas las dependencias **poetry install**

**Arrancar el proyecto**

- Para arrancar el poyecto **poetry run py 'nombre_archivo'**
- Para arracar el servidor **poetry run uvicorn src.api:app --reload**, para accede a la documentación de la api **http://127.0.0.1:8000/docs**

**Gestion de dependencias**

- Para agregar una dependencia **poetry add 'nombre_paquete'**
- Para agregar una dependencia de desarrollo **poetry add 'nombre_paquete' --dev**
- Para desinstalar una dependencia **poetry remove 'nombre_paquete'**

**Debug**

- Para correr un archivo en modo post mortem **poetry run py -m pdbp 'nombre_archivo'**
- Para lanzar los test **poetry run pytest -v**
