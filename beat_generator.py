# def current_beat(bars):
# 	bars *= 2
# 	max = bars
# 	nums = (1,2,3,4)
# 	i = 0
# 	result = []
# 	while len(result) < max:
# 		if i >= len(nums): i = 0
# 		result.append(nums[i])
# 		i += 1
# 	return result

# print(current_beat(4))



def current_beat():
	nums = (1,2,3,4)
	i = 0
	while True:
		if i >= len(nums): i = 0
		yield nums[i]
		i += 1

counter = current_beat()
print(next(counter)) # beat 1
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter)) # beat 1
print(next(counter))
print(next(counter))
print(next(counter))