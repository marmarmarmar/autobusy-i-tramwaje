build:
	docker build -t autobusy-i-tramwaje .

run:
	docker run -id --network=host -v ${PWD}:/srv autobusy-i-tramwaje python main.py
