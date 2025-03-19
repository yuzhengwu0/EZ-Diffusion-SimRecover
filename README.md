# EZ-Diffusion-SimRecover

This repository contains a simulate-and-recover exercise for the EZ diffusion model.  
We randomly select parameters a (boundary separation), v (drift rate), and t (non-decision time) from realistic ranges, then simulate response times.  
We repeat this 1000 times for each of three sample sizes: N=10, N=40, and N=4000.

The results show that the recovered parameters have minimal bias, especially for larger N.  
As N increases, the estimation error decreases, indicating that the EZ diffusion model can recover parameters reliably from its own simulated data.  
This is a common consistency check in cognitive modeling.  
Overall, these results support the internal consistency of the EZ diffusion model under ideal conditions.
