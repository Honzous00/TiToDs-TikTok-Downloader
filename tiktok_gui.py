import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
from tiktok_downloader_core import download_tiktok, batch_download

class TikTokDownloaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("TikTok Downloader")
        self.root.geometry("500x200")
        self.root.resizable(False, False)
        
        self.create_widgets()
    
    def create_widgets(self):
        # Hlavní kontejner
        main_frame = ttk.Frame(self.root, padding=10)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Radio buttony pro výběr režimu
        self.mode_var = tk.StringVar(value="single")
        mode_frame = ttk.Frame(main_frame)
        mode_frame.pack(fill=tk.X, pady=2)
        
        ttk.Radiobutton(
            mode_frame,
            text="Jedno video",
            variable=self.mode_var,
            value="single",
            command=self.switch_mode
        ).pack(side=tk.LEFT)
        
        ttk.Radiobutton(
            mode_frame,
            text="Více videí",
            variable=self.mode_var,
            value="batch",
            command=self.switch_mode
        ).pack(side=tk.LEFT, padx=10)

        # Frame pro obsah (bude obsahovat buď URL entry nebo text area)
        self.content_frame = ttk.Frame(main_frame)
        self.content_frame.pack(fill=tk.BOTH, expand=True, pady=2)

        # Entry pro jedno video
        self.url_frame = ttk.Frame(self.content_frame)
        ttk.Label(self.url_frame, text="URL videa:").pack(side=tk.LEFT)
        self.url_entry = ttk.Entry(self.url_frame)
        self.url_entry.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)

        # Text area pro více videí
        self.text_area = scrolledtext.ScrolledText(
            self.content_frame,
            height=3,
            wrap=tk.WORD,
            font=('Tahoma', 9)
        )

        # Řádek s výstupní složkou (vždy pod obsahem)
        self.output_frame = ttk.Frame(main_frame)
        self.output_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(self.output_frame, text="Cílová složka:").pack(side=tk.LEFT)
        self.output_var = tk.StringVar(value=".")
        self.output_entry = ttk.Entry(self.output_frame, textvariable=self.output_var, state='readonly')
        self.output_entry.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)
        
        self.select_dir_btn = ttk.Button(self.output_frame, text="📂", width=3, command=self.select_output_dir)
        self.select_dir_btn.pack(side=tk.LEFT)

        # Hlavní tlačítko (vždy pod výstupní složkou)
        btn_frame = ttk.Frame(main_frame)
        btn_frame.pack(pady=10)
        
        self.download_btn = ttk.Button(
            btn_frame, 
            text="⬇️ Stáhnout video", 
            command=self.start_download,
            width=20
        )
        self.download_btn.pack()

        # Status (vždy dole)
        self.status_var = tk.StringVar()
        ttk.Label(main_frame, textvariable=self.status_var).pack()

        # Výchozí stav
        self.switch_mode()
    
    def switch_mode(self):
        """Přepíná mezi režimy"""
        # Odstraníme všechny prvky z content_frame
        for widget in self.content_frame.winfo_children():
            widget.pack_forget()
        
        if self.mode_var.get() == "single":
            self.url_frame.pack(fill=tk.X)
            self.download_btn.config(text="⬇️ Stáhnout video")
        else:
            self.text_area.pack(fill=tk.BOTH, expand=True)
            self.download_btn.config(text="⬇️ Stáhnout vše")
    
    def select_output_dir(self):
        folder = filedialog.askdirectory()
        if folder:
            self.output_var.set(folder)
    
    def start_download(self):
        if self.mode_var.get() == "single":
            self.download_single()
        else:
            self.download_batch()
    
    def download_single(self):
        url = self.url_entry.get().strip()
        if not url:
            messagebox.showerror("Chyba", "Zadejte URL videa!")
            return
        
        self.status_var.set("Stahuji...")
        self.root.update()
        
        result = download_tiktok(url, self.output_var.get())
        if result:
            messagebox.showinfo("Úspěch", f"Video staženo:\n{result}")
        else:
            messagebox.showerror("Chyba", "Stahování selhalo! Viz logy.")
        self.status_var.set("")
    
    def download_batch(self):
        urls = [url.strip() for url in self.text_area.get("1.0", tk.END).splitlines() if url.strip()]
        if not urls:
            messagebox.showerror("Chyba", "Nebyly zadány žádné URL!")
            return
        
        self.status_var.set(f"Stahuji {len(urls)} videí...")
        self.root.update()
        
        results = batch_download(urls, self.output_var.get())
        success = sum(1 for r in results if r)
        
        messagebox.showinfo(
            "Výsledek", 
            f"Staženo {success}/{len(urls)} videí!\n"
            f"Chyby jsou v failed_downloads.log"
        )
        self.status_var.set("")

if __name__ == "__main__":
    root = tk.Tk()
    app = TikTokDownloaderApp(root)
    root.mainloop()