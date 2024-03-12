from tkinter import filedialog
import sqlite3
import pandas as pd

connection = sqlite3.connect("site_diary.db")
cursor = connection.cursor()
data_frame = pd.read_sql('SELECT ID, TITLE, CONTENT FROM USER_JGP', connection)

file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Spreadsheet files", "*.xlsx"), ("All files", "*.*")])
data_frame.to_excel(file_path, index=False)     

# root = tk.Tk()

# root.title("Text Editor")

# save_button = tk.Button(root, text="Save to File", command=save_to_file)
# save_button.pack(pady=10)

#status_label = tk.Label(root, text="", padx=20, pady=10)
# status_label.pack()

# root.mainloop()