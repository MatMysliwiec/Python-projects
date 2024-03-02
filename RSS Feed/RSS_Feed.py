import feedparser


def get_feed_data(feed_url):
    feed = feedparser.parse(feed_url)
    return feed


def display_posts(feed_data):
    print(f"Feed Title: {feed_data.feed.title}")
    print(f"Feed Description: {feed_data.feed.description}")

    for entry in feed_data.entries:
        print("\n----------------------------------------")
        print(f"Title: {entry.title}")
        print(f"Published: {entry.published}")
        print(f"Link: {entry.link}")
        print(f"Summary: {entry.summary}")
        print("----------------------------------------\n")


if __name__ == "__main__":
    # Replace the URL with the RSS/Atom feed URL you want to read
    feed_url = "http://www.cbssports.com/partners/feeds/rss/home_news"

    try:
        feed_data = get_feed_data(feed_url)
        display_posts(feed_data)
    except Exception as e:
        print(f"Error: {e}")
