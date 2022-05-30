# fibonacci-term
Finds the index of the first term in the Fibonacci sequence to contain num digits.<br>
See '*2022 Technical Assignment Corigine Recruitement.pdf*' for additional details.

## Usage

### Running Directly
1. `$> python ./fibonacci-term.py number_of_digits`

### Building Docker Image
1. `$> docker build -t fibonacci-term .`
2. `$> docker run --rm fibonacci-term number_of_digits`

## Algorithm Derivation
A closed form solution to the n-th Fibonacci term is given as<br>
f(n) = ( &phi;<sup>n</sup> - (1 - &phi;)<sup>n</sup>) / sqrt(5)<br>
where<br>
&phi; = (1 + sqrt(5))/2 ≈ 1.618 is the golden ratio<br>
<br>
Due to (1 - &phi;)<sup>n</sup> / sqrt(5) being less than 0.5 for all n ∈ **N** and<br>
f(n) being an integer for all n ∈ **Z**, the n-th Fibonacci term can also be expressed as<br>
f(n) = round( &phi;<sup>n</sup> / sqrt(5) ) <br>
<br>
The number of digits in the n-th Fibonacci term is<br>
N(n) = floor(log<sub>10</sub>(f(n))) + 1<br>
N(n) = floor(log<sub>10</sub>(round( &phi;<sup>n</sup> / sqrt(5) ))) + 1<br>
and since no term in the Fibonacci sequence is a power of 10 (except the trivial f(1) = f(2) = 10<sup>0</sup>),<br>
we can ignore the round() operator. Resulting in<br>
N(n) = floor(log<sub>10</sub>( &phi;<sup>n</sup> / sqrt(5) )) + 1<br>
N(n) = floor( n · log<sub>10</sub>(&phi;) - log<sub>10</sub>(sqrt(5)) ) + 1<br>
Inverting the equation to solve for n yeilds<br>
n = ceil( ( N(n) - 1 + log<sub>10</sub>(sqrt(5)) ) / log<sub>10</sub>(&phi;) )<br>
for all n > 1 (also N(n) > 1)
