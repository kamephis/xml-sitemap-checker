import xml.etree.ElementTree as ET
import requests
import sys

def check_urls_in_sitemap(sitemap_path):
    try:
        tree = ET.parse(sitemap_path)
        root = tree.getroot()
        namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}

        bad_urls = []
        for url in root.findall('ns:url/ns:loc', namespace):
            try:
                response = requests.get(url.text)
                if response.status_code != 200:
                    bad_urls.append(url.text + " - Status: " + str(response.status_code))
            except requests.RequestException as e:
                bad_urls.append(url.text + " - Error: " + str(e))

        with open('bad_urls_log.txt', 'w') as file:
            for url in bad_urls:
                file.write(url + '\n')

        print("Log file created with URLs not returning HTTP Status 200.")

    except ET.ParseError:
        print("Error parsing the XML file.")
    except Exception as e:
        print("An error occurred: " + str(e))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Please provide the path to the sitemap.xml as a parameter.")
    else:
        sitemap_path = sys.argv[1]
        check_urls_in_sitemap(sitemap_path)

