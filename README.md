# AngryFuzz3r
![screen_1](http://i.imgur.com/QetqbO1.png)

Status: **Development**
## About LinksF1nder
Extracts links from an HTML page and display them with friendly way ,this tool could be used for web information gathering ,to get more details about the web application.

## Features

* Extract all the links not only the <a href="#"> tags
* Identifying the extention of the linked file
* Generate report
* Count the links based on the extension

## Usage

~~~
$ python linksF1nd3r.py URL

~~~

Example:
* Fuzzing an url with default dictionary
~~~
python linksF1nd3r.py
~~~
![screen_2](http://i.imgur.com/0C4Lb42.png)

## How to install
##### Clone
 - Clone the repository with:
```sh
$ https://github.com/ihebski/LinksF1nd3r.git
$ cd LinksF1nd3r
$ python linksF1nd3r.py
```
##### Dependencies
* Install the required dependencies with:
```bash
$ sudo pip install -r requirements.txt
```
## License
The MIT License (MIT)