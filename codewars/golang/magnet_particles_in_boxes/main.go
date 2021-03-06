package magnet_particles_in_boxes

import (
	// "fmt"
	"math"
)

func Doubles(maxk, maxn int) float64 {
	sum := 0.0
	for k := 1; k <= maxk; k++ {
		for n := 1; n <= maxn; n++ {
			sum += 1.0 / (float64(k) * math.Pow(float64(n+1), float64(2*k)))
		}
	}
	return sum
}
