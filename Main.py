import tkinter as tk
import threading
import pyautogui
import webbrowser

# === Configuration ===
SCROLL_AMOUNT = -5
SCROLL_AMOUNT_INCREASER = -5
SCROLL_AMOUNT_DECREASER = 5

# === State ===
scrolling = False
paused = False
scroll_amount = SCROLL_AMOUNT
scroll_thread = None

# === Scroll Logic ===
def scroll_loop():
    global scrolling, paused, scroll_amount
    while scrolling:
        if not paused:
            pyautogui.scroll(scroll_amount)

# === Button Commands ===
def start_scrolling():
    global scrolling, scroll_thread
    if not scrolling:
        scrolling = True
        scroll_thread = threading.Thread(target=scroll_loop, daemon=True)
        scroll_thread.start()

def pause_scrolling():
    global paused
    paused = True

def resume_scrolling():
    global paused
    paused = False

def increase_speed():
    global scroll_amount
    scroll_amount += SCROLL_AMOUNT_INCREASER
def decrease_speed():
    global scroll_amount
    scroll_amount += SCROLL_AMOUNT_DECREASER

def quit_app():
    global scrolling
    scrolling = False
    root.destroy()

def open_manga():
    # Enter Your Link
    url = url_entry.get()
    if url.strip():
        webbrowser.open(url)

# === GUI Setup ===
root = tk.Tk()
root.title("Manga Auto-Scroller")
root.geometry("300x400")
root.resizable(False, False)
root.configure(bg="#121212")

# url getting from user
url_label = tk.Label(root, text="Enter Manga URL:", fg="white", bg="#121212", font=("Segoe UI", 10))
url_label.pack(pady=(10, 0))

url_entry = tk.Entry(root, width=40)
url_entry.insert(0, "https://")  
url_entry.pack(pady=(0, 10))


# === Buttons ===
tk.Button(root, text="Open Manga", command=open_manga).pack(pady=5)
tk.Button(root, text="Start Scrolling", command=start_scrolling).pack(pady=5)
tk.Button(root, text="Pause", command=pause_scrolling).pack(pady=5)
tk.Button(root, text="Resume", command=resume_scrolling).pack(pady=5)
tk.Button(root, text="Increase Speed", command=increase_speed).pack(pady=5)
tk.Button(root, text="Decrease Speed", command=decrease_speed).pack(pady=5)
tk.Button(root, text="Quit", command=quit_app).pack(pady=5)

root.mainloop()
