package main

import (
	"fmt"
	"math"
)

func Sqrt(x float64) float64 {
	z := 1.0
	for i := 0; i < 10; i++ {
		z -= (z*z - x) / (2*z)
		fmt.Println(z)
	}
	return z
}

func SqrtOpt(x float64, lim float64) float64 {
	z := x/2
	var old float64
	diff := 1.0; 
	for diff > lim {
		old = z 
		z -= (z*z - x) / (2*z)
		diff = old - z
		if diff < 0 {
			diff = -diff
		}
		fmt.Println(z)
	}
	return z
}

func main() {
	num := 7.0
	lim := 0.00000000000001
	fmt.Println("final result:",Sqrt(num))
	fmt.Println("final result optimised:",SqrtOpt(num,lim))	
	fmt.Println("verdadero:",math.Sqrt(num))
}
