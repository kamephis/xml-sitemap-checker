import xml.etree.ElementTree as ET
import requests
import sys

def check_urls_in_sitemap(sitemap_path):
    try:
        # Register the namespaces
        ET.register_namespace('', 'http://www.sitemaps.org/schemas/sitemap/0.9')

        # Parse the XML
        tree = ET.parse(sitemap_path)
        root = tree.getroot()

        # Namespace mapping
        ns = {'sitemap': 'http://www.sitemaps.org/schemas/sitemap/0.9'}

        bad_urls = []
        for url in root.findall('sitemap:url/sitemap:loc', ns):
            print(f"Checking URL: {url.text}")
            try:
                response = requests.get(url.text)
                print(f"Status Code for {url.text}: {response.status_code}")
                if response.status_code != 200:
                    bad_urls.append(url.text + " - Status: " + str(response.status_code))
            except requests.RequestException as e:
                print(f"Request Exception for {url.text}: {e}")
                bad_urls.append(url.text + " - Error: " + str(e))

        if bad_urls:
            with open('bad_urls_log.txt', 'w') as file:
                for url in bad_urls:
                    file.write(url + '\n')
            print("Log file created with URLs not returning HTTP Status 200.")
        else:
            print("No bad URLs found.")

    except ET.ParseError as e:
        print("Error parsing the XML file: " + str(e))
    except Exception as e:
        print("An error occurred: " + str(e))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Please provide the path to the sitemap.xml as a parameter.")
    else:
        sitemap_path = sys.argv[1]
        check_urls_in_sitemap(sitemap_path)
