# template_letters

To get started, you need Python 3 installed. I use python 3.9, but this may work on lower versions. 

in the root of the repository, type in the following:

```
$ python3 -m venv venv
```
```
$ source venv/bin/activate
```
```
(venv) $ pip3 install -r requirements.txt
```

Finally, to run the program:
```
(venv) $ flask run
```
Then, go to `localhost:5000` in your web browser to see the template form. Feel free to edit bulletpoints.txt to customize it to your needs. 

In `bulletpoints.txt`, The string `SPLIT_HERE` is used to make a new paragraph. 

In `defaults.py`, feel free to change the default `greeting`, `intro`, and `outtro`.

In the root directory of the repo, you need to make a .env file with the following data entered, feel free to copy/paste, and edit to your needs:
```
first_name="James"
last_name="Ng"
SECRET_KEY="hackerz"
```