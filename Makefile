say_hello:
		docker buildx build --platform linux/amd64 -t helloworld .
		docker run helloworld
