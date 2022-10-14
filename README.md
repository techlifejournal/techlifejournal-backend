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

## Contributing

If you want to contribute to a project and make it better, your help is very welcome. Contributing is also a great way to learn more about social coding on Github, new technologies and and their ecosystems and how to make constructive, helpful bug reports, feature requests and the noblest of all contributions: a good, clean pull request.


### How to make a clean pull request

- Create a personal fork of the project on Github.
- Clone the fork on your local machine. Your remote repo on Github is called `origin`.
- Add the original repository as a remote called `upstream`.
- If you created your fork a while ago be sure to pull upstream changes into your local repository.
- Create a new branch to work on! Branch from `development` if it exists, else from `master`.
- Implement/fix your feature, comment your code.
- Follow the code style of the project.
- Add or change the documentation as needed.
- Squash your commits into a single commit with git's [interactive rebase](https://help.github.com/articles/interactive-rebase). Create a new branch if necessary.
- Push your branch to your fork on Github, the remote `origin`.
- From your fork open a pull request in the correct branch. Target the project's `development` branch if there is one, else go for `master`!
- If the maintainer requests further changes just push them to your branch. The pull request will be updated automatically.
- Once the pull request is approved and merged you can pull the changes from `upstream` to your local repo and delete
your extra branch(es).

And last but not least: Always write your commit messages in the present tense. Your commit message should describe what the commit, when applied, does to the code – not what you did to the code.

## Authors
* [**swasthikshetty10**](https://github.com/swasthikshetty10)

See also the list of [contributors](https://github.com/techlifejournal/techlifejournal/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details

<img style= " " src = "https://camo.githubusercontent.com/7998890254268d8ed476c9f66d3fa59d21dd354d2090036083c82af4cda2a0eb/68747470733a2f2f666f7274686562616467652e636f6d2f696d616765732f6261646765732f6275696c742d776974682d6c6f76652e737667">

