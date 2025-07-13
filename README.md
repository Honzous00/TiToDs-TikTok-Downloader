# TiToDs (TikTok Downloads)

## Multi-platform TikTok Video Downloader (CLI & GUI)

TiToDs, short for **TikTok Downloads**, is a versatile desktop application designed for effortlessly downloading videos from TikTok. It offers a flexible interface, allowing you to choose between a **straightforward Command-Line Interface (CLI)** for quick operations or a **user-friendly Graphical User Interface (GUI)** for visual control. The program supports downloading individual videos as well as batch downloading from a text file.

-----

### 🇬🇧 English Version

### Features

  * **TikTok Video Download:** Download videos directly from TikTok URLs.
  * **Command-Line Interface (CLI):** Ideal for quick downloads, scripting, and automation.
  * **Graphical User Interface (GUI):** A user-friendly `tkinter`-based interface for easy interaction.
  * **Single Video Download:** Download one video at a time.
  * **Batch Download:** Process multiple video URLs from a text file.
  * **Smart Filenaming:** Automatically generates unique filenames to prevent overwrites.
  * **Internet Connection Check:** Verifies internet connectivity before attempting downloads.
  * **Logging:** Detailed logs help track download progress and identify failed URLs.

-----

### Installation and Usage

#### 1\. Standalone Executable (Windows Only - Recommended for most users)

For the easiest way to use TiToDs on Windows without needing to install Python or any dependencies, download the pre-built `.exe` file.

