<h3>Project Euler #546 - The Floor's Revenge<\h3>

Problem description: https://projecteuler.net/problem=546

Try it out at: https://www.codewars.com/kata/56b85fc4f18876abf0000877/python

To solve this efficiently, we must avoid a recursive function. If we write down a pattern, we find that:

fₖ(n) = 1 * (n+1) when n < k

fₖ(n) = f(floor(i/k)) + k * (fₖ(floor(i/k) - 1)) + ... fₖ(0) when n > k

Thus, if we fill an array with this sequence, we can find fₖ(n) very quickly by iterating the array till n