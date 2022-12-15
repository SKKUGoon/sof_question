Question was posted on stack overflow.

* https://stackoverflow.com/questions/74811707/python-docker-container-not-running-simultaneously/74811891#74811891

* Answered thanks to nice comment. 
```
docker-python-py1-1  | InfProcess 1
docker-python-py2-1  | InfProcess 2
```
It works like a charm. Thanks!


Question >>
I tried to start 3 docker containers from single repository. 
My file tree is like so.

```
.
├── docker
│   ├── inf1
│   │   └── Dockerfile
│   ├── inf2
│   │   └── Dockerfile
│   └── proc1
│       └── Dockerfile
├── docker-compose.yaml
├── example
│   ├── __init__.py
│   ├── infinite_process1.py
│   ├── infinite_process2.py
│   └── stop_process.py
├── exe_inf1.py
├── exe_inf2.py
└── exe_proc.py

```

`infinite_process1.py` and `infinite_process2.py` contains infinite loop process using `while True` like so

```
# ./example/infinite_process1.py
# ./example/infinite_process2.py

import time


class InfiniteProcess1:  # InfiniteProcess2 respectively
    def __init__(self):
        pass

    def infinite_loop(self):
        while True:
            print("InfProcess 1")
            time.sleep(2)
```

`./example/stop_process.py` is like so. It does not run infinitely

```
# ./example/stop_process.py
class SimpleProcess:
    def __init__(self, name_: str):
        self.my_name = name_

    def run(self):
        print(f"my name is {self.my_name}")
```

`exe_inf1.py` `exe_inf2.py` `exe_proc.py` runs classes in `infinite_process1.py` `infinite_process2.py` `stop_process.py` respectively. 

For example, `./docker/inf1/Dockerfile` looks like this

```
FROM python:3.10.7

WORKDIR /app

COPY . .

ENTRYPOINT [ "python" ]

CMD [ "exe_inf1.py" ]
```

I wanted to create all 3 `exe_*.py` files start independently so, I've created a .yaml file like so
```
version: '2'
services:
  py1:
    build:
      context: .
      dockerfile: ./docker/inf1/Dockerfile
  
  py2:
    build:
      context: .
      dockerfile: ./docker/inf2/Dockerfile

  py3:
    build:
      context: .
      dockerfile: ./docker/proc1/Dockerfile
```

However, while docker containers were build successfully, docker container doesn't seem to be running `./exe_inf1.py ` and `./exe_inf2.py` correctly. It should be printing `"InfProcess 1"` every 2 seconds. 

```
[+] Running 4/1
 ⠿ Network docker-python_default  Created                                                         0.0s
 ⠿ Container docker-python-py2-1  Created                                                         0.0s
 ⠿ Container docker-python-py3-1  Created                                                         0.0s
 ⠿ Container docker-python-py1-1  Created                                                         0.0s
Attaching to docker-python-py1-1, docker-python-py2-1, docker-python-py3-1
docker-python-py3-1  | my name is foo
docker-python-py3-1 exited with code 0
```

So my question is:

What can I do to make infinite looping docker container to run independently? Or am I doing something wrong here