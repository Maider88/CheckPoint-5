#CheckPoint 5

##***¿Qué es un condicional?***

Los condicionales en Python, son una estructura de control esencial al momento de programar y aprender a programar. Tanto Python como la mayoría de los lenguajes de programación utilizados actualmente, nos permiten hacer uso de estas estructuras para definir ciertas acciones y decisiones específicas en nuestros programas. Un condicional, permite establecer una serie de condiciones al interior de nuestro programa, que nos ayudan a determinar qué acciones llevar a cabo dadas ciertas circunstancias. Básicamente, tomar decisiones. Por ejemplo, si queremos decidir cuándo dar acceso a un usuario, dependiendo de si el nombre de usuario y contraseña son correctos. En ese caso, un condicional, nos permite verificar si se cumple la condición de que el usuario y la contraseña ingresados sean lo que esperamos; y de acuerdo a que se cumpla o no, ejecutar ciertas acciones. Los condicionales aumentan la "expresividad" de un programa, es decir, nos permiten considerar diferentes situaciones con antelación, permitiendo sortear diferentes tipos de situaciones que son del interés de nuestra aplicación.

Existen diferentes tipos de condicionales, cada uno tiene una utilidad y funcionalidad diferente. Cada uno considera diferentes situaciones que se pueden llegar a presentar durante la ejecución de un programa. Depende entonces del conocimiento que tengamos acerca de cada uno de los condicionales saber determinar correctamente cuando es necesario usar uno u otro. Tenemos a nuestra disposición los siguientes tipos de condicionales en Python:


- Condicional If en Python


- Condicional if-else en Python  

Como puedes ver, hay diferentes tipos de condicionales en Python y, como indiqué anteriormente, cada uno de estos condicionales tiene ciertas características que lo hacen útil para momentos específicos, a lo largo de los contenidos de esta sección veremos cada uno de estos al detalle, aprendiendo durante el proceso los componentes de un condicional, sintaxis de los condicionales y esas características particulares que permiten decidir cuál usar y en qué momento. 


###Condicional if

Básicamente, un condicional if en Python, es una estructura que nos posibilita definir las acciones a ejecutar si se cumple cierta condición y de ese modo modificar la ejecución de tareas en un programa según lo necesites.


`if user, password = Correct `  

Si es yes, nos dirá; `let into the site` de lo contrario, si es no; `not auth`,y podríamos decirle; Register?
  

Otro ejemplo podría ser:
    
    age = 25  
    if age <25:  
    	print(f" I'm sorry, you need to be al least 25 years old")  

Eso no ejecutaría nada porque hemos establecido 25 años, pero si ponemos ;

    age = 15  
    if age <25:  
    	print(f" I'm sorry, you need to be al least 25 years old")  


###Condicional if-else

Los condicionales if else, son una estructura de control que nos permite tomar cierta decisión al interior de nuestro programa. Es decir, nos permite determinar qué acciones tomar dada o no cierta condición. Es importante notar la parte del NO, pues ya no solo definimos qué hacer en caso de que se cumpla, sino también qué hacer si no se cumple cierta condición. 

Se les conoce también como estructuras selectivas de casos dobles (porque definen ambas posibilidades en la ejecución --si se cumple y si no se cumple --). 

Otro ejemplo podría ser;

    age = 55  
    if age <25:  
    	print(f" I'm sorry, you need to be al least 25 years old")  
    else:  
    	print(f"You're good to go,{age} fits in the range to rent a car.")  

###Condicionales anidados

Los condicionales, permiten escribir código en su interior y en realidad, nada de impide incluso al interior de un condicional, poner otros (u otros). A eso se le llama condiciones anidados, pues una estructura condicional dentro de otra. De hecho, puedes anidar cuantos condicionales requieras, aunque no se recomienda más de dos o tres niveles.

Dentro de un condicional, puedes poner cualquier instrucción válida y eso incluye a cualquier tipo de condicional que necesites y el funcionamiento, sigue siendo el mismo. De hecho, Python tiene una instrucción llamada elif() que permite simplificar un if() que se encuentra al interior de un else en Python.

    password = input('Ingrese la contraseña: ')  
    if (len(password) >= 8):
    	print('Tu contraseña es suficientemente larga.')
    
    	if(password == 'miClaveSegura'):  
    		print("Además es la contraseña correcta.") 
     	else:  
    		print("Pero es incorrecta.")  
    else:  
    	print('Tu contraseña es muy corta e insegura.')  
    		if (password != 'miClaveSegura'):  
    			print('Además, es incorrecta (por supuesto') 


###Operadores condicionales de Python

 >== Igual a   
 != Diferente a  
 <> Expresa inequalidad pero está obsoleto  
 \> Mayor que  
 \>= Mayor o igual que  
 < Menor que  
 <= Menor o igual que  

