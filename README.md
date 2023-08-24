# Password-Vault-Webapp
A webapp that will take care of remembering your passwords and keeping them secure.

# How to Run
1. Move to the directory which contains the requirements.txt file 
2. Run `pip install -r requirements.txt`
3. Run `py manage.py runserver`
4. Visit http://127.0.0.1:8000/

# Product Backlog

- | Id | Feature title                                    | Start     |    End    |   Status    |
- | 01 | About us Page introducing the app                | 17-7-2023 | 18-7-2023 |  Complete   |
- | 02 | Login and register page and navbar               | 17-7-2023 | 18-7-2023 |  Complete   |
- | 03 | Add password and according website               | 17-7-2023 | 20-7-2023 |  Complete   |
- | 04 | Encrypt password inside database                 | 17-7-2023 | 20-7-2023 |  Complete   |
- | 05 | Display cards with copy password to clipboard btn| 17-7-2023 | 21-7-2023 |  Complete   |
- | 06 | Password Generator recommendation                | 17-7-2023 | 21-7-2023 |  Complete   |

# Distinctiveness and Complexity
PassGuard is the name of this web app. Basically, it is an app that stores all your passwords in a safe place. I have decided to pick this as my project of choice because I've noticed many people constantly forgetting their passwords and storing them in places like their notes app which is not safe at all. It is clearly distinct from all the other projects built in this course before. It has no relation to commerce,social network, wikipedia, and email front-end platform. However, the previous projects gave me the required skills to build this project. I was comfortable with Django and Javascript thanks to the previous projects of CS50 Web. 

In terms of complexity this web app was actually kind of complex to build because I wanted a smart way of storing the passwords in the database. 
If I stored the passwords without encrypting them then anyone with access to the database could use the passwords. 
However, if I encrypted them and stored the encryption keys in the database then hackers (people with access to the database) could easily decrypt the encrypted passwords. 
So it took me a while to think of a solution for this problem. Finally, I thought of generating an encryption key for everyone that shows up only once when the user signs up. 
This encryption key will be the responsibility of the user to keep somewhere safe. Either a physical copy or on some notepad. Then this encryption key will be required when saving a password. And also required when you want to view the saved password. I picked this choice so that if someone has access to the database all they see is a bunch of encrypted passwords with no way to decrypt them. And all the user has to do is to keep one encryption key safe. 
If the wrong encryption key is inserted then the "fernet" library spots that when it tries to decrypt the password and raises an error. (This will all be made clearer in the video of this project.) 

As for the requirements of this project. This project does utilize Django framework which was very useful for the back-end and Javascript was used in this project on the front-end. Furthermore, this application is mobile-responsive as shown in the 
Therefore, this project was complex enough (in terms of keeping the passwords secure) and distinct from all the other projects.

# File Contents
For this section I am going to explain the contents of the files that I have used and not all the files of the project since the Django framework sets up many files for its own functionality.
Firstly, vault is the application of this specific project under the vault directory admin.py contains the registering of the models used in this project,
models.py contains the database object models (password and User),
urls.py contains all the paths, views.py contains all the backend logic used for this project.
Under the static folder you will find 3 things one an image used for this project to add a card, a css file used for the front end, and a javascript file used to manipulate the front-end and make API calls to the back-end.
Migrations directory contains the database created by the models.py file when it is run.
Under templates -> vault there are html files, layout.html contains the navbar shared across all pages, a login.html and register.html page, an aboutus.html page, an addpassword.html a mainuserpage.html that contains all the users card for passwords, and lastly a masterkey.html page which generates a encryption and decryption key that shows up once for every user. (This will all be made clearer in the video of this project.) 






