import typing


def main(numbers: typing.List[int], target_sum: int):
    # START WRITING CODE HERE


    dict = {}
    for i, e in enumerate(numbers):
    	dict[e] = i
    	for i in range(len(numbers) - 1):
    		for j in range(i + 1, len(numbers)):
    			val = target_sum - (numbers[i] + numbers[j])
    			if val in dict:
    				if dict[val] != i and dict[val] != j:
    					# print(numbers[i],numbers[j],val)
    					return True
    return False


if __name__ == "__main__":
	if main([5, 4, 10, 7, 1, 9], 13):
		print("Triplet exists")
	else:
		print("Triplet does not exist")

	if main([4, 2, 5, 9, 11, 23], 9):
		print("Triplet exists")
	else:
		print("Triplet does not exist")

	# print(main([5, 4, 10, 7, 1, 9], 13) is True, "Triplet exists")
	# print(main([4, 2, 5, 9, 11, 23], 9) is False, "Triplet does not exist")
	# assert (main([5, 4, 10, 7, 1, 9], 13) is True), "Triplet exists"
	# assert (main([4, 2, 5, 9, 11, 23], 9) is 'False'), "Triple does not exist"
