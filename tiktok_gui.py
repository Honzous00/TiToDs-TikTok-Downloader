import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
from tiktok_downloader_core import download_tiktok, batch_download
import os # Přidáno
import sys # Přidáno

class TikTokDownloaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("TiToDs (TikTok Downloads)")
        self.root.geometry("500x200") # Původní velikost
        self.root.resizable(False, False)

        # --- Nastavení ikony okna ---
        try:
            # Použijeme funkci resource_path pro správné načítání cesty k souboru
            # Funkce resource_path bude definována níže
            icon_path = self.resource_path("icons/icon.ico")
            if os.path.exists(icon_path):
                self.root.iconbitmap(icon_path)
            else:
                print(f"Upozornění: Soubor ikony nenalezen na cestě: {icon_path}")
        except Exception as e:
            print(f"Chyba při nastavení ikony okna: {e}")
        
        self.create_widgets()

    # Tato funkce je nezbytná pro správnou práci s PyInstallerem
    def resource_path(self, relative_path):
        """
        Získá absolutní cestu k souboru, funguje ve vývojovém režimu i po zabalení PyInstallerem.
        """
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)
    
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

        # URL Entry / Batch Text Area
        self.url_frame = ttk.Frame(main_frame)
        self.url_frame.pack(fill=tk.X, pady=5)
        
        self.url_label = ttk.Label(self.url_frame, text="URL TikTok videa:")
        self.url_label.pack(side=tk.LEFT, padx=(0, 5))
        
        self.url_entry = ttk.Entry(self.url_frame)
        self.url_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        self.text_area = scrolledtext.ScrolledText(main_frame, height=5, width=40, wrap=tk.WORD)
        
        # Výběr výstupní složky
        output_frame = ttk.Frame(main_frame)
        output_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(output_frame, text="Výstupní složka:").pack(side=tk.LEFT, padx=(0, 5))
        self.output_var = tk.StringVar(value="")
        self.output_entry = ttk.Entry(output_frame, textvariable=self.output_var)
        self.output_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        ttk.Button(output_frame, text="Procházet", command=self.browse_output_dir).pack(side=tk.RIGHT, padx=5)

        # Tlačítko Stáhnout
        download_button = ttk.Button(main_frame, text="Stáhnout", command=self.start_download)
        download_button.pack(pady=10)

        # Stavový řádek
        self.status_var = tk.StringVar(value="")
        self.status_label = ttk.Label(main_frame, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W)
        self.status_label.pack(side=tk.BOTTOM, fill=tk.X)

        self.switch_mode() # Initialize UI based on default mode

    def switch_mode(self):
        if self.mode_var.get() == "single":
            self.url_frame.pack(fill=tk.X, pady=5)
            self.text_area.pack_forget()
        else:
            self.url_frame.pack_forget()
            self.text_area.pack(fill=tk.BOTH, expand=True, pady=5)

    def browse_output_dir(self):
        directory = filedialog.askdirectory()
        if directory:
            self.output_var.set(directory)

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
        
        messagebox.showinfo("Dávkové stahování dokončeno", 
                            f"Úspěšně staženo: {success}/{len(urls)} videí.\n"
                            "Podrobnosti viz logy.")
        self.status_var.set("")


if __name__ == "__main__":
    try:
        import yt_dlp
    except ImportError:
        print("yt-dlp není nainstalován. Prosím, nainstalujte ho pomocí 'pip install yt-dlp'")
        sys.exit(1)

    root = tk.Tk()
    app = TikTokDownloaderApp(root)
    root.mainloop()