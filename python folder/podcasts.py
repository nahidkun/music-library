import tkinter as tk
from tkinter import messagebox
from tkinter import ttk 
import sqlite3

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
















import main