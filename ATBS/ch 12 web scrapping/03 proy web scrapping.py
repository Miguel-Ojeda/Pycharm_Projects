'''
It would be nice if I could simply type a search term on the command line and have my computer automatically open
a browser with all the top search results in new tabs. Let’s write a script to do this with the
search results page for the Python Package Index at https://pypi.org/.

A program like this can be adapted to many other websites, although the Google and DuckDuckGo often employ
measures that make scraping their search results pages difficult.

This is what your program does:
1. Gets search keywords from the command line arguments
2. Retrieves the search results page
3. Opens a browser tab for each result
This means your code will need to do the following:
1. Read the command line arguments from sys.argv.
2. Fetch the search result page with the requests module.
3. Find the links to each search result.
4. Call the webbrowser.open() function to open the web browser.
Open a new file editor tab and save it as searchpypi.py
'''

# Está hecho en search_pypi














