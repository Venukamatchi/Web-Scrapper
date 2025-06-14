import argparse
from dorks import generate_dorks
from scraper import search_google
from utils import print_banner

def main():
    parser = argparse.ArgumentParser(description="Webscrapper Dorker: Find info on people using Google dorks")
    parser.add_argument('--query', '-q', required=True, help='Name, email, or username to search')
    parser.add_argument('--max', '-m', type=int, default=3, help='Number of dorks to use (default 3)')
    args = parser.parse_args()

    print_banner()
    dorks = generate_dorks(args.query)[:args.max]
    all_results = []

    for idx, dork in enumerate(dorks, 1):
        print(f"\n[{idx}] Dork: {dork}")
        links = search_google(dork)
        if links:
            for link in links:
                print(f"  - {link}")
            all_results.extend(links)
        else:
            print("  No results found or blocked by Google.")

    print(f"\nTotal links found: {len(set(all_results))}")

if __name__ == "__main__":
    main()
