actions = ["jump", "close your eyes", "double blink", "wink"]
def commands(sequence: str):
	bin = list(sequence)
	x = bin.pop(0)
	if x == "1":
		answer = [actions[idx] for idx, x in enumerate(bin) if x == "1"]
	else:
		answer = [actions[idx] for idx, x in enumerate(bin) if x == "1"][::-1]
	return answer