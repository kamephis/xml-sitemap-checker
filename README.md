# Sitemap URL Checker

This script checks all URLs in a specified `sitemap.xml` file and generates a log file with URLs that do not return an HTTP status of 200.

## Prerequisites

Before using this script, ensure that you have Python installed on your system. You will also need the `requests` library. If it's not already installed, you can install it using the following command:

```bash
pip install requests
```

## Usage
To use the script, navigate to the script's directory in the terminal and execute it with the path to the sitemap.xml file as an argument:

```bash
python check_sitemap.py /path/to/sitemap.xml
```

The script reads the specified sitemap.xml file, checks each URL for its HTTP status, and writes all URLs that do not return status 200 to a log file named bad_urls_log.txt.

## Log File Format
The created log file bad_urls_log.txt contains lines in the following format:
```bash
<URL> - Status: <HTTP Status Code>
```
or in case of an error while fetching the URL:
```bash
<URL> - Error: <Error Description>
```

## License
This script is free software released under the terms of the MIT License.

## Disclaimer
This script is provided "as is", without warranty of any kind.

This `README.md` provides clear instructions on how to use the script, along with important information about prerequisites and the output format. Including a license and disclaimer is always advisable to cover legal aspects.


