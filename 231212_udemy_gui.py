
import tkinter

window = tkinter.Tk()
window.title("Manager Center")
window.minsize(width=500, height=300)

wiki_search = tkinter.Label (text="search")
wiki_search.grid(row=0, column=0, padx=10, pady=10)

wiki_search_btn = tkinter.Button (text="Click")
wiki_search_btn.grid(row=0, column=1, padx=10, pady=10)



day_off = tkinter.Label (text="day_off")
day_off.grid(row=0, column=5, padx=10, pady=10)

dev_build = tkinter.Label (text="dev_build")
dev_build.grid(row=1, column=5, padx=10, pady=10)

find_issue = tkinter.Label (text="find_issue")
find_issue.grid(row=2, column=5, padx=10, pady=10)


















window.mainloop()