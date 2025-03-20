import tkinter as tk
from tkinter import messagebox
from tkinter import ttk 
import sqlite3

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
    data_view_fav_artists = '''SELECT fav_artist_name, fav_artists_genre
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

    del_fartists_label = tk.Label(Frame3, text = "write favorite name to delete")
    del_fartists_label.grid(row=0,column=0,pady=10)

    del_fartists_entry = tk.Entry(Frame3)
    del_fartists_entry.grid(row = 1, column = 0, pady = 10)

    data_deletion_fartists = tk.Button(Frame3, text = "delete", command=lambda: delete_fartists(del_fartists_entry))
    data_deletion_fartists.grid(row = 2, column = 0, pady=10)  



    import main