# Product Name
Building up on the [Kenya Coffee Directory, K.C.T.A (2012)](https://issuu.com/kcta.coffee.directory/docs/kcta2012) to update the list of Kenya coffee producers and buyers based on transactions reported by the [Nairobi Coffee Auction weekly](http://nairobicoffeeexchange.co.ke). The website links coffee transactions at the auction to their respective producers and buyers. This will allow farmers and overseas coffee importers, who depend on intermediaries at the auction, to be able to follow the auction remotely and engage in dialogue to negotiate better deals for themselves.

## Installation

Create virtual environment

```sh
$ sudo pip3 install virtualenv
$ virtualenv myvirtualenv -p python3.6 
```
Enable virtual environment 
```sh
#Option one
$ cd myvirtualenv
$ source bin/activate
(myvirtualenv)$

#Option two
$ workon myvirtualenv
(myvirtualenv)$
```
Disable virtual environment
```sh
$ source deactivate
```
Install django version 1.11
```sh
$ pip install django==1.11.2
```
Start the project
```sh
$ django-admin startproject mycoffeeproject
```
Run the project
```sh
$ python manage.py runserver
```
Stop the project
```sh
# hold Ctrl + C
```
Collect static files e.g. CSS, js, ..
```sh
$ python manage.py collectstatic
```

## Usage example

A few motivating and useful examples of how your product can be used. Spice this up with code blocks and potentially more screenshots.

_For more examples and usage, please refer to the [Wiki][wiki]._

## Development setup

Refer to [requirements.txt](https://github.com/wasisi/website/blob/master/requirements.txt) for the list of dependencies needed for this project. To install the specific versions used in this project.

```sh
# pip install module==version (See example below)
$ pip install djangorestframework==3.7.7
```
Testing instructions needs to be developed (Help needed)

## Release History
* 0.1.1
    * Working versions of the coffee directory and transactions app
* 0.1.0
    * First working version of the site with customisations and lookup models for Kenya counties and coffee grades
* 0.0.1
    * Initial code and template by Alex Giavaras

## Meta

Benedict Omare – [@benaboki](https://twitter.com/benaboki) – benaboki@hotmail.fr

Distributed under the XYZ license. See ``LICENSE`` for more information.

[https://github.com/benaboki](https://github.com/benaboki/)

## Contributing
https://github.com/wasisi/website/edit/master/README.md#fork-destination-box

1. Fork it (<https://github.com/wasisi/website/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
