# README.md
## Docker clean up
```
docker-compose rm -f

docker rmi -f $(docker images -qf dangling=true)
```

### Notes: 
Dangling is for for the cleanup of dead containers. Do this once a week