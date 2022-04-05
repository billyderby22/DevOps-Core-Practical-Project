export MYSQL_ROOT_PASSWORD
docker stack deploy --compose-file docker-compose.yaml football-gen-stack
docker service update --replicas 3 football-gen-stack_front-end