import requests

# Read URLs from the file
def read_urls(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file if line.strip()]

# Visit each URL
def visit_urls(urls):
    for url in urls:
        try:
            response = requests.get(url, timeout=10)
            print(f"Visited: {url}, Status Code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error visiting {url}: {e}")

if __name__ == "__main__":
    urls = read_urls('urls.txt')
    visit_urls(urls)
