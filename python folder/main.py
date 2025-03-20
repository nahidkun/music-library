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

#album functions
def albumadd():
    root = tk.Toplevel()
    root.title("add albums section")

    Frame = tk.Frame(root)
    Frame.pack(padx = 20, pady = 20)
    
    album_add = tk.LabelFrame(Frame, text = "album details")
    album_add.grid(row = 0, column = 0, padx = 20, pady = 10)
#album name
    album_name_label = tk.Label(album_add, text = "name")
    album_name_label.grid(row = 0, column = 0)
    album_name_entry = tk.Entry(album_add)
    album_name_entry.grid(row = 1, column = 0)
#album artist
    album_artist_label = tk.Label(album_add, text = "artist")
    album_artist_label.grid(row = 0, column = 1)
    album_artist_entry = tk.Entry(album_add)
    album_artist_entry.grid(row = 1, column = 1)
#album release year
    album_rlsyr_label = tk.Label(album_add, text = "release year")
    album_rlsyr_label.grid(row = 0, column = 2)
    album_rlsyr_entry = tk.Entry(album_add)
    album_rlsyr_entry.grid(row = 1, column = 2)
#album genre
    album_genre_label = tk.Label(album_add, text = "genre")
    album_genre_label.grid(row = 0, column = 3)
    album_genre_entry = tk.Entry(album_add)
    album_genre_entry.grid(row = 1, column = 3)
#album track number
    album_tknr_label = tk.Label(album_add, text = "track number")
    album_tknr_label.grid(row = 0, column = 4)
    album_tknr_entry = tk.Entry(album_add)
    album_tknr_entry.grid(row = 1, column = 4)

    def submit_albums():

        album_name = album_name_entry.get()
        album_artist_name = album_artist_entry.get()
        album_rlsyr_data = album_rlsyr_entry.get()
        album_genre_name = album_genre_entry.get()
        album_tknr_name = album_tknr_entry.get()

        print("album name: ", album_name)
        print("artist name: ", album_artist_name)
        print("album release year: ", album_rlsyr_data)
        print("album genre: ", album_genre_name )
        print("album track number: ", album_tknr_name)

        connection = sqlite3.connect('musify.db')
        table_create_albums = '''CREATE TABLE IF NOT EXISTS Album_Table 
            (album_name TEXT, album_artist_name TEXT, album_rlsyr_data INT, album_genre_name TEXT, album_tknr_name INT)'''

        connection.execute(table_create_albums)

        data_insert_albums = '''INSERT INTO Album_Table 
            (album_name, album_artist_name, album_rlsyr_data, album_genre_name, album_tknr_name) VALUES 
                    (?, ?, ?, ?, ?)'''
        data_album_tuple = (album_name, album_artist_name, album_rlsyr_data, album_genre_name, album_tknr_name)
        cursor = connection.cursor()
        cursor.execute(data_insert_albums, data_album_tuple)
        connection.commit()
        connection.close()

    submitdata = tk.Button(Frame, text = "submit data", command = submit_albums)
    submitdata.grid(row = 1, column = 4)

def view_albums():
        root2 = tk.Toplevel()
        root2.title("view albums")

        Frame2 = tk.Frame(root2)
        Frame2.pack(padx = 20, pady= 10)

        columns = ("name", "artist", "release year", "genre", "track number")
        tree = ttk.Treeview(Frame2, columns=columns, show = "headings", height = 15)

        for col in columns:
             tree.heading(col, text=col)
             tree.column(col, anchor = "w", width = 130)
       
        tree.pack(side = "left", fill = "both", expand = True)
        #viewing songs
        connection = sqlite3.connect('musify.db')
        cursor = connection.cursor()
        data_view_album = '''SELECT album_name, album_artist_name, album_genre_name, album_rlsyr_data, album_tknr_name 
                            FROM Album_Table'''
        cursor.execute(data_view_album)
        all_album = cursor.fetchall()
        print(all_album) 
        for album in all_album:
             tree.insert("", "end", values = album)
        connection.close()

def delete_album_db(album_entry):
     album_name = album_entry.get()
     connection = sqlite3.connect('musify.db')
     cursor = connection.cursor()
     delete_albums_query = '''DELETE FROM Album_Table WHERE song_name = ?'''
     cursor.execute(delete_albums_query, (album_name,))
     connection.commit()
     print(f"song '{album_name}' was deleted successfully")
     connection.close()

