import time

def get_bpm(times):
	if len(times) < 2:
		return 0
	total_time = sum(times)
	avg_time = total_time / len(times)
	bpm = 60 / avg_time
	return bpm

def taps(num_taps):
	times = []
	previous_time = time.time()

	input("Tap Enter to start")

	counter = len(times) + 1

	for tap in range(num_taps):
		input(f"Beat {counter}")
		current_time = time.time()
		elapsed_time = current_time - previous_time
		previous_time = current_time
		if tap > 0:
			times.append(elapsed_time)

		current_bpm = get_bpm(times)
		if current_bpm > 0:
			print(f"{round(current_bpm, 2)}")
		else:
			print("...")
		counter += 1
		
	return times

num_taps = 15
tap_times = taps(num_taps)
bpm = get_bpm(tap_times)

print(f"Beat 16 \n\nBPM is {round(bpm, 2)}")
time.sleep(4)

