# 🖊 How to contribute to Repl Customs! <img src="https://img.shields.io/github/issues-pr/IreTheKID/repl-customs.svg"> <img src="https://img.shields.io/github/issues/IreTheKID/repl-customs.svg">

 
First of all, if you're new here, thanks for your consideration to contribute to Repl Customs! 😀 This guide will help you get started and walk you the process of making improvements or changes to the Repl Customs web application.

### Opening Issues

If you want to open an issue for a bug/problem please make sure to include a code snippet of the issue or a link to  the file(s) in which the problem is located. If you already have fix or suggestion for the issue you opened please include a code snippet or link it as well as a description of your fix.

### Opening A Pull Request 

*details will be coming soon!*

### Modifying the Code

When you set up an environment to modify the code for the web-app, you'll need a CSRF token to run it or Flask will throw a fit. You can generate a 16 character token in Python with the built-in `secrets` module. Generate one and change the token to match with this code:

```python
import secrets

token = secrets.token_hex()
app.config['SECRET_KEY'] = token
```

Since this token will be unique to you, the code will need to be changed back before it can merged into the master branch.

# Conclusion

I hope this has helped you out and again I thank you for your contributions! Happy Coding! 👏🎉
