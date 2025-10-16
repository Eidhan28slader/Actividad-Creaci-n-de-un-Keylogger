import keyboard

def saca(event):
    with open("salida.txt", "a") as file:
         file.write(f"{event.name}")

keyboard.on_press(saca)
keyboard.wait(".")