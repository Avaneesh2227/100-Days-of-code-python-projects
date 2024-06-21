from tkinter import *
from tkinter import messagebox
import random
import json

def create_pw(website,uname,pw):
    new_data={
        website: {
        "email": uname,
        "password": pw
    }
    }
    if len(website)==0 or len(pw)==0:
        messagebox.showinfo(title="Oops", message="Please dont leave any fields empty")
    else:
        is_ok=messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail/Username:{uname} \n Password:{pw}\n Is it okay to save?")
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)

            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data,data_file,indent=4)
            else:
                data.update(new_data)
                with open("data.json","w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                website_label.delete(0, END)
                pw_label.delete(0, END)
                #json.dump(new_data, data, indent=4)
                #var=json.load(data) converts data into a dictionary
                #data.write(f"{website} | {uname} | {pw}\n")
                '''
                    #How to update json data
                    with open("data.json","r") as data_file:
                        data=json.load(data_file)
                        data.update(new_data)
                    with open("data.json","w") as data_file:
                       json.dump(data,data_file,indent=4)
                '''


#Password Generator Project
def create_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
    one=[random.choice(letters) for _ in range(nr_letters)]
    two=[random.choice(symbols) for _ in range(nr_symbols)]
    three=[random.choice(numbers) for _ in range(nr_numbers)]
    password_list = one+two+three
    password="".join(password_list)
    pw_label.insert(0,password)

def find_password(search):
    try:
        with open("data.json","r") as data_file:
            data=json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message="Error. Please add a password first!")
    else:
        search=search.capitalize()
        if search in data:
            messagebox.showinfo(title=search, message=f"{data[search]['email']}\n{data[search]['password']}")
        else:
            messagebox.showinfo(title="Oops", message="Error. No record of website found!")

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
myimg = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=myimg)
canvas.grid(row=0, column=1)



website_name = Label(text="Website: ")
website_name.grid(row=1, column=0)
website_label = Entry(width=20)
website_label.grid(row=1, column=1,sticky="EW")
website_label.focus()

search=Button(text="Search",command=lambda:find_password(website_label.get()))
search.grid(row=1,column=2, sticky="EW")


email_name = Label(text="Email/Username: ")
email_name.grid(row=2, column=0)
email_label = Entry(width=35)
email_label.grid(row=2, column=1,columnspan=2,sticky="EW")
email_label.insert(0,"12appu04@gmailcom")

pw_name = Label(text="Password: ")
pw_name.grid(row=3, column=0)
pw_label = Entry(width=20)
pw_label.grid(row=3, column=1,sticky="EW")

pw_button = Button(text="Generate", command=create_password)
pw_button.grid(row=3, column=2,sticky="EW")
add_button = Button(text="Add", width=36,command=lambda: create_pw(website_label.get(),email_label.get(),pw_label.get()))
add_button.grid(row=4, column=1,columnspan=2,sticky="EW")

window.mainloop()

