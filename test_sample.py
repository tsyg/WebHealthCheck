from env import env_


def grab_all_links(htm: str):
    from bs4 import BeautifulSoup  # https://www.crummy.com/software/BeautifulSoup/bs4/doc/
    print(" ************** GRAB-ALL-LINKS *******************  ")
    soup = BeautifulSoup(htm, 'html.parser')
    # print(soup.prettify())
    # print(" ************** END-OF-Prettify *******************  ")

    links = [link.get('href') for link in soup.find_all('a')]
    print(f"==>> Found {len(links)} links")
    return links


if __name__ == "__main__":
    htm = env_().get('/').text
    for link in grab_all_links(htm):
        print(link)

