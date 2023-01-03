A very easy and simple to use basic containerized python ELT in Docker.

## Pre-requirements

It requires the subject machine has below tools pre-installed.

1- Make

2- Docker and Docker Compose


## Usage
Open the terminal in the solution directory and run the below command.

```bash
sudo su
```
```python
make up
```

## Output
The input file is already in the directory. It takes the given input csv file and generates an output json file. 
Finally deletes the Container and Images it uses, just to not let the unused resources dangling, saves time for manual clean up later.
