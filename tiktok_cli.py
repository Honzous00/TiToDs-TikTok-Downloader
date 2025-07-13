import argparse
from tiktok_downloader_core import download_tiktok, batch_download

def main():
    parser = argparse.ArgumentParser(description='TikTok Video Downloader (CLI)')
    parser.add_argument('url', nargs='?', help='URL TikTok videa')
    parser.add_argument('--batch', help='Soubor s URL (1 na řádek)')
    parser.add_argument('--output', help='Výstupní složka', default=".")
    args = parser.parse_args()

    if args.batch:
        with open(args.batch, 'r') as f:
            urls = [line.strip() for line in f if line.strip()]
        batch_download(urls, args.output)
    elif args.url:
        download_tiktok(args.url, args.output)
    else:
        url = input("Zadej URL TikTok videa: ")
        download_tiktok(url, args.output)

if __name__ == "__main__":
    main()