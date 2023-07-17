# Amazon-reviews-extract
Amazon reviews extracts by using BeautifulSoup, Splash JS, Docker, Python.

# Installation
## Install Docker.

### For Windows
Make sure Docker version >= 17 is installed.

Pull the image:
```docker pull scrapinghub/splash```

Start the container:
```docker run -it -p 8050:8050 --rm scrapinghub/splash```

### For linux
Make sure Docker version >= 17 is installed.

Pull the image:
```$ sudo docker pull scrapinghub/splash```

Start the container:
```$ sudo docker run -it -p 8050:8050 --rm scrapinghub/splash```

Splash is now available at 0.0.0.0 at port 8050 (http).

### For OS X
Install Docker for Mac (see https://docs.docker.com/docker-for-mac/). Make sure Docker version >= 17 is installed.

Pull the image:
```$ docker pull scrapinghub/splash```

Start the container:
```$ docker run -it -p 8050:8050 --rm scrapinghub/splash```

Splash is available at 0.0.0.0 address at port 8050 (http).
