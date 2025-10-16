
We need to copy the code in VS code and see the result in the folder salida.txt
and we can see that the program can excute in any place of the computer

En mi codigo primero importamos la libreria con  "import keyboard"
Despues de eso creamos una funcion saca que va a tener un evento 
despues ponemos "with open("salida.txt", "a") as file:" para creaar una carpeta llamada "salida.txt" y agregue todo el contenido
luego usamos este codigo "file.write(f"{event.name}")" para que todo el contenido que hagamos (las teclas presionadas) se guarden en el nombre del evento el cual es Keyboard
Despues de eso ingresamos los dos ultimos comandos:
keyboard.on_press(saca), este comando sirve para que cada tecla qe presionemos se guarde en la funcion
keyboard.wait("."), el programa terminara cuando se presione la tecla "."
