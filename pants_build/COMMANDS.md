To lock the python dependencies 
```
./pants generate-lockfiles --resolve=python-default
```

To run main:
```
./pants run :main -- I <working_dir>
```