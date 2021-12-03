Característica: Como usuario me gustaría registar un nuevo usuario.

    Escenario: Datos de registro correctos.
        Dado que ingreso a la url "http://192.168.33.10:8000/usuarios/lista"
        Y presiono el botón "Nuevo"
        Y capturo el nombre "Josue" 
        Y capturo el primer apellido "Gonzalez" 
        Y capturo el segundo apellido "Pinedo"
        Y capturo el usuario "jozuelenuv"
        Y capturar la contraseña "jozue123"
        Cuando presiono el botón "Guardar"
        Entonces puedo ver al usuario "jozuelenuv" en la lista de usuarios.

    Escenario: Datos de registro correctos sin el segundo apellido.
        Dado que ingreso a la url "http://192.168.33.10:8000/usuarios/lista"
        Y presiono el botón "Nuevo"
        Y capturo el nombre "Josue" 
        Y capturo el primer apellido "Gonzalez" 
        Y capturo el usuario "jozuelenuv_1"
        Y capturar la contraseña "jozue123"
        Cuando presiono el botón "Guardar"
        Entonces puedo ver al usuario "jozuelenuv_1" en la lista de usuarios.

    Escenario: Datos de registro con un usuario que ya existe en el sistema.
        Dado que ingreso a la url "http://192.168.33.10:8000/usuarios/lista"
        Y presiono el botón "Nuevo"
        Y capturo el nombre "Josue" 
        Y capturo el primer apellido "Gonzalez" 
        Y capturo el segundo apellido "Pinedo"
        Y capturo el usuario "jozuelenuv"
        Y capturar la contraseña "jozue123"
        Cuando presiono el botón "Guardar"
        Entonces puedo ver el mensaje "A user with that username already exists."

    Escenario: Datos de registro con nombre alfanumérico y con caracteres especiales.
        Dado que ingreso a la url "http://192.168.33.10:8000/usuarios/lista"
        Y presiono el botón "Nuevo"
        Y capturo el nombre "Josue_432" 
        Y capturo el primer apellido "Gonzalez" 
        Y capturo el segundo apellido "Pinedo"
        Y capturo el usuario "jozuelenuv_2"
        Y capturar la contraseña "jozue123"
        Cuando presiono el botón "Guardar"
        Entonces puedo ver el mensaje "El nombre debe contener solamente letras del alfabeto latino"

    Escenario: Datos de registro con primer apellido alfanumérico y con caracteres especiales.
        Dado que ingreso a la url "http://192.168.33.10:8000/usuarios/lista"
        Y presiono el botón "Nuevo"
        Y capturo el nombre "Josue" 
        Y capturo el primer apellido "123Gonzalez%$12" 
        Y capturo el segundo apellido "Pinedo"
        Y capturo el usuario "jozuelenuv_3"
        Y capturar la contraseña "jozue123"
        Cuando presiono el botón "Guardar"
        Entonces puedo ver el mensaje "El apellido debe contener solamente letras del alfabeto latino"

    Escenario: Datos de registro con segundo apellido alfanumérico y con caracteres especiales.
        Dado que ingreso a la url "http://192.168.33.10:8000/usuarios/lista"
        Y presiono el botón "Nuevo"
        Y capturo el nombre "Josue" 
        Y capturo el primer apellido "Gonzalez" 
        Y capturo el segundo apellido "_:Pinedo54354"
        Y capturo el usuario "jozuelenuv_4"
        Y capturar la contraseña "jozue123"
        Cuando presiono el botón "Guardar"
        Entonces puedo ver el mensaje "El apellido debe contener solamente letras del alfabeto latino"

    Escenario: Datos de registro con usuario con espacios.
        Dado que ingreso a la url "http://192.168.33.10:8000/usuarios/lista"
        Y presiono el botón "Nuevo"
        Y capturo el nombre "Josue" 
        Y capturo el primer apellido "Gonzalez" 
        Y capturo el segundo apellido "Pinedo"
        Y capturo el usuario "jozue lenuv"
        Y capturar la contraseña "jozue123"
        Cuando presiono el botón "Guardar"
        Entonces puedo ver el mensaje "El usuario no debe contener espacios"

    Escenario: Datos de registro sin el Nombre
        Dado que ingreso a la url "http://192.168.33.10:8000/usuarios/lista"
        Y presiono el botón "Nuevo"
        Y capturo el primer apellido "Gonzalez" 
        Y capturo el segundo apellido "Pinedo"
        Y capturo el usuario "jozuelenuv_6"
        Y capturar la contraseña "jozue123"
        Cuando presiono el botón "Guardar"
        Entonces puedo ver el mensaje "Completa este campo"

    Escenario: Datos de registro sin el primer apellido
        Dado que ingreso a la url "http://192.168.33.10:8000/usuarios/lista"
        Y presiono el botón "Nuevo"
        Y capturo el nombre "Josue" 
        Y capturo el segundo apellido "Pinedo"
        Y capturo el usuario "jozuelenuv_7"
        Y capturar la contraseña "jozue123"
        Cuando presiono el botón "Guardar"
        Entonces puedo ver el mensaje "Completa este campo"

    Escenario: Datos de registro sin el usuario  
        Dado que ingreso a la url "http://192.168.33.10:8000/usuarios/lista"
        Y presiono el botón "Nuevo"
        Y capturo el nombre "Josue" 
        Y capturo el primer apellido "Gonzalez" 
        Y capturo el segundo apellido "Pinedo"
        Y capturar la contraseña "jozue123"
        Cuando presiono el botón "Guardar"
        Entonces puedo ver el mensaje "Completa este campo"
