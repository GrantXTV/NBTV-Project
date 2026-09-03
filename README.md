# NBTV-Project
Version 3.16,
OS Ubuntu Linux, 
NBTV help

This application is a hybrid Analog / Digital Television decoder to receive audio and video via Narrow Band Television (NBTV). 
This application is designed to send television (Sound and Video) via Sky-wave, using OFDM with 192 carriers, made of four parts. 
The Encode and Decoder, with the modulator and demodulator using GNU radio. The SDR modulator take the video data in via UDP, formats
it in a way to be encoded into 192 RF carriers and unconverted using SDR TX. On the receiver side this is done in reverse by 
demodulation the OFDM QAM carriers and rebuilding them into a data stream to send back out via UDP.

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

Sync delay, set the delay time to adjuct the image to fit the screen size, as NBTV is without sync to save RF bandwidth and therefore this done 
manually by the user. This can be done with the sync alignment meter display, by looking for the transition between the Chrominance and the 
Luminance video information. 

Frame auto will only display Key frames, without the Motion frames.

Video and audio record that will save the Mpeg2 video into the temp folder.

By Grant Taylor,
VE3XTV

Please note that the .gambas files run with bugs, a work in progress. When the encoder and decoder are working via UDP, you can run the "UDP_loopback_test.py" file to test the interface via GNU Radio.

<hr>
<p></p>
<img width="1943" height="808" alt="NBTV RX Test" src="https://github.com/user-attachments/assets/985f3855-5a1e-44c3-bae3-657556653941" />