Los últimos cuatro operadores no podrán utilizarse para strings.

###Condicionales compuestos

Los condicionales compuestos consisten en condiciones múltiples dentro de una clave if. La sintaxis consiste en unir las condiciones mediante las palabras clave and (ambas condiciones deben cumplirse) u or (basta con que se cumpla solo una de las condiciones).


    username = "jonsnow"  
    email = jon@snow.com  
    password = "thenorth"
    if username =="jonsnow" and password == "thenorth":`  
    	print("Access permitted")  
    else:  
    	print("You shall not pass") 
 
>En ese código lo que decimos es que si el nombre de usuario y la contraseña coincide tiene el acceso permitido de lo contrario no pasaras.

Otra forma de ponerlo es;
        
    if username =="jonsnow" or password == "thenorth":  
       	print("Access permitted")  
    else:  
    	print("you shall not pass")  

>Hay decimos que si el usuario es jonsnow o la contraseña es thenorth tiene el acceso permitido de lo contrario no pasaras.


##***¿Cuáles son los diferentes tipos de bucles en Python? ¿Por qué son útiles?***  

Los ciclos, también conocidos como bucles o estructuras de control repetitivas, son de total importancia para el proceso de creación de un programa. Un ciclo en Python o bucle en Python (como prefieras llamarlos) te permite repetir una o varias instrucciones cuantas veces lo necesitemos, por ejemplo, si quisiéramos escribir los números del uno al cien no tendría sentido escribir cien líneas de código mostrando un número en cada una, para eso y para varias cosas más (que veremos enseguida), es útil un ciclo. Un ciclo nos ayuda a llevar a cabo una tarea repetitiva en una cantidad de líneas muy pequeña y de forma prácticamente automática (y muy rápida).

Hay dos tipos deferentes de bucles en Python. Los dos tipos de bucles son for-in y while, ambos se pueden usar para iterar colecciones, un rango de números, listas o cualquier cosa así.

Nota: Si vienes de algún otro lenguaje de programación y te lo preguntas: NO, en Python no existe el ciclo do-while. De hecho, no lo necesitas.

###For-in

Los ciclos for (o ciclos para) son una estructura de control cíclica. Nos permiten ejecutar una o varias líneas de código de forma iterativa (o repetitiva), pero teniendo cierto control y conocimiento sobre las iteraciones. En el ciclo for en Python, es necesario tener un valor inicial y un valor final, y opcionalmente podemos hacer uso del tamaño del "paso" entre cada "giro" o iteración del ciclo.

En resumen, un ciclo for en Python es una estructura iterativa para ejecutar un mismo segmento de código una cantidad de veces deseada y conocida. Pues necesitamos conoces previamente un valor de inicio, un tamaño de paso y un valor final para el ciclo.

    
    for num in [1, 2, 3, 4, 5]:
     
    	print(num)  

###While

 No es tan inteligente como for-in, continuara tantas veces como queramos. Aunque haya 5000 elementos while seguirá ejecutándose y si no lo implementamos correctamente nos toparemos con un bucle infinito y con el tiempo el pc o servidor fallará, le tendremos que decir cuando parar.

    nums = list(range(1,100))  
    while len(nums)>0:  
    	print(nums.pop())  

>Y eso nos hará una lista del 99 al 1.

###Break

Como su nombre lo indica, esta instrucción permitirá "romper" o básicamente detener cualquier ciclo en el que se encuentre una vez es ejecutada. Como siempre, una forma de comprenderla será con un ejemplo.


    usernames =["Jon", "Tyrion", "Theon", "Cersei", "Sansa",]
    
    for username in usernames:  
    	if username == "Cersei":  
    		print(f'{username} was found al index {username.index(username)}')   
    		break`  
    	print(username)

>Esto imprimiría Jon, Tyrion, Theon y al llegar a Cersei nos diría; Cersei was found al index 3. Y hay se detendría porque lo habría encontrado.



##***¿Qué es una lista por comprensión en Python?***

Las listas comprensivas de Python, podemos configurar una serie de for en bucles para funcionar en una sola linea y en realidad podemos generar listas a partir de esas lineas de código. Es una lista de bucles for y condicionales que se pueden colocar todos dentro de una sola linea de código.

    num_list = range(1,11)  
    cubed_nums = [num **3 for num in nums_list]  
    print(list(num:list))
 
>Esto nos imprimiría del 1 al 10 [1,2,3,4,5,6,7,8,9,10]. 
 
`print(cubed_nums)`  

>Y esto nos imprimiría la lista al cubo [1,8,27,64,125,216,343,512,729,1000]. 


