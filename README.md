# Desarrollo de Aplicaciones Web

Para lograr entender que se hizo en esta tarea, tambien añadire las consideraciones que se tuvo en las anteriores partes.

# Tarea 1
Aca dare una breve explicacion de porque se hicieron algunas cosas y algunos detalles.

En todos los html a excepcion del indice, se creo una navbar, donde aparece el logo de los juegos y un boton la volver al inicio, ademas en informacion artesano e informacion hincha se agrego un boton para volver a su respectiva lista

Se cambio el formato de "comentario adicionales" a una textarea, ya que hace mayor sentido con el tipo de mensaje que se entregan aca, pero se mantiene el largo maximo que se pide por enunciado.

Para las validaciones se asumio lo siguiente


Nombres: Nombre + Apellido, se aceptan compuestos tambien y algunos carecteres de otros alfabetos

Email: se aceptan correos de la forma x@ug.uchile.cl (con mas de un punto despues del @)

Region: Si queda en la opcion Seleccione una Region, se considera que no se eligio nada

Comuna: Si queda en la opcion Seleccione una Comuna, se considera que no se eligio nada

Modo de transporte: Si queda en la opcion Elija su modo de transporte, se considera que no se eligio nada

Numero de Contacto: Se aceptan numeros que empiecen con "+" y que tengan 12 digitos o mas digitos 


# Tarea 2

## Consideraciones

1. Esta el archivo requirements.txt, donde se muestran lo que se uso para implementar la tarea

2. La navbar paso a ser una implementacion de cada html, a estar en base.html para asi poder extenderlo, ademas se cambio el css, para que la navbar tenga el suyo propio

3. La barra de paginacion tiene un error, que a pesar de que no quedan mas artesanos, se puede seguir avanzando, mostrando una tabla vacia

4. Las validaciones en .js se hacen cuando se apreta el boton registrar y las server-side se hacen al apretar el boton confirmar en el pop up

5. Cuando se registra un artesano y pasa las validaciones, sale un notificacion de la pagina, que impide que vuelva al inicio hasta que se cierre

6. informacion-artesano.html muestra que tiene un error, esto es porque tuve un problemas con las comillas, a pesar de esto funciona correctamente el enlace


## Base de datos

1. La base de dato se creo directamente en beekeeper studio, con las indicaciones que se dieron en el enunciado 

2. Los archivos subidos por el usuario, luego de la validacion, van a ./static/uploads, 

3. Se importo la funcion secure_file de werkzeug.utils y uuid, para poder insertar de manera segura y evitar nombres repetidos


# Tarea 3

## Consideraciones

1. En el apartado de estadisticas, se creo 2 botones, una para ver cada grafico, asi el usuario solo revisara el que le interese
2. Ademas se añadieron 2 botones en cada grafico, uno para volver y otro para actualizar los datos de la tabla
3. Informacion-artesano.html sigue mostrando que contiene un error, por usar multiple comillas, pero pareciera que es solo visual, no provoca ningun problema (si me dan un consejo para evitar esto se agradece)
4. Las validaciones en .js se hacen cuando se apreta el boton registrar y las server-side se hacen al apretar el boton confirmar en el pop up
5. Cuando se registra un artesano o hincha y pasa las validaciones, sale un notificacion de la pagina, que impide que vuelva al inicio hasta que se cierre (es poco practico, pero funciona)

## Validaciones

1. Se agrego validaciones para comuna y region, revisando si pertenecen a la base de datos, ademas de ver si la comuna elegica es de la region escogida
2. Para las validacion de server-side, se consideraron las mismas cosas que en las validaciones en .js

