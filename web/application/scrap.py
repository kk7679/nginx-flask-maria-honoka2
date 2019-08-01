from robobrowser import RoboBrowser


def get_hatena_entries(target_url):
    results = []
    robo = RoboBrowser(
        parser='html.parser',  # Beautiful Soupで使用するパーサーを指定
        timeout=5
    )
    robo.open(target_url)
    target_class = 'div.entrylist-contents-main'
    for data in (robo.select(target_class)):
        title = data.select('a.js-keyboard-openable')
        users = data.select('span.entrylist-contents-users')
        posted_date = data.select('li.entrylist-contents-date')
        link = data.find('a').get('href')
        # link = source.get('href')
        line = [] # リストで帰ってくるので取り出す
        line.append(title[0].text)
        line.append(posted_date[0].text)
        line.append(users[0].text)
        line.append(link)
        results.append(line)
    return(results)

if __name__ == "__main__":
    results = scrap.get_hatena_entries('https://b.hatena.ne.jp/hotentry/it')
    for line in results:
        print(line)