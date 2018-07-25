## Web-Crawler for the russian imageboard 2ch (actually in progress)
- [x] Using the html-parser libraries, get the URLs of all media files in a thread
- [x] Write all URLs with a timestamp in a structured file
- [x] Create subfolder with timestamp for each thread-URL
- [ ] Adapt this script to the DeskChan project (proxy3.py)

### Needed Python libraries:
* [__Requests: HTTP for Humans__](http://docs.python-requests.org/en/master/user/install/#install)
* [__BeautifulSoup4__](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup)

For Windows user: You will need to install [Python 3](https://www.python.org/downloads/release/python-370/).
While the installation process you have to "*add Python 3.x to PATH*". After the reboot type 'python' in your command prompt.
If you don't get an error, your installation was successful.
Notice you can also use the pip for automatic updates of the (also missing) libraries.

To update pip himself, type in your command prompt:
```
python -m pip install --upgrade pip
```

To download the *Requests*, type:
```
pip install requests
```

To download the *BeautifulSoup* library, type:
```
pip install beautifulsoup4
```

Now you should be ready for using this plugin.

