package main

func checkPerfectNumber(num int) bool {
	if num <= 1 {
		return false
	}
	sum := 1
	for i := 2; i*i <= num; i++ {
		if num%i == 0 {
			sum += i + num/i
		}
	}
	if sum == num {
		return true
	}
	return false
}
