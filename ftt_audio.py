# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 10:48:07 2015

@author: Administrator
"""

import numpy as np
import pylab as pl
import wave
import pyaudio


wf = wave.open("D:\\SRTP project\\test3.wav", "rb")

#创建PyAudio对象

p = pyaudio.PyAudio()

stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),

channels=wf.getnchannels(),

rate=wf.getframerate(),

output=True)

nframes = wf.getnframes()

framerate = wf.getframerate()

#读取完整的帧数据到str_data中，这是一个string类型的数据

str_data = wf.readframes(nframes)

wf.close()

#将波形数据转换为数组

# A new 1-D array initialized from raw binary or text data in a string.

wave_data = np.fromstring(str_data, dtype=np.short)
#将wave_data数组改为2列，行数自动匹配。在修改shape的属性时，需使得数组的总长度不变。
wave_data.shape = -1,2

#将数组转置

wave_data = wave_data.T
wave_data= wave_data/(2.**15)
sampling_rate = 44100#采样频率为44100Hz
fft_size =nframes#FFT处理的取样长度
t = np.arange(0, 2.0, 2.0/sampling_rate)#np.arange(起点，终点，间隔)产生1s长的取样时间
x=wave_data
# N点FFT进行精确频谱分析的要求是N个取样点包含整数个取样对象的波形。因此N点FFT能够完美计算频谱对取样对象的要求是n*Fs/N（n*采样频率/FFT长度），
# 因此对8KHZ和512点而言，完美采样对象的周期最小要求是8000/512=15.625HZ,所以156.25的n为10,234.375的n为15。
xs = x[0][:fft_size]# 从波形数据中取样fft_size个点进行运算
xf = np.fft.rfft(xs)/fft_size# 利用np.fft.rfft()进行FFT计算，rfft()是为了更方便对实数信号进行变换，由公式可知/fft_size为了正确显示波形能量
# rfft函数的返回值是N/2+1个复数，分别表示从0(Hz)到sampling_rate/2(Hz)的分。
#于是可以通过下面的np.linspace计算出返回值中每个下标对应的真正的频率：
freqs = np.linspace(0, sampling_rate/2, fft_size/2+1)
# np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
#在指定的间隔内返回均匀间隔的数字
#xfp = 20*np.log10(np.clip(np.abs(xf), 1e-20, 1e100))
#最后我们计算每个频率分量的幅值，并通过 20*np.log10()将其转换为以db单位的值。为了防止0幅值的成分造成log10无法计算，我们调用np.clip对xf的幅值进行上下限处理
xfp = np.clip(np.abs(xf), 1e-20, 1e100)
#绘图显示结果
pl.figure(figsize=(8,4))
pl.subplot(211)
#pl.plot(t[:fft_size], xs)
pl.xlabel(u"Time(S)")
pl.title(u"noise")
pl.subplot(212)
pl.plot(freqs, xfp)
pl.xlabel(u"Freq(Hz)")
pl.subplots_adjust(hspace=0.4)
pl.show()
