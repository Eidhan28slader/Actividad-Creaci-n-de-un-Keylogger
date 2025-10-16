
We need to copy the code in VS code and see the result in the folder salida.txt
and we can see that the program can excute in any place of the computer

In my code, we first import the library with “import keyboard.”
After that, we create a function that will have an event. 
Then we put “with open(‘output.txt’, ‘a’) as file:” to create a folder called “output.txt” and add all the content.
Then we use this code “file.write(f”{event.name}“)” so that all the content we create (the keys pressed) is saved in the name of the event, which is Keyboard
After that, we enter the last two commands:
keyboard.on_press(saca), this command is used so that each key we press is saved in the function
keyboard.wait(“.”), the program will end when the “.” key is pressed
