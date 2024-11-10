# NBTV-Project
Version 3.4,
OS Ubuntu Linux, 
NBTV help

This application is a hybrid Analog / Digital Television decoder to receive audio and video via Narrow Band Television (NBTV). 
This application is designed to send television (Sound and Video) via Sky-wave, using OFDM with 192 carriers, made of four parts. 
The Encode and Decoder, with the modulator and demodulator using GNU radio.

This software needs to work within Gambas3 interpretion software layer (VB for Linux), with these install files. 

There are four modes 1 to 4, where 4 has lowest level of video compression
The input can be a video file URL or screen capture.

This software sends data via UDP from the encoder to the modulator and this will need to set up by the user. 
Or this could set up as a loop back test between the encoder and the decoder sections.  

The Scan sets horizontal or vertical scanning, left to right or top down.

4:3 or 16:9 will set the aspect ratio required.

On the decoder there is View, to enable the decoder.

Wavelet on / off to enable the wavelet decode for 240 x 192 mode, only with mode 1, else it is disabled. 

Y+C has colour and video enabled, else black and white.

Sync delay, set the delay time to adjuct the image to fit the screen size, as NBTV is without sync to save RF bandwidth and therefore this done manually by the user.

Frame auto will only display Key frames, without the Motion frames.

Video and audio record that will save the Mpeg2 video into the temp folder.

By Grant Taylor,
VE3XTV


Before Installing the NBTV software do this to

add this repository:

sudo add-apt-repository ppa:gambas-team/gambas3

sudo apt update

![NBTV_1](https://github.com/user-attachments/assets/1d3b3995-1ab8-486d-9bb2-ee72394ff3ba)


