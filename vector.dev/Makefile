.PHONY: test 

test:
	@docker build -f Dockerfile.unit-tests . -t vector-unit-test-runner:0.0.0

run-local:
	@docker run -p9090:9090 -i -t --rm vector-unit-test-runner:0.0.0

prometheus-metrics: # (Has to be executed while another session is running 'run-local'
	@curl localhost:9090/metrics
