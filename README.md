# [TechLifeJournal](https://techlifejournal.com)

#### Description
platform to read articles, news and updates all over the tech community and place to share knowledge and bring value to the community

####
<img src="https://res.cloudinary.com/practicaldev/image/fetch/s--ds97LCK---/c_imagga_scale,f_auto,fl_progressive,h_420,q_auto,w_1000/https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ymlmr15l83rrjq8natft.jpg" alt="Hacktobar" />
<img src="https://camo.githubusercontent.com/f5054ffcd4245c10d3ec85ef059e07aacf787b560f83ad4aec2236364437d097/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f636f6e747269627574696f6e732d77656c636f6d652d627269676874677265656e2e7376673f7374796c653d666c6174" alt="contributions welcome" data-canonical-src="https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat" style="max-width: 100%;">

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/techlifejournal/techlifejournal-backend.git
$ cd teachlifejournal-backend
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ python venv -m env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd project
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.
