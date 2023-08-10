# PyChatVerse - Real-Time Chat Application

![](https://dayanidigv.github.io/PyChatVerse/Images/pychatversepng.png)
PyChatVerse is an innovative and user-friendly chat application package for Python, designed to provide a seamless real-time communication experience. With a focus on simplicity, interactivity, and versatility, PyChatVerse enables users to engage in both global and private chat rooms, making it an ideal solution for a wide range of communication needs.


## Key Features:

- **Global Chat**: Immerse yourself in the lively atmosphere of the global chat room, where users from various backgrounds and locations converge to share thoughts, opinions, and experiences.

- **Private Chat Rooms**: Foster more intimate and exclusive conversations by creating or joining private chat rooms, enabling focused interactions with specific individuals.

- **Stylized Input Prompts**: Enjoy an aesthetically pleasing and user-friendly input interface that enhances the chat experience by offering visually appealing prompts.

- **Real-Time Message Updates**: Stay connected and engaged with instant updates on new messages, ensuring that you're always part of the ongoing conversations.

- **Feedback Integration**: Provide valuable insights and suggestions by seamlessly sharing your feedback with the developers from within the application.



# Installation:

## Getting started with PyChatVerse is a breeze:

### Install the package using the simple `pip` command:
   

```bash
pip install PyChatVerse
```


# Usage:
## Import and integrate the PyChatVerse module within your Python codebase:


### Initialize the chat application and display the main menu
```python
import PyChatVerse as py
# Initialize the chat application and display the main menu
chat = py.pychatverse(start=True)
```
output:
```
╭───────────────────────────────╮
│       Py-ChatVerse (Home)    
╰───────────────────────────────╯

   1. Global Chat. 🌎
   2. Private Chat. 🔒
   3. Feedback. 💬
   4. Help. 📚
   5. Exit. ❌

╭───────────────────────────────╮
│    Enter your Choice:
```


# Global Chat
## Join the Global Chat

You can easily join the global chat using the PyChatVerse package.



### Option 1: Join Global Chat with User Input
```python
import pychatverse as py

chat = py.pychatverse()

# Join the global chat with user input
chat.GlobalChat()
```
ouput:
```
╭───────────────────────────────╮
│    Enter Your Name:  Dayanidi
╰───────────────────────────────╯
   Successfully Joined Global Room.
```



### Option 2: Join Global Chat with Specified Name
```python
import pychatverse as py

chat = py.pychatverse()
```


```python
# Join the global chat with a specified name
chat.GlobalChat(name = "Dayanidi")
```
ouput:
```
Successfully Joined Global Room.
```
Now open chat windows instantly and start engaging in the global chat with other users.



# Private Chats
## Create or join private chat rooms
### You can also create and join private chat rooms using the PyChatVerse package.

```python
import pychatverse as py

chat = py.pychatverse()
```

##   Display the private chat room menu

```python
chat.PrivateChat()
```

output:
```
╭───────────────────────────────╮
│    Py-ChatVerse (Room Control)    
╰───────────────────────────────╯

   1. Create a New Room. ➕
   2. Join an Existing Room. ➡️   
   3. Go Back. ↩️
   4. Exit. ❌

╭───────────────────────────────╮
│    Enter your Choice:

```



## Create a private chat room with User Input
```python
chat.PrivateChat(creater=True)
```

output:
```
╭───────────────────────────────╮
│    Enter Your Name:  Surya
╰───────────────────────────────╯
╭───────────────────────────────╮
│    Enter your Room ID:  123@
╰───────────────────────────────╯
   Successfully Room 123@ created
```
Now open chat windows instantly and start engaging in the global chat with other users.



## Join a private chat room with User Input

```python
chat.PrivateChat(joiner=True)
```

output:
```
╭───────────────────────────────╮
│    Enter Your Name:  Surya
╰───────────────────────────────╯
╭───────────────────────────────╮
│    Enter your Room ID:  123@
╰───────────────────────────────╯
   Successfully Room 123@ Joined
```
Now open chat windows instantly and start engaging in the global chat with other users.


```python
# Create a private chat room as the creator
chat.PrivateChat(creater=True,name="Surya",RoomID="123@")
```


```python
# Join a private chat room as a participant
chat.PrivateChat(joiner=True,name="Daya",RoomID="123@")
```


# Providing Feedback
### You can share your feedback on PyChatVerse using the following commands:

```python
# Provide feedback without a message
chat.feedback()
```

```python
# Provide feedback with a message
chat.feedback(message="yeah! it's Good")
```


# Getting Help

```python
# Display the help message
chat.help()
```
Now you can explore and use the various features of PyChatVerse to engage in real-time chats and communication!



# Portfolio

## Explore more of my projects and work on my portfolio:

 ### [Dayanidi's Portfolio](http://dayanidiportfolio.github.io/) 


# Contact

 For questions, feedback, and inquiries, please email [dayanidigv954@gmail.com](mailto:dayanidigv954@gmail.com).

Connect with me on [GitHub](https://github.com/dayanidigv) and [LinkedIn](https://www.linkedin.com/in/dayanidi-gv-a37732249/).

[Project Repository](https://github.com/dayanidigv/PyChatVerse)
