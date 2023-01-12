# import webbrowser

# The "webbrowser" module has the method "open"
# You simply pass the URL of the target website to the "open" method

print("Deployment Completed")

# webbrowser.open("http://www.tecvinson.se")
# webbrowser.open(chrome, "http://www.tecvinson.se")


# new = 2 # open in a new tab, if possible

# open a public URL, in this case, the webbrowser docs
# url = "http://www.tecvinson.se"
# webbrowser.get(using='google-chrome').open(url,new=new)

# chrome_path = 'C:\\Users\\VIOKE\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe'
# urL = 'http://docs.python.org/'
# # webbrowser.get(chrome_path).open(urL)
# webbrowser.register('chrome', webbrowser.BackgroundBrowser(chrome_path))
# webbrowser.get('chrome').open_new_tab(urL)

import webbrowser

url = 'https://pythonexamples.org'
webbrowser.register('chrome',
	None,
	webbrowser.BackgroundBrowser("C:\\Users\\VIOKE\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe"))
webbrowser.get('chrome').open(url)