# Tutorial-Flask
Creación de una aplicación básica

Carpeta "flaskr" -> Fábrica de aplicaciones

/create y register: funcionan igual

Actualizacion - update y delete -> vistas (necesitarán obtener un post por id y comprobar si el autor coincide con el usuario conectado)

El archivo "tests/conftest.py" contiene funciones de configuración llamadas fixtures que cada prueba utilizará

GET = comunicación la base de datos+

-------------28/05
La sesión se guarda en la memoria, se pierde el logueo
"quiero que chequees esto antes de todo" -> @bp.before_app_request

cookies: información que el servidor guarda en el navegador
NO TENGO LA COOKIE y no puedo entrar logueado

El objeto g existe hasta yo devuelvo la página. Se hace cada vez antes de cada pedido

Borro de la base de datos a un usuario: en que queda g.user, que pasa con el usuario que vuelve a ingresar

¿Por que sigo logueado si borre la cookie? Hay que Recargar la página para ver cambios

fetchall devuelve en una lista, si no hay nada para devolver, devuelve una lista vacía (none)

Reutilizar ids borrado -> NO se vuelven a usar porque puede generar fallas

Como se combina?

ENTENDER MECANISMOS 