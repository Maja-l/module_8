from pynput import keyboard

buffer = []

def on_press(key):
    try:
        if key.char:
            buffer.append(key.char)
    except AttributeError:
        if key == keyboard.Key.enter:
            print(f"Entered: {''.join(buffer)}")
            buffer.clear()
        elif key == keyboard.Key.space:
            buffer.append(' ')
        # Handle other special keys if needed

# Collect events until released
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
