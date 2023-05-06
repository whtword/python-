from pynput import keyboard

def on_press(key):
    print(f'{key} :pushed')


def on_release(key):
    if key == keyboard.Key.esc:
        return False


with keyboard.Listener(on_press=on_press, on_release=on_release) as lsn:
    lsn.join()