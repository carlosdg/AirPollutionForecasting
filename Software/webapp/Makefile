# Builds the docker image
build_docker:
	docker build -t web --build-arg API_BASE_URL=http://localhost:5000 .

# Runs the docker container  (need to use `make` command inside this folder)
run_docker:
	docker run --rm -it -v ${PWD}:/web -p 1234:1234 web