import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube

class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master 
        self.pack()
        self.create_widgets()

    def create_widgets(self):

        self.radio_value = tk.IntVar()
        self.radio_value.set(0)

        self.video_button = tk.Radiobutton(self,text="Video",variable=self.radio_value,value=1)
        self.video_button.pack(side="top")

        self.music_button = tk.Radiobutton(self,text="Music",variable=self.radio_value,value=0)
        self.music_button.pack(side="top")

        self.link_label = tk.Label(self, text="Youtube Links: ")
        self.link_label.pack(side="top")

        self.url_input = tk.Text(self, height=8, width=30)
        self.url_input.pack(side="top")

        self.select_folder_tkvar = tk.StringVar()
        self.select_folder_tkvar.set("")
        
        self.folder_button = tk.Button(self, text='Download Folder', command=self.openfileexplorer)
        self.folder_button.pack(side="top")
        self.path = tk.Label(self, textvariable=self.select_folder_tkvar)
        self.path.pack(side="top")

        self.progress = ttk.Progressbar(self, length = 100, mode = 'determinate')
        self.progress.pack(side="top")

        self.download_button = tk.Button(self,text="Download",command=self.download)
        self.download_button.pack(side="top")

        self.quit = tk.Button(self,text="Exit",command=self.master.destroy)
        self.quit.pack(side="bottom")

    def openfileexplorer(self):
        self.filename = filedialog.askdirectory(initialdir = "/", title = "Select a Folder")
        self.select_folder_tkvar.set(self.filename)

    
    def download(self):
        self.links = list(self.url_input.get("1.0","end-1c").split("\n"))
        self.download_type = self.radio_value.get()
        self.location = self.select_folder_tkvar.get()
        self.progress["value"] = 0
        self.progress["maximum"] = 1

        if not self.download_type:
            for i in self.links:
                try:
                    self.yt = YouTube(i)
                    self.stream = self.yt.streams.get_by_itag('140')

                    self.stream.download(self.location)
                except KeyError:
                    print("Skipping Song: " + i)
                
        else:
            for i in self.links:
                try:
                    self.yt = YouTube(i)
                    self.stream = self.yt.streams.get_by_itag('22')

                    self.stream.download(self.location)
                except KeyError:
                    print("Skipping Video: " + i)
        self.progress["value"] = 1
        
    


root = tk.Tk()
root.title("Youtube Downloader")
root.iconphoto(False, tk.PhotoImage(file='logo.png'))
root.geometry("300x320+200+50")
app = Application(master=root)
app.mainloop()