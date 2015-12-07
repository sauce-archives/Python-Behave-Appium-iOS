run_all_in_parallel:
	make -j iPhone_6 iPhone_6_plus

iPhone_6:
	deviceName="iPhone 6" behave-parallel/bin/behave --processes 12 --parallel-element scenario

iPhone_6_plus:
	deviceName="iPhone 6 Plus" behave-parallel/bin/behave --processes 12 --parallel-element scenario