import requests
import re


def link_to_link_check(start_url: str, end_url: str) -> str:
    """
    By two given urls checks if it is possible to go to end_url
    from any page specified on the start_url page

    :start_url: Start page url
    :end_url: End Page url
    :return: 'Yes' or 'No' string value
    """

    pattern = r'<a href="(.+?)">'
    res = requests.get(start_url)

    for link in re.findall(pattern, res.text):
        cur_res = requests.get(link)
        if end_url in re.findall(pattern, cur_res.text):
            return "Yes"
    else:
        return "No"


print(link_to_link_check(input(), input()))
