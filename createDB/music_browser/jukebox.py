import sqlite3
try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

conn = sqlite3.connect("music.sqlite")

mainWindow = tkinter.Tk()
mainWindow.title("Music DB Browser")
mainWindow.geometry("1024x768")

mainWindow.columnconfigure(0, weight=2)
mainWindow.columnconfigure(1, weight=2)
mainWindow.columnconfigure(2, weight=2)
mainWindow.columnconfigure(3, weight=1)  # spacer column on right

mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=5)
mainWindow.rowconfigure(2, weight=5)
mainWindow.rowconfigure(3, weight=1)

# Labels
tkinter.Label(mainWindow, text="Artists").grid(row=0, column=0)
tkinter.Label(mainWindow, text="Albums").grid(row=0, column=1)
tkinter.Label(mainWindow, text="Songs").grid(row=0, column=2)

# Artists Listbox
artistList = tkinter.Listbox(mainWindow)
artistList.grid(row=1, column=0, sticky="NSEW", rowspan=2, padx=(30, 0))
artistList.config(border=2, relief='sunken')

# Scrollbar
artistScroll = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=artistList.yview)
artistScroll.grid(row=1, column=0, sticky="NSE", rowspan=2)
artistList['yscrollcommand'] = artistScroll.set


# Albums Listbox
albumLV = tkinter.Variable(mainWindow)
albumLV.set(("Choose an artist",))
albumList = tkinter.Listbox(mainWindow, listvariable=albumLV)
albumList.grid(row=1, column=1, sticky="NSEW", padx=(30,0))
albumList.config(border=2, relief='sunken')

# Scrollbar
albumScroll = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=albumList.yview)
albumScroll.grid(row=1, column=1, sticky="NSE", rowspan=2)
albumList['yscrollcommand'] = albumScroll.set

# Song Listbox
songLV = tkinter.Variable(mainWindow)
songLV.set(("Choose and album",))
songList = tkinter.Listbox(mainWindow, listvariable=songLV)
songList.grid(row=1, column=2, sticky="NSEW", padx=(30, 0))
songList.config(border=2, relief='sunken')

# Main loop
testList = range(0,100)
albumLV.set(tuple(testList))
# albumLV.set((1, 2, 3, 4, 5))
mainWindow.mainloop()
print("Closing database connection")
conn.close()
