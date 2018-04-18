# Product Name
Building up on the [Kenya Coffee Directory, K.C.T.A (2012)](https://issuu.com/kcta.coffee.directory/docs/kcta2012) to update the list of Kenya coffee producers and buyers based on transactions reported by the [Nairobi Coffee Auction](http://nairobicoffeeexchange.co.ke) weekly. The website links coffee transactions at the auction to their respective producers and buyers. This will allow farmers and coffee buyers, who depend on intermediaries at the auction, to be able to follow the auction remotely and engage in dialogue to negotiate better deals for themselves.

## Installation

Create virtual environment and install python version 3.6. This will probably be different to what your computer has.

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
Install django version 1.11. Project is incompatible with Django version 2
```sh
$ pip install django==1.11.2
```
Start the project
```sh
$ django-admin startproject mycoffeeproject
```
Add the secret_key in wasisi/settings.py
```sh
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'add secret key between apostrophes'
```
Run the project
```sh
$ python manage.py runserver
```
Stop the project
```sh
# hold Ctrl + C
```
Collect static files contained in the static folder e.g. CSS,js, images and fonts. This should be done whenever there are additions or changes to these files. 
* CSS, fonts and js are contained in /static/cssjsfonts/
```sh
$ python manage.py collectstatic
```
Configure the database. We are using mysql
* settings, username and password for the database are contained in wasisi/conf/dev.py
```sh
$ sudo pip install mysqlclient
```
Register the models to the database. This also needs to be done each time you make any change to any of the models e.g. adding or modifying a field
```sh
$ python manage.py makemigrations
$ python manage.py migrate
```
For more details about configuring and further developing the app please refer to [Django Documentation](https://docs.djangoproject.com/en/1.7/intro/tutorial01/). Note that these instructions are for Django 1.7 but they provide more details than those of Django 1.11.

## Usage example

* A farmer belonging to a cooperative can go to the coffee directory page and search for his/her cooperative and then click on the cooperative to find out all the coffee that the cooperative has sold at the auction since February 2015. Please note that this may not include coffee that is sold as bulk coffee. The farmer can then have the information needed to mobilise other farmers to demand transparency and justification for the money paid for delivered coffee. 
* A coffee importer who depends on a registered dealer based in Kenya can track the prices paid and volumes bought by the contracted dealer(s).
* County governments and relevant organisations from coffee producing areas can monitor trends using the analytics per county (to be developed) and make appropriate decisions or interventions.
* Subscribed farmers can provide insights and share stories that can be shared with coffee consumers to help market coffee and raise awareness on issues that the farmers are facing.
* Potential for coffee importers to engage directly with the producers and negotiate for direct sales.


## Development setup

Refer to [requirements.txt](https://github.com/wasisi/website/blob/master/requirements.txt) for the list of dependencies needed for this project. To install the specific versions used in this project.

```sh
# pip install module==version (See example below)
$ pip install djangorestframework==3.7.7
```
Testing instructions needs to be developed (Help needed)

## Deployment set up
The following settings contained in wasisi/settings.py are only needed for local development and should be removed/modified when deploying the code to live environment
```sh
# Allow email testing in development server
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# Allow file upload in development server
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
```

## Release History
* 0.1.1
    * Working versions of the coffee directory and transactions app
* 0.1.0
    * First working version of the site with customisations and lookup models for Kenya counties and coffee grades
* 0.0.1
    * Initial code and template by Alex Giavaras

## Meta

Benedict Omare – [@benaboki](https://twitter.com/benaboki) – oasis@wasisivillage.com

Distributed under the MIT license. See ``LICENSE`` for more information.

[https://github.com/benaboki](https://github.com/benaboki/)

## Contributing
https://github.com/wasisi/website/edit/master/README.md#fork-destination-box

1. Fork it (<https://github.com/wasisi/website/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Remove secret_key from wasisi/settings.py
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

## Similar sites
http://www.coffeetransparency.com/c/ke/

