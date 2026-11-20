# NBTV-Project
NBTV SDR 
Version 1.14

NBTV SDR puts the NBTV system on the air. It encodes pictures and stereo sound and transmits them as OFDM. It also receives and decodes, in the same window.

It uses the same codec and modem as the NBTV OFDM Lab, so the lab and NBTV SDR understand each other.

The window has three parts:
  - left: Encode and TX
  - centre: On the air - the settings the transmitter and receiver share
  - right: Decoder and RX

NBTV SDR is half duplex. It receives until you press TX, and goes back to receive when you press TX again. It always starts on receive.


Getting started

1. Press "Radio / I/Q setup..." (Encode and TX) and set up your hardware:
   - ExSDR radio: choose the serial port from the drop-down and the 192 kHz sound card's output and input.
   - HackRF: choose the HackRF.
2. Choose Hardware: ExSDR radio or HackRF.
3. Set the frequency (centre). Click or roll the mouse wheel on the digits, or type kHz in the box.
4. Set the guard, frame rate and the other modem settings to match the other station. Or tick "Auto mode (RX)" and the receiver finds them itself.
5. To transmit, choose a picture source and press TX. Start with a low TX level.
<img width="959" height="521" alt="NBTV_SDRv1" src="https://github.com/user-attachments/assets/3ea008c7-d6cd-459a-ac3b-c83aafab3a28" />


<hr>
