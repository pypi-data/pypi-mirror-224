import os
import json
import socket
import requests
import tkinter as tk
from tkinter import *
import pyrebase as fb
import time 
import threading

class pychatverse:
    
    """
    PyChatVerse is a simple chat application that allows users to chat with each other in real time.
    It provides features such as global chat, private chat, and user-friendly interface.
    """

    #
    COLORS = ["green", "blue", "red", "orange", "purple",   "magenta",  "indigo"]  

    project_name = "Py-ChatVerse"

    # Display Home main menu
    home_message = f"""
\033[1;35m╭───────────────────────────────╮\033[m
\033[1;35m│    \t{project_name} (Home)    \033[m
\033[1;35m╰───────────────────────────────╯\033[m

\033[1;32m   1. Global Chat. 🌎\033[m
\033[1;32m   2. Private Chat. 🔒\033[m
\033[1;32m   3. Feedback. 💬\033[m
\033[1;32m   4. Help. 📚\033[m
\033[1;31m   5. Exit. ❌\033[m
"""

    room_control = f"""
\033[1;35m╭───────────────────────────────╮\033[m
\033[1;35m│    {project_name} (Room Control)    \033[m
\033[1;35m╰───────────────────────────────╯\033[m

\033[1;32m   1. Create a New Room. ➕\033[m
\033[1;32m   2. Join an Existing Room. ➡️\033[m
\033[1;32m   3. Go Back. ↩️\033[m
\033[1;31m   4. Exit. ❌\033[m
"""

    help_message = f"""
\033[1;35m╭━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╮\033[m
  \033[1;35m\033[1;35m         \t*{project_name} Help*          \033[m\033[m
\033[1;35m╰━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╯\033[m

\033[1;37mThis project is a simple chat application that allows you to chat with other users in real time. 💬\033[m

\033[1;32m**Commands** 📝\033[m

    \033[1;36m1. 'Global Chat' 🌎\033[m - Opens a chat window where you can chat with all other users.
    \033[1;36m2. 'Private Chat' 🔒\033[m - Opens a chat window where you can chat with a specific user.
    \033[1;36m3. 'Exit' ❌\033[m - Exits the chat application.

\033[1;37m**To create a private chat, you must first create a room. To do this, enter the following command:**\033[m

    \033[1;36m1. 'Create a New Room' ➕\033[m

\033[1;37mOnce you have created a room, you can join it by entering the following command:\033[m

    \033[1;36m2. 'Join an Existing Room' ➡️\033[m

\033[1;37m**To chat with other users, simply enter your message and press Enter.** 💬\033[m

\033[1;32m**For more help, please visit the project's GitHub repository:** 📚\033[m

  \033[4;34mhttps://github.com/dayanidigv/Py-ChatVerse\033[m 

"""
    feedback_message = f"""
\033[1;32mWelcome to {project_name} Feedback! 🌟

\033[1;32mWe appreciate your feedback on PyChatVerse. 🙌

\033[1;32mPlease take a moment to share your thoughts with us. 💬
    """

    feedback_thankyou_message = f"""
\033[1;32mThank you for your feedback on {project_name}! 🎉

\033[1;32mYour input helps us enhance the PyChatVerse experience. 👍

\033[1;32mWe value your contribution to making our package better. 💪\033[m 
    """

    def __init__(self,start = False):
        """
        Initialize the PyChatApp instance and start the application.
        """
        
        db = self.get_firebase_config()
        if(start):
            if db:
                self.home(db)


    def stylized_input(self, prompt, single_line=True):
        """
        Display a stylized input prompt and get user input.

        Args:
            prompt (str): The prompt message to display.
            single_line (bool): Flag to indicate whether to use single line style.

        Returns:
            str: User's input.
        """


        if single_line:
            print("\033[1;35m╭───────────────────────────────╮\033[m")
            user_input = input(f"\033[1;35m│    \033[m{prompt}\033[m ")
            print("\033[1;35m╰───────────────────────────────╯\033[m")
        else:
            print(f"\033[1;35m    \033[m{prompt}")
            print("\033[1;35m╭───────────────────────────────\033[m")
            user_input = input("\033[1;35m│    Enter your input: \033[m")
            print("\033[1;35m╰───────────────────────────────╯\033[m")
        return user_input




    def error(self,msg):
        """
        Display an error message.

        Args:
            msg (str): The error message to display.
        """


        print(f"""\033[1;31m {msg} \033[m""")

    def success(self,msg):
        """
        Display a success message.

        Args:
            msg (str): The success message to display.
        """


        print(f"\033[1;32m   {msg}\033[m")

    def sendFeedback(self,message):
        """
        Send user feedback to a Telegram bot.

        Args:
            message (str): The feedback message to send.

        Returns:
            bool: True if the feedback was successfully sent, False otherwise.
        """

        feedback = f"""
        Feedback From PyChatVerse✔️

        Feedback:\t{message}
        """
        resp = requests.post(f"https://api.telegram.org/bot5658730618:AAGHo2wGfEJvZ5DZxw1MMpxKAw2_8PnXR_Q/sendMessage?chat_id=1221832086&text={feedback}")
        if resp.status_code == 200:
            return True
        else:
            return False

    def feedback(self,message = None):
        """
        Collect and send user feedback.

        Args:
            message (str, optional): The feedback message to send. If None, prompt for user input.
        """

        if not message:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(pychatverse.feedback_message)
            message = self.stylized_input("Please share your feedback",single_line=False)
        my_thread = threading.Thread(target=self.sendFeedback, args=(message,))
        my_thread.start()
        #os.system('cls' if os.name == 'nt' else 'clear')
        print(pychatverse.feedback_thankyou_message)
        
    def help(self):
        """
        Display the help information for the chat application.
        """

        os.system('cls' if os.name == 'nt' else 'clear')
        print(pychatverse.help_message)
        input()

    def check_internet_connection(self):
        """
        Check if the device has an active internet connection.

        Returns:
            bool: True if internet connection is available, else False.
        """

        try:
            socket.create_connection(("8.8.8.8", 53), timeout=3)
            return True
        except OSError:
            return False
    
    def get_firebase_config(self):
        """
        Get the Firebase configuration and initialize the database connection.

        Returns:
            firebase.database.Database: Firebase database instance.
        """

        if self.check_internet_connection():
            try:
                url = "https://dayanidigv.github.io/PyConsoleChat.json"
                response = requests.get(url)
                if response.status_code == 200:
                    response_text = response.text
                    json_start = response_text.find('{')
                    json_end = response_text.rfind('}') + 1
                    json_data = response_text[json_start:json_end]
                    parsed_json = json.loads(json_data)
                    firebaseConfig = parsed_json
                    if firebaseConfig:
                        firebase = fb.initialize_app(firebaseConfig)
                        self.db = firebase.database()
                        return self.db
                self.error("Firebase configuration not found in the response.")
            except Exception as e:
                self.error("Failed to initialize Firebase:", e)
        else:
            self.error("Check Your Internet Connection.")
        return None

    def send_message(self,RoomID, name, message_entry):
        """
        Send a message to the chat room.

        Args:
            RoomID (str): ID of the chat room.
            name (str): User's name.
            message_entry (tk.Entry): Entry widget for message input.
        """

        message = message_entry.get()
        if message:
            data = {"name": name, "message": message}
            try:
                if RoomID:
                    self.db.child(RoomID).child("messages").push(data)
                    message_entry.delete(0, tk.END)
            except Exception as e:
                self.error("Failed to send message:", e)

    def get_user_color(self,user_name):
        """
        Get a unique color for the user's messages.

        Args:
            user_name (str): User's name.

        Returns:
            str: Color code.
        """

        user_index = abs(hash(user_name)) % len(pychatverse.COLORS)
        return pychatverse.COLORS[user_index]

    def chat_container(self,RoomID, name, delete_room):
        """
        Display the chat interface for a chat room.

        Args:
            RoomID (str): ID of the chat room.
            name (str): User's name.
            delete_room (bool): Whether the user created the room.
        """

        if RoomID == "Global":
            self.success(f"Successfully Joined {RoomID} Room.")
            try:
                people_count = self.db.child(RoomID).child("peopleCount").get().val()
                if people_count:
                    self.db.child(RoomID).child("peopleCount").set(people_count + 1)
                else:
                    self.db.child(RoomID).child("peopleCount").set(1)
            except Exception as e:
                #self.error("Failed to update People Count:", e)
                pass
        self.chat_window = tk.Tk()
        self.chat_window.title(f"{pychatverse.project_name} - Room: {RoomID} {'(Creator)' if delete_room else '(joiner)' if RoomID != 'Global' else ''}")
        self.chat_window.geometry("400x600")
        self.chat_window.config(background="lightgray")
        self.frame = LabelFrame(
        self.chat_window,
        text=f"Hello, {name}! Nice to meet you.",
        bg='#f0f0f0',
        font=(20)
        )
        self.frame.pack(expand=True, fill=BOTH)
        self.my_label = Label(self.frame,text = "")
        if RoomID != "Global":
            if delete_room:
                self.my_label.config(text = "Waiting For Joiner...")
                self.my_label.configure(foreground="red", font=("Helvetica", 12))
        self.my_label.pack()
        self.messages_frame = tk.Frame(self.frame)
        self.messages_frame.pack(fill=tk.BOTH, expand=True)
        self.scrollbar = tk.Scrollbar(self.messages_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.messages_text = tk.Text(self.messages_frame, wrap=tk.WORD, yscrollcommand=self.scrollbar.set)
        self.messages_text.pack(fill=tk.BOTH, expand=True)
        self.scrollbar.config(command=self.messages_text.yview)
        for color in pychatverse.COLORS:
            self.messages_text.tag_configure(color, foreground=color, font=("Helvetica", 15))
        
        self.messages_text.config(background="lightgray")
        message_entry = tk.Entry(self.chat_window, font=("Helvetica", 15))
        message_entry.pack(fill=tk.X, padx=10, pady=5)

        send_button = tk.Button(self.chat_window, text="Send", font=("Helvetica", 15), bg="#007bff", fg="white",
                                activebackground="#0056b3", activeforeground="white",
                                command=lambda: self.send_message(RoomID, name, message_entry))
        send_button.pack(pady=5)
       
        self.update_chat(RoomID,name)
        self.chat_window.mainloop()
        if delete_room:
            self.db.child(RoomID).remove()
        else:
            self.db.child(RoomID).child("connection").set(False)
        if RoomID == "Global":
            try:
                people_count = self.db.child(RoomID).child("peopleCount").get().val()
                if people_count:
                    self.db.child(RoomID).child("peopleCount").set(people_count - 1)
                else:
                    self.db.child(RoomID).child("peopleCount").set(0)
            except Exception as e:
                #self.error("Failed to update People Count:", e)
                pass
        exit(0)
        

    def update_chat(self,RoomID,name):
        """
        Update the chat window with new messages.

        Args:
            RoomID (str): ID of the chat room.
            name (str): User's name.
        """

        try:
            if RoomID  != "Global":
                joiner = self.db.child(RoomID).child("connection").get().val()
                if joiner:
                    self.my_label.config(text = "Connected..")
                    self.my_label.configure(foreground="green", font=("Helvetica", 12))
                else:
                    self.my_label.config(text = "Not Connected")
                    self.my_label.configure(foreground="red", font=("Helvetica", 12))
            else:
                user_count = self.db.child(RoomID).child("peopleCount").get().val()
                if user_count <= 1:
                    self.my_label.config(text = "No one is currently online.")
                    self.my_label.configure(foreground="red", font=("Helvetica", 12))
                else:
                    self.my_label.config(text = f"{user_count - 1} people are now online.")
                    self.my_label.configure(foreground="green", font=("Helvetica", 12))
            messages_ref = self.db.child(RoomID).child("messages")
            messages = messages_ref.get().val()
            total_messages = int(self.messages_text.index(tk.END).split('.')[0]) - 2
            if messages:
                msg = 0
                for message_id, message_data in messages.items():
                    msg = msg + 1
                    sender_name = message_data['name'] if name != message_data['name'] else "you" if message_data['name'] != pychatverse.project_name else pychatverse.project_name
                    style = self.get_user_color(sender_name)
                    message = message_data['message']
                    formatted_message = f"ㅤ{sender_name} : {message}\n"
                    if msg > total_messages:
                        self.messages_text.insert(tk.END, formatted_message, style)
        except Exception as e:
            self.error("Failed to update chat:", e)

        def _update_chat():
            self.update_chat(RoomID, name)
        self.messages_text.after(1000, _update_chat)


    def create_room(self,name,RoomID):
        """
        Create a new chat room.

        Args:
            name (str): User's name.
            RoomID (str): ID for the new chat room.
        """

        while not name:
            name = self.stylized_input("Enter Your Name: ")
            if not name:
                self.error("Name cannot be empty. Please enter your name.")
        while not RoomID:
            RoomID = self.stylized_input("Enter your Room ID: ")
            if not RoomID:
                self.error("Room ID cannot be empty. Please enter a valid Room ID.")
        try:
            room_ref = self.db.child(RoomID)
            room_data = room_ref.get()
            if room_data.val() is not None:
                self.error(f"Room ID '{RoomID}' already exists.")
            else:
                self.db.child(RoomID).child("connection").set(False)
                self.db.child(RoomID).child("creater").set(name)
                self.success(f"Successfully Room {RoomID} created")
                self.chat_container(RoomID, name , True)
        except Exception as e:
            self.error(f"Failed to create Room {RoomID}: {e}")
 
    
    def join_room(self,name,RoomID):
        """
        Join an existing chat room.

        Args:
            name (str): User's name.
            RoomID (str): ID of the chat room to join.
        """

        while not name:
            name = self.stylized_input("Enter Your Name: ")
            if not name:
                self.error("Name cannot be empty. Please enter your name.")
        while not RoomID:
            RoomID = self.stylized_input("Enter your Room ID: ")
            if not RoomID:
                self.error("Room ID cannot be empty. Please enter a valid Room ID.") 
        try:
            room_ref = self.db.child(RoomID)
            room_data = room_ref.get()
            if room_data.val() is not None:
                self.db.child(RoomID).child("connection").set(True)
                self.success(f"\nSuccessfully joined Room {RoomID}.")
                self.chat_container(RoomID, name, False)
                os.system('cls' if os.name == 'nt' else 'clear')
            else:
                self.error(f"\nRoom ID '{RoomID}' does not exist.")
                self.error("press Enter key to Join Other Room.")
                input()
        except Exception as e:
            self.error(f"Failed to join the room: {e}")

    def GlobalChat(self, name = None):
        """
        Join the global chat room.

        Args:
            name (str, optional): User's name. If None, prompt for user input.
        """

        while not name:
            name = self.stylized_input("Enter Your Name: ")
            if not name:
                self.error("Name cannot be empty. Please enter your name.")
        self.chat_container("Global", name, False)
        os.system('cls' if os.name == 'nt' else 'clear')
        exit(0)

    def PrivateChat(self,creater = False,joiner = False,RoomID = None,name = None):
        """
        Manage private chat functionalities.

        Args:
            creater (bool, optional): Create a new private chat room. Default is False.
            joiner (bool, optional): Join an existing private chat room. Default is False.
            RoomID (str, optional): ID of the private chat room.
            name (str, optional): User's name. If None, prompt for user input.
        """

        if creater:
            self.create_room(name,RoomID)
        elif joiner:
            self.join_room(name,RoomID)
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(pychatverse.room_control)
            ch = self.stylized_input("Enter your Choice: ")
            if ch == "1":
                self.create_room(name,RoomID)
            elif ch == "2":
                self.join_room(name,RoomID)
            elif ch == "3":
                self.home()
            elif ch == "4":
                exit(0)
            else:
                self.error("Choice invalid")
        exit(0)

    def home(self,ref=False):
        """
        Display the main menu and handle user choices.

        Args:
            ref (bool, optional): Flag to refresh the menu. Default is False.
        """

        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(pychatverse.home_message)
            if not ref:
                ch = self.stylized_input("Enter your Choice: ")
            else:
                self.home()
            if ch == "1":
                self.GlobalChat()
            elif ch == "2":
                self.PrivateChat()
            elif ch == "3":
                self.feedback()
            elif ch == "4":
                self.help()
            elif ch == "5":
                exit(0)
            else:
                self.error("Choice invalid")

if __name__ == "__main__":
    app = pychatverse(start=True)