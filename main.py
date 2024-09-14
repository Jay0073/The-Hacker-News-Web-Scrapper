from customtkinter import *
from tkinter import TclError
import extractNews
import requesting
import webbrowser

# Set the appearance mode to dark
set_appearance_mode("dark")
root = CTk()
root.title("The Hacker News - Jay")
root.geometry("900x600")
root.resizable(False, False)

# Global variable to keep track of the current main frame
main_frame = None

def create_news(news):
    global main_frame

    # Destroy the previous main frame if it exists
    if main_frame is not None:
        main_frame.destroy()

    # Create a new main frame
    main_frame = CTkFrame(root, fg_color='#2b2b2b')
    main_frame.pack(pady=10, padx=(10, 20), fill='both', expand=True)

    # Title label
    title_label = CTkLabel(main_frame, text=news[1], font=('Arial', 22, 'bold'), wraplength=500)
    title_label.pack(pady=10)

    # Frame for side-by-side labels
    side_by_side_frame = CTkFrame(main_frame, fg_color='#2b2b2b')
    side_by_side_frame.pack(pady=10, fill='x')

    # Left label
    left_label = CTkLabel(side_by_side_frame, text=news[4], font=('Arial', 17))
    left_label.pack(side='left', padx=30)

    # Right label
    right_label = CTkLabel(side_by_side_frame, text=news[2], font=('Arial', 17))
    right_label.pack(side='left', padx=30)

    # Big label to display the main content
    big_label = CTkLabel(main_frame, text=f"{news[3]}...", font=('arial', 16), wraplength=550, justify='left')
    big_label.pack(pady=10, fill='both', expand=True, padx=15)

    # Button to open the web link
    linkBut = CTkButton(main_frame, text="Web Link", font=(None, 15), command=lambda: webbrowser.open_new_tab(news[0]))
    linkBut.pack(anchor='center', pady=20)

def on_enter(event):
    try:
        # Change text color to black on hover
        event.widget.config(fg='black')
    except TclError:
        pass

def on_leave(event):
    try:
        # Change text color back to white when not hovering
        event.widget.config(fg='white')
    except TclError:
        pass

def add_labels(frame, button, list):
    for news in list:
        # Create a label for each news item
        label = CTkLabel(frame, text=f"{news[1][:17]}...", font=('arial', 20), width=220, anchor='w')
        label.pack(pady=5)
        # Bind click and hover events to the label
        label.bind("<Button-1>", lambda event, news=news: create_news(news))
        label.bind("<Enter>", on_enter)
        label.bind("<Leave>", on_leave)

def getNews(button, label):
    # Request and extract news data
    soup = requesting.requestSoup()
    newsList = extractNews.extract(soup=soup)

    # Create a scrollable frame for the news labels
    sideFrame = CTkScrollableFrame(root, width=220)
    sideFrame.pack(side='left', pady=10, padx=10, fill=Y)

    # Add news labels to the scrollable frame
    add_labels(sideFrame, getBut, newsList)
    # Hide the button and info label after fetching news
    button.pack_forget()
    label.pack_forget()

# Title label for the main window
titleLabel = CTkLabel(root, text='Cyber Security News', font=('san serif', 40))
titleLabel.pack(pady=10)

# Info label with description
infoLabel = CTkLabel(root, text='Hacker News is a popular online community focused on technology news and discussion. Hacker News is a valuable resource for tech enthusiasts, developers, and entrepreneurs looking to stay updated on the latest trends and innovations in the tech world.\n\nThis GUI is designed to display cybersecurity news articles in an interactive and user-friendly manner.\n\nClick below button to get the latest news.', font=('san serif', 20), wraplength=600)
infoLabel.pack(pady=10)

# Button to fetch the latest news
getBut = CTkButton(root, text="Get News", command=lambda: getNews(getBut, infoLabel), font=(None, 20))
getBut.pack(anchor='center', pady=50)

root.mainloop()
