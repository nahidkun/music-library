import tkinter as tk
from tkinter import messagebox
from tkinter import ttk 
import sqlite3

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
        album_tknr_data = album_tknr_entry.get()

        print("album name: ", album_name)
        print("artist name: ", album_artist_name)
        print("album release year: ", album_rlsyr_data)
        print("album genre: ", album_genre_name )
        print("album track number: ", album_tknr_data)

        connection = sqlite3.connect('musify.db')
        table_create_albums = '''CREATE TABLE IF NOT EXISTS Album_Table 
            (album_name TEXT, album_artist_name TEXT, album_rlsyr_data INT, album_genre_name TEXT, album_tknr_data INT)'''

        connection.execute(table_create_albums)

        data_insert_albums = '''INSERT INTO Album_Table 
            (album_name, album_artist_name, album_rlsyr_data, album_genre_name, album_tknr_name) VALUES 
                    (?, ?, ?, ?, ?)'''
        data_album_tuple = (album_name, album_artist_name, album_rlsyr_data, album_genre_name, album_tknr_data)
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
        data_view_album = '''SELECT album_name, album_artist_name, album_genre_name, album_rlsyr_data, album_tknr_data 
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
     delete_albums_query = '''DELETE FROM Album_Table WHERE album_name = ?'''
     cursor.execute(delete_albums_query, (album_name,))
     connection.commit()
     print(f"album '{album_name}' was deleted successfully")
     connection.close()

def delete_album():  
     root3 = tk.Toplevel()
     root3.title("album deletion")

     Frame3 = tk.Frame(root3, padx = 20, pady = 20)
     Frame3.pack(padx = 20, pady = 20)

     del_album_label = tk.Label(Frame3, text = "write album name to delete")
     del_album_label.grid(row=0,column=0,pady=10)

     del_album_entry = tk.Entry(Frame3)
     del_album_entry.grid(row = 1, column = 0, pady = 10)

     data_deletion_album = tk.Button(Frame3, text = "delete", command=lambda: delete_album_db(del_album_entry))
     data_deletion_album.grid(row = 2, column = 0, pady=10)

     










import main