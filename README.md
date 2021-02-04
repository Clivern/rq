### RQ

Simple Django Application with RQ Integration

```bash
$ git clone https://github.com/Clivern/RQ.git
$ cd RQ
$ cp .env.example .env

# Setup py env
$ python3 -m venv venv
$ source venv/bin/activate

# Install packages
$ make config

# Web App
$ make run

# RQ Worker
$ make worker

# RQ Statistics
$ make rqstats

$ curl http://127.0.0.1:8000/_health
```