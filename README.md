docker build -t botq .

docker run -v $(pwd):/botQ-poll:rw --rm botq
