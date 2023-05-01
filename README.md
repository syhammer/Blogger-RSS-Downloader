# Blogger RSS Downloader

## Setup

Before running [main.py](main.py), make sure to configure the script properly in the [configuration file](config.json). Here are your configuration options:

1. The URL to your Blogger website (JSON variable: <i>blogger_url</i>). Make sure that there is no forward slash in the url. Here are some examples:
    * YES: https://example.blogspot.com
    * NO: https://example.blogspot.com/
2. The URL extension that points to the feed once added to the previous variable (JSON variable: <i>feed_url</i>). I recommend not touching this. By default, this is set to _/feeds/posts/default?alt=rss_. If you want an __ATOM__ feed instead of an __RSS__ feed, change the _?alt=rss_ to _?alt=atom_.
3. The _iteration_ variable keeps track of the number of feed downloads. Don't touch this.
4. The <i>max_results</i> variable specifies how many posts are loaded from the feed at a time. Blogger only allows 150 posts per feed maximum. Don't set this to anything over 150.
5. The last two variables (<i>max_results_keyword</i> and <i>start_index_keyword</i>) specify the URL parameter names. Don't change this unless you are importing RSS feeds from a different blog platform.

Theoretically, you could use this to import RSS feeds from anywhere if configured properly. But this is currently set up only for Blogger.

## Running

Open your terminal inside the main folder of this script and type this:

```powershell
python main.py
```

Multiple batches of feeds should be imported and saved as xml files in the [feeds folder](feeds).