def delete_album():  
     root3 = tk.Toplevel()
     root3.title("album deletion")

     Frame3 = tk.Frame(root3, padx = 20, pady = 20)
     Frame3.pack(padx = 20, pady = 20)

     del_album_label = tk.Label(Frame3, text = "write song name to delete")
     del_album_label.grid(row=0,column=0,pady=10)

     del_album_entry = tk.Entry(Frame3)
     del_album_entry.grid(row = 1, column = 0, pady = 10)

     data_deletion_album = tk.Button(Frame3, text = "delete", command=lambda: delete_album_db(del_album_entry))
     data_deletion_album.grid(row = 2, column = 0, pady=10)
#fav artists functions
def favartists():
    root = tk.Toplevel()
    root.title("add favorite artists section")

    Frame = tk.Frame(root)
    Frame.pack(padx = 20, pady = 20)
    
    fav_artists_add = tk.LabelFrame(Frame, text = "favorite artists details")
    fav_artists_add.grid(row = 0, column = 0, padx = 20, pady = 10)
#fav artists name
    fartist_name_label = tk.Label(fav_artists_add, text = "name")
    fartist_name_label.grid(row = 0, column = 0)
    fartist_name_entry = tk.Entry(fav_artists_add)
    fartist_name_entry.grid(row = 1, column = 0)
#fav artists genre
    fartist_genre_label = tk.Label(fav_artists_add, text = "genre")
    fartist_genre_label.grid(row = 0, column = 1)
    fartist_genre_entry = tk.Entry(fav_artists_add)
    fartist_genre_entry.grid(row = 1, column = 1)

    def submit_fav_artists():

        fav_artist_name = fartist_name_entry.get()
        fav_artist_genre = fartist_genre_entry.get()

        print("favorite artist name:", fav_artist_name)
        print("favorite artist genre:", fav_artist_genre)

        connection = sqlite3.connect('musify.db')
        table_create_fartists = '''CREATE TABLE IF NOT EXISTS Fav_Artists_Table 
            (fav_artist_name TEXT, fav_artist_genre TEXT)'''

        connection.execute(table_create_fartists)

        data_insert_fav_artists = '''INSERT INTO Fav_Artists_Table 
            (fav_artist_name, fav_artist_genre) VALUES 
                    (?, ?)'''
        data_fartists_tuple = (fav_artist_name, fav_artist_genre)
        cursor = connection.cursor()
        cursor.execute(data_insert_fav_artists, data_fartists_tuple)
        connection.commit()
        connection.close()

    submitdata = tk.Button(Frame, text = "submit data", command = submit_fav_artists)
    submitdata.grid(row = 1, column = 4)

def view_fav_artists():
    root2 = tk.Toplevel()
    root2.title("view favorite artists")

    Frame2 = tk.Frame(root2)
    Frame2.pack(padx = 20, pady= 10)

    columns = ("name", "genre")
    tree = ttk.Treeview(Frame2, columns=columns, show = "headings", height = 15)

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor = "w", width = 130)
       
    tree.pack(side = "left", fill = "both", expand = True)
        #viewing songs
    connection = sqlite3.connect('musify.db')
    cursor = connection.cursor()
    data_view_fav_artists = '''SELECT fav_artist_name, fav_artist_genre
                            FROM Fav_Artists_Table'''
    cursor.execute(data_view_fav_artists)
    all_favorite_artists = cursor.fetchall()
    print(all_favorite_artists) 
    for fav_artists_x in all_favorite_artists:
        tree.insert("", "end", values = fav_artists_x)
    connection.close()  

def delete_fav_artists_db(fav_artist_entry):
    fav_artist_name = fav_artist_entry.get()
    connection = sqlite3.connect('musify.db')
    cursor = connection.cursor()
    delete_fartists_query = '''DELETE FROM Fav_Artist_Table WHERE fav_artist_name = ?'''
    cursor.execute(delete_fartists_query, (fav_artist_name,))
    connection.commit()
    print(f"song '{fav_artist_name}' was deleted successfully")
    connection.close()

def delete_fartists():  
    root3 = tk.Toplevel()
    root3.title("fav artists deletion")

    Frame3 = tk.Frame(root3, padx = 20, pady = 20)
    Frame3.pack(padx = 20, pady = 20)

    del_fartists_label = tk.Label(Frame3, text = "write favorite artist name to delete")
    del_fartists_label.grid(row=0,column=0,pady=10)

    del_fartists_entry = tk.Entry(Frame3)
    del_fartists_entry.grid(row = 1, column = 0, pady = 10)

    data_deletion_fartists = tk.Button(Frame3, text = "delete", command=lambda: delete_fav_artists_db(del_fartists_entry))
    data_deletion_fartists.grid(row = 2, column = 0, pady=10)  
#podcasts functions
def podcasts():
    root = tk.Toplevel()
    root.title("add podcasts section")

    Frame = tk.Frame(root)
    Frame.pack(padx = 20, pady = 20)
    
    podcasts_add = tk.LabelFrame(Frame, text = "podcasts details")
    podcasts_add.grid(row = 0, column = 0, padx = 20, pady = 10)
