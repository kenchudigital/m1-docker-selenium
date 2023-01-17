say_hello:
		docker buildx build --platform linux/amd64 --no-cache --progress=plain --network="host" -t helloworld .
		docker run helloworld
