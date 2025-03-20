import tkinter as tk
from tkinter import messagebox
from tkinter import ttk 
import sqlite3

def songadd():
    # child window of the main application
    root = tk.Toplevel()
    root.title("add songs section")

    Frame = tk.Frame(root)
    Frame.pack(padx = 20, pady = 20)
    #song details frame
    song_add = tk.LabelFrame(Frame, text = "song details")
    song_add.grid(row = 0, column = 0, padx = 20, pady = 10)
    #song name
    song_name_label = tk.Label(song_add, text = "name")
    song_name_label.grid(row = 0, column = 0)
    song_name_entry = tk.Entry(song_add)
    song_name_entry.grid(row = 1, column = 0)
    #song artist
    song_artist_label = tk.Label(song_add, text = "artist")
    song_artist_label.grid(row = 0, column = 1)
    song_artist_entry = tk.Entry(song_add)
    song_artist_entry.grid(row = 1, column = 1)
    #song genre
    song_genre_label = tk.Label(song_add, text = "genre")
    song_genre_label.grid(row = 0, column = 2)
    song_genre_entry = tk.Entry(song_add)
    song_genre_entry.grid(row = 1, column = 2)
    #song release year
    song_rlsyr_label = tk.Label(song_add, text = "release year")
    song_rlsyr_label.grid(row = 0, column = 3)
    song_rlsyr_entry = tk.Entry(song_add)
    song_rlsyr_entry.grid(row = 1, column = 3)


    def submit_dataa():

        song_name = song_name_entry.get()
        artist_name = song_artist_entry.get()
        genre_name = song_genre_entry.get()
        rlsyr_data = song_rlsyr_entry.get()
        
        print("song name:", song_name)
        print("artist name:", artist_name)
        print("genre_name", genre_name)
        print("release year:", rlsyr_data)

        connection = sqlite3.connect('musify.db')
        #table_create_songs = '''CREATE TABLE IF NOT EXISTS Song_Table 
        #    (song_name TEXT, artist_name TEXT, genre_name TEXT, rlsyr_data INT)'''

        #connection.execute(table_create_songs)

        data_insert_songs = '''INSERT INTO Song_Table 
            (song_name, artist_name, genre_name, rlsyr_data) VALUES 
                    (?, ?, ?, ?)'''
        data_song_tuple = (song_name, artist_name, genre_name, rlsyr_data)
        cursor = connection.cursor()
        cursor.execute(data_insert_songs, data_song_tuple)
        connection.commit()
        connection.close()

    submitdata = tk.Button(Frame, text = "submit data", command = submit_dataa)
    submitdata.grid(row = 1, column = 4)

def view_songs():
        root2 = tk.Toplevel()
        root2.title("view songs")

        Frame2 = tk.Frame(root2)
        Frame2.pack(padx = 20, pady= 10)

        columns = ("name", "artist", "genre", "release year")
        tree = ttk.Treeview(Frame2, columns=columns, show = "headings", height = 15)

        for col in columns:
             tree.heading(col, text=col)
             tree.column(col, anchor = "w", width = 130)
       
        tree.pack(side = "left", fill = "both", expand = True)
        #viewing songs
        connection = sqlite3.connect('musify.db')
        cursor = connection.cursor()
        data_view_songs = '''SELECT song_name, artist_name, genre_name, rlsyr_data 
                            FROM Song_Table'''
        cursor.execute(data_view_songs)
        all_songs = cursor.fetchall()
        print(all_songs) 
        for song in all_songs:
             tree.insert("", "end", values = song)
        connection.close()

def delete_data_db(song_entry):
     song_name = song_entry.get()
     connection = sqlite3.connect('musify.db')
     cursor = connection.cursor()
     delete_songs_query = '''DELETE FROM Song_Table WHERE song_name = ?'''
     cursor.execute(delete_songs_query, (song_name,))
     connection.commit()
     print(f"song '{song_name}' was deleted successfully")
     connection.close()

def delete():  
     root3 = tk.Toplevel()
     root3.title("song deletion")

     Frame3 = tk.Frame(root3, padx = 20, pady = 20)
     Frame3.pack(padx = 20, pady = 20)

     del_song_label = tk.Label(Frame3, text = "write song name to delete")
     del_song_label.grid(row=0,column=0,pady=10)

     del_song_entry = tk.Entry(Frame3)
     del_song_entry.grid(row = 1, column = 0, pady = 10)

     data_deletion = tk.Button(Frame3, text = "delete", command=lambda: delete_data_db(del_song_entry))
     data_deletion.grid(row = 2, column = 0, pady=10)
     #defined functions before importing main file to avoid circular error

import main