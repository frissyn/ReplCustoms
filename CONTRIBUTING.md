# 🖊 How to contribute to Repl Customs <img src="https://img.shields.io/github/issues-pr/IreTheKID/repl-customs.svg"> <img src="https://img.shields.io/github/issues/IreTheKID/repl-customs.svg">

 
First of all, if you're new here, thanks for your consideration to contribute to Repl Customs! 😀 This guide will help you get started and walk you the process of making improvements or changes to the Repl Customs web application.

### What do I need to know?
Repl-Customs is a web application built on the Flask micro-web framework. The languages used to run are Python 3, JavaScript, and the web markup languages HTML and CSS. If you have any level of skill beyond beginner in any these languages, then you're good to contribute to Repl-Customs! If you want to work on the frontend side of RC, then head over to the `templates` folder! If you want to work on the backend, then check out the `app.py` file!

### Opening Issues

If you want to open an issue for a bug/problem please make sure to include a code snippet of the issue or a link to  the file(s) in which the problem is located. If you already have fix or suggestion for the issue you opened please include a code snippet or link it as well as a description of your fix. Simply follow the Issue template of your choice and you should be good for approval.

### Opening A Pull Request 

When opening a pull request please make sure your changes only affect one file at one time. If you need to change multiple files, then please open multiple pull requests and make it clear in your descriptions that they are are corresponding pull requests. Just like with opening an issue, please be as clear as possible when describing the reason you have opened a pull request. Only change multiple files in one pull request if the same shange is being made to each of the files, such as adding a back button to a few of the template files.

### Describing Your Pull Request
In the RC repository, we like to use emojis to describe and classify our changes; here's a list for you to check before you get started.

+ 🔥 The Fire emoji is for changes that mark a file ready for a new release
+ ✏️ The Pencil emoji is for minor *changes* to a file such as spelling errors or syntax changes.
+ 🖋️ The Pen emoji is for minor *additions* to a file such as a new feature.
+ ❗ The Exclamation emoji is for changes to information such as new info in the Markdown files.
+ ➕ The Plus emoji is for the addition of a file that didn't exist before.
+ ⭐ The Star emoji is for the addtiotion of a feature that didn't exist before.

### Modifying the Code

When you set up an environment to modify the code for the web-app, you'll need a CSRF token to run it or Flask will throw a fit. You can generate a 16 character token in Python with the built-in `secrets` module. In the code that starts the Flask app in `app.py` you'll need to put in your generated token at `line 72`:

Instead of:
```python
KEY = os.getenv('APP_KEY')

app = Flask(__name__)
app.config['SECRET_KEY'] = KEY
```

Do:
```python
KEY = secrets.token_hex()

app = Flask(__name__)
app.config['SECRET_KEY'] = KEY
```

Since this token will be unique to you, the code will need to be changed back before it can merged into the master branch.

### Conclusion
I hope this has helped you out and again I thank you for your contributions! Happy Coding! 👏🎉