1.  **Download:** Go to the [Releases](https://github.com/Honzous00/TiToDs-TikTok-Downloader/releases) section of this repository.
2.  **Get the Latest Release:** Download the `TiToDs.exe` (or similarly named) file under the latest release.
3.  **Run:** Simply double-click the downloaded `.exe` file to start the application.

#### 2\. From Source (Cross-platform - For Developers or Advanced Users)

If you prefer to run the application from source, contribute to its development, or use it on Linux/macOS, follow these steps.

1.  **Prerequisites:**

      * **Python:** Ensure you have **Python 3.8 or newer** installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
      * **Git:** For cloning the repository.
      * **FFmpeg (Recommended):** While `yt-dlp` can often work without it, installing `ffmpeg` can improve compatibility and performance for various video formats. Download it from [ffmpeg.org](https://ffmpeg.org/download.html) and ensure it's in your system's PATH.

2.  **Clone the Repository:**

    ```bash
    git clone https://github.com/Honzous00/TiToDs-TikTok-Downloader.git
    cd TiToDs
    ```

3.  **Install Dependencies:**

      * It's highly recommended to use a **virtual environment** to manage dependencies:
        ```bash
        python -m venv venv
        # On Windows:
        venv\Scripts\activate
        # On macOS/Linux:
        source venv/bin/activate
        ```
      * Install the required Python packages using the `requirements.txt` file:
        ```bash
        pip install -r requirements.txt
        ```

4.  **Run the Application:**

      * **Graphical User Interface (GUI):**

        ```bash
        python tiktok_gui.py
        ```

        This will open the application's window.

      * **Command-Line Interface (CLI):**

        ```bash
        python tiktok_cli.py
        ```

        You can then interact with it via command-line arguments:

          * **Single video download:**
            ```bash
            python tiktok_cli.py <TikTok_URL> --output <output_directory>
            # Example:
            python tiktok_cli.py https://www.tiktok.com/@user/video/1234567890 --output ./downloaded_videos
            ```
          * **Batch download from a file:**
            ```bash
            python tiktok_cli.py --batch <path_to_urls_file.txt> --output <output_directory>
            # Example:
            python tiktok_cli.py --batch urls.txt --output ./batch_downloads
            ```
            (The `urls.txt` file should contain one TikTok URL per line.)
          * **Interactive mode (if no arguments provided):**
            ```bash
            python tiktok_cli.py
            # The program will prompt you to enter a URL.
            ```

-----

### Project Structure

```
.
├── tiktok_cli.py               # Command-Line Interface for the downloader
├── tiktok_downloader_core.py   # Core logic for downloading, validation, and logging
├── tiktok_gui.py               # Graphical User Interface for the downloader
├── requirements.txt            # Python dependencies
├── tiktok_downloader.log       # Log file for download activities
├── failed_downloads.log        # Log for failed URL attempts
└── README.md                   # This file
```

-----

### Python Dependencies (from `requirements.txt`)

  * `yt-dlp`: The primary library used for video downloading.

You can install them using `pip install -r requirements.txt`.

-----

### Contributing

We welcome contributions\! If you encounter any bugs, have feature suggestions, or want to improve the code, please feel free to:

1.  **Open an Issue:** Describe the bug or feature request in detail.
2.  **Submit a Pull Request:** Fork the repository, make your changes, and create a pull request to merge your contributions.

-----

### License

This project is licensed under the MIT License - see the `LICENSE` file for details.

-----


-----

# TiToDs (TikTok Downloads)

## Multiplatformní Nástroj pro Stahování TikTok Videí (CLI & GUI)

TiToDs, zkráceně pro **TikTok Downloads**, je univerzální desktopová aplikace pro snadné stahování videí z TikToku. Nabízí flexibilní rozhraní – můžete si vybrat mezi **jednoduchou příkazovou řádkou (CLI)** pro rychlé operace nebo **uživatelsky přívětivým grafickým rozhraním (GUI)** pro vizuální ovládání. Program podporuje stahování jednotlivých videí i dávkové stahování z textového souboru.

-----

### 🇨🇿 Česká Verze

### Vlastnosti

  * **Stahování TikTok videí:** Stahujte videa přímo z TikTok URL.
  * **Rozhraní příkazové řádky (CLI):** Ideální pro rychlé stahování, skriptování a automatizaci.
  * **Grafické uživatelské rozhraní (GUI):** Uživatelsky přívětivé rozhraní postavené na `tkinter` pro snadnou interakci.
  * **Stahování jednoho videa:** Stáhněte jedno video najednou.
  * **Dávkové stahování:** Zpracujte více URL videí z textového souboru.
  * **Chytré pojmenování souborů:** Automaticky generuje unikátní názvy souborů, aby se zabránilo přepisování.
  * **Kontrola připojení k internetu:** Před pokusem o stahování ověří připojení k internetu.
  * **Logování:** Podrobné logy pomáhají sledovat průběh stahování a identifikovat neúspěšná URL.

-----

### Instalace a použití

#### 1\. Samostatný spustitelný soubor (Pouze pro Windows - Doporučeno pro většinu uživatelů)

Pro nejjednodušší způsob použití TiToDs ve Windows, aniž byste museli instalovat Python nebo jakékoli závislosti, si stáhněte předkompilovaný soubor `.exe`.

1.  **Stáhněte:** Přejděte do sekce [Releases](https://github.com/Honzous00/TiToDs-TikTok-Downloader/releases) tohoto repozitáře.
2.  **Získejte nejnovější vydání:** Stáhněte soubor `TiToDs.exe` (nebo podobně pojmenovaný) pod nejnovějším vydáním.
3.  **Spusťte:** Jednoduše dvakrát klikněte na stažený soubor `.exe` a spusťte aplikaci.

#### 2\. Ze zdrojového kódu (Multiplatformní - Pro vývojáře nebo pokročilé uživatele)

Pokud chcete aplikaci spustit ze zdrojového kódu, přispět k jejímu vývoji nebo ji použít na Linuxu/macOS, postupujte takto.

1.  **Předpoklady:**

      * **Python:** Ujistěte se, že máte nainstalovaný **Python 3.8 nebo novější**. Můžete si jej stáhnout z [python.org](https://www.python.org/downloads/).
      * **Git:** Pro klonování repozitáře.
      * **FFmpeg (Doporučeno):** Ačkoli `yt-dlp` často funguje i bez něj, instalace `ffmpeg` může zlepšit kompatibilitu a výkon pro různé formáty videa. Stáhněte si jej z [ffmpeg.org](https://ffmpeg.org/download.html) a ujistěte se, že je v systémové proměnné PATH.

2.  **Klonování repozitáře:**

    ```bash
    git clone https://github.com/Honzous00/TiToDs-TikTok-Downloader.git
    cd TiToDs
    ```

3.  **Instalace závislostí:**

      * Důrazně se doporučuje použít **virtuální prostředí** pro správu závislostí:
        ```bash
        python -m venv venv
        # Na Windows:
        venv\Scripts\activate
        # Na macOS/Linux:
        source venv/bin/activate
        ```
      * Nainstalujte požadované Python balíčky pomocí souboru `requirements.txt`:
        ```bash
        pip install -r requirements.txt
        ```

4.  **Spuštění aplikace:**

      * **Grafické uživatelské rozhraní (GUI):**

        ```bash
        python tiktok_gui.py
        ```

        Tím se otevře okno aplikace.

      * **Rozhraní příkazové řádky (CLI):**

        ```bash
        python tiktok_cli.py
        ```

        Poté s ní můžete interagovat pomocí argumentů příkazové řádky:

          * **Stahování jednoho videa:**
            ```bash
            python tiktok_cli.py <TikTok_URL> --output <výstupní_složka>
            # Příklad:
            python tiktok_cli.py https://www.tiktok.com/@user/video/1234567890 --output ./stazena_videa
            ```
          * **Dávkové stahování ze souboru:**
            ```bash
            python tiktok_cli.py --batch <cesta_k_souboru_urls.txt> --output <výstupní_složka>
            # Příklad:
            python tiktok_cli.py --batch urls.txt --output ./batch_downloads
            ```
            (Soubor `urls.txt` by měl obsahovat jedno TikTok URL na řádek.)
          * **Interaktivní režim (pokud nejsou zadány žádné argumenty):**
            ```bash
            python tiktok_cli.py
            # Program vás vyzve k zadání URL
            ```

-----

### Struktura projektu

```
.
├── tiktok_cli.py               # Rozhraní příkazové řádky pro stahovač
├── tiktok_downloader_core.py   # Základní logika pro stahování, validaci a logování
├── tiktok_gui.py               # Grafické uživatelské rozhraní pro stahovač
├── requirements.txt            # Python závislosti
├── tiktok_downloader.log       # Logovací soubor pro aktivity stahování
├── failed_downloads.log        # Log pro neúspěšné pokusy o stažení URL
└── README.md                   # Tento soubor
```

-----

### Python závislosti (z `requirements.txt`)

  * `yt-dlp`: Hlavní knihovna používaná pro stahování videí.

Můžete je nainstalovat pomocí `pip install -r requirements.txt`.

-----

### Přispívání

Příspěvky jsou vítány\! Pokud narazíte na chyby, máte návrhy na funkce nebo chcete vylepšit kód, neváhejte:

1.  **Otevřete Issue:** Podrobně popište chybu nebo požadavek na funkci.
2.  **Odešlete Pull Request:** Forkněte repozitář, proveďte své změny a vytvořte pull request pro sloučení vašich příspěvků.

-----

### Licence

Tento projekt je licencován pod licencí MIT - podrobnosti naleznete v souboru `LICENSE`.

-----