![Listas de comprensión](https://codigospython.com/wp-content/uploads/2023/10/listas-por-comprension-en-python-explicacion-y-ejemplos.png)

###Ventajas

Las listas por comprensión ofrecen una serie de ventajas sobre las formas tradicionales de crear listas:

Son más concisas y fáciles de leer.
Permiten crear listas de forma más eficiente.
Son más flexibles y permiten crear listas con condiciones y operaciones complejas.

###Desventajas

Las listas por comprensión pueden ser difíciles de entender para los principiantes. Además, pueden ser menos eficientes que las formas tradicionales de crear listas en algunos casos.

###Conclusión

Las listas por comprensión son una herramienta poderosa que puede utilizarse para crear listas de forma concisa y eficiente. Son una parte esencial de la sintaxis de Python y son utilizadas por desarrolladores experimentados en todo el mundo.

###Errores

Si intentamos ejecutar la comprensión de listas y se nos olvida envolver el código entre corchetes [], Python nos indicará un error de sintaxis.

Por otro lado, debemos destacar que hay que tener cuidado con su uso, ya que las compresiones muy largas pueden ser muy difíciles de leer.

##***¿Qué es un argumento en Python?***

###Argumentos de funciones

Antes de entrar a explicar el tema, hagamos un repaso de lo que son las funciones en Python. Una función es un bloque de líneas de código o un conjunto de instrucciones cuya finalidad es realizar una tarea específica. Puede reutilizarse a voluntad para repetir dicha tarea. Una función tiene tres componentes, un input, los procesos, y el output.

El input consiste en los argumentos o parámetros de la función, en a que podemos proporcionarle datos para que los procesos se realicen en base a ellos.

Existen funciones que no tienen argumentos, y por lo tanto no requieren un input para ser ejecutadas. Por ejemplo:
Argumento por defecto(Invitado en página)
    
    def greeting(name = "Guest"):  
    	print(f" Hi {name}!")  
    greeting()  
    greeting("Kristine")

Esto nos imprimiría; Hi Guest! Hi Kristine!

###¿Argumentos o parámetros?

Los términos parámetro y argumento son utilizados para el mismo concepto: información que se pasa a una función.

Desde la perspectiva de una función:



- Un parámetro es la variable que aparece entre paréntesis en la definición de la función.


- Un argumento es el valor que se envía a la función cuando ésta es llamada.

###Errores de argumentos

    def some_fuction(collection=[])  
    	collection.append(1)  
    	return collection   
    print(some_fuction())


>Esto nos imprimiría [1]

En otra parte del programa si lo volveríamos ha sacar;

    	print(some_fuction())

>Nos imprimiría [1,1], pues se duplican porque tienen el mismo id los dos aunque este en otro lado del programa.

###Argumentos por defecto

Como hemos visto antes, llamar una función sin los argumentos requeridos nos dará un error.

Sin embargo, puede ser que deseemos que una función se ejecute incluso si no pasamos el argumento. Para esto podemos tener un valor por defecto para nuestros argumentos. La sintáxis es la siguiente, en la que el valor por defecto será Brian.

    def praise(name = 'Brian'):  
    	print(f"Bless {name}")
    
    praise("the cheesemakers")  
    Bless the cheesemakers
    praise()  
    Bless Brian  

Así, si pasamos un valor al llamar a la función, se tomará este nuevo valor. Si no pasamos ninguno, tomará el argumento por defecto.

###**Args y kwars**

####Uso de *args

Con los *args en Python, podemos definir funciones cuyo número de argumentos es variable. A esto también se le conoce como unpacking de argumentos.

La sintaxis consiste en añadir *args como argumento al definir la función. El uso de este término es una convención general, pero el código se ejecutará si en lugar de args se usa otra palabra.

En el ejemplo a continuación usamos la interpolación de strings junto con la función join() para imprimir todos los posibles argumentos, separados por una coma y un espacio:

    def greeting(*args)  
    	print("Hi"'+ ' '.join(args))
    
    greeting("Tiffany", "Hudgens")  

>Esto nos diría Hi Tiffany Hudgens.

####Uso de kwargs


A diferencia de *args, los **kwargs nos permiten dar un nombre a cada argumento de entrada, pudiendo acceder a ellos dentro de la función a través de un diccionario.

Como en el caso de args, la palabra kwargs es tan solo una convención.

Veamos en el siguiente ejemplo como en la definición de la función estamos proporcionando una key con sintaxis de diccionario, y al llamar la función especificamos los valores de estas keys.

    

    def greeting(**kwargs):  
    	if kwargs:  
    		print(f"Hi {kwargs["first_name"]} {kwargs[last_name]} have a great day!")
    	else:  
    		print(f"Hi Guest, have a great day!")
    
    greeting(first_name = "Kristine", last_name ="Hudgens")  
    greeting()

  


##***¿Qué es una función Lambda en Python?***


Cuando trabajamos con Lambdas podemos empaquetar un comportamiento, en general un comportamiento chico, y luego introducirlo en otras funciones. Son móviles y fáciles de usar. Es muy similar a una variable.



####Sintaxis básica;
    
    lambda arguments: expression

####La función lambda;
    
    full_name = lambda first, last: f'{first} {last}'  

####Equivalente a la siguiente función;

    
    def greeting(name):  
    --print (f"Hi there{name}")
    
    greeting(full_name('Tiffany', 'Hudgens'))

>Y esto nos imprimira Hi there Tiffany Hudgens

###¿Cómo usarlas?

Una función básica de las funciones lambda es poder almacenar su resultado en una variable, para luego poder usarla en otros puntos del programa.

De hecho, al guardarla en una variable podemos posteriormente tratarla como una función normal y llamarla con los arguments:

    sum = lambda num1, num2: num1 + num2
    
    print(suma(3,5))

>Esto nos imprime 8.

###Usarla dentro de una función

Podemos usar una función lambda dentro de la definición de otra función. En el siguiente ejemplo usamos la función reduce de functools. Esta función toma dos argumentos, una función lambda y una colección, ejecuta la suma definida en la función lambda con los dos primeros elementos, y hace la misma operación con el resultado y el tercer elemento:

    import functools
    
    my_list = [1,2,3]
    
    def cumulative_sum(list):
      return functools.reduce((lambda num1, num2: num1 + num2), list)
    
    
    print(cumulative_sum(my_list))

>Esto nos imprime 6.

  
##***¿Qué es un paquete pip?***

Un paquete pip en Python se refiere a un paquete o librería que se puede instalar y gestionar mediante pip, el instalador de paquetes oficial de Python.

Dentro de esto hay una cantidad enorme de librerías.

-Aprendizaje automático.  
-Estructura de datos.  
-Flask.  
-Django.  

Para poder introducir esos datos necesitamos que haya una conexión. El conector se llama "pip", el cual nos dará una conexión directa para toda esta base de datos. Luego simplemente es instalar las librerías en nuestro sistema e introducirlas igual.

####Como instalar Pip

Para instalar PIP, debemos seguir las instrucciones del siguiente enlace:

[Instalar paquete pip] <https://pip.pypa.io/en/stable/installation/>

Tal y como se indica, PIP estará automáticamente instalado si estas trabajando en un entorno virtual, utilizando Python descargado desde python.org o utilizando Python que no haya sido modificado por un redistribuidor para eliminar ensurepip.

Si no tienes PIP instalado, existen dos mecanismos apoyados directamente por los mantenedores de PIP, hacerlo mediante el módulo ensurepip o mediante el script get-pip.py.

Lo recomendable será comprobar primero que tengamos PIP instalado, y si no, elegir el método que prefiramos y seguir las indicaciones del link arriba mencionado.

####Comprobar si esta instalado

Es muy fácil simplemente tenéis que ejecutar el siguiente código en la línea de comando:

    pip –version



####Python Package Index (PyPI)

PyPI o the Python Package Index es una herramienta de Python que funciona como un centro de paquetes de dependencias y otras herramientas para Python.

La URL por la que se accede es la siguiente:

<http://pypi.org/>

PyPI te perminte también tener una cuenta de usuario para poder agregar nuevos paquetes, buscarlos o guardarlos para utilizarlos en tus programas.

- Para instalar un paquete;
	Para instalar un paquete podemos acceder a <http://pypi.org/> e introducir en el buscador el nombre del paquete. Para instalarlo debemos simplemente pegar la línea de código en la línea de comando:

    
    `pip install numpy`



- Usar los paquetes;primero deberás importarlo en la parte superior de tu código.

>Ponemos, por ejemplo;

    python
    import numpy as np
    num_range = np.arange(16)
    num_range

>Esto nos ejecuta : 

    array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])

>Y seguimos;

    num_range.reshape(4,4)

>Y ejecuta lo siguiente:

    array([[0,1,2,3],
    	   [4,5,6,7],
    	   [8,9,10,11]
    	   [12,13,14,15]])


####Desinstalar un paquete

Para desinstalar un paquete, simplemente podemos teclar pip uninstall seguido del nombre del paquete en la línea de comando, y responder a las preguntas Y/N que nos hace. Para desinstalar numpy deberíamos introducir la siguiente línea:

    pip uninstall numpy


#Fuentes

<https://basque.devcamp.com/pt-full-stack-development-javascript-python-react/guide/>  
<https://ellibrodepython.com/>  
<https://codigospython.com/>  
<https://wiki.python.org/moin/CheeseShop>  
<https://pip.pypa.io/en/stable/installation/>  
<http://pypi.org/>





