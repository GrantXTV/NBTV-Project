#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: UDP Monitor
# Author: pcuser
# GNU Radio version: 3.10.9.2

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio import analog
from gnuradio import blocks
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import network
import sip



class UDP_Monitor(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "UDP Monitor", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("UDP Monitor")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except BaseException as exc:
            print(f"Qt GUI: Could not set Icon: {str(exc)}", file=sys.stderr)
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "UDP_Monitor")

        try:
            geometry = self.settings.value("geometry")
            if geometry:
                self.restoreGeometry(geometry)
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 3000
        self.Variable_Noise = Variable_Noise = 0
        self.DB = DB = 5760

        ##################################################
        # Blocks
        ##################################################

        if "int" == "int":
        	isFloat = False
        	scaleFactor = 1
        else:
        	isFloat = True
        	scaleFactor = 1

        _Variable_Noise_dial_control = qtgui.GrDialControl('Noise', self, 0,63,0,"default",self.set_Variable_Noise,isFloat, scaleFactor, 100, True, "'value'")
        self.Variable_Noise = _Variable_Noise_dial_control

        self.top_layout.addWidget(_Variable_Noise_dial_control)
        self.qtgui_time_sink_x_0_0 = qtgui.time_sink_f(
            1024, #size
            3000, #samp_rate
            "PLL Sync", #name
            2, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0.set_y_axis(0, 255)

        self.qtgui_time_sink_x_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0.enable_tags(False)
        self.qtgui_time_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_AUTO, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(2):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_0_win)
        self.network_udp_source_0_0_0 = network.udp_source(gr.sizeof_char, 1, 1245, 0, 500, False, False, False)
        self.network_udp_source_0_0 = network.udp_source(gr.sizeof_char, 1, 1243, 0, 1440, False, False, False)
        self.network_udp_source_0 = network.udp_source(gr.sizeof_char, 1, 1244, 0, 34560, False, False, False)
        self.network_udp_sink_0_0_0_0 = network.udp_sink(gr.sizeof_char, 1, '192.168.2.15', 1236, 0, 240, False)
        self.network_udp_sink_0_0_0 = network.udp_sink(gr.sizeof_char, 1, '192.168.2.15', 1235, 0, 500, False)
        self.network_udp_sink_0 = network.udp_sink(gr.sizeof_char, 1, '192.168.2.15', 1234, 0, 34560, False)
        self.blocks_uchar_to_float_0_2_0_0 = blocks.uchar_to_float()
        self.blocks_uchar_to_float_0_2_0 = blocks.uchar_to_float()
        self.blocks_uchar_to_float_0_2 = blocks.uchar_to_float()
        self.blocks_uchar_to_float_0_1_1_0 = blocks.uchar_to_float()
        self.blocks_uchar_to_float_0_1_0_2 = blocks.uchar_to_float()
        self.blocks_uchar_to_float_0_1_0_1 = blocks.uchar_to_float()
        self.blocks_uchar_to_float_0_1_0_0_1 = blocks.uchar_to_float()
        self.blocks_uchar_to_float_0_1_0_0_0 = blocks.uchar_to_float()
        self.blocks_uchar_to_float_0_1_0_0 = blocks.uchar_to_float()
        self.blocks_uchar_to_float_0_1_0 = blocks.uchar_to_float()
        self.blocks_uchar_to_float_0_1 = blocks.uchar_to_float()
        self.blocks_throttle_0_0 = blocks.throttle(gr.sizeof_char*1, 24000,True)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_char*1, 24000,True)
        self.blocks_sub_xx_0_0_0 = blocks.sub_ff(1)
        self.blocks_sub_xx_0_0 = blocks.sub_ff(1)
        self.blocks_stream_mux_1 = blocks.stream_mux(gr.sizeof_char*1, (1,1))
        self.blocks_stream_mux_0_0_1 = blocks.stream_mux(gr.sizeof_char*1, (120,120))
        self.blocks_stream_demux_1 = blocks.stream_demux(gr.sizeof_char*1, (1,1))
        self.blocks_stream_demux_0_1_0 = blocks.stream_demux(gr.sizeof_float*1, (120,120,120,120,120,120))
        self.blocks_stream_demux_0_1 = blocks.stream_demux(gr.sizeof_float*1, (120,120,120,120,120,120))
        self.blocks_stream_demux_0_0 = blocks.stream_demux(gr.sizeof_char*1, (720,720))
        self.blocks_null_sink_0_4 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_null_sink_0_3 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_null_sink_0_2 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_null_sink_0_1 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_null_sink_0_0_3 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_null_sink_0_0_2 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_null_sink_0_0_1 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_null_sink_0_0_0 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_null_sink_0_0 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_multiply_const_vxx_2_1 = blocks.multiply_const_ff(.25)
        self.blocks_multiply_const_vxx_2_0_1_0 = blocks.multiply_const_ff(1)
        self.blocks_multiply_const_vxx_2_0_0_0 = blocks.multiply_const_ff(1)
        self.blocks_multiply_const_vxx_2_0_0 = blocks.multiply_const_ff(.25)
        self.blocks_multiply_const_vxx_1_0 = blocks.multiply_const_cc(128)
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_cc(128)
        self.blocks_float_to_uchar_1_1 = blocks.float_to_uchar()
        self.blocks_float_to_uchar_1_0_0 = blocks.float_to_uchar()
        self.blocks_float_to_uchar_0_2_0 = blocks.float_to_uchar()
        self.blocks_float_to_uchar_0_1_0_1_0 = blocks.float_to_uchar()
        self.blocks_float_to_uchar_0_1_0 = blocks.float_to_uchar()
        self.blocks_float_to_uchar_0_1 = blocks.float_to_uchar()
        self.blocks_float_to_uchar_0_0_0 = blocks.float_to_uchar()
        self.blocks_float_to_uchar_0_0 = blocks.float_to_uchar()
        self.blocks_float_to_uchar_0 = blocks.float_to_uchar()
        self.blocks_float_to_complex_1_0 = blocks.float_to_complex(1)
        self.blocks_float_to_complex_0_0 = blocks.float_to_complex(1)
        self.blocks_delay_0_1 = blocks.delay(gr.sizeof_float*1, 9)
        self.blocks_delay_0_0_0 = blocks.delay(gr.sizeof_float*1, 6)
        self.blocks_complex_to_float_1_0 = blocks.complex_to_float(1)
        self.blocks_complex_to_float_0_0 = blocks.complex_to_float(1)
        self.blocks_add_xx_1_0_0 = blocks.add_vff(1)
        self.blocks_add_xx_1_0 = blocks.add_vff(1)
        self.blocks_add_xx_0_2_0 = blocks.add_vff(1)
        self.blocks_add_xx_0_2 = blocks.add_vff(1)
        self.blocks_add_xx_0_0_0_0_1_1 = blocks.add_vff(1)
        self.blocks_add_xx_0_0_0_0_1_0 = blocks.add_vff(1)
        self.blocks_add_xx_0_0_0_0_1 = blocks.add_vff(1)
        self.blocks_add_const_vxx_1_0 = blocks.add_const_ff((-128))
        self.blocks_add_const_vxx_0_1 = blocks.add_const_ff((-128))
        self.blocks_add_const_vxx_0_0_1 = blocks.add_const_ff(128)
        self.blocks_add_const_vxx_0_0_0_0 = blocks.add_const_ff((+128))
        self.band_pass_filter_0_1 = filter.fir_filter_ccf(
            1,
            firdes.band_pass(
                1,
                3000,
                100,
                150,
                10,
                window.WIN_KAISER,
                8.32))
        self.band_pass_filter_0_0_0 = filter.fir_filter_ccf(
            1,
            firdes.band_pass(
                1,
                3000,
                75,
                125,
                10,
                window.WIN_KAISER,
                8.32))
        self.analog_pll_refout_cc_1_0 = analog.pll_refout_cc(.2, 0.1, 0.066)
        self.analog_pll_refout_cc_0_0 = analog.pll_refout_cc(0.2, 0.083, 0.05)
        self.analog_noise_source_x_0_1_0_3 = analog.noise_source_f(analog.GR_GAUSSIAN, Variable_Noise, 2)
        self.analog_noise_source_x_0_1_0_1_1 = analog.noise_source_f(analog.GR_GAUSSIAN, Variable_Noise, 1)
        self.analog_noise_source_x_0_1_0_1_0_0 = analog.noise_source_f(analog.GR_GAUSSIAN, Variable_Noise, 0)
        self.analog_noise_source_x_0_1_0_1_0 = analog.noise_source_f(analog.GR_GAUSSIAN, Variable_Noise, 4)
        self.analog_noise_source_x_0_1_0_1 = analog.noise_source_f(analog.GR_GAUSSIAN, Variable_Noise, 5)
        self.analog_fm_preemph_0_0 = analog.fm_preemph(fs=24000, tau=(50e-6), fh=12000)
        self.analog_fm_preemph_0 = analog.fm_preemph(fs=24000, tau=(50e-6), fh=12000)
        self.analog_fm_deemph_0_0 = analog.fm_deemph(fs=24000, tau=(25e-6))
        self.analog_fm_deemph_0 = analog.fm_deemph(fs=24000, tau=(25e-6))


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_fm_deemph_0, 0), (self.blocks_float_to_uchar_0_1, 0))
        self.connect((self.analog_fm_deemph_0_0, 0), (self.blocks_float_to_uchar_0_0_0, 0))
        self.connect((self.analog_fm_preemph_0, 0), (self.blocks_float_to_uchar_0, 0))
        self.connect((self.analog_fm_preemph_0_0, 0), (self.blocks_float_to_uchar_0_0, 0))
        self.connect((self.analog_noise_source_x_0_1_0_1, 0), (self.blocks_add_xx_0_0_0_0_1_0, 0))
        self.connect((self.analog_noise_source_x_0_1_0_1_0, 0), (self.blocks_add_xx_0_0_0_0_1, 0))
        self.connect((self.analog_noise_source_x_0_1_0_1_0_0, 0), (self.blocks_add_xx_0_2_0, 1))
        self.connect((self.analog_noise_source_x_0_1_0_1_1, 0), (self.blocks_add_xx_0_2, 1))
        self.connect((self.analog_noise_source_x_0_1_0_3, 0), (self.blocks_add_xx_0_0_0_0_1_1, 0))
        self.connect((self.analog_pll_refout_cc_0_0, 0), (self.blocks_multiply_const_vxx_1_0, 0))
        self.connect((self.analog_pll_refout_cc_1_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))
        self.connect((self.band_pass_filter_0_0_0, 0), (self.analog_pll_refout_cc_0_0, 0))
        self.connect((self.band_pass_filter_0_1, 0), (self.analog_pll_refout_cc_1_0, 0))
        self.connect((self.blocks_add_const_vxx_0_0_0_0, 0), (self.blocks_float_to_uchar_1_0_0, 0))
        self.connect((self.blocks_add_const_vxx_0_0_1, 0), (self.blocks_float_to_uchar_1_1, 0))
        self.connect((self.blocks_add_const_vxx_0_1, 0), (self.blocks_delay_0_0_0, 0))
        self.connect((self.blocks_add_const_vxx_0_1, 0), (self.blocks_float_to_complex_0_0, 0))
        self.connect((self.blocks_add_const_vxx_1_0, 0), (self.blocks_delay_0_1, 0))
        self.connect((self.blocks_add_const_vxx_1_0, 0), (self.blocks_float_to_complex_1_0, 0))
        self.connect((self.blocks_add_xx_0_0_0_0_1, 0), (self.blocks_add_const_vxx_0_1, 0))
        self.connect((self.blocks_add_xx_0_0_0_0_1_0, 0), (self.blocks_add_const_vxx_1_0, 0))
        self.connect((self.blocks_add_xx_0_0_0_0_1_1, 0), (self.blocks_float_to_uchar_0_1_0_1_0, 0))
        self.connect((self.blocks_add_xx_0_2, 0), (self.blocks_multiply_const_vxx_2_0_0_0, 0))
        self.connect((self.blocks_add_xx_0_2_0, 0), (self.blocks_multiply_const_vxx_2_0_1_0, 0))
        self.connect((self.blocks_add_xx_1_0, 0), (self.blocks_multiply_const_vxx_2_1, 0))
        self.connect((self.blocks_add_xx_1_0_0, 0), (self.blocks_float_to_uchar_0_1_0, 0))
        self.connect((self.blocks_complex_to_float_0_0, 0), (self.blocks_add_const_vxx_0_0_1, 0))
        self.connect((self.blocks_complex_to_float_1_0, 0), (self.blocks_add_const_vxx_0_0_0_0, 0))
        self.connect((self.blocks_delay_0_0_0, 0), (self.blocks_float_to_complex_0_0, 1))
        self.connect((self.blocks_delay_0_1, 0), (self.blocks_float_to_complex_1_0, 1))
        self.connect((self.blocks_float_to_complex_0_0, 0), (self.band_pass_filter_0_1, 0))
        self.connect((self.blocks_float_to_complex_1_0, 0), (self.band_pass_filter_0_0_0, 0))
        self.connect((self.blocks_float_to_uchar_0, 0), (self.blocks_uchar_to_float_0_1_1_0, 0))
        self.connect((self.blocks_float_to_uchar_0_0, 0), (self.blocks_uchar_to_float_0_2_0, 0))
        self.connect((self.blocks_float_to_uchar_0_0_0, 0), (self.blocks_stream_mux_1, 1))
        self.connect((self.blocks_float_to_uchar_0_1, 0), (self.blocks_stream_mux_1, 0))
        self.connect((self.blocks_float_to_uchar_0_1_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_float_to_uchar_0_1_0_1_0, 0), (self.network_udp_sink_0, 0))
        self.connect((self.blocks_float_to_uchar_0_2_0, 0), (self.blocks_throttle_0_0, 0))
        self.connect((self.blocks_float_to_uchar_1_0_0, 0), (self.blocks_stream_mux_0_0_1, 1))
        self.connect((self.blocks_float_to_uchar_1_0_0, 0), (self.blocks_uchar_to_float_0_1_0_0_1, 0))
        self.connect((self.blocks_float_to_uchar_1_1, 0), (self.blocks_stream_mux_0_0_1, 0))
        self.connect((self.blocks_float_to_uchar_1_1, 0), (self.blocks_uchar_to_float_0_1_0_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.blocks_complex_to_float_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1_0, 0), (self.blocks_complex_to_float_1_0, 0))
        self.connect((self.blocks_multiply_const_vxx_2_0_0, 0), (self.blocks_add_xx_0_2, 0))
        self.connect((self.blocks_multiply_const_vxx_2_0_0_0, 0), (self.blocks_add_xx_1_0_0, 1))
        self.connect((self.blocks_multiply_const_vxx_2_0_0_0, 0), (self.blocks_sub_xx_0_0_0, 1))
        self.connect((self.blocks_multiply_const_vxx_2_0_1_0, 0), (self.blocks_add_xx_1_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_2_0_1_0, 0), (self.blocks_sub_xx_0_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_2_1, 0), (self.blocks_add_xx_0_2_0, 0))
        self.connect((self.blocks_stream_demux_0_0, 0), (self.blocks_uchar_to_float_0_1_0_0, 0))
        self.connect((self.blocks_stream_demux_0_0, 1), (self.blocks_uchar_to_float_0_1_0_1, 0))
        self.connect((self.blocks_stream_demux_0_1, 0), (self.blocks_add_xx_0_0_0_0_1, 1))
        self.connect((self.blocks_stream_demux_0_1, 1), (self.blocks_null_sink_0, 0))
        self.connect((self.blocks_stream_demux_0_1, 2), (self.blocks_null_sink_0_0, 0))
        self.connect((self.blocks_stream_demux_0_1, 4), (self.blocks_null_sink_0_0_0, 0))
        self.connect((self.blocks_stream_demux_0_1, 3), (self.blocks_null_sink_0_1, 0))
        self.connect((self.blocks_stream_demux_0_1, 5), (self.blocks_null_sink_0_2, 0))
        self.connect((self.blocks_stream_demux_0_1_0, 0), (self.blocks_add_xx_0_0_0_0_1_0, 1))
        self.connect((self.blocks_stream_demux_0_1_0, 1), (self.blocks_null_sink_0_0_1, 0))
        self.connect((self.blocks_stream_demux_0_1_0, 3), (self.blocks_null_sink_0_0_2, 0))
        self.connect((self.blocks_stream_demux_0_1_0, 5), (self.blocks_null_sink_0_0_3, 0))
        self.connect((self.blocks_stream_demux_0_1_0, 2), (self.blocks_null_sink_0_3, 0))
        self.connect((self.blocks_stream_demux_0_1_0, 4), (self.blocks_null_sink_0_4, 0))
        self.connect((self.blocks_stream_demux_1, 0), (self.blocks_uchar_to_float_0_1, 0))
        self.connect((self.blocks_stream_demux_1, 1), (self.blocks_uchar_to_float_0_2, 0))
        self.connect((self.blocks_stream_mux_0_0_1, 0), (self.network_udp_sink_0_0_0_0, 0))
        self.connect((self.blocks_stream_mux_1, 0), (self.network_udp_sink_0_0_0, 0))
        self.connect((self.blocks_sub_xx_0_0, 0), (self.blocks_multiply_const_vxx_2_0_0, 0))
        self.connect((self.blocks_sub_xx_0_0_0, 0), (self.blocks_float_to_uchar_0_2_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_uchar_to_float_0_1_0_2, 0))
        self.connect((self.blocks_throttle_0_0, 0), (self.blocks_uchar_to_float_0_2_0_0, 0))
        self.connect((self.blocks_uchar_to_float_0_1, 0), (self.analog_fm_preemph_0, 0))
        self.connect((self.blocks_uchar_to_float_0_1_0, 0), (self.blocks_add_xx_0_0_0_0_1_1, 1))
        self.connect((self.blocks_uchar_to_float_0_1_0_0, 0), (self.blocks_stream_demux_0_1, 0))
        self.connect((self.blocks_uchar_to_float_0_1_0_0_0, 0), (self.qtgui_time_sink_x_0_0, 0))
        self.connect((self.blocks_uchar_to_float_0_1_0_0_1, 0), (self.qtgui_time_sink_x_0_0, 1))
        self.connect((self.blocks_uchar_to_float_0_1_0_1, 0), (self.blocks_stream_demux_0_1_0, 0))
        self.connect((self.blocks_uchar_to_float_0_1_0_2, 0), (self.analog_fm_deemph_0, 0))
        self.connect((self.blocks_uchar_to_float_0_1_1_0, 0), (self.blocks_add_xx_1_0, 0))
        self.connect((self.blocks_uchar_to_float_0_1_1_0, 0), (self.blocks_sub_xx_0_0, 0))
        self.connect((self.blocks_uchar_to_float_0_2, 0), (self.analog_fm_preemph_0_0, 0))
        self.connect((self.blocks_uchar_to_float_0_2_0, 0), (self.blocks_add_xx_1_0, 1))
        self.connect((self.blocks_uchar_to_float_0_2_0, 0), (self.blocks_sub_xx_0_0, 1))
        self.connect((self.blocks_uchar_to_float_0_2_0_0, 0), (self.analog_fm_deemph_0_0, 0))
        self.connect((self.network_udp_source_0, 0), (self.blocks_uchar_to_float_0_1_0, 0))
        self.connect((self.network_udp_source_0_0, 0), (self.blocks_stream_demux_0_0, 0))
        self.connect((self.network_udp_source_0_0_0, 0), (self.blocks_stream_demux_1, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "UDP_Monitor")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

    def get_Variable_Noise(self):
        return self.Variable_Noise

    def set_Variable_Noise(self, Variable_Noise):
        self.Variable_Noise = Variable_Noise
        self.analog_noise_source_x_0_1_0_1.set_amplitude(self.Variable_Noise)
        self.analog_noise_source_x_0_1_0_1_0.set_amplitude(self.Variable_Noise)
        self.analog_noise_source_x_0_1_0_1_0_0.set_amplitude(self.Variable_Noise)
        self.analog_noise_source_x_0_1_0_1_1.set_amplitude(self.Variable_Noise)
        self.analog_noise_source_x_0_1_0_3.set_amplitude(self.Variable_Noise)

    def get_DB(self):
        return self.DB

    def set_DB(self, DB):
        self.DB = DB




def main(top_block_cls=UDP_Monitor, options=None):

    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
