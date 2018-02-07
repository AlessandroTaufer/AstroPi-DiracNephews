# AstroPi
DIRAC's NEPHEWS


TEAM NAME: DIRAC’S NEPHEWS
AGE: 17-19
STUDENTS: Giordani Davide, Giongo Daniele, Taufer Alessandro, Marchetti Davide

>>What is your experiment idea?

Search for magnetic monopole. A magnetic monopole is an hypothetical elementary particle that is an isolated magnetic charge, its existence has been initially proposed in 1931 by Paul Dirac, it is predicted in many theories beyond the standard model and it is also expected within the standard model of particles (https://arxiv.org/abs/1602.01745). Magnetic monopoles could contribute to the dark matter in Universe, however this particle has never been detected. Magnetic monopoles are expected to be very massive and have large energy loss by ionization when they cross the atmosphere (about a factor 4500 larger than the proton's ionization yield). Therefore they are searched for by many experiments, for example Auger observatory search for Magnetic Monopoles by measuring the light emitted by the shower formed by cosmic rays in the atmosphere (https://arxiv.org/pdf/1609.04451.pdf). It is very unlikely to detect a Magnetic Monopole with the proposed device, however the technique might be interesting and might be improved in future experiments.

>>How will you use the Astro Pi to perform your experiment? Describe how you plan to use the Astro Pi hardware in your experiment, which sensors will be used and what kinds of data will be gathered

We would proceed with a technique similar to the JEM-EUSO project (https://arxiv.org/pdf/1703.01875.pdf), that is searching for a particle shower in the atmosphere by collecting images from space. To trigger the IR camera acquisition we will use the magnetometer embedded in the Astro-PI. The idea is that a magnetic monopole passing near the magnetometer would be detected as a (positive/negative) spike in the measurement of magnetic field and after a millisecond could produce a shower in the atmosphere that could be detected by the camera. Therefore we would continuously monitor the stream of the magnetic sensor and take pictures with the camera at the maximum rate. Only the 3 frames taken: 1) after, 2) near and 3) before, a detected magnetic anomaly would be stored for off-line analysis. The threshold to trigger this image acquisition would be chosen dynamically, to not exceed the maximum allowed data size. When an "event" occurs, we would record also the time-stamp and a message would appear in the LED display giving the #sigma amplitude of the detected magnetic anomaly. The streams of the other sensors would be stored as well, to search for possible systematic effects.
