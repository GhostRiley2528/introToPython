import webbrowser

def open_url():
    webbrowser.open("https://www.youtube.com")

def open_urls():
    webbrowser.open("https://www.codingal.com")

# Open YouTube and Codingal
choice = int(input("Choose an option: 1. Open YouTube and Codingal 2.\n"))

if choice == 1:
    open_url()
elif choice == 2:
    open_urls()
else:
    print("Invalid choice. Opening Both.")
    open_url()
    open_urls()
