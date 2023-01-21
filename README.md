# movie-FastAPI

## Flujo de autenticación

### Ruta para iniciar sesión
Se obtiene como resultado la protección de determinadas rutas de la aplicación para las cuales solo se podrá acceder mediante el inicio de sesión del usuario. Para esto se crea una ruta que utilice el método POST donde se solicitarán los datos como email y contraseña.

### Creación y envío de token
Luego de que el usuario ingrese sus datos de sesión correctos este obtendrá un token que le servirá para enviarlo al momento de hacer una petición a una ruta protegida.

### Validación de token
Al momento de que la API reciba la petición del usuario, comprobará que este le haya enviado el token y validará si es correcto y le pertenece. Finalmente, se le dará acceso a la ruta que está solicitando.

Se utiliza la librería pyjwt.
