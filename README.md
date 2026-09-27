# NBTV-Project
Version 3.22,
OS Ubuntu Linux, 
NBTV help

This application is a hybrid Analog / Digital Television decoder to receive audio and video via Narrow Band Television (NBTV). This application is designed to send television (Sound and Video) via Sky-wave, using OFDM with 200 carriers, made of four parts. The Encode and Decoder, with the modulator and demodulator using GUN radio.

This software needs to work within Gambas3 software layer (VB for Linux), with these install files. 

There are five modes 1 to 5, where 5 has lowest level of video compression
The input can be a video file URL or screen capture

This software sends data via UDP from the encoder to the modulator and this will need to set up by the user. Or this could set up as a loop back test between the encoder and the decoder sections.

4:3 or 16:9 will set the aspect ratio required

On the decoder there is View, to enable the decoder

Wavelet on / off to enable the wavelet decode for 240 x 192 mode, only with mode 1, else it is disabled 

Y+C has colour and video enabled, else black and white

Frame auto will only display Key frames, without the Motion frames

Video and audio record that will save the Mpeg2 video into the temp folder
<hr>
<p></p>
<img width="905" height="428" alt="Screenshot_NBTV_3 22" src="https://github.com/user-attachments/assets/784529ab-ac67-4ae9-ba6c-261bb13331b8" />
<p></p>
Background:

The system operates through a video and audio encoder application that transforms each video frame into a series of uncompressed bitmap files. Each set of three frames is divided into components for color and a monochrome image, which are subsequently converted into key and motion frames. This constitutes a single data frame that is then encapsulated within a User Datagram Protocol (UDP) packet, that is sent to the SDR modulator. The incoming data undergoes preprocessing for noise reduction and is randomized for the OFDM or CDMA modulator, before being converted to RF using a HackRF.

On the demodulator end, the HackRF captures the RF signal and sends it to the SDR block for demodulation. After the noise processing is completed and the data frame is reconstructed, it is forwarded to the audio/video decoder via UDP. The video decoder synchronizes with the sync bits to identify the beginning of the data frame, allowing it to reconstruct the three video frames as uncompressed bitmap files. These images are then displayed alongside the recovered audio information within the viewer application.

By Grant Taylor
VE3XTV

Please note that the .gambas files run with bugs, a work in progress. When the encoder and decoder are working via UDP, you can run the "UDP_loopback_test_v2.py" file to test the interface via GNU Radio.

<hr>
<p></p>
<img width="646" height="425" alt="Screenshot_NBTV_3 22A" src="https://github.com/user-attachments/assets/dda92361-eef0-4b54-a990-9ad5f5252823" />
<p></p>
From GNU Radio showing the 8 different parts of the NBTV OFDM modulation, where there is pilot carriers between each part of the video signal for sync recovery and signal alinement. From left to right there is:
<p></p>
Digital audio A, Luminance odd, Luminance even, Chrominance R-Y & B-Y, Video frames A & B, Motion information odd, Motion information even, Digital audio B.

Placement of digital audio A&B have been done this way, as this part of the video signal works better with group delay affects of OFDM output filtering.
