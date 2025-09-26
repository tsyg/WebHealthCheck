"""
 Tests methods themselves
"""
from bs4 import BeautifulSoup  # https://www.crummy.com/software/BeautifulSoup/bs4/doc/
from env import Env, env_


def grab_all_links(htm: str):
    """
    Parse the HTML code. extract all links.
    return the list of urls
    """
    print(" ************** GRAB-ALL-LINKS *******************  ")
    soup = BeautifulSoup(htm, 'html.parser')
    # print(soup.prettify())
    # print(" ************** END-OF-Prettify *******************  ")

    links = [link.get('href') for link in soup.find_all('a')
             if link not in ['/', ""]   # skip trash ones
             ]
    print(f"==>> Found {len(links)} links")
    return links


def link_to_full_url(env: Env, link: str):
    """ Convert link to full format:
    Not changing those already in the full format
    Prevents doubling slash - from host ending and link start symbol
    """
    if link.startswith("https://"):
        return link
    else:
        # remove extra slash: when host_url ends with '/' and the link itself
        if env.host_url[-1:] == '/' and link[0] == '/':
            return env.host_url[:-1] + link
        else:
            return env.host_url + link


def pytest_generate_tests(metafunc):
    print("** pytest_generate_tests ** ")
    # print(metafunc.fixturenames)

    if "link" in metafunc.fixturenames:
        html = env_().get_endpoint('').text
        links = [link_to_full_url(env=env_(), link=link) for link in grab_all_links(html)]

        selected_links = links  # [l for l in links if 'e' in l and 'i' in l]  # 'e','i' used to filter only some links
        print(links)
        print(f"{len(links)} / {len(selected_links)}")
        metafunc.parametrize("link", selected_links, ids=selected_links)


def test_link_valid(env, link: str):
    print(f" >> testing link {link} --{link[-1]}")
    assert "#" not in link  ### TO MAKE IT FAIL
    res = env.get(link)
    assert res.status_code == 200


if __name__ == "__main__":
    htm = env_().get_endpoint('/').text
    for link in grab_all_links(htm):
        # print(link)
        print(link_to_full_url(env=env_(), link=link))
