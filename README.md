## Web-Crawler for the russian imageboard 2ch

### Actually in progress
- [x] Using the html-parser libraries, get the URLs of all media files in a thread
- [x] Write all URLs with a timestamp in a structured file
- [x] Create subfolder with timestamp for each thread-URL
- [ ] Adapt this script to the DeskChan project (proxy3.py)

### For future projects
- [ ] Crawling for 4ch
- [ ] Universal crawling of the imageboards
- [ ] Tagging and sorting algorithms

### Features
* You have a URL from a 2ch thread.
* You put the URL from a 2ch thread into the script
* The script uses a parser searching all media files in this thread
* The script writes all direct URLs into a *thread.txt* file
* The script writes all files of the thread into a subfolder with a timestamp

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

To download the *Requests* library:
```
pip install requests
```

To download the *BeautifulSoup* library:
```
pip install beautifulsoup4
```

Now you should be ready for using this plugin.

