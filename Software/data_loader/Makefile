# Builds the docker image
build_docker:
	docker build -t data_loader .

# Runs the docker container  (need to use `make` command inside this folder)
run_docker:
	docker run --rm -it -v ${PWD}:/home/data_loader data_loader