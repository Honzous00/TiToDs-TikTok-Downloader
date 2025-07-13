import yt_dlp
import os
import subprocess
import logging
import urllib.request
import socket
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

# Nastavení logování
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='tiktok_downloader.log'
)

def check_internet_connection():
    """Kontrola internetového připojení"""
    try:
        urllib.request.urlopen("https://www.google.com", timeout=5)
        return True
    except (urllib.request.URLError, socket.timeout):
        return False

def validate_tiktok_url(url):
    """Validace TikTok URL"""
    if not url:
        logging.error("Prázdné URL")
        return False
    if "tiktok.com" not in url and "tiktokv.com" not in url:
        logging.error(f"Neplatný TikTok odkaz: {url}")
        return False
    return True

def get_original_filename(url, output_dir="."):
    """Generování unikátního názvu souboru"""
    try:
        with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
            info = ydl.extract_info(url, download=False)
            base_name = ydl.prepare_filename(info).replace('.webm', '.mp4').replace('.part', '')
            
            # Ošetření duplicit
            counter = 1
            original_path = Path(output_dir) / base_name
            while original_path.exists():
                stem = original_path.stem
                suffix = original_path.suffix
                original_path = original_path.with_name(f"{stem}_{counter}{suffix}")
                counter += 1
                
            return str(original_path)
    except Exception as e:
        logging.error(f"Chyba při získávání názvu: {str(e)}")
        return str(Path(output_dir) / "tiktok_video.mp4")

def log_failed_url(url, error_msg):
    """Zápis chybných URL do speciálního logu"""
    with open("failed_downloads.log", "a", encoding="utf-8") as f:
        f.write(f"{url} | {error_msg}\n")

def download_tiktok(url, output_dir="."):
    """Hlavní funkce pro stahování"""
    if not validate_tiktok_url(url):
        return False

    if not check_internet_connection():
        logging.error("Nedetekováno připojení k internetu")
        return False

    original_filename = get_original_filename(url, output_dir)
    ydl_opts = {
        'outtmpl': original_filename,
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',
        'postprocessor_args': ['-c:v', 'copy', '-an'],
        'merge_output_format': 'mp4',
        'quiet': True,
        'no_warnings': True,
        'concurrent_fragments': 4,
        'ratelimit': 1_000_000
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        if os.path.exists(original_filename) and os.path.getsize(original_filename) > 0:
            logging.info(f"Úspěšně staženo: {original_filename}")
            return original_filename
    except Exception as e:
        error_msg = f"Stahování selhalo: {str(e)}"
        log_failed_url(url, error_msg)
        logging.error(error_msg)

    return False

def batch_download(urls, output_dir="."):
    """Dávkové stahování"""
    with ThreadPoolExecutor(max_workers=3) as executor:
        results = list(executor.map(
            lambda url: download_tiktok(url, output_dir), 
            urls
        ))
    return results