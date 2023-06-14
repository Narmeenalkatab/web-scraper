import requests
from bs4 import BeautifulSoup

def get_citations_needed_count(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    citations = soup.find_all('sup', class_='noprint Inline-Template Template-Fact')
    return len(citations)

def get_citations_needed_report(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    citations = soup.find_all('sup', class_='noprint Inline-Template Template-Fact')

    report = ''
    for citation in citations:
        passage = citation.find_parent('p').text.strip()
        report += f'{passage}\n\n'

    return report

url = 'https://en.wikipedia.org/wiki/History_of_Mexico'

# Get the number of citations needed
count = get_citations_needed_count(url)
print(f"Number of citations needed: {count}")

# Get the report of relevant passages with citations needed
report = get_citations_needed_report(url)
print(f"Report:\n{report}")
