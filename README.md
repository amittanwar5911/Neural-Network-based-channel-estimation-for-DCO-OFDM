# Neural Network Based Channel Estimation for DCO-OFDM

1.) Project Overview
This project presents a neural network based approach for channel estimation in DC-biased Optical Orthogonal Frequency Division Multiplexing (DCO-OFDM) systems. Traditional channel estimation techniques such as Least Squares (LS) and Minimum Mean Square Error (MMSE) suffer from performance degradation under non-linear LED effects and noise. To overcome these limitations, a neural network model is employed to accurately estimate the optical channel.

2.) Objectives
  To model a DCO-OFDM based optical communication system
  To analyze channel estimation challenges in VLC systems
  To design and train a neural network for channel estimation
  To compare neural network performance with conventional methods

3.) Technologies Used
  Python
  NumPy
  TensorFlow
  MATLAB-style signal processing
  DCO-OFDM modulation techniques

4.) System Methodology
1. Random data generation
2. OFDM modulation with Hermitian symmetry
3. DC bias addition (DCO-OFDM)
4. Optical channel modeling (AWGN / multipath)
5. Neural network based channel estimation
6. OFDM demodulation and BER/MSE evaluation

5.) Results
  Improved Mean Square Error (MSE) performance
  Better channel estimation accuracy compared to LS method
  Robustness against LED non-linearity and noise

Graphs and plots are available in the `results/` folder.

# Folder Description
- `src/` – Source code for DCO-OFDM and neural network
- `models/` – Trained neural network model
- `data/` – Training and testing datasets
- `docs/` – Diagrams and system documentation
- `results/` – Output plots and performance analysis
- `references/` – Research papers and literature

# How to Run
```bash
pip install -r requirements.txt
python training.py
python testing.py

