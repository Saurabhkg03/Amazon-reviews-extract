# Amazon-reviews-extract
Amazon reviews extracts by using BeautifulSoup, Splash JS, Docker, Python.

**Extract/Scrape the amazon reviews of your desired product easily by following the next steps one by one:-**

# Installation
## 1.Install all the Dependancies and libraries you need-
Make sure you have latest version version of python installed. Visit the official Python website at <a href="https://www.python.org/downloads/">https://www.python.org/downloads/</a> to download and install the latest version of Python.
You can install the libraries by running the following commands in your terminal or command prompt:

pandas-```pip install pandas```<br>
openpyxl-```pip install openpyxl```<br>
requests-```pip install requests```<br>
beautifulsoup4-```pip install beautifulsoup4```<br>

## 2.Install Docker.
First of all we need to install docker
*Download from here according to your machine-* 
<a href="https://www.docker.com/products/docker-desktop/"> https://www.docker.com/products/docker-desktop/</a>

## 3.Installation of Splash JS

Run the following commands in the terminal.
### ※For Windows
Make sure Docker version >= 17 is installed.

Pull the image:
```docker pull scrapinghub/splash```

Start the container:
```docker run -it -p 8050:8050 --rm scrapinghub/splash```

### ※For linux
Make sure Docker version >= 17 is installed.

Pull the image:
```$ sudo docker pull scrapinghub/splash```

Start the container:
```$ sudo docker run -it -p 8050:8050 --rm scrapinghub/splash```

Splash is now available at 0.0.0.0 at port 8050 (http).

### ※For OS X
Install Docker for Mac (see https://docs.docker.com/docker-for-mac/). Make sure Docker version >= 17 is installed.

Pull the image:
```$ docker pull scrapinghub/splash```

Start the container:
```$ docker run -it -p 8050:8050 --rm scrapinghub/splash```

Splash is available at 0.0.0.0 address at port 8050 (http).

*Check out the whole Splash JS Documentation here-* <a href="https://splash.readthedocs.io/en/stable/">https://splash.readthedocs.io/en/stable/</a>

# Run the code
Run the python code which is created with BeautifulSoup and requests libraries.<br>
(Make sure you have all  the libraries and dependancies installed.<br>
Remember to replace the https link with the second page of product link you want and keep the ={x} as it is by removing =2 in the code.)

The Reviews will be saved in an excel file.
