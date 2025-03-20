import tkinter as tk
from tkinter import messagebox
from tkinter import ttk 
import sv_ttk
import sqlite3
import darkdetect
from addfunctions import *
from albums import *
from favartists import *
from podcasts import *

window = tk.Tk()
window.title("Musify")
window.configure(bg = "light blue")
# frame inside window
frame = tk.Frame(window)
frame.pack(expand=True )

#songs frame
songs_info = tk.LabelFrame(frame,bg = "light blue" ,text = "songs" )
songs_info.grid(row =0, column = 0, sticky= "news", padx = 20, pady = 10)
#songadd is new window of options
add_song = tk.Button(songs_info, text = "add songs",command = songadd)
add_song.grid(row = 0, column = 0)
view_song = tk.Button(songs_info, text = "view songs",command = view_songs)
view_song.grid(row = 0, column = 1)
delete_song = tk.Button(songs_info, text = "delete songs", command = delete)
delete_song.grid(row = 0, column = 2)

for widget in songs_info .winfo_children():
    widget.grid_configure(padx = 10, pady = 5)

#album frame
albums_info = tk.LabelFrame(frame, bg = "light blue", text = "albums")
albums_info.grid(row = 1, column = 0, sticky = "news", padx = 20, pady = 10)

add_album = tk.Button(albums_info, text = "add albums", command = albumadd)
add_album.grid(row = 0, column = 0)
view_album = tk.Button(albums_info, text = "view albums", command = view_albums)
view_album.grid(row = 0, column = 1)
delete_album = tk.Button(albums_info, text = "delete albums", command = delete_album)
delete_album.grid(row = 0, column = 2)


for widget in albums_info .winfo_children():
    widget.grid_configure(padx = 10, pady = 5)

#favorite artists
artists_info = tk.LabelFrame(frame, bg = "light blue",text = "favorite artists")
artists_info.grid(row = 2, column = 0,sticky = "news", padx = 20, pady = 10 )

add_artists = tk.Button(artists_info, text = "add favorite artists", command = favartists)
add_artists.grid(row=0, column = 0)
view_artists = tk.Button(artists_info, text = "view artists", command = view_fav_artists)
view_artists.grid(row = 0, column = 1)
delete_artists = tk.Button(artists_info, text = "delete artists", command = delete_fartists)
delete_artists.grid(row = 0 , column = 2)

for widget in artists_info .winfo_children():
    widget.grid_configure(padx = 10, pady = 5)

#podcasts
podcasts_info = tk.LabelFrame(frame,bg = "light blue", text = "podcasts")
podcasts_info.grid(row = 3, column = 0,sticky = "news", padx = 20, pady = 10 )

add_podcasts = tk.Button(podcasts_info, text = "add podcasts", command = podcasts)
add_podcasts.grid(row=0, column = 0)
view_podcasts = tk.Button(podcasts_info, text = "view podcasts", command = view_podcasts)
view_podcasts.grid(row = 0, column = 1)
delete_podcasts = tk.Button(podcasts_info, text = "delete podcasts", command = delete_podcasts)
delete_podcasts.grid(row = 0 , column = 2)

for widget in podcasts_info .winfo_children():
    widget.grid_configure(padx = 10, pady = 5)


window.mainloop()
