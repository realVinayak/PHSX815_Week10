# Homework 11

The homework 11 is on the central limit theorem. 
In one experiment, `n_meas` number of exponential distributions with a fixed
rate parameter (`1/LAMBDA`) is sampled. The average is calculated. Multiple experiments (`N_experiments`)
are conducted and the average from each experiment are stored. Finally, the histogram
of collected averages is plotted. It is expected that the histogram resembles a Gaussian
distribution as `n_meas` increases.
</br>
</br>
To run the code, type `python3 driver_hw_11.py`. This runs the steps mentioned previously
and the resulting histogram is stored in `outputs`. The current `outputs` directory
contains results for `n_meas = 1, 4, 8, 12, 40`. It can be seen that as the `n_meas`
increases, the resulting probability density of the averages approaches a Gaussian
distribution more closely. The number of experiments is `N_experiments = 100000`.
The rate parameter is `1/LAMDA = 1/0.6`. The number of measurements per experiment (`n_meas`)
is a parameter to `main(n_meas)`.