#podcasts name
    podcasts_name_label = tk.Label(podcasts_add, text = "name")
    podcasts_name_label.grid(row = 0, column = 0)
    podcasts_name_entry = tk.Entry(podcasts_add)
    podcasts_name_entry.grid(row = 1, column = 0)
#podcasts theme
    podcasts_theme_label = tk.Label(podcasts_add, text = "theme")
    podcasts_theme_label.grid(row = 0, column = 1)
    podcasts_theme_entry = tk.Entry(podcasts_add)
    podcasts_theme_entry.grid(row = 1, column = 1)
#podcast host
    podcasts_host_label = tk.Label(podcasts_add, text = "host")
    podcasts_host_label.grid(row = 0, column = 2)
    podcasts_host_entry = tk.Entry(podcasts_add)
    podcasts_host_entry.grid(row = 1, column = 2)
#podcasts number of episodes
    podcasts_nreps_label = tk.Label(podcasts_add, text = "number of episodes")
    podcasts_nreps_label.grid(row = 0, column = 3)
    podcasts_nreps_entry = tk.Entry(podcasts_add)
    podcasts_nreps_entry.grid(row = 1, column = 3)

    def submit_podcasts():

        podcast_name = podcasts_name_entry.get()
        podcast_theme = podcasts_theme_entry.get()
        podcast_host = podcasts_host_entry.get()
        podcast_nreps = podcasts_nreps_entry.get()

        print("podcast name:", podcast_name)
        print("podcast theme:", podcast_theme)
        print("podcast host:", podcast_host)
        print("podcast number of episodes:", podcast_nreps)

        connection = sqlite3.connect('musify.db')
        table_create_podcasts = '''CREATE TABLE IF NOT EXISTS Podcast_Table 
            (podcast_name TEXT, podcast_theme TEXT, podcast_host TEXT, podcast_nreps TEXT)'''

        connection.execute(table_create_podcasts)

        data_insert_podcasts = '''INSERT INTO Podcast_Table 
            (podcast_name, podcast_theme, podcast_host, podcast_nreps) VALUES 
                    (?, ?, ?, ?)'''
        data_podcasts_tuple = (podcast_name, podcast_theme, podcast_host, podcast_nreps)
        cursor = connection.cursor()
        cursor.execute(data_insert_podcasts, data_podcasts_tuple)
        connection.commit()
        connection.close()

    submitdata = tk.Button(Frame, text = "submit data", command = submit_podcasts)
    submitdata.grid(row = 1, column = 4)

def view_podcasts():
    root2 = tk.Toplevel()
    root2.title("view podcasts")

    Frame2 = tk.Frame(root2)
    Frame2.pack(padx = 20, pady= 10)

    columns = ("name", "theme", "host", "nr of episodes")
    tree = ttk.Treeview(Frame2, columns=columns, show = "headings", height = 15)

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor = "w", width = 130)
       
    tree.pack(side = "left", fill = "both", expand = True)
        #viewing songs
    connection = sqlite3.connect('musify.db')
    cursor = connection.cursor()
    data_view_podcasts = '''SELECT podcast_name, podcast_theme, podcast_host, podcast_nreps
                            FROM Podcast_Table'''
    cursor.execute(data_view_podcasts)
    all_podcasts = cursor.fetchall()
    print(all_podcasts) 
    for pd in all_podcasts:
        tree.insert("", "end", values = pd)
    connection.close()  

def delete_pod_db(pd_name_entry):
    podcast_name = pd_name_entry.get()
    connection = sqlite3.connect('musify.db')
    cursor = connection.cursor()
    delete_podcasts_query = '''DELETE FROM Podcast_Table WHERE podcast_name = ?'''
    cursor.execute(delete_podcasts_query, (podcast_name,))
    connection.commit()
    print(f"podcast '{podcast_name}' was deleted successfully")
    connection.close()

def delete_podcasts():  
     root3 = tk.Toplevel()
     root3.title("podcasts deletion")

     Frame3 = tk.Frame(root3, padx = 20, pady = 20)
     Frame3.pack(padx = 20, pady = 20)

     del_pod_label = tk.Label(Frame3, text = "write podcasts name to delete")
     del_pod_label.grid(row=0,column=0,pady=10)

     del_pod_entry = tk.Entry(Frame3)
     del_pod_entry.grid(row = 1, column = 0, pady = 10)

     data_deletion_pod = tk.Button(Frame3, text = "delete", command=lambda: delete_pod_db(del_pod_entry))
     data_deletion_pod.grid(row = 2, column = 0, pady=10)  


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
