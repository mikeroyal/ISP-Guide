<h1 align="center">
 <img src="https://user-images.githubusercontent.com/45159366/134823726-37092704-e401-457e-82c5-e24c78475635.png">
  <br />
 Image Signal Processing (ISP) Guide
</h1>

#### A guide covering Image Signal Processing (ISP) including the applications, libraries and tools that will make you a better and more efficient Image Signal Processing (ISP) development.

**Note: You can easily convert this markdown file to a PDF in [VSCode](https://code.visualstudio.com/) using this handy extension [Markdown PDF](https://marketplace.visualstudio.com/items?itemName=yzane.markdown-pdf).**

<p align="center">
 <img src="https://user-images.githubusercontent.com/45159366/134823728-48c13a29-d198-46bb-8192-8e68bddbc0af.png">
  <br />
</p>

<p align="center">
 <img src="https://user-images.githubusercontent.com/45159366/134823733-028ab097-c5b6-4ea2-982c-09fa8a6fe3bd.png">
  <br />
</p>

**Architectural Analysis of a Baseline ISP Pipeline. Source: [SpringerLink](https://link.springer.com/chapter/10.1007/978-94-017-9987-4_2)**

# Table of Contents

1. [Image Signal Processing(ISP) Learning Resources](https://github.com/mikeroyal/iSP-Guide#ISP-learning-resources)

2. [Image Signal Processing(ISP) Tools, Libraries, and Frameworks](https://github.com/mikeroyal/ISP-Guide#ISP-tools-libraries-and-frameworks)

3. [Digital Signal Processing (DSP) Development](https://github.com/mikeroyal/ISP-Guide#DSP-Development)

4. [Machine Learning](https://github.com/mikeroyal/ISP-Guide#machine-learning)

5. [Algorithms](https://github.com/mikeroyal/ISP-Guide#Algorithms)

6. [Deep Learning Development](https://github.com/mikeroyal/ISP-Guide#Deep-Learning-Development)

7. [Reinforcement Learning Development](https://github.com/mikeroyal/ISP-Guide#Reinforcement-Learning-Development)

8. [Computer Vision Development](https://github.com/mikeroyal/ISP-Guide#computer-vision-development)

9. [Photogrammetry Development](https://github.com/mikeroyal/ISP-Guide#photogrammetry-development)

10. [LiDAR Development](https://github.com/mikeroyal/ISP-Guide#lidar-development)

11. [Bioinformatics](https://github.com/mikeroyal/ISP-Guide#bioinformatics)

12. [Augmented Reality (AR) & Virtual Reality (VR) Tools and Frameworks](https://github.com/mikeroyal/ISP-Guide#arvr-development)

13. [Game Development](https://github.com/mikeroyal/ISP-Guide#game-development)

14. [CUDA Development](https://github.com/mikeroyal/ISP-Guide#cuda-development)

15. [MATLAB Development](https://github.com/mikeroyal/ISP-Guide#matlab-development)

16. [C/C++ Development](https://github.com/mikeroyal/ISP-Guide#cc-development)

17. [Java Development](https://github.com/mikeroyal/ISP-Guide#java-development)

18. [Python Development](https://github.com/mikeroyal/ISP-Guide#python-development)

19. [Scala Development](https://github.com/mikeroyal/ISP-Guide#scala-development)

20. [R Development](https://github.com/mikeroyal/ISP-Guide#r-development)


# ISP Learning Resources
[Back to the Top](https://github.com/mikeroyal/ISP-Guide#table-of-contents)

[Image Signal Processing (ISP)](https://en.wikipedia.org/wiki/Image_processor) is the processs of converting an image into digital form by performing operations like noise reduction, auto exposure, autofocus, auto white balance, HDR correction, and image sharpening with a Specialized type of media processor.

[Image & signal processing | NIST](https://www.nist.gov/image-signal-processing)

[Image Processing Onramp | MATLAB & Simulink Tutorial](https://in.mathworks.com/learn/tutorials/image-processing-onramp.html)

[Apply convolution to image processing | MATLAB & Simulink Tutorial](https://www.mathworks.com/discovery/convolution.html)

[Signal Processing Onramp | MATLAB & Simulink Tutorial](https://www.mathworks.com/learn/tutorials/signal-processing-onramp.html)

[Deep Learning for Signal Processing Applications | MATLAB & Simulink](https://blogs.mathworks.com/deep-learning/2019/05/13/deep-learning-for-signal-processing-applications/)

[Top Signal Processing Courses Online | Coursera](https://www.coursera.org/courses?query=signal%20processing)

[Introduction to Data, Signal, and Image Analysis with MATLAB | Coursera](https://www.coursera.org/learn/matlab-image-processing)

[Top Signal Processing Courses Online | Udemy](https://www.udemy.com/courses/search/?src=ukw&q=+image+processing)

[Learn Image Processing with Online Courses and Lessons | edX](https://www.edx.org/learn/image-processing)

[Image & Signal Processing Courses: Wolfram U](https://www.wolfram.com/wolfram-u/catalog/image-signal-processing/)

[Biomedical Signal and Image Processing | MIT OpencourseWare](https://ocw.mit.edu/courses/health-sciences-and-technology/hst-582j-biomedical-signal-and-image-processing-spring-2007/)

[Digital Signal Processing Course | Prosoundtraining](https://www.prosoundtraining.com/digital-signal-processing/)

# ISP Tools, Libraries, and Frameworks
[Back to the Top](https://github.com/mikeroyal/ISP-Guide#table-of-contents)

[CCD(charge coupled device)](https://global.canon/en/technology/s_labo/light/003/04.html) is a semiconductor image sensor used in digital cameras to convert light into electrical signals. CCD Sensors are made up of tiny elements known as pixels with expressions such as 6 MP(megapixel) or 12 MP(megapixel) refering to the number of pixels comprising the CCD Sensors of a camera. With each pixel there is a tiny photodiode that is sensitive to light(photon) and becomes electrically charged in accordance with the strength of light it captures.

[CMOS(Complementary Metal Oxide Semiconductor) sensors](https://global.canon/en/technology/s_labo/light/003/05.html) are semiconductor image sensors that convert light into electrical signals. It includes features such as timing logic, exposure control, analog-to-digital conversion, shuttering, white balance, gain adjustment, and initial image processing algorithms. CMOS sensors contain rows of photodiodes coupled with individual amplifiers to amplify the electric signal from the photodiodes. This not only enables CMOS sensors to operate on less electrical power than CCDs, but also enables speedier and easier reading of electrical charges at a relatively low-cost.

<p align="center">
 <img src="https://user-images.githubusercontent.com/45159366/126912536-fba83d70-3abb-464e-8ad6-1c109471a03f.png">
  <br />
</p>

**Sensors from Alps Alpine. Source: [Alps Alpine](https://tech.alpsalpine.com/e/category_sensor.html)**

<p align="center">
 <img src="https://user-images.githubusercontent.com/45159366/126912537-82a856cb-9d4c-48a8-9d35-13a760198ddb.png">
  <br />
</p>

**Different Types of Sensors. Source: [electronicshub](https://www.electronicshub.org/different-types-sensors/)**

[Signal Processing Toolbox™](https://www.mathworks.com/products/signal.html) is a tool that provides functions and apps to analyze, preprocess, and extract features from uniformly and nonuniformly sampled signals. The toolbox includes tools for filter design and analysis, resampling, smoothing, detrending, and power spectrum estimation. The toolbox also provides functionality for extracting features like changepoints and envelopes, finding peaks and signal patterns, quantifying signal similarities, and performing measurements such as SNR and distortion.

[Embedded Coder®](https://www.mathworks.com/products/embedded-coder.html) is a tool that generates readable, compact, and fast C and C++ code for embedded processors used in mass production. It extends MATLAB Coder™ and Simulink Coder™ with advanced optimizations for precise control of the generated functions, files, and data. These optimizations improve code efficiency and facilitate integration with legacy code, data types, and calibration parameters.

[Phased Array System Toolbox™](https://www.mathworks.com/products/phased-array.html) is a tool that provides algorithms and apps for designing and simulating sensor array and beamforming systems in wireless communication, radar, sonar, acoustic, and medical imaging applications. You can model and analyze the behavior of active and passive arrays, including subarrays and arbitrary geometries.

[Radar Toolbox™](https://www.mathworks.com/products/radar.html) is a tool that includes algorithms and tools for designing, simulating, analyzing, and testing multifunction radar systems. Reference examples provide a starting point for implementing airborne, ground-based, shipborne, and automotive radar systems.

[Audio Toolbox™](https://www.mathworks.com/products/audio.html) is a tool that provides tools for audio processing, speech analysis, and acoustic measurement. It includes algorithms for processing audio signals such as equalization and time stretching, estimating acoustic signal metrics such as loudness and sharpness, and extracting audio features such as MFCC and pitch. It also provides advanced machine learning models, including i-vectors, and pretrained deep learning networks, including VGGish and CREPE.

[Wavelet Toolbox™](https://www.mathworks.com/products/wavelet.html) is a tool that provides functions and apps for analyzing and synthesizing signals and images. The toolbox includes algorithms for continuous wavelet analysis, wavelet coherence, synchrosqueezing, and data-adaptive time-frequency analysis.

[RF Toolbox™](https://www.mathworks.com/products/rftoolbox.html) is a tool that provides functions, objects, and apps for designing, modeling, analyzing, and visualizing networks of radio frequency (RF) components. It supports wireless communications, radar, and signal integrity applications.

[RF Blockset™](https://www.mathworks.com/products/rf-blockset.html) is a tool that  provides a Simulink® model library and simulation engine for designing RF communications and radar systems. The RF Blockset lets you simulate RF transceivers and front-ends. You can model nonlinear RF amplifiers to estimate gain, noise, even-order, and odd-order intermodulation distortion, including memory effects. For RF mixers, you can predict image rejection, reciprocal mixing, local oscillator phase noise, and DC offset.

[Mixed-Signal Blockset™](https://www.mathworks.com/products/mixed-signal.html) is a tool that provides models of components and impairments, analysis tools, and test benches for designing and verifying mixed-signal integrated circuits (ICs).

[H.264(AVC)](https://en.wikipedia.org/wiki/H.264/MPEG-4_AVC) is a video compression standard based on block-oriented and motion-compensated integer-DCT coding that defines multiple profiles (tools) and levels (max bitrates and resolutions) with support up to 8K.

[H.265(HEVC)](https://en.wikipedia.org/wiki/High_Efficiency_Video_Coding) is a video compression standard that is the successor to H.264(AVC). It offers a 25% to 50% better data compression at the same level of video quality, or improved video quality at the same bit-rate.

[FFmpeg](https://ffmpeg.org) is a leading multimedia framework that can decode, encode, transcode, mux, demux, stream, filter and play pretty much anything that humans and machines have created. It supports the most obscure ancient formats up to the cutting edge ones on multiple platforms such as Windows, macOS, and Linux.

[Apple ProRes](https://support.apple.com/en-us/HT200321) is a codec technology developed by Apple for high-quality & high-performance editing in Final Cut Pro that supports up to 8K.

[Logic Pro](https://www.apple.com/logic-pro/) is a digital audio workstation (DAW) and MIDI sequencer software application for macOS.

[HTTP Live Streaming (HLS)](https://developer.apple.com/streaming/) is a communications protocol developed by Apple that sends live and on‐demand audio and video to iPhone, iPad, Mac, Apple Watch, Apple TV, and PC.

[Dynamic Adaptive Streaming over HTTP (DASH)](https://developer.mozilla.org/en-US/docs/Web/HTML/DASH_Adaptive_Streaming_for_HTML_5_Video) is an adaptive streaming protocol that allows for a video stream to switch between bit rates on the basis of network performance, in order to keep a video playing.

[OpenMAX™](https://www.khronos.org/openmax/) is a cross-platform API that provides comprehensive streaming media codec and application portability by enabling accelerated multimedia components to be developed, integrated and programmed across multiple operating systems and silicon platforms.

[GStreamer](https://gstreamer.freedesktop.org/) is a library for constructing graphs of media-handling components. The applications it supports range from simple Ogg/Vorbis playback, audio/video streaming to complex audio (mixing) and video (non-linear editing) processing. Applications can take advantage of advances in codec and filter technology transparently.

[Media Source Extensions (MSE)](https://www.w3.org/TR/media-source/) is a [W3C specification](https://github.com/w3c/media-source) that allows JavaScript to send byte streams to media codecs within Web browsers that support HTML5 video and audio. Also, this allows the implementation of client-side prefetching and buffering code for streaming media entirely in JavaScript.

[NVIDIA® TensorRT™](https://developer.nvidia.com/tensorrt) is an SDK for high-performance deep learning inference. It includes a deep learning inference optimizer and runtime that delivers low latency and high throughput for deep learning inference applications.

[OpenCV](https://opencv.org) is a highly optimized library with focus on real-time computer vision applications. The C++, Python, and Java interfaces support Linux, MacOS, Windows, iOS, and Android.

[Scikit-Learn](https://scikit-learn.org/stable/index.html) is a Python module for machine learning built on top of SciPy, NumPy, and matplotlib, making it easier to apply robust and simple implementations of many popular machine learning algorithms.

[Pillow](https://python-pillow.org/) is the friendly PIL(Python Imaging Library) fork. The Python Imaging Library adds image processing capabilities to your Python interpreter. Including extensive file format support, an efficient internal representation, and fairly powerful image processing capabilities.

[CuPy](https://cupy.dev/) is an open-source array library accelerated with NVIDIA CUDA. It uses CUDA-related libraries including cuBLAS, cuDNN, cuRand, cuSolver, cuSPARSE, cuFFT and NCCL to make full use of the GPU architecture.

[Open Neural Network Exchange(ONNX)](https://github.com/onnx) is an open ecosystem that empowers AI developers to choose the right tools as their project evolves. ONNX provides an open source format for AI models, both deep learning and traditional ML. It defines an extensible computation graph model, as well as definitions of built-in operators and standard data types.

[Apache MXNet](https://mxnet.apache.org/) is a deep learning framework designed for both efficiency and flexibility. It allows you to mix symbolic and imperative programming to maximize efficiency and productivity. At its core, MXNet contains a dynamic dependency scheduler that automatically parallelizes both symbolic and imperative operations on the fly. A graph optimization layer on top of that makes symbolic execution fast and memory efficient. MXNet is portable and lightweight, scaling effectively to multiple GPUs and multiple machines. Support for Python, R, Julia, Scala, Go, Javascript and more.

[AutoGluon](https://autogluon.mxnet.io/index.html) is toolkit for Deep learning that automates machine learning tasks enabling you to easily achieve strong predictive performance in your applications. With just a few lines of code, you can train and deploy high-accuracy deep learning models on tabular, image, and text data.

[Anaconda](https://www.anaconda.com/) is a very popular Data Science platform for machine learning and deep learning that enables users to develop models, train them, and deploy them.

[PlaidML](https://github.com/plaidml/plaidml) is an advanced and portable tensor compiler for enabling deep learning on laptops, embedded devices, or other devices where the available computing hardware is not well supported or the available software stack contains unpalatable license restrictions.

# DSP Development
[Back to the Top](https://github.com/mikeroyal/ISP-Guide#table-of-contents)

<p align="center">
 <img src="https://user-images.githubusercontent.com/45159366/130368423-65b10b6e-941e-4427-b10e-4c92e239bd1b.png">
  <br />
</p>

## Digital Signal Processing(DSP) Learning Resources

[Digital Signal Processing (DSP)](https://en.wikipedia.org/wiki/Digital_signal_processing) is the application of a digital computer to modify an analog or digital signal. It's wadely used in many applications including video/audio/data communications and networking, medical imaging and computer vision, speech synthesis and coding, digital audio and video, and control of complex systems and industrial processes.

[Learn Digital Signal Processing (DSP) | Udemy](https://www.udemy.com/course/learn-digital-signal-processing/)

[Digital Signal Processing (DSP) From Ground Up™ in C | Udemy](https://www.udemy.com/course/digital-signal-processing-dsp-from-ground-uptm-in-c/)

[Digital Signal Processing Courses | Coursera](https://www.coursera.org/specializations/digital-signal-processing)

[DSP - Digital Signal Processing - Intel® FPGA](https://www.intel.com/content/www/us/en/architecture-and-technology/programmable/digital-signal-processing/overview.html)

[Digital Signal Processing | Stanford Online](https://online.stanford.edu/courses/ee264-digital-signal-processing)

[Digital Signal Processing | UC San Diego Extension](https://extension.ucsd.edu/courses-and-programs/digital-signal-processing)

[Digital Signal Processing I Courses Online | Purdue](https://engineering.purdue.edu/online/courses/digital-signal-processing-i)

[Digital Signal Processing | MIT OpenCourseWare](https://ocw.mit.edu/resources/res-6-008-digital-signal-processing-spring-2011/)

[Creative Digital Signal Processing (DSP) for Music and Visuals](https://online.berklee.edu/courses/creative-digital-signal-processing-dsp-for-music-and-visuals)

[Digital Signal Processing Course | Prosoundtraining](https://www.prosoundtraining.com/digital-signal-processing/)


## Digital Signal Processing(DSP) Tools, Libraries and Frameworks

[DSP System Toolbox™](https://www.mathworks.com/products/dsp-system.html) is a tool that provides algorithms, apps, and scopes for designing, simulating, and analyzing signal processing systems in MATLAB® and Simulink®. You can model real-time DSP systems for communications, radar, audio, medical devices, IoT, and other applications. The DSP System Toolbox you can design and analyze FIR, IIR, multirate, multistage, and adaptive filters. You can stream signals from variables, data files, and network devices for system development and verification.

[Signal Processing Toolbox™](https://www.mathworks.com/products/signal.html) is a tool that provides functions and apps to analyze, preprocess, and extract features from uniformly and nonuniformly sampled signals. The toolbox includes tools for filter design and analysis, resampling, smoothing, detrending, and power spectrum estimation. The toolbox also provides functionality for extracting features like changepoints and envelopes, finding peaks and signal patterns, quantifying signal similarities, and performing measurements such as SNR and distortion.

[Phased Array System Toolbox™](https://www.mathworks.com/products/phased-array.html) is a tool that provides algorithms and apps for designing and simulating sensor array and beamforming systems in wireless communication, radar, sonar, acoustic, and medical imaging applications. You can model and analyze the behavior of active and passive arrays, including subarrays and arbitrary geometries.

[Radar Toolbox™](https://www.mathworks.com/products/radar.html) is a tool that includes algorithms and tools for designing, simulating, analyzing, and testing multifunction radar systems. Reference examples provide a starting point for implementing airborne, ground-based, shipborne, and automotive radar systems.

[Audio Toolbox™](https://www.mathworks.com/products/audio.html) is a tool that provides tools for audio processing, speech analysis, and acoustic measurement. It includes algorithms for processing audio signals such as equalization and time stretching, estimating acoustic signal metrics such as loudness and sharpness, and extracting audio features such as MFCC and pitch. It also provides advanced machine learning models, including i-vectors, and pretrained deep learning networks, including VGGish and CREPE.

[Wavelet Toolbox™](https://www.mathworks.com/products/wavelet.html) is a tool that provides functions and apps for analyzing and synthesizing signals and images. The toolbox includes algorithms for continuous wavelet analysis, wavelet coherence, synchrosqueezing, and data-adaptive time-frequency analysis.

[Antenna Toolbox™](https://www.mathworks.com/products/antenna.html) is a tool that provides functions and apps for the design, analysis, and visualization of antenna elements and arrays. It can design standalone antennas and build arrays of antennas using predefined elements with parameterized geometry, arbitrary planar structures, or custom 3D structures described with STL files.

[RF Toolbox™](https://www.mathworks.com/products/rftoolbox.html) is a tool that provides functions, objects, and apps for designing, modeling, analyzing, and visualizing networks of radio frequency (RF) components. It supports wireless communications, radar, and signal integrity applications.

[RF Blockset™](https://www.mathworks.com/products/rf-blockset.html) is a tool that  provides a Simulink® model library and simulation engine for designing RF communications and radar systems. The RF Blockset lets you simulate RF transceivers and front-ends. You can model nonlinear RF amplifiers to estimate gain, noise, even-order, and odd-order intermodulation distortion, including memory effects. For RF mixers, you can predict image rejection, reciprocal mixing, local oscillator phase noise, and DC offset.

[Mixed-Signal Blockset™](https://www.mathworks.com/products/mixed-signal.html) is a tool that provides models of components and impairments, analysis tools, and test benches for designing and verifying mixed-signal integrated circuits (ICs).

[SerDes Toolbox™](https://www.mathworks.com/products/serdes.html) is a tool that provides a MATLAB® and Simulink® model library and a set of analysis tools and apps for the design and verification of serializer/deserializer (SerDes) systems or high-speed memory PHYs such as DDR5.

[Communications Toolbox™](https://www.mathworks.com/products/communications.html) is a tool that provides algorithms and apps for the analysis, design, end-to-end simulation, and verification of communications systems. Toolbox algorithms including channel coding, modulation, MIMO, and OFDM enable you to compose and simulate a physical layer model of your standard-based or custom-designed wireless communications system.

[WLAN Toolbox™](https://www.mathworks.com/products/wlan.html) is a tool that provides standards-compliant functions for the design, simulation, analysis, and testing of wireless LAN communications systems. It includes configurable physical layer waveforms for the IEEE® 802.11 family of standards. It also provides transmitter, channel modeling, and receiver operations, including channel coding, modulation, spatial stream mapping, and MIMO receivers.

[LTE Toolbox™](https://www.mathworks.com/products/lte.html) is a tool that provides standard-compliant functions and apps for the design, simulation, and verification of LTE, LTE-Advanced, and LTE-Advanced Pro communications systems. The system toolbox accelerates LTE algorithm and physical layer (PHY) development, supports golden reference verification and conformance testing, and enables test waveform generation.

[5G Toolbox™](https://www.mathworks.com/products/5g.html) is a tool that provides standard-compliant functions and reference examples for the modeling, simulation, and verification of 5G New Radio (NR) communications systems. The toolbox supports link-level simulation, golden reference verification, conformance testing, and test waveform generation.

[Satellite Communications Toolbox™](https://www.mathworks.com/products/satellite-communications.html) is a tool that provides standards-based tools for designing, simulating, and verifying satellite communications systems and links. The toolbox enables you to model and visualize satellite orbits and perform link analysis and access calculations.

[Data Acquisition Toolbox™](https://www.mathworks.com/products/data-acquisition.html) is a tool that provides apps and functions for configuring data acquisition hardware, reading data into MATLAB® and Simulink®, and writing data to DAQ analog and digital output channels. The toolbox supports a variety of DAQ hardware, including USB, PCI, PCI Express®, PXI®, and PXI Express® devices, from National Instruments® and other vendors.

[Instrument Control Toolbox™](https://www.mathworks.com/products/instrument.html) is a tool that lets you connect MATLAB® directly to instruments such as oscilloscopes, function generators, signal analyzers, power supplies, and analytical instruments. The toolbox connects to your instruments via instrument drivers such as IVI and VXIplug&play or via text-based SCPI commands over commonly used communication protocols such as GPIB, VISA, TCP/IP, and UDP.

[Embedded Coder®](https://www.mathworks.com/products/embedded-coder.html) is a tool that generates readable, compact, and fast C and C++ code for embedded processors used in mass production. It extends MATLAB Coder™ and Simulink Coder™ with advanced optimizations for precise control of the generated functions, files, and data. These optimizations improve code efficiency and facilitate integration with legacy code, data types, and calibration parameters.

### DSP Tools & Protocols for Audio/Video

[H.264(AVC)](https://en.wikipedia.org/wiki/H.264/MPEG-4_AVC) is a video compression standard based on block-oriented and motion-compensated integer-DCT coding that defines multiple profiles (tools) and levels (max bitrates and resolutions) with support up to 8K.

[H.265(HEVC)](https://en.wikipedia.org/wiki/High_Efficiency_Video_Coding) is a video compression standard that is the successor to H.264(AVC). It offers a 25% to 50% better data compression at the same level of video quality, or improved video quality at the same bit-rate.

[FFmpeg](https://ffmpeg.org) is a leading multimedia framework that can decode, encode, transcode, mux, demux, stream, filter and play pretty much anything that humans and machines have created. It supports the most obscure ancient formats up to the cutting edge ones on multiple platforms such as Windows, macOS, and Linux.

[HandBrake](https://handbrake.fr/) is a tool for transcoding video from almost any format with a selection of widely supported codecs. It is supported on Window, macOS, and Linux.

[HTTP Live Streaming (HLS)](https://developer.apple.com/streaming/) is a communications protocol developed by Apple that sends live and on‐demand audio and video to iPhone, iPad, Mac, Apple Watch, Apple TV, and PC.

[Dynamic Adaptive Streaming over HTTP (DASH)](https://developer.mozilla.org/en-US/docs/Web/HTML/DASH_Adaptive_Streaming_for_HTML_5_Video) is an adaptive streaming protocol that allows for a video stream to switch between bit rates on the basis of network performance, in order to keep a video playing.

[OpenMAX™](https://www.khronos.org/openmax/) is a cross-platform API that provides comprehensive streaming media codec and application portability by enabling accelerated multimedia components to be developed, integrated and programmed across multiple operating systems and silicon platforms.

[GStreamer](https://gstreamer.freedesktop.org/) is a library for constructing graphs of media-handling components. The applications it supports range from simple Ogg/Vorbis playback, audio/video streaming to complex audio (mixing) and video (non-linear editing) processing. Applications can take advantage of advances in codec and filter technology transparently.

[Media Source Extensions (MSE)](https://www.w3.org/TR/media-source/) is a [W3C specification](https://github.com/w3c/media-source) that allows JavaScript to send byte streams to media codecs within Web browsers that support HTML5 video and audio. Also, this allows the implementation of client-side prefetching and buffering code for streaming media entirely in JavaScript.

[WebRTC](https://webrtc.org/) is an open-source project that adds real-time communication capabilities to your application that works on top of an open standard. It supports video, voice, and generic data to be sent between peers, allowing developers to build powerful voice- and video-communication solutions.

[Apple ProRes](https://support.apple.com/en-us/HT200321) is a codec technology developed by Apple for high-quality & high-performance editing in Final Cut Pro that supports up to 8K.

[Logic Pro](https://www.apple.com/logic-pro/) is a digital audio workstation (DAW) and MIDI sequencer software application for macOS.

[JACK Audio Connection Kit AKA JACK](https://jackaudio.org/) is a professional sound server daemon that provides real-time, low-latency connections for both audio and MIDI data between applications that implement its API. JACK can be configured to send audio data over a network to a main machine, which then outputs the audio to a physical device. This can be useful to mix audio from a number of connected computers without requiring additional cables or hardware mixers, and keeping the audio path digital for as long as possible.

### Sensors

[CCD(charge coupled device)](https://global.canon/en/technology/s_labo/light/003/04.html) is a semiconductor image sensor used in digital cameras to convert light into electrical signals. CCD Sensors are made up of tiny elements known as pixels with expressions such as 6 MP(megapixel) or 12 MP(megapixel) refering to the number of pixels comprising the CCD Sensors of a camera. With each pixel there is a tiny photodiode that is sensitive to light(photon) and becomes electrically charged in accordance with the strength of light it captures.

[CMOS(Complementary Metal Oxide Semiconductor) sensors](https://global.canon/en/technology/s_labo/light/003/05.html) are semiconductor image sensors that convert light into electrical signals. It includes features such as timing logic, exposure control, analog-to-digital conversion, shuttering, white balance, gain adjustment, and initial image processing algorithms. CMOS sensors contain rows of photodiodes coupled with individual amplifiers to amplify the electric signal from the photodiodes. This not only enables CMOS sensors to operate on less electrical power than CCDs, but also enables speedier and easier reading of electrical charges at a relatively low-cost.

<p align="center">
 <img src="https://user-images.githubusercontent.com/45159366/126912536-fba83d70-3abb-464e-8ad6-1c109471a03f.png">
  <br />
</p>

**Sensors from Alps Alpine. Source: [Alps Alpine](https://tech.alpsalpine.com/e/category_sensor.html)**

<p align="center">
 <img src="https://user-images.githubusercontent.com/45159366/126912537-82a856cb-9d4c-48a8-9d35-13a760198ddb.png">
  <br />
</p>

**Different Types of Sensors. Source: [electronicshub](https://www.electronicshub.org/different-types-sensors/)**

# Machine Learning
[Back to the Top](https://github.com/mikeroyal/ISP-Guide#table-of-contents)

<p align="center">
 <img src="https://user-images.githubusercontent.com/45159366/134075212-b132056a-5980-4610-a141-dd0677b17b5f.png">
  <br />
</p>

## Learning Resources for ML

[Machine Learning](https://www.ibm.com/cloud/learn/machine-learning) is a branch of artificial intelligence (AI) focused on building apps using algorithms that learn from data models and improve their accuracy over time without needing to be programmed.

[Machine Learning by Stanford University from Coursera](https://www.coursera.org/learn/machine-learning)

[AWS Training and Certification for Machine Learning (ML) Courses](https://aws.amazon.com/training/learning-paths/machine-learning/)

[Machine Learning Scholarship Program for Microsoft Azure from Udacity](https://www.udacity.com/scholarships/machine-learning-scholarship-microsoft-azure)

[Microsoft Certified: Azure Data Scientist Associate](https://docs.microsoft.com/en-us/learn/certifications/azure-data-scientist)

[Microsoft Certified: Azure AI Engineer Associate](https://docs.microsoft.com/en-us/learn/certifications/azure-ai-engineer)

[Azure Machine Learning training and deployment](https://docs.microsoft.com/en-us/azure/devops/pipelines/targets/azure-machine-learning)

[Learning Machine learning and artificial intelligence from Google Cloud Training](https://cloud.google.com/training/machinelearning-ai)

[Machine Learning Crash Course for Google Cloud](https://developers.google.com/machine-learning/crash-course/)

[JupyterLab](https://jupyterlab.readthedocs.io/)

[Scheduling Jupyter notebooks on Amazon SageMaker ephemeral instances](https://aws.amazon.com/blogs/machine-learning/scheduling-jupyter-notebooks-on-sagemaker-ephemeral-instances/)

[How to run Jupyter Notebooks in your Azure Machine Learning workspace](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-run-jupyter-notebooks)

[Machine Learning Courses Online from Udemy](https://www.udemy.com/topic/machine-learning/)

[Machine Learning Courses Online from Coursera](https://www.coursera.org/courses?query=machine%20learning&)

[Learn Machine Learning with Online Courses and Classes from edX](https://www.edx.org/learn/machine-learning)

## ML Frameworks, Libraries, and Tools

[TensorFlow](https://www.tensorflow.org) is an end-to-end open source platform for machine learning. It has a comprehensive, flexible ecosystem of tools, libraries and community resources that lets researchers push the state-of-the-art in ML and developers easily build and deploy ML powered applications.

[Keras](https://keras.io) is a high-level neural networks API, written in Python and capable of running on top of TensorFlow, CNTK, or Theano.It was developed with a focus on enabling fast experimentation. It is capable of running on top of TensorFlow, Microsoft Cognitive Toolkit, R, Theano, or PlaidML.

[PyTorch](https://pytorch.org) is a library for deep learning on irregular input data such as graphs, point clouds, and manifolds. Primarily developed by Facebook's AI Research lab.

[Amazon SageMaker](https://aws.amazon.com/sagemaker/) is a fully managed service that provides every developer and data scientist with the ability to build, train, and deploy machine learning (ML) models quickly. SageMaker removes the heavy lifting from each step of the machine learning process to make it easier to develop high quality models.

[Azure Databricks](https://azure.microsoft.com/en-us/services/databricks/) is a fast and collaborative Apache Spark-based big data analytics service designed for data science and data engineering. Azure Databricks, sets up your Apache Spark environment in minutes, autoscale, and collaborate on shared projects in an interactive workspace. Azure Databricks supports Python, Scala, R, Java, and SQL, as well as data science frameworks and libraries including TensorFlow, PyTorch, and scikit-learn.

[Microsoft Cognitive Toolkit (CNTK)](https://docs.microsoft.com/en-us/cognitive-toolkit/) is an open-source toolkit for commercial-grade distributed deep learning. It describes neural networks as a series of computational steps via a directed graph. CNTK allows the user to easily realize and combine popular model types such as feed-forward DNNs, convolutional neural networks (CNNs) and recurrent neural networks (RNNs/LSTMs). CNTK implements stochastic gradient descent (SGD, error backpropagation) learning with automatic differentiation and parallelization across multiple GPUs and servers.

[Apple CoreML](https://developer.apple.com/documentation/coreml) is a framework that helps integrate machine learning models into your app. Core ML provides a unified representation for all models. Your app uses Core ML APIs and user data to make predictions, and to train or fine-tune models, all on the user's device. A model is the result of applying a machine learning algorithm to a set of training data. You use a model to make predictions based on new input data.

[Tensorflow_macOS](https://github.com/apple/tensorflow_macos) is a Mac-optimized version of TensorFlow and TensorFlow Addons for macOS 11.0+ accelerated using Apple's ML Compute framework.

[Apache OpenNLP](https://opennlp.apache.org/) is an open-source library for a machine learning based toolkit used in the processing of natural language text. It features an API for use cases like [Named Entity Recognition](https://en.wikipedia.org/wiki/Named-entity_recognition), [Sentence Detection](), [POS(Part-Of-Speech) tagging](https://en.wikipedia.org/wiki/Part-of-speech_tagging), [Tokenization](https://en.wikipedia.org/wiki/Tokenization_(data_security)) [Feature extraction](https://en.wikipedia.org/wiki/Feature_extraction), [Chunking](https://en.wikipedia.org/wiki/Chunking_(psychology)), [Parsing](https://en.wikipedia.org/wiki/Parsing), and [Coreference resolution](https://en.wikipedia.org/wiki/Coreference).

[Apache Airflow](https://airflow.apache.org) is an open-source workflow management platform created by the community to programmatically author, schedule and monitor workflows. Install. Principles. Scalable. Airflow has a modular architecture and uses a message queue to orchestrate an arbitrary number of workers. Airflow is ready to scale to infinity.

[Open Neural Network Exchange(ONNX)](https://github.com/onnx) is an open ecosystem that empowers AI developers to choose the right tools as their project evolves. ONNX provides an open source format for AI models, both deep learning and traditional ML. It defines an extensible computation graph model, as well as definitions of built-in operators and standard data types.

[Apache MXNet](https://mxnet.apache.org/) is a deep learning framework designed for both efficiency and flexibility. It allows you to mix symbolic and imperative programming to maximize efficiency and productivity. At its core, MXNet contains a dynamic dependency scheduler that automatically parallelizes both symbolic and imperative operations on the fly. A graph optimization layer on top of that makes symbolic execution fast and memory efficient. MXNet is portable and lightweight, scaling effectively to multiple GPUs and multiple machines. Support for Python, R, Julia, Scala, Go, Javascript and more.

[AutoGluon](https://autogluon.mxnet.io/index.html) is toolkit for Deep learning that automates machine learning tasks enabling you to easily achieve strong predictive performance in your applications. With just a few lines of code, you can train and deploy high-accuracy deep learning models on tabular, image, and text data.

[Anaconda](https://www.anaconda.com/) is a very popular Data Science platform for machine learning and deep learning that enables users to develop models, train them, and deploy them.

[PlaidML](https://github.com/plaidml/plaidml) is an advanced and portable tensor compiler for enabling deep learning on laptops, embedded devices, or other devices where the available computing hardware is not well supported or the available software stack contains unpalatable license restrictions.

[OpenCV](https://opencv.org) is a highly optimized library with focus on real-time computer vision applications. The C++, Python, and Java interfaces support Linux, MacOS, Windows, iOS, and Android.

[Scikit-Learn](https://scikit-learn.org/stable/index.html) is a Python module for machine learning built on top of SciPy, NumPy, and matplotlib, making it easier to apply robust and simple implementations of many popular machine learning algorithms.

[Weka](https://www.cs.waikato.ac.nz/ml/weka/) is an open source machine learning software that can be accessed through a graphical user interface, standard terminal applications, or a Java API. It is widely used for teaching, research, and industrial applications, contains a plethora of built-in tools for standard machine learning tasks, and additionally gives transparent access to well-known toolboxes such as scikit-learn, R, and Deeplearning4j.

[Caffe](https://github.com/BVLC/caffe) is a deep learning framework made with expression, speed, and modularity in mind. It is developed by Berkeley AI Research (BAIR)/The Berkeley Vision and Learning Center (BVLC) and community contributors.

[Theano](https://github.com/Theano/Theano) is a Python library that allows you to define, optimize, and evaluate mathematical expressions involving multi-dimensional arrays efficiently including tight integration with NumPy.

[nGraph](https://github.com/NervanaSystems/ngraph) is an open source C++ library, compiler and runtime for Deep Learning. The nGraph Compiler aims to accelerate developing AI workloads using any deep learning framework and deploying to a variety of hardware targets.It provides the freedom, performance, and ease-of-use to AI developers.

[NVIDIA cuDNN](https://developer.nvidia.com/cudnn) is a GPU-accelerated library of primitives for [deep neural networks](https://developer.nvidia.com/deep-learning). cuDNN provides highly tuned implementations for standard routines such as forward and backward convolution, pooling, normalization, and activation layers. cuDNN accelerates widely used deep learning frameworks, including [Caffe2](https://caffe2.ai/), [Chainer](https://chainer.org/), [Keras](https://keras.io/), [MATLAB](https://www.mathworks.com/solutions/deep-learning.html), [MxNet](https://mxnet.incubator.apache.org/), [PyTorch](https://pytorch.org/), and [TensorFlow](https://www.tensorflow.org/).

[Jupyter Notebook](https://jupyter.org/) is an open-source web application that allows you to create and share documents that contain live code, equations, visualizations and narrative text. Jupyter is used widely in industries that do data cleaning and transformation, numerical simulation, statistical modeling, data visualization, data science, and machine learning.

[Apache Spark](https://spark.apache.org/) is a unified analytics engine for large-scale data processing. It provides high-level APIs in Scala, Java, Python, and R, and an optimized engine that supports general computation graphs for data analysis. It also supports a rich set of higher-level tools including Spark SQL for SQL and DataFrames, MLlib for machine learning, GraphX for graph processing, and Structured Streaming for stream processing.

[Apache Spark Connector for SQL Server and Azure SQL](https://github.com/microsoft/sql-spark-connector) is a high-performance connector that enables you to use transactional data in big data analytics and persists results for ad-hoc queries or reporting. The connector allows you to use any SQL database, on-premises or in the cloud, as an input data source or output data sink for Spark jobs.

[Apache PredictionIO](https://predictionio.apache.org/) is an open source machine learning framework for developers, data scientists, and end users. It supports event collection, deployment of algorithms, evaluation, querying predictive results via REST APIs. It is based on scalable open source services like Hadoop, HBase (and other DBs), Elasticsearch, Spark and implements what is called a Lambda Architecture.

[Cluster Manager for Apache Kafka(CMAK)](https://github.com/yahoo/CMAK) is a tool for managing [Apache Kafka](https://kafka.apache.org/) clusters.

[BigDL](https://bigdl-project.github.io/) is a distributed deep learning library for Apache Spark. With BigDL, users can write their deep learning applications as standard Spark programs, which can directly run on top of existing Spark or Hadoop clusters.

[Eclipse Deeplearning4J (DL4J)](https://deeplearning4j.konduit.ai/) is a set of projects intended to support all the needs of a JVM-based(Scala, Kotlin, Clojure, and Groovy) deep learning application. This means starting with the raw data, loading and preprocessing it from wherever and whatever format it is in to building and tuning a wide variety of simple and complex deep learning networks.

[Tensorman](https://github.com/pop-os/tensorman) is a utility for easy management of Tensorflow containers by developed by [System76]( https://system76.com).Tensorman allows Tensorflow to operate in an isolated environment that is contained from the rest of the system. This virtual environment can operate independent of the base system, allowing you to use any version of Tensorflow on any version of a Linux distribution that supports the Docker runtime.

[Numba](https://github.com/numba/numba) is an open source, NumPy-aware optimizing compiler for Python sponsored by Anaconda, Inc. It uses the LLVM compiler project to generate machine code from Python syntax. Numba can compile a large subset of numerically-focused Python, including many NumPy functions. Additionally, Numba has support for automatic parallelization of loops, generation of GPU-accelerated code, and creation of ufuncs and C callbacks.

[Chainer](https://chainer.org/) is a Python-based deep learning framework aiming at flexibility. It provides automatic differentiation APIs based on the define-by-run approach (dynamic computational graphs) as well as object-oriented high-level APIs to build and train neural networks. It also supports CUDA/cuDNN using [CuPy](https://github.com/cupy/cupy) for high performance training and inference.

[XGBoost](https://xgboost.readthedocs.io/) is an optimized distributed gradient boosting library designed to be highly efficient, flexible and portable. It implements machine learning algorithms under the Gradient Boosting framework. XGBoost provides a parallel tree boosting (also known as GBDT, GBM) that solve many data science problems in a fast and accurate way. It supports distributed training on multiple machines, including AWS, GCE, Azure, and Yarn clusters. Also, it can be integrated with Flink, Spark and other cloud dataflow systems.

[cuML](https://github.com/rapidsai/cuml) is a suite of libraries that implement machine learning algorithms and mathematical primitives functions that share compatible APIs with other RAPIDS projects. cuML enables data scientists, researchers, and software engineers to run traditional tabular ML tasks on GPUs without going into the details of CUDA programming. In most cases, cuML's Python API matches the API from scikit-learn.

# Algorithms
[Back to the Top](https://github.com/mikeroyal/ISP-Guide#table-of-contents)

[Fuzzy logic](https://www.investopedia.com/terms/f/fuzzy-logic.asp) is a heuristic approach that allows for more advanced decision-tree processing and better integration with rules-based programming.

<p align="center">
 <img src="https://user-images.githubusercontent.com/45159366/123861872-858dce80-d8dc-11eb-9a2c-51205d1541e9.png">
  <br />
</p>

**Architecture of a Fuzzy Logic System. Source: [ResearchGate](https://www.researchgate.net/figure/Architecture-of-a-fuzzy-logic-system_fig2_309452475)**

[Support Vector Machine (SVM)](https://web.stanford.edu/~hastie/MOOC-Slides/svm.pdf) is a supervised machine learning model that uses classification algorithms for two-group classification problems.

<p align="center">
 <img src="https://user-images.githubusercontent.com/45159366/123858065-ec5cb900-d8d7-11eb-81c5-c6a8feefa84f.png">
  <br />
</p>

**Support Vector Machine (SVM). Source:[OpenClipArt](https://openclipart.org/detail/182977/svm-support-vector-machines)**

[Neural networks](https://www.ibm.com/cloud/learn/neural-networks) are a subset of machine learning and are at the heart of deep learning algorithms. The name/structure is inspired by the human brain copying the process that biological neurons/nodes signal to one another.

<p align="center">
 <img src="https://user-images.githubusercontent.com/45159366/123858036-e5ce4180-d8d7-11eb-8c52-43d7c7e6e3c4.png">
  <br />
</p>

**Deep neural network. Source: [IBM](https://www.ibm.com/cloud/learn/neural-networks)**

[Convolutional Neural Networks (R-CNN)](https://stanford.edu/~shervine/teaching/cs-230/cheatsheet-convolutional-neural-networks) is an object detection algorithm that first segments the image to find potential relevant bounding boxes and then run the detection algorithm to find most probable objects in those bounding boxes.

<p align="center">
 <img src="https://user-images.githubusercontent.com/45159366/123858026-e36be780-d8d7-11eb-9034-8859d6f09490.png">
  <br />
</p>

**Convolutional Neural Networks. Source:[CS231n](https://cs231n.github.io/convolutional-networks/#conv)**

[Recurrent neural networks (RNNs)](https://www.ibm.com/cloud/learn/recurrent-neural-networks) is a type of artificial neural network which uses sequential data or time series data.

<p align="center">
 <img src="https://user-images.githubusercontent.com/45159366/123858062-ebc42280-d8d7-11eb-9252-97e058bda8bd.png">
  <br />
</p>

**Recurrent Neural Networks. Source: [Slideteam](https://www.slideteam.net/recurrent-neural-networks-rnns-ppt-powerpoint-presentation-file-templates.html)**

[Multilayer Perceptrons (MLPs)](https://deepai.org/machine-learning-glossary-and-terms/multilayer-perceptron) is multi-layer neural networks composed of multiple layers of [perceptrons](https://en.wikipedia.org/wiki/Perceptron) with a threshold activation.

<p align="center">
 <img src="https://user-images.githubusercontent.com/45159366/123858053-e8c93200-d8d7-11eb-844c-60463ecf662c.png">
  <br />
</p>

**Multilayer Perceptrons. Source: [DeepAI](https://deepai.org/machine-learning-glossary-and-terms/multilayer-perceptron)**

[Random forest](https://www.ibm.com/cloud/learn/random-forest) is a commonly-used machine learning algorithm, which combines the output of multiple decision trees to reach a single result. A decision tree in a forest cannot be pruned for sampling and therefore, prediction selection. Its ease of use and flexibility have fueled its adoption, as it handles both classification and regression problems.

<p align="center">
 <img src="https://user-images.githubusercontent.com/45159366/124398881-fe21d000-dccc-11eb-8f5f-0a0730d85d55.png">
  <br />
</p>

**Random forest. Source: [wikimedia](https://community.tibco.com/wiki/random-forest-template-tibco-spotfirer-wiki-page)**

[Decision trees](https://www.cs.cmu.edu/~bhiksha/courses/10-601/decisiontrees/) are tree-structured models for classification and regression.

<p align="center">
 <img src="https://user-images.githubusercontent.com/45159366/124398883-ffeb9380-dccc-11eb-9adb-66729a353132.png">
  <br />
</p>

***Decision Trees. Source: [CMU](http://www.cs.cmu.edu/~bhiksha/courses/10-601/decisiontrees/)*

[Naive Bayes](https://en.wikipedia.org/wiki/Naive_Bayes_classifier) is a machine learning algorithm that is used solved calssification problems. It's based on applying [Bayes' theorem](https://www.mathsisfun.com/data/bayes-theorem.html) with strong independence assumptions between the features.

<p align="center">
 <img src="https://user-images.githubusercontent.com/45159366/124398885-00842a00-dccd-11eb-89c1-bd4c1adbf305.png">
  <br />
</p>

**Bayes' theorem. Source:[mathisfun](https://www.mathsisfun.com/data/bayes-theorem.html)**

# Deep Learning Development
[Back to the Top](https://github.com/mikeroyal/ISP-Guide#table-of-contents)

<p align="center">
 <img src="https://user-images.githubusercontent.com/45159366/133943699-6dcfcb40-ddf7-4501-86e0-41e8aee91fe2.png">
  <br />
</p>

## Deep Learning Learning Resources

[Deep Learning](https://www.ibm.com/cloud/learn/deep-learning) is a subset of machine learning, which is essentially a neural network with three or more layers. These neural networks attempt to simulate the behavior of the human brain,though, far from matching its ability. This allows the neural networks to "learn" from large amounts of data. The Learning can be [supervised](https://en.wikipedia.org/wiki/Supervised_learning), [semi-supervised](https://en.wikipedia.org/wiki/Semi-supervised_learning) or [unsupervised](https://en.wikipedia.org/wiki/Unsupervised_learning).

[Deep Learning Online Courses | NVIDIA](https://www.nvidia.com/en-us/training/online/)

[Top Deep Learning Courses Online | Coursera](https://www.coursera.org/courses?query=deep%20learning)

[Top Deep Learning Courses Online | Udemy](https://www.udemy.com/topic/deep-learning/)

[Learn Deep Learning with Online Courses and Lessons | edX](https://www.edx.org/learn/deep-learning)

[Deep Learning Online Course Nanodegree | Udacity](https://www.udacity.com/course/deep-learning-nanodegree--nd101)

[Machine Learning Course by Andrew Ng | Coursera](https://www.coursera.org/learn/machine-learning?)

[Machine Learning Engineering for Production (MLOps) course by Andrew Ng | Coursera](https://www.coursera.org/specializations/machine-learning-engineering-for-production-mlops)

[Data Science: Deep Learning and Neural Networks in Python | Udemy](https://www.udemy.com/course/data-science-deep-learning-in-python/)

[Understanding Machine Learning with Python | Pluralsight ](https://www.pluralsight.com/courses/python-understanding-machine-learning)

[How to Think About Machine Learning Algorithms | Pluralsight](https://www.pluralsight.com/courses/machine-learning-algorithms)

[Deep Learning Courses | Stanford Online](https://online.stanford.edu/courses/cs230-deep-learning)

[Deep Learning - UW Professional & Continuing Education](https://www.pce.uw.edu/courses/deep-learning)

[Deep Learning Online Courses | Harvard University](https://online-learning.harvard.edu/course/deep-learning-0)

[Machine Learning for Everyone Courses | DataCamp](https://www.datacamp.com/courses/introduction-to-machine-learning-with-r)

[Artificial Intelligence Expert Course: Platinum Edition | Udemy](https://www.udemy.com/course/artificial-intelligence-exposed-future-10-extreme-edition/)

[Top Artificial Intelligence Courses Online | Coursera](https://www.coursera.org/courses?query=artificial%20intelligence)

[Learn Artificial Intelligence with Online Courses and Lessons | edX](https://www.edx.org/learn/artificial-intelligence)

[Professional Certificate in Computer Science for Artificial Intelligence | edX](https://www.edx.org/professional-certificate/harvardx-computer-science-for-artifical-intelligence)

[Artificial Intelligence Nanodegree program](https://www.udacity.com/course/ai-artificial-intelligence-nanodegree--nd898)

[Artificial Intelligence (AI) Online Courses | Udacity](https://www.udacity.com/school-of-ai)

[Intro to Artificial Intelligence Course | Udacity](https://www.udacity.com/course/intro-to-artificial-intelligence--cs271)

[Edge AI for IoT Developers Course | Udacity](https://www.udacity.com/course/intel-edge-ai-for-iot-developers-nanodegree--nd131)

[Reasoning: Goal Trees and Rule-Based Expert Systems | MIT OpenCourseWare](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-034-artificial-intelligence-fall-2010/lecture-videos/lecture-3-reasoning-goal-trees-and-rule-based-expert-systems/)

[Expert Systems and Applied Artificial Intelligence](https://www.umsl.edu/~joshik/msis480/chapt11.htm)

[Autonomous Systems - Microsoft AI](https://www.microsoft.com/en-us/ai/autonomous-systems)

[Introduction to Microsoft Project Bonsai](https://docs.microsoft.com/en-us/learn/autonomous-systems/intro-to-project-bonsai/)

[Machine teaching with the Microsoft Autonomous Systems platform](https://docs.microsoft.com/en-us/azure/architecture/solution-ideas/articles/autonomous-systems)

[Autonomous Maritime Systems Training | AMC Search](https://www.amcsearch.com.au/ams-training)

[Top Autonomous Cars Courses Online | Udemy](https://www.udemy.com/topic/autonomous-cars/)

[Applied Control Systems 1: autonomous cars: Math + PID + MPC | Udemy](https://www.udemy.com/course/applied-systems-control-for-engineers-modelling-pid-mpc/)

[Learn Autonomous Robotics with Online Courses and Lessons | edX](https://www.edx.org/learn/autonomous-robotics)

[Artificial Intelligence Nanodegree program](https://www.udacity.com/course/ai-artificial-intelligence-nanodegree--nd898)

[Autonomous Systems Online Courses & Programs | Udacity](https://www.udacity.com/school-of-autonomous-systems)

[Edge AI for IoT Developers Course | Udacity](https://www.udacity.com/course/intel-edge-ai-for-iot-developers-nanodegree--nd131)

[Autonomous Systems MOOC and Free Online Courses | MOOC List](https://www.mooc-list.com/tags/autonomous-systems)

[Robotics and Autonomous Systems Graduate Program | Standford Online](https://online.stanford.edu/programs/robotics-and-autonomous-systems-graduate-program)

[Mobile Autonomous Systems Laboratory | MIT OpenCourseWare](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-186-mobile-autonomous-systems-laboratory-january-iap-2005/lecture-notes/)

## Deep Learning Tools, Libraries, and Frameworks

[NVIDIA cuDNN](https://developer.nvidia.com/cudnn) is a GPU-accelerated library of primitives for [deep neural networks](https://developer.nvidia.com/deep-learning). cuDNN provides highly tuned implementations for standard routines such as forward and backward convolution, pooling, normalization, and activation layers. cuDNN accelerates widely used deep learning frameworks, including [Caffe2](https://caffe2.ai/), [Chainer](https://chainer.org/), [Keras](https://keras.io/), [MATLAB](https://www.mathworks.com/solutions/deep-learning.html), [MxNet](https://mxnet.incubator.apache.org/), [PyTorch](https://pytorch.org/), and [TensorFlow](https://www.tensorflow.org/).

[NVIDIA DLSS (Deep Learning Super Sampling)](https://developer.nvidia.com/dlss) is a temporal image upscaling AI rendering technology that increases graphics performance using dedicated Tensor Core AI processors on GeForce RTX™ GPUs. DLSS uses the power of a deep learning neural network to boost frame rates and generate beautiful, sharp images for your games.

[AMD FidelityFX Super Resolution (FSR)](https://www.amd.com/en/technologies/radeon-software-fidelityfx) is an open source, high-quality solution for producing high resolution frames from lower resolution inputs. It uses a collection of cutting-edge Deep Learning algorithms with a particular emphasis on creating high-quality edges, giving large performance improvements compared to rendering at native resolution directly. FSR enables “practical performance” for costly render operations, such as hardware ray tracing for the AMD RDNA™ and AMD RDNA™ 2 architectures.

[Intel Xe Super Sampling (XeSS)](https://www.youtube.com/watch?v=Y9hfpf-SqEg) is a temporal image upscaling AI rendering technology that increases graphics performance similar to NVIDIA's [DLSS (Deep Learning Super Sampling)](https://developer.nvidia.com/dlss). Intel's Arc GPU architecture (early 2022) will have GPUs that feature dedicated Xe-cores to run XeSS. The GPUs will have Xe Matrix eXtenstions matrix (XMX) engines for hardware-accelerated AI processing. XeSS will be able to run on devices without XMX, including integrated graphics, though, the performance of XeSS will be lower on non-Intel graphics cards because it will be powered by [DP4a instruction](https://www.intel.com/content/dam/www/public/us/en/documents/reference-guides/11th-gen-quick-reference-guide.pdf).

[Jupyter Notebook](https://jupyter.org/) is an open-source web application that allows you to create and share documents that contain live code, equations, visualizations and narrative text. Jupyter is used widely in industries that do data cleaning and transformation, numerical simulation, statistical modeling, data visualization, data science, and machine learning.

[Apache Spark](https://spark.apache.org/) is a unified analytics engine for large-scale data processing. It provides high-level APIs in Scala, Java, Python, and R, and an optimized engine that supports general computation graphs for data analysis. It also supports a rich set of higher-level tools including Spark SQL for SQL and DataFrames, MLlib for machine learning, GraphX for graph processing, and Structured Streaming for stream processing.

[Apache Spark Connector for SQL Server and Azure SQL](https://github.com/microsoft/sql-spark-connector) is a high-performance connector that enables you to use transactional data in big data analytics and persists results for ad-hoc queries or reporting. The connector allows you to use any SQL database, on-premises or in the cloud, as an input data source or output data sink for Spark jobs.

[Apache PredictionIO](https://predictionio.apache.org/) is an open source machine learning framework for developers, data scientists, and end users. It supports event collection, deployment of algorithms, evaluation, querying predictive results via REST APIs. It is based on scalable open source services like Hadoop, HBase (and other DBs), Elasticsearch, Spark and implements what is called a Lambda Architecture.

[Cluster Manager for Apache Kafka(CMAK)](https://github.com/yahoo/CMAK) is a tool for managing [Apache Kafka](https://kafka.apache.org/) clusters.

[BigDL](https://bigdl-project.github.io/) is a distributed deep learning library for Apache Spark. With BigDL, users can write their deep learning applications as standard Spark programs, which can directly run on top of existing Spark or Hadoop clusters.

[Eclipse Deeplearning4J (DL4J)](https://deeplearning4j.konduit.ai/) is a set of projects intended to support all the needs of a JVM-based(Scala, Kotlin, Clojure, and Groovy) deep learning application. This means starting with the raw data, loading and preprocessing it from wherever and whatever format it is in to building and tuning a wide variety of simple and complex deep learning networks.

[Deep Learning Toolbox™](https://www.mathworks.com/products/deep-learning.html) is a tool that provides a framework for designing and implementing deep neural networks with algorithms, pretrained models, and apps. You can use convolutional neural networks (ConvNets, CNNs) and long short-term memory (LSTM) networks to perform classification and regression on image, time-series, and text data. You can build network architectures such as generative adversarial networks (GANs) and Siamese networks using automatic differentiation, custom training loops, and shared weights. With the Deep Network Designer app, you can design, analyze, and train networks graphically. It can exchange models with TensorFlow™ and PyTorch through the ONNX format and import models from TensorFlow-Keras and Caffe. The toolbox supports transfer learning with DarkNet-53, ResNet-50, NASNet, SqueezeNet and many other pretrained models.

[Reinforcement Learning Toolbox™](https://www.mathworks.com/products/reinforcement-learning.html) is a tool that provides an app, functions, and a Simulink® block for training policies using reinforcement learning algorithms, including DQN, PPO, SAC, and DDPG. You can use these policies to implement controllers and decision-making algorithms for complex applications such as resource allocation, robotics, and autonomous systems.

[Deep Learning HDL Toolbox™](https://www.mathworks.com/products/deep-learning-hdl.html) is a tool that provides functions and tools to prototype and implement deep learning networks on FPGAs and SoCs. It provides pre-built bitstreams for running a variety of deep learning networks on supported Xilinx® and Intel® FPGA and SoC devices. Profiling and estimation tools let you customize a deep learning network by exploring design, performance, and resource utilization tradeoffs.

[Parallel Computing Toolbox™](https://www.mathworks.com/products/matlab-parallel-server.html) is a tool that lets you solve computationally and data-intensive problems using multicore processors, GPUs, and computer clusters. High-level constructs such as parallel for-loops, special array types, and parallelized numerical algorithms enable you to parallelize MATLAB® applications without CUDA or MPI programming. The toolbox lets you use parallel-enabled functions in MATLAB and other toolboxes. You can use the toolbox with Simulink® to run multiple simulations of a model in parallel. Programs and models can run in both interactive and batch modes.

[XGBoost](https://xgboost.readthedocs.io/) is an optimized distributed gradient boosting library designed to be highly efficient, flexible and portable. It implements machine learning algorithms under the Gradient Boosting framework. XGBoost provides a parallel tree boosting (also known as GBDT, GBM) that solve many data science problems in a fast and accurate way. It supports distributed training on multiple machines, including AWS, GCE, Azure, and Yarn clusters. Also, it can be integrated with Flink, Spark and other cloud dataflow systems.

[LIBSVM](https://www.csie.ntu.edu.tw/~cjlin/libsvm/) is an integrated software for support vector classification, (C-SVC, nu-SVC), regression (epsilon-SVR, nu-SVR) and distribution estimation (one-class SVM). It supports multi-class classification.

[Scikit-Learn](https://scikit-learn.org/stable/index.html) is a simple and efficient tool for data mining and data analysis. It is built on NumPy,SciPy, and mathplotlib.

[TensorFlow](https://www.tensorflow.org) is an end-to-end open source platform for machine learning. It has a comprehensive, flexible ecosystem of tools, libraries and community resources that lets researchers push the state-of-the-art in ML and developers easily build and deploy ML powered applications.

[Keras](https://keras.io) is a high-level neural networks API, written in Python and capable of running on top of TensorFlow, CNTK, or Theano.It was developed with a focus on enabling fast experimentation. It is capable of running on top of TensorFlow, Microsoft Cognitive Toolkit, R, Theano, or PlaidML.

[PyTorch](https://pytorch.org) is a library for deep learning on irregular input data such as graphs, point clouds, and manifolds. Primarily developed by Facebook's AI Research lab.

[Azure Databricks](https://azure.microsoft.com/en-us/services/databricks/) is a fast and collaborative Apache Spark-based big data analytics service designed for data science and data engineering. Azure Databricks, sets up your Apache Spark environment in minutes, autoscale, and collaborate on shared projects in an interactive workspace. Azure Databricks supports Python, Scala, R, Java, and SQL, as well as data science frameworks and libraries including TensorFlow, PyTorch, and scikit-learn.

[Microsoft Cognitive Toolkit (CNTK)](https://docs.microsoft.com/en-us/cognitive-toolkit/) is an open-source toolkit for commercial-grade distributed deep learning. It describes neural networks as a series of computational steps via a directed graph. CNTK allows the user to easily realize and combine popular model types such as feed-forward DNNs, convolutional neural networks (CNNs) and recurrent neural networks (RNNs/LSTMs). CNTK implements stochastic gradient descent (SGD, error backpropagation) learning with automatic differentiation and parallelization across multiple GPUs and servers.

[Tensorflow_macOS](https://github.com/apple/tensorflow_macos) is a Mac-optimized version of TensorFlow and TensorFlow Addons for macOS 11.0+ accelerated using Apple's ML Compute framework.

[Apache Airflow](https://airflow.apache.org) is an open-source workflow management platform created by the community to programmatically author, schedule and monitor workflows. Install. Principles. Scalable. Airflow has a modular architecture and uses a message queue to orchestrate an arbitrary number of workers. Airflow is ready to scale to infinity.

[Open Neural Network Exchange(ONNX)](https://github.com/onnx) is an open ecosystem that empowers AI developers to choose the right tools as their project evolves. ONNX provides an open source format for AI models, both deep learning and traditional ML. It defines an extensible computation graph model, as well as definitions of built-in operators and standard data types.

[Apache MXNet](https://mxnet.apache.org/) is a deep learning framework designed for both efficiency and flexibility. It allows you to mix symbolic and imperative programming to maximize efficiency and productivity. At its core, MXNet contains a dynamic dependency scheduler that automatically parallelizes both symbolic and imperative operations on the fly. A graph optimization layer on top of that makes symbolic execution fast and memory efficient. MXNet is portable and lightweight, scaling effectively to multiple GPUs and multiple machines. Support for Python, R, Julia, Scala, Go, Javascript and more.

[AutoGluon](https://autogluon.mxnet.io/index.html) is toolkit for Deep learning that automates machine learning tasks enabling you to easily achieve strong predictive performance in your applications. With just a few lines of code, you can train and deploy high-accuracy deep learning models on tabular, image, and text data.

[Anaconda](https://www.anaconda.com/) is a very popular Data Science platform for machine learning and deep learning that enables users to develop models, train them, and deploy them.

[PlaidML](https://github.com/plaidml/plaidml) is an advanced and portable tensor compiler for enabling deep learning on laptops, embedded devices, or other devices where the available computing hardware is not well supported or the available software stack contains unpalatable license restrictions.

[OpenCV](https://opencv.org) is a highly optimized library with focus on real-time computer vision applications. The C++, Python, and Java interfaces support Linux, MacOS, Windows, iOS, and Android.

[Scikit-Learn](https://scikit-learn.org/stable/index.html) is a Python module for machine learning built on top of SciPy, NumPy, and matplotlib, making it easier to apply robust and simple implementations of many popular machine learning algorithms.

[Weka](https://www.cs.waikato.ac.nz/ml/weka/) is an open source machine learning software that can be accessed through a graphical user interface, standard terminal applications, or a Java API. It is widely used for teaching, research, and industrial applications, contains a plethora of built-in tools for standard machine learning tasks, and additionally gives transparent access to well-known toolboxes such as scikit-learn, R, and Deeplearning4j.

[Caffe](https://github.com/BVLC/caffe) is a deep learning framework made with expression, speed, and modularity in mind. It is developed by Berkeley AI Research (BAIR)/The Berkeley Vision and Learning Center (BVLC) and community contributors.

[Theano](https://github.com/Theano/Theano) is a Python library that allows you to define, optimize, and evaluate mathematical expressions involving multi-dimensional arrays efficiently including tight integration with NumPy.

[Microsoft Project Bonsai](https://azure.microsoft.com/en-us/services/project-bonsai/) is a low-code AI platform that speeds AI-powered automation development and part of the Autonomous Systems suite from Microsoft. Bonsai is used to build AI components that can provide operator guidance or make independent decisions to optimize process variables, improve production efficiency, and reduce downtime.

[Microsoft AirSim](https://microsoft.github.io/AirSim/lidar.html) is a simulator for drones, cars and more, built on Unreal Engine (with an experimental Unity release). AirSim is open-source, cross platform, and supports [software-in-the-loop simulation](https://www.mathworks.com/help///ecoder/software-in-the-loop-sil-simulation.html) with popular flight controllers such as PX4 & ArduPilot and [hardware-in-loop](https://www.ni.com/en-us/innovations/white-papers/17/what-is-hardware-in-the-loop-.html) with PX4 for physically and visually realistic simulations. It is developed as an Unreal plugin that can simply be dropped into any Unreal environment. AirSim is being developed  as a platform for AI research to experiment with deep learning, computer vision and reinforcement learning algorithms for autonomous vehicles.

[CARLA](https://github.com/carla-simulator/carla) is an open-source simulator for autonomous driving research. CARLA has been developed from the ground up to support development, training, and validation of autonomous driving systems. In addition to open-source code and protocols, CARLA provides open digital assets (urban layouts, buildings, vehicles) that were created for this purpose and can be used freely.

[ROS/ROS2 bridge for CARLA(package)](https://github.com/carla-simulator/ros-bridge) is a bridge that enables two-way communication between ROS and CARLA. The information from the CARLA server is translated to ROS topics. In the same way, the messages sent between nodes in ROS get translated to commands to be applied in CARLA.

[ROS Toolbox](https://www.mathworks.com/products/ros.html) is a tool that provides an interface connecting MATLAB® and Simulink® with the Robot Operating System (ROS and ROS 2), enabling you to create a network of ROS nodes. The toolbox includes MATLAB functions and Simulink blocks to import, analyze, and play back ROS data recorded in rosbag files. You can also connect to a live ROS network to access ROS messages.

[Robotics Toolbox™](https://www.mathworks.com/products/robotics.html) provides a toolbox that brings robotics specific functionality(designing, simulating, and testing manipulators, mobile robots, and humanoid robots) to MATLAB, exploiting the native capabilities of MATLAB (linear algebra, portability, graphics). The toolbox also supports mobile robots with functions for robot motion models (bicycle), path planning algorithms (bug, distance transform, D*, PRM), kinodynamic planning (lattice, RRT), localization (EKF, particle filter), map building (EKF) and simultaneous localization and mapping (EKF), and a Simulink model a of non-holonomic vehicle. The Toolbox also including a detailed Simulink model for a quadrotor flying robot.

[Image Processing Toolbox™](https://www.mathworks.com/products/image.html) is a tool that provides a comprehensive set of reference-standard algorithms and workflow apps for image processing, analysis, visualization, and algorithm development. You can perform image segmentation, image enhancement, noise reduction, geometric transformations, image registration, and 3D image processing.

[Computer Vision Toolbox™](https://www.mathworks.com/products/computer-vision.html) is a tool that provides algorithms, functions, and apps for designing and testing computer vision, 3D vision, and video processing systems. You can perform object detection and tracking, as well as feature detection, extraction, and matching. You can automate calibration workflows for single, stereo, and fisheye cameras. For 3D vision, the toolbox supports visual and point cloud SLAM, stereo vision, structure from motion, and point cloud processing.

[Robotics Toolbox™](https://www.mathworks.com/products/robotics.html) is a tool that provides a toolbox that brings robotics specific functionality(designing, simulating, and testing manipulators, mobile robots, and humanoid robots) to MATLAB, exploiting the native capabilities of MATLAB (linear algebra, portability, graphics). The toolbox also supports mobile robots with functions for robot motion models (bicycle), path planning algorithms (bug, distance transform, D*, PRM), kinodynamic planning (lattice, RRT), localization (EKF, particle filter), map building (EKF) and simultaneous localization and mapping (EKF), and a Simulink model a of non-holonomic vehicle. The Toolbox also including a detailed Simulink model for a quadrotor flying robot.

[Model Predictive Control Toolbox™](https://www.mathworks.com/products/model-predictive-control.html) is a tool that provides functions, an app, and Simulink® blocks for designing and simulating controllers using linear and nonlinear model predictive control (MPC). The toolbox lets you specify plant and disturbance models, horizons, constraints, and weights. By running closed-loop simulations, you can evaluate controller performance.

[Predictive Maintenance Toolbox™](https://www.mathworks.com/products/predictive-maintenance.html)  is a tool that lets you manage sensor data, design condition indicators, and estimate the remaining useful life (RUL) of a machine. The toolbox provides functions and an interactive app for exploring, extracting, and ranking features using data-based and model-based techniques, including statistical, spectral, and time-series analysis.

[Vision HDL Toolbox™](https://www.mathworks.com/products/vision-hdl.html) is a tool that provides pixel-streaming algorithms for the design and implementation of vision systems on FPGAs and ASICs. It provides a design framework that supports a diverse set of interface types, frame sizes, and frame rates. The image processing, video, and computer vision algorithms in the toolbox use an architecture appropriate for HDL implementations.

[Automated Driving Toolbox™](https://www.mathworks.com/products/automated-driving.html) is a MATLAB tool that provides algorithms and tools for designing, simulating, and testing ADAS and autonomous driving systems. You can design and test vision and lidar perception systems, as well as sensor fusion, path planning, and vehicle controllers. Visualization tools include a bird’s-eye-view plot and scope for sensor coverage, detections and tracks, and displays for video, lidar, and maps. The toolbox lets you import and work with HERE HD Live Map data and OpenDRIVE® road networks. It also provides reference application examples for common ADAS and automated driving features, including FCW, AEB, ACC, LKA, and parking valet. The toolbox supports C/C++ code generation for rapid prototyping and HIL testing, with support for sensor fusion, tracking, path planning, and vehicle controller algorithms.

[UAV Toolbox](https://www.mathworks.com/products/uav.html) is an application that provides tools and reference applications for designing, simulating, testing, and deploying unmanned aerial vehicle (UAV) and drone applications. You can design autonomous flight algorithms, UAV missions, and flight controllers. The Flight Log Analyzer app lets you interactively analyze 3D flight paths, telemetry information, and sensor readings from common flight log formats.

[Navigation Toolbox™](https://www.mathworks.com/products/navigation.html) is a tool that provides algorithms and analysis tools for motion planning, simultaneous localization and mapping (SLAM), and inertial navigation. The toolbox includes customizable search and sampling-based path planners, as well as metrics for validating and comparing paths. You can create 2D and 3D map representations, generate maps using SLAM algorithms, and interactively visualize and debug map generation with the SLAM map builder app.

[Lidar Toolbox™](https://www.mathworks.com/products/lidar.html) is a tool that provides algorithms, functions, and apps for designing, analyzing, and testing lidar processing systems. You can perform object detection and tracking, semantic segmentation, shape fitting, lidar registration, and obstacle detection. Lidar Toolbox supports lidar-camera cross calibration for workflows that combine computer vision and lidar processing.

[Mapping Toolbox™](https://www.mathworks.com/products/mapping.html) is a tool that provides algorithms and functions for transforming geographic data and creating map displays. You can visualize your data in a geographic context, build map displays from more than 60 map projections, and transform data from a variety of sources into a consistent geographic coordinate system.

# Reinforcement Learning Development
[Back to the Top](https://github.com/mikeroyal/ISP-Guide#table-of-contents)

<p align="center">
 <img src="https://user-images.githubusercontent.com/45159366/133943722-059d8f26-44d7-40c3-9850-4b3a88d46b01.png">
  <br />
</p>

## Reinforcement Learning Learning Resources

[Reinforcement Learning](https://www.ibm.com/cloud/learn/deep-learning#toc-deep-learn-md_Q_Of3) is a subset of machine learning, which is a neural network with three or more layers. These neural networks attempt to simulate the behavior of the human brain,though, far from matching its ability. This allows the neural networks to "learn" from a process in which a model learns to become more accurate for performing an action in an environment based on feedback in order to maximize the reward. The Learning can be [supervised](https://en.wikipedia.org/wiki/Supervised_learning), [semi-supervised](https://en.wikipedia.org/wiki/Semi-supervised_learning) or [unsupervised](https://en.wikipedia.org/wiki/Unsupervised_learning).

[Top Reinforcement Learning Courses | Coursera](https://www.coursera.org/courses?query=reinforcement%20learning)

[Top Reinforcement Learning Courses | Udemy](https://www.udemy.com/topic/reinforcement-learning/)

[Top Reinforcement Learning Courses | Udacity](https://www.udacity.com/course/reinforcement-learning--ud600)

[Reinforcement Learning Courses | Stanford Online](https://online.stanford.edu/courses/xcs234-reinforcement-learning)

[Deep Learning Online Courses | NVIDIA](https://www.nvidia.com/en-us/training/online/)

[Top Deep Learning Courses Online | Coursera](https://www.coursera.org/courses?query=deep%20learning)

[Top Deep Learning Courses Online | Udemy](https://www.udemy.com/topic/deep-learning/)

[Learn Deep Learning with Online Courses and Lessons | edX](https://www.edx.org/learn/deep-learning)

[Deep Learning Online Course Nanodegree | Udacity](https://www.udacity.com/course/deep-learning-nanodegree--nd101)

[Machine Learning Course by Andrew Ng | Coursera](https://www.coursera.org/learn/machine-learning?)

[Machine Learning Engineering for Production (MLOps) course by Andrew Ng | Coursera](https://www.coursera.org/specializations/machine-learning-engineering-for-production-mlops)

[Data Science: Deep Learning and Neural Networks in Python | Udemy](https://www.udemy.com/course/data-science-deep-learning-in-python/)

[Understanding Machine Learning with Python | Pluralsight ](https://www.pluralsight.com/courses/python-understanding-machine-learning)

[How to Think About Machine Learning Algorithms | Pluralsight](https://www.pluralsight.com/courses/machine-learning-algorithms)

[Deep Learning Courses | Stanford Online](https://online.stanford.edu/courses/cs230-deep-learning)

[Deep Learning - UW Professional & Continuing Education](https://www.pce.uw.edu/courses/deep-learning)

[Deep Learning Online Courses | Harvard University](https://online-learning.harvard.edu/course/deep-learning-0)

[Machine Learning for Everyone Courses | DataCamp](https://www.datacamp.com/courses/introduction-to-machine-learning-with-r)

[Artificial Intelligence Expert Course: Platinum Edition | Udemy](https://www.udemy.com/course/artificial-intelligence-exposed-future-10-extreme-edition/)

[Top Artificial Intelligence Courses Online | Coursera](https://www.coursera.org/courses?query=artificial%20intelligence)

[Learn Artificial Intelligence with Online Courses and Lessons | edX](https://www.edx.org/learn/artificial-intelligence)

[Professional Certificate in Computer Science for Artificial Intelligence | edX](https://www.edx.org/professional-certificate/harvardx-computer-science-for-artifical-intelligence)

[Artificial Intelligence Nanodegree program](https://www.udacity.com/course/ai-artificial-intelligence-nanodegree--nd898)

[Artificial Intelligence (AI) Online Courses | Udacity](https://www.udacity.com/school-of-ai)

[Intro to Artificial Intelligence Course | Udacity](https://www.udacity.com/course/intro-to-artificial-intelligence--cs271)

[Edge AI for IoT Developers Course | Udacity](https://www.udacity.com/course/intel-edge-ai-for-iot-developers-nanodegree--nd131)

[Reasoning: Goal Trees and Rule-Based Expert Systems | MIT OpenCourseWare](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-034-artificial-intelligence-fall-2010/lecture-videos/lecture-3-reasoning-goal-trees-and-rule-based-expert-systems/)

[Expert Systems and Applied Artificial Intelligence](https://www.umsl.edu/~joshik/msis480/chapt11.htm)

[Autonomous Systems - Microsoft AI](https://www.microsoft.com/en-us/ai/autonomous-systems)

[Introduction to Microsoft Project Bonsai](https://docs.microsoft.com/en-us/learn/autonomous-systems/intro-to-project-bonsai/)

[Machine teaching with the Microsoft Autonomous Systems platform](https://docs.microsoft.com/en-us/azure/architecture/solution-ideas/articles/autonomous-systems)

[Autonomous Maritime Systems Training | AMC Search](https://www.amcsearch.com.au/ams-training)

[Top Autonomous Cars Courses Online | Udemy](https://www.udemy.com/topic/autonomous-cars/)

[Applied Control Systems 1: autonomous cars: Math + PID + MPC | Udemy](https://www.udemy.com/course/applied-systems-control-for-engineers-modelling-pid-mpc/)

[Learn Autonomous Robotics with Online Courses and Lessons | edX](https://www.edx.org/learn/autonomous-robotics)

[Artificial Intelligence Nanodegree program](https://www.udacity.com/course/ai-artificial-intelligence-nanodegree--nd898)

[Autonomous Systems Online Courses & Programs | Udacity](https://www.udacity.com/school-of-autonomous-systems)

[Edge AI for IoT Developers Course | Udacity](https://www.udacity.com/course/intel-edge-ai-for-iot-developers-nanodegree--nd131)

[Autonomous Systems MOOC and Free Online Courses | MOOC List](https://www.mooc-list.com/tags/autonomous-systems)

[Robotics and Autonomous Systems Graduate Program | Standford Online](https://online.stanford.edu/programs/robotics-and-autonomous-systems-graduate-program)

[Mobile Autonomous Systems Laboratory | MIT OpenCourseWare](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-186-mobile-autonomous-systems-laboratory-january-iap-2005/lecture-notes/)

## Reinforcement Learning Tools, Libraries, and Frameworks

[OpenAI](https://gym.openai.com/) is an open source Python library for developing and comparing reinforcement learning algorithms by providing a standard API to communicate between learning algorithms and environments, as well as a standard set of environments compliant with that API.

[ReinforcementLearning.jl](https://juliareinforcementlearning.org/) is a collection of tools for doing reinforcement learning research in Julia.

[Reinforcement Learning Toolbox™](https://www.mathworks.com/products/reinforcement-learning.html) is a tool that provides an app, functions, and a Simulink® block for training policies using reinforcement learning algorithms, including DQN, PPO, SAC, and DDPG. You can use these policies to implement controllers and decision-making algorithms for complex applications such as resource allocation, robotics, and autonomous systems.

[Amazon SageMaker](https://aws.amazon.com/robomaker/) is a fully managed service that provides every developer and data scientist with the ability to build, train, and deploy machine learning (ML) models quickly.

[AWS RoboMaker](https://aws.amazon.com/robomaker/) is a service that provides a fully-managed, scalable infrastructure for simulation that customers use for multi-robot simulation and CI/CD integration with regression testing in simulation.

[TensorFlow](https://www.tensorflow.org) is an end-to-end open source platform for machine learning. It has a comprehensive, flexible ecosystem of tools, libraries and community resources that lets researchers push the state-of-the-art in ML and developers easily build and deploy ML powered applications.

[Keras](https://keras.io) is a high-level neural networks API, written in Python and capable of running on top of TensorFlow, CNTK, or Theano.It was developed with a focus on enabling fast experimentation. It is capable of running on top of TensorFlow, Microsoft Cognitive Toolkit, R, Theano, or PlaidML.

[PyTorch](https://pytorch.org) is a library for deep learning on irregular input data such as graphs, point clouds, and manifolds. Primarily developed by Facebook's AI Research lab.

[Scikit-Learn](https://scikit-learn.org/stable/index.html) is a simple and efficient tool for data mining and data analysis. It is built on NumPy,SciPy, and mathplotlib.

[NVIDIA cuDNN](https://developer.nvidia.com/cudnn) is a GPU-accelerated library of primitives for [deep neural networks](https://developer.nvidia.com/deep-learning). cuDNN provides highly tuned implementations for standard routines such as forward and backward convolution, pooling, normalization, and activation layers. cuDNN accelerates widely used deep learning frameworks, including [Caffe2](https://caffe2.ai/), [Chainer](https://chainer.org/), [Keras](https://keras.io/), [MATLAB](https://www.mathworks.com/solutions/deep-learning.html), [MxNet](https://mxnet.incubator.apache.org/), [PyTorch](https://pytorch.org/), and [TensorFlow](https://www.tensorflow.org/).

[Jupyter Notebook](https://jupyter.org/) is an open-source web application that allows you to create and share documents that contain live code, equations, visualizations and narrative text. Jupyter is used widely in industries that do data cleaning and transformation, numerical simulation, statistical modeling, data visualization, data science, and machine learning.

[Apache Spark](https://spark.apache.org/) is a unified analytics engine for large-scale data processing. It provides high-level APIs in Scala, Java, Python, and R, and an optimized engine that supports general computation graphs for data analysis. It also supports a rich set of higher-level tools including Spark SQL for SQL and DataFrames, MLlib for machine learning, GraphX for graph processing, and Structured Streaming for stream processing.

[Apache Spark Connector for SQL Server and Azure SQL](https://github.com/microsoft/sql-spark-connector) is a high-performance connector that enables you to use transactional data in big data analytics and persists results for ad-hoc queries or reporting. The connector allows you to use any SQL database, on-premises or in the cloud, as an input data source or output data sink for Spark jobs.

[Apache PredictionIO](https://predictionio.apache.org/) is an open source machine learning framework for developers, data scientists, and end users. It supports event collection, deployment of algorithms, evaluation, querying predictive results via REST APIs. It is based on scalable open source services like Hadoop, HBase (and other DBs), Elasticsearch, Spark and implements what is called a Lambda Architecture.

[Cluster Manager for Apache Kafka(CMAK)](https://github.com/yahoo/CMAK) is a tool for managing [Apache Kafka](https://kafka.apache.org/) clusters.

[BigDL](https://bigdl-project.github.io/) is a distributed deep learning library for Apache Spark. With BigDL, users can write their deep learning applications as standard Spark programs, which can directly run on top of existing Spark or Hadoop clusters.

[Eclipse Deeplearning4J (DL4J)](https://deeplearning4j.konduit.ai/) is a set of projects intended to support all the needs of a JVM-based(Scala, Kotlin, Clojure, and Groovy) deep learning application. This means starting with the raw data, loading and preprocessing it from wherever and whatever format it is in to building and tuning a wide variety of simple and complex deep learning networks.

[Deep Learning Toolbox™](https://www.mathworks.com/products/deep-learning.html) is a tool that provides a framework for designing and implementing deep neural networks with algorithms, pretrained models, and apps. You can use convolutional neural networks (ConvNets, CNNs) and long short-term memory (LSTM) networks to perform classification and regression on image, time-series, and text data. You can build network architectures such as generative adversarial networks (GANs) and Siamese networks using automatic differentiation, custom training loops, and shared weights. With the Deep Network Designer app, you can design, analyze, and train networks graphically. It can exchange models with TensorFlow™ and PyTorch through the ONNX format and import models from TensorFlow-Keras and Caffe. The toolbox supports transfer learning with DarkNet-53, ResNet-50, NASNet, SqueezeNet and many other pretrained models.

[Deep Learning HDL Toolbox™](https://www.mathworks.com/products/deep-learning-hdl.html) is a tool that provides functions and tools to prototype and implement deep learning networks on FPGAs and SoCs. It provides pre-built bitstreams for running a variety of deep learning networks on supported Xilinx® and Intel® FPGA and SoC devices. Profiling and estimation tools let you customize a deep learning network by exploring design, performance, and resource utilization tradeoffs.

[Parallel Computing Toolbox™](https://www.mathworks.com/products/matlab-parallel-server.html) is a tool that lets you solve computationally and data-intensive problems using multicore processors, GPUs, and computer clusters. High-level constructs such as parallel for-loops, special array types, and parallelized numerical algorithms enable you to parallelize MATLAB® applications without CUDA or MPI programming. The toolbox lets you use parallel-enabled functions in MATLAB and other toolboxes. You can use the toolbox with Simulink® to run multiple simulations of a model in parallel. Programs and models can run in both interactive and batch modes.

[XGBoost](https://xgboost.readthedocs.io/) is an optimized distributed gradient boosting library designed to be highly efficient, flexible and portable. It implements machine learning algorithms under the Gradient Boosting framework. XGBoost provides a parallel tree boosting (also known as GBDT, GBM) that solve many data science problems in a fast and accurate way. It supports distributed training on multiple machines, including AWS, GCE, Azure, and Yarn clusters. Also, it can be integrated with Flink, Spark and other cloud dataflow systems.

[LIBSVM](https://www.csie.ntu.edu.tw/~cjlin/libsvm/) is an integrated software for support vector classification, (C-SVC, nu-SVC), regression (epsilon-SVR, nu-SVR) and distribution estimation (one-class SVM). It supports multi-class classification.

[Azure Databricks](https://azure.microsoft.com/en-us/services/databricks/) is a fast and collaborative Apache Spark-based big data analytics service designed for data science and data engineering. Azure Databricks, sets up your Apache Spark environment in minutes, autoscale, and collaborate on shared projects in an interactive workspace. Azure Databricks supports Python, Scala, R, Java, and SQL, as well as data science frameworks and libraries including TensorFlow, PyTorch, and scikit-learn.

[Microsoft Cognitive Toolkit (CNTK)](https://docs.microsoft.com/en-us/cognitive-toolkit/) is an open-source toolkit for commercial-grade distributed deep learning. It describes neural networks as a series of computational steps via a directed graph. CNTK allows the user to easily realize and combine popular model types such as feed-forward DNNs, convolutional neural networks (CNNs) and recurrent neural networks (RNNs/LSTMs). CNTK implements stochastic gradient descent (SGD, error backpropagation) learning with automatic differentiation and parallelization across multiple GPUs and servers.

[Tensorflow_macOS](https://github.com/apple/tensorflow_macos) is a Mac-optimized version of TensorFlow and TensorFlow Addons for macOS 11.0+ accelerated using Apple's ML Compute framework.

[Apache Airflow](https://airflow.apache.org) is an open-source workflow management platform created by the community to programmatically author, schedule and monitor workflows. Install. Principles. Scalable. Airflow has a modular architecture and uses a message queue to orchestrate an arbitrary number of workers. Airflow is ready to scale to infinity.

[Open Neural Network Exchange(ONNX)](https://github.com/onnx) is an open ecosystem that empowers AI developers to choose the right tools as their project evolves. ONNX provides an open source format for AI models, both deep learning and traditional ML. It defines an extensible computation graph model, as well as definitions of built-in operators and standard data types.

[Apache MXNet](https://mxnet.apache.org/) is a deep learning framework designed for both efficiency and flexibility. It allows you to mix symbolic and imperative programming to maximize efficiency and productivity. At its core, MXNet contains a dynamic dependency scheduler that automatically parallelizes both symbolic and imperative operations on the fly. A graph optimization layer on top of that makes symbolic execution fast and memory efficient. MXNet is portable and lightweight, scaling effectively to multiple GPUs and multiple machines. Support for Python, R, Julia, Scala, Go, Javascript and more.

[AutoGluon](https://autogluon.mxnet.io/index.html) is toolkit for Deep learning that automates machine learning tasks enabling you to easily achieve strong predictive performance in your applications. With just a few lines of code, you can train and deploy high-accuracy deep learning models on tabular, image, and text data.

[Anaconda](https://www.anaconda.com/) is a very popular Data Science platform for machine learning and deep learning that enables users to develop models, train them, and deploy them.

[PlaidML](https://github.com/plaidml/plaidml) is an advanced and portable tensor compiler for enabling deep learning on laptops, embedded devices, or other devices where the available computing hardware is not well supported or the available software stack contains unpalatable license restrictions.

[OpenCV](https://opencv.org) is a highly optimized library with focus on real-time computer vision applications. The C++, Python, and Java interfaces support Linux, MacOS, Windows, iOS, and Android.

[Scikit-Learn](https://scikit-learn.org/stable/index.html) is a Python module for machine learning built on top of SciPy, NumPy, and matplotlib, making it easier to apply robust and simple implementations of many popular machine learning algorithms.

[Weka](https://www.cs.waikato.ac.nz/ml/weka/) is an open source machine learning software that can be accessed through a graphical user interface, standard terminal applications, or a Java API. It is widely used for teaching, research, and industrial applications, contains a plethora of built-in tools for standard machine learning tasks, and additionally gives transparent access to well-known toolboxes such as scikit-learn, R, and Deeplearning4j.

[Caffe](https://github.com/BVLC/caffe) is a deep learning framework made with expression, speed, and modularity in mind. It is developed by Berkeley AI Research (BAIR)/The Berkeley Vision and Learning Center (BVLC) and community contributors.

[Theano](https://github.com/Theano/Theano) is a Python library that allows you to define, optimize, and evaluate mathematical expressions involving multi-dimensional arrays efficiently including tight integration with NumPy.

[Microsoft Project Bonsai](https://azure.microsoft.com/en-us/services/project-bonsai/) is a low-code AI platform that speeds AI-powered automation development and part of the Autonomous Systems suite from Microsoft. Bonsai is used to build AI components that can provide operator guidance or make independent decisions to optimize process variables, improve production efficiency, and reduce downtime.

[Microsoft AirSim](https://microsoft.github.io/AirSim/lidar.html) is a simulator for drones, cars and more, built on Unreal Engine (with an experimental Unity release). AirSim is open-source, cross platform, and supports [software-in-the-loop simulation](https://www.mathworks.com/help///ecoder/software-in-the-loop-sil-simulation.html) with popular flight controllers such as PX4 & ArduPilot and [hardware-in-loop](https://www.ni.com/en-us/innovations/white-papers/17/what-is-hardware-in-the-loop-.html) with PX4 for physically and visually realistic simulations. It is developed as an Unreal plugin that can simply be dropped into any Unreal environment. AirSim is being developed  as a platform for AI research to experiment with deep learning, computer vision and reinforcement learning algorithms for autonomous vehicles.

[CARLA](https://github.com/carla-simulator/carla) is an open-source simulator for autonomous driving research. CARLA has been developed from the ground up to support development, training, and validation of autonomous driving systems. In addition to open-source code and protocols, CARLA provides open digital assets (urban layouts, buildings, vehicles) that were created for this purpose and can be used freely.

[ROS/ROS2 bridge for CARLA(package)](https://github.com/carla-simulator/ros-bridge) is a bridge that enables two-way communication between ROS and CARLA. The information from the CARLA server is translated to ROS topics. In the same way, the messages sent between nodes in ROS get translated to commands to be applied in CARLA.

[ROS Toolbox](https://www.mathworks.com/products/ros.html) is a tool that provides an interface connecting MATLAB® and Simulink® with the Robot Operating System (ROS and ROS 2), enabling you to create a network of ROS nodes. The toolbox includes MATLAB functions and Simulink blocks to import, analyze, and play back ROS data recorded in rosbag files. You can also connect to a live ROS network to access ROS messages.

[Robotics Toolbox™](https://www.mathworks.com/products/robotics.html) provides a toolbox that brings robotics specific functionality(designing, simulating, and testing manipulators, mobile robots, and humanoid robots) to MATLAB, exploiting the native capabilities of MATLAB (linear algebra, portability, graphics). The toolbox also supports mobile robots with functions for robot motion models (bicycle), path planning algorithms (bug, distance transform, D*, PRM), kinodynamic planning (lattice, RRT), localization (EKF, particle filter), map building (EKF) and simultaneous localization and mapping (EKF), and a Simulink model a of non-holonomic vehicle. The Toolbox also including a detailed Simulink model for a quadrotor flying robot.

[Image Processing Toolbox™](https://www.mathworks.com/products/image.html) is a tool that provides a comprehensive set of reference-standard algorithms and workflow apps for image processing, analysis, visualization, and algorithm development. You can perform image segmentation, image enhancement, noise reduction, geometric transformations, image registration, and 3D image processing.

[Computer Vision Toolbox™](https://www.mathworks.com/products/computer-vision.html) is a tool that provides algorithms, functions, and apps for designing and testing computer vision, 3D vision, and video processing systems. You can perform object detection and tracking, as well as feature detection, extraction, and matching. You can automate calibration workflows for single, stereo, and fisheye cameras. For 3D vision, the toolbox supports visual and point cloud SLAM, stereo vision, structure from motion, and point cloud processing.

[Robotics Toolbox™](https://www.mathworks.com/products/robotics.html) is a tool that provides a toolbox that brings robotics specific functionality(designing, simulating, and testing manipulators, mobile robots, and humanoid robots) to MATLAB, exploiting the native capabilities of MATLAB (linear algebra, portability, graphics). The toolbox also supports mobile robots with functions for robot motion models (bicycle), path planning algorithms (bug, distance transform, D*, PRM), kinodynamic planning (lattice, RRT), localization (EKF, particle filter), map building (EKF) and simultaneous localization and mapping (EKF), and a Simulink model a of non-holonomic vehicle. The Toolbox also including a detailed Simulink model for a quadrotor flying robot.

[Model Predictive Control Toolbox™](https://www.mathworks.com/products/model-predictive-control.html) is a tool that provides functions, an app, and Simulink® blocks for designing and simulating controllers using linear and nonlinear model predictive control (MPC). The toolbox lets you specify plant and disturbance models, horizons, constraints, and weights. By running closed-loop simulations, you can evaluate controller performance.

[Predictive Maintenance Toolbox™](https://www.mathworks.com/products/predictive-maintenance.html)  is a tool that lets you manage sensor data, design condition indicators, and estimate the remaining useful life (RUL) of a machine. The toolbox provides functions and an interactive app for exploring, extracting, and ranking features using data-based and model-based techniques, including statistical, spectral, and time-series analysis.

[Vision HDL Toolbox™](https://www.mathworks.com/products/vision-hdl.html) is a tool that provides pixel-streaming algorithms for the design and implementation of vision systems on FPGAs and ASICs. It provides a design framework that supports a diverse set of interface types, frame sizes, and frame rates. The image processing, video, and computer vision algorithms in the toolbox use an architecture appropriate for HDL implementations.

[Automated Driving Toolbox™](https://www.mathworks.com/products/automated-driving.html) is a MATLAB tool that provides algorithms and tools for designing, simulating, and testing ADAS and autonomous driving systems. You can design and test vision and lidar perception systems, as well as sensor fusion, path planning, and vehicle controllers. Visualization tools include a bird’s-eye-view plot and scope for sensor coverage, detections and tracks, and displays for video, lidar, and maps. The toolbox lets you import and work with HERE HD Live Map data and OpenDRIVE® road networks. It also provides reference application examples for common ADAS and automated driving features, including FCW, AEB, ACC, LKA, and parking valet. The toolbox supports C/C++ code generation for rapid prototyping and HIL testing, with support for sensor fusion, tracking, path planning, and vehicle controller algorithms.

[Navigation Toolbox™](https://www.mathworks.com/products/navigation.html) is a tool that provides algorithms and analysis tools for motion planning, simultaneous localization and mapping (SLAM), and inertial navigation. The toolbox includes customizable search and sampling-based path planners, as well as metrics for validating and comparing paths. You can create 2D and 3D map representations, generate maps using SLAM algorithms, and interactively visualize and debug map generation with the SLAM map builder app.

[UAV Toolbox](https://www.mathworks.com/products/uav.html) is an application that provides tools and reference applications for designing, simulating, testing, and deploying unmanned aerial vehicle (UAV) and drone applications. You can design autonomous flight algorithms, UAV missions, and flight controllers. The Flight Log Analyzer app lets you interactively analyze 3D flight paths, telemetry information, and sensor readings from common flight log formats.

[Lidar Toolbox™](https://www.mathworks.com/products/lidar.html) is a tool that provides algorithms, functions, and apps for designing, analyzing, and testing lidar processing systems. You can perform object detection and tracking, semantic segmentation, shape fitting, lidar registration, and obstacle detection. Lidar Toolbox supports lidar-camera cross calibration for workflows that combine computer vision and lidar processing.

[Mapping Toolbox™](https://www.mathworks.com/products/mapping.html) is a tool that provides algorithms and functions for transforming geographic data and creating map displays. You can visualize your data in a geographic context, build map displays from more than 60 map projections, and transform data from a variety of sources into a consistent geographic coordinate system.

# Computer Vision Development
[Back to the Top](https://github.com/mikeroyal/ISP-Guide#table-of-contents)

<p align="center">
 <img src="https://user-images.githubusercontent.com/45159366/129494417-b0ee8192-ac41-4a6d-8e1d-4761ffc8bab1.png">
  <br />
</p>

## Computer Vision Learning Resources

[Computer Vision](https://azure.microsoft.com/en-us/overview/what-is-computer-vision/) is a field of Artificial Intelligence (AI) that focuses on enabling computers to identify and understand objects and people in images and videos.

[OpenCV Courses](https://opencv.org/courses/)

[Exploring Computer Vision in Microsoft Azure](https://docs.microsoft.com/en-us/learn/paths/explore-computer-vision-microsoft-azure/)

[Top Computer Vision Courses Online | Coursera](https://www.coursera.org/courses?languages=en&query=computer%20vision)

[Top Computer Vision Courses Online | Udemy](https://www.udemy.com/topic/computer-vision/)

[Learn Computer Vision with Online Courses and Lessons | edX](https://www.edx.org/learn/computer-vision)

[Computer Vision and Image Processing Fundamentals | edX](https://www.edx.org/course/computer-vision-and-image-processing-fundamentals)

[Introduction to Computer Vision Courses | Udacity](https://www.udacity.com/course/introduction-to-computer-vision--ud810)

[Computer Vision Nanodegree program | Udacity](https://www.udacity.com/course/computer-vision-nanodegree--nd891)

[Machine Vision Course |MIT Open Courseware ](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-801-machine-vision-fall-2004/)

[Computer Vision Training Courses | NobleProg](https://www.nobleprog.com/computer-vision-training)

[Visual Computing Graduate Program | Stanford Online](https://online.stanford.edu/programs/visual-computing-graduate-program)

## Computer Vision Tools, Libraries, and Frameworks

[OpenCV](https://opencv.org) is a highly optimized library with focus on real-time computer vision applications. The C++, Python, and Java interfaces support Linux, MacOS, Windows, iOS, and Android.

[Microsoft Cognitive Toolkit (CNTK)](https://docs.microsoft.com/en-us/cognitive-toolkit/) is an open-source toolkit for commercial-grade distributed deep learning. It describes neural networks as a series of computational steps via a directed graph. CNTK allows the user to easily realize and combine popular model types such as feed-forward DNNs, convolutional neural networks (CNNs) and recurrent neural networks (RNNs/LSTMs). CNTK implements stochastic gradient descent (SGD, error backpropagation) learning with automatic differentiation and parallelization across multiple GPUs and servers.

[Scikit-Learn](https://scikit-learn.org/stable/index.html) is a Python module for machine learning built on top of SciPy, NumPy, and matplotlib, making it easier to apply robust and simple implementations of many popular machine learning algorithms.

[NVIDIA cuDNN](https://developer.nvidia.com/cudnn) is a GPU-accelerated library of primitives for [deep neural networks](https://developer.nvidia.com/deep-learning). cuDNN provides highly tuned implementations for standard routines such as forward and backward convolution, pooling, normalization, and activation layers. cuDNN accelerates widely used deep learning frameworks, including [Caffe2](https://caffe2.ai/), [Chainer](https://chainer.org/), [Keras](https://keras.io/), [MATLAB](https://www.mathworks.com/solutions/deep-learning.html), [MxNet](https://mxnet.incubator.apache.org/), [PyTorch](https://pytorch.org/), and [TensorFlow](https://www.tensorflow.org/).

[Automated Driving Toolbox™](https://www.mathworks.com/products/automated-driving.html) is a MATLAB tool that provides algorithms and tools for designing, simulating, and testing ADAS and autonomous driving systems. You can design and test vision and lidar perception systems, as well as sensor fusion, path planning, and vehicle controllers. Visualization tools include a bird’s-eye-view plot and scope for sensor coverage, detections and tracks, and displays for video, lidar, and maps. The toolbox lets you import and work with HERE HD Live Map data and OpenDRIVE® road networks. It also provides reference application examples for common ADAS and automated driving features, including FCW, AEB, ACC, LKA, and parking valet. The toolbox supports C/C++ code generation for rapid prototyping and HIL testing, with support for sensor fusion, tracking, path planning, and vehicle controller algorithms.

[LRSLibrary](https://github.com/andrewssobral/lrslibrary) is a Low-Rank and Sparse Tools for Background Modeling and Subtraction in Videos. The library was designed for moving object detection in videos, but it can be also used for other computer vision and machine learning problems.

[Image Processing Toolbox™](https://www.mathworks.com/products/image.html) is a tool that provides a comprehensive set of reference-standard algorithms and workflow apps for image processing, analysis, visualization, and algorithm development. You can perform image segmentation, image enhancement, noise reduction, geometric transformations, image registration, and 3D image processing.

[Computer Vision Toolbox™](https://www.mathworks.com/products/computer-vision.html) is a tool that provides algorithms, functions, and apps for designing and testing computer vision, 3D vision, and video processing systems. You can perform object detection and tracking, as well as feature detection, extraction, and matching. You can automate calibration workflows for single, stereo, and fisheye cameras. For 3D vision, the toolbox supports visual and point cloud SLAM, stereo vision, structure from motion, and point cloud processing.

[Statistics and Machine Learning Toolbox™](https://www.mathworks.com/products/statistics.html) is a tool that provides functions and apps to describe, analyze, and model data. You can use descriptive statistics, visualizations, and clustering for exploratory data analysis; fit probability distributions to data; generate random numbers for Monte Carlo simulations, and perform hypothesis tests. Regression and classification algorithms let you draw inferences from data and build predictive models either interactively, using the Classification and Regression Learner apps, or programmatically, using AutoML.

[Lidar Toolbox™](https://www.mathworks.com/products/lidar.html) is a tool that provides algorithms, functions, and apps for designing, analyzing, and testing lidar processing systems. You can perform object detection and tracking, semantic segmentation, shape fitting, lidar registration, and obstacle detection. Lidar Toolbox supports lidar-camera cross calibration for workflows that combine computer vision and lidar processing.

[Mapping Toolbox™](https://www.mathworks.com/products/mapping.html) is a tool that provides algorithms and functions for transforming geographic data and creating map displays. You can visualize your data in a geographic context, build map displays from more than 60 map projections, and transform data from a variety of sources into a consistent geographic coordinate system.

[UAV Toolbox](https://www.mathworks.com/products/uav.html) is an application that provides tools and reference applications for designing, simulating, testing, and deploying unmanned aerial vehicle (UAV) and drone applications. You can design autonomous flight algorithms, UAV missions, and flight controllers. The Flight Log Analyzer app lets you interactively analyze 3D flight paths, telemetry information, and sensor readings from common flight log formats.

[Parallel Computing Toolbox™](https://www.mathworks.com/products/matlab-parallel-server.html) is a tool that lets you solve computationally and data-intensive problems using multicore processors, GPUs, and computer clusters. High-level constructs such as parallel for-loops, special array types, and parallelized numerical algorithms enable you to parallelize MATLAB® applications without CUDA or MPI programming. The toolbox lets you use parallel-enabled functions in MATLAB and other toolboxes. You can use the toolbox with Simulink® to run multiple simulations of a model in parallel. Programs and models can run in both interactive and batch modes.

[Partial Differential Equation Toolbox™](https://www.mathworks.com/products/pde.html) is a tool that provides functions for solving structural mechanics, heat transfer, and general partial differential equations (PDEs) using finite element analysis.

[ROS Toolbox](https://www.mathworks.com/products/ros.html) is a tool that provides an interface connecting MATLAB® and Simulink® with the Robot Operating System (ROS and ROS 2), enabling you to create a network of ROS nodes. The toolbox includes MATLAB functions and Simulink blocks to import, analyze, and play back ROS data recorded in rosbag files. You can also connect to a live ROS network to access ROS messages.

[Robotics Toolbox™](https://www.mathworks.com/products/robotics.html) provides a toolbox that brings robotics specific functionality(designing, simulating, and testing manipulators, mobile robots, and humanoid robots) to MATLAB, exploiting the native capabilities of MATLAB (linear algebra, portability, graphics). The toolbox also supports mobile robots with functions for robot motion models (bicycle), path planning algorithms (bug, distance transform, D*, PRM), kinodynamic planning (lattice, RRT), localization (EKF, particle filter), map building (EKF) and simultaneous localization and mapping (EKF), and a Simulink model a of non-holonomic vehicle. The Toolbox also including a detailed Simulink model for a quadrotor flying robot.

[Deep Learning Toolbox™](https://www.mathworks.com/products/deep-learning.html) is a tool that provides a framework for designing and implementing deep neural networks with algorithms, pretrained models, and apps. You can use convolutional neural networks (ConvNets, CNNs) and long short-term memory (LSTM) networks to perform classification and regression on image, time-series, and text data. You can build network architectures such as generative adversarial networks (GANs) and Siamese networks using automatic differentiation, custom training loops, and shared weights. With the Deep Network Designer app, you can design, analyze, and train networks graphically. It can exchange models with TensorFlow™ and PyTorch through the ONNX format and import models from TensorFlow-Keras and Caffe. The toolbox supports transfer learning with DarkNet-53, ResNet-50, NASNet, SqueezeNet and many other pretrained models.

[Reinforcement Learning Toolbox™](https://www.mathworks.com/products/reinforcement-learning.html) is a tool that provides an app, functions, and a Simulink® block for training policies using reinforcement learning algorithms, including DQN, PPO, SAC, and DDPG. You can use these policies to implement controllers and decision-making algorithms for complex applications such as resource allocation, robotics, and autonomous systems.

[Deep Learning HDL Toolbox™](https://www.mathworks.com/products/deep-learning-hdl.html) is a tool that provides functions and tools to prototype and implement deep learning networks on FPGAs and SoCs. It provides pre-built bitstreams for running a variety of deep learning networks on supported Xilinx® and Intel® FPGA and SoC devices. Profiling and estimation tools let you customize a deep learning network by exploring design, performance, and resource utilization tradeoffs.

[Model Predictive Control Toolbox™](https://www.mathworks.com/products/model-predictive-control.html) is a tool that provides functions, an app, and Simulink® blocks for designing and simulating controllers using linear and nonlinear model predictive control (MPC). The toolbox lets you specify plant and disturbance models, horizons, constraints, and weights. By running closed-loop simulations, you can evaluate controller performance.

[Vision HDL Toolbox™](https://www.mathworks.com/products/vision-hdl.html) is a tool that provides pixel-streaming algorithms for the design and implementation of vision systems on FPGAs and ASICs. It provides a design framework that supports a diverse set of interface types, frame sizes, and frame rates. The image processing, video, and computer vision algorithms in the toolbox use an architecture appropriate for HDL implementations.

[Data Acquisition Toolbox™](https://www.mathworks.com/products/data-acquisition.html) is a tool that provides apps and functions for configuring data acquisition hardware, reading data into MATLAB® and Simulink®, and writing data to DAQ analog and digital output channels. The toolbox supports a variety of DAQ hardware, including USB, PCI, PCI Express®, PXI®, and PXI Express® devices, from National Instruments® and other vendors.

[Microsoft AirSim](https://microsoft.github.io/AirSim/lidar.html) is a simulator for drones, cars and more, built on Unreal Engine (with an experimental Unity release). AirSim is open-source, cross platform, and supports [software-in-the-loop simulation](https://www.mathworks.com/help///ecoder/software-in-the-loop-sil-simulation.html) with popular flight controllers such as PX4 & ArduPilot and [hardware-in-loop](https://www.ni.com/en-us/innovations/white-papers/17/what-is-hardware-in-the-loop-.html) with PX4 for physically and visually realistic simulations. It is developed as an Unreal plugin that can simply be dropped into any Unreal environment. AirSim is being developed  as a platform for AI research to experiment with deep learning, computer vision and reinforcement learning algorithms for autonomous vehicles.


# Photogrammetry Development
[Back to the Top](https://github.com/mikeroyal/ISP-Guide#table-of-contents)

<p align="center">
 <img src="https://user-images.githubusercontent.com/45159366/129494677-0341843b-c78c-4027-8a2c-43e98a995f6f.png">
  <br />
</p>

## Photogrammetry Learning Resources

[Photogrammetry](https://www.autodesk.com/solutions/photogrammetry-software) is the art and science of extracting 3D information from photographs. The process involves taking overlapping photographs of an object, structure, or space, and converting them into 2D or 3D digital models. Photogrammetry is often used by surveyors, architects, engineers, and contractors to create topographic maps, meshes, point clouds, or drawings based on the real-world.

[Aerial photogrammetry](https://www.autodesk.com/solutions/photogrammetry-software) is process of utilizing aircrafts to produce aerial photography that can be turned into a 3D model or mapped digitally. Now, it is possible to do the same work with a drone.

[Terrestrial(Close-range) photogrammetry](https://www.autodesk.com/solutions/photogrammetry-software) is when images are captured using a handheld camera or with a camera mounted to a tripod. The output of this method is not to create topographic maps, but rather to make 3D models of a smaller object.

[Top Photogrammetry Courses Online | Udemy](https://www.udemy.com/topic/photogrammetry/)

[Photogrammetry With Drones: In Mapping Technology | Udemy](https://www.udemy.com/course/essentials-of-photogrammetry/)

[Introduction to Photogrammetry Course | Coursera](https://www.coursera.org/lecture/aerial-photography-with-uav/introduction-to-photogrammetry-KyP30)

[Photogrammetry Online Classes and Training | Linkedin Learning](https://www.linkedin.com/learning/search?keywords=Photogrammetry&upsellOrderOrigin=default_guest_learning&trk=learning-course_learning-search-bar_search-submit)

[Pix4D training and certification for mapping professionals](https://training.pix4d.com/)

[Drone mapping and photogrammetry workshops with Pix4D](https://training.pix4d.com/pages/workshops)

[Digital Photogrammetric Systems Course | Purdue Online Learning](https://engineering.purdue.edu/online/courses/digital-photogrammetric-systems)

[Photogrammetry Training | Deep3D Photogrammetry](https://deep3d.co.uk/photogrammetry-training/)

[ASPRS Certification Program](https://www.asprs.org/certification)

## Photogrammetry Tools, Libraries, and Frameworks

[Autodesk® ReCap™](https://www.autodesk.com/products/recap/free-trial) is a software tool that converts reality captured from laser scans or photos into a 3D model or 2D drawing that's ready to be used in your design built for UAV and drone processes.

[Autodesk® ReCap™ Photo](http://blogs.autodesk.com/recap/introducing-recap-photo/) is a cloud-connected solution tailored for drone/UAV photo capturing workflows. Using ReCap Photo, you can create textured meshes, point clouds with geolocation, and high-resolution orthographic views with elevation maps.

[Pix4D](https://www.pix4d.com/) is a unique suite of photogrammetry software for drone mapping. Capture images with our app, process on desktop or cloud and create maps and 3D models.

[PIX4Dmapper](https://www.pix4d.com/product/pix4dmapper-photogrammetry-software) is the leading photogrammetry software for professional drone mapping.

[RealityCapture](https://www.capturingreality.com/) is a state-of-the-art photogrammetry software solution that creates virtual reality scenes, textured 3D meshes, orthographic projections, geo-referenced maps and much more from images and/or laser scans completely automatically.

[Adobe Scantastic](https://labs.adobe.com/projects/scantastic/) is a tool that makes the creation of 3D assets accessible to everyone. It can be used with just a mobile device (combined with Adobe's server-based photogrammetry pipeline), users can easily scan objects in their physical environment and turn them into 3D models which can then be imported into tools like [Adobe Dimension](https://www.adobe.com/products/dimension.html)  and [Adobe Aero](https://www.adobe.com/products/aero.html).

[Adobe Aero](https://www.adobe.com/products/aero.html) is a tool that helps you build, view, and share immersive AR experiences. Simply build a scene by bringing in 2D images from Adobe Photoshop and Illustrator, or 3D models from Adobe Dimension, Substance, third-party apps like Cinema 4D, or asset libraries like Adobe Stock and TurboSquid. Aero optimizes a wide array of assets, including OBJ, GLB, and glTF files, for AR, so you can visualize them in real time.

[Agisoft Metashape](https://www.agisoft.com/) is a stand-alone software product that performs photogrammetric processing of digital images and generates 3D spatial data to be used in GIS applications, cultural heritage documentation, and visual effects production as well as for indirect measurements of objects of various scales.

[MicroStation](https://www.bentley.com/en/products/brands/microstation) is a CAD software platform for 2D and 3D dimensional design and drafting, developed and sold by Bentley Systems. It generates 2D/3D vector graphics objects and elements and includes building information modeling (BIM) features.

[Leica Photogrammetry Suite (LPS)](https://support.hexagonsafetyinfrastructure.com/infocenter/index?page=product&facRef=LPS&facDisp=Leica%20Photogrammetry%20Suite%20(LPS)&landing=1) is a powerful photogrammetry system that delivers full analytical triangulation, the generation of digital terrain models, orthophoto production, mosaicking, and 3D feature extraction in a user-friendly environment that guarantees results even for photogrammetry novices.

[Terramodel](https://heavyindustry.trimble.com/products/terramodel) is a powerful software package for the surveyor, civil engineer or contractor who requires a CAD and design package with integrated support for raw survey data.

[MicMac](https://github.com/micmacIGN/micmac) is a free and  open-source photogrammetry software tools for 3D reconstruction.

[3DF Zephyr] (https://www.3dflow.net/3df-zephyr-photogrammetry-software/) is a photogrammetry software solution by 3Dflow. It allows you automatically reconstruct 3D models from photos and deal with any 3D reconstruction and scanning challenge. No matter what camera sensor, drone or laser scanner device you are going to use.

[COLMAP](https://colmap.github.io/) is a general-purpose Structure-from-Motion (SfM) and Multi-View Stereo (MVS) pipeline with a graphical and command-line interface. It offers a wide range of features for reconstruction of ordered and unordered image collections.

[Multi-View Environment (MVE)](https://www.gcc.tu-darmstadt.de/home/proj/mve/) is an effort to ease the work with multi-view datasets and to support the development of algorithms based on multiple views. It features Structure from Motion, Multi-View Stereo and Surface Reconstruction. MVE is developed at the TU Darmstadt.

[AliceVision](https://github.com/alicevision/AliceVision) is a Photogrammetric Computer Vision Framework which provides 3D Reconstruction and Camera Tracking algorithms. AliceVision comes up with strong software basis and state-of-the-art computer vision algorithms that can be tested, analyzed and reused.

[Meshroom](https://github.com/alicevision/meshroom) is a free, open-source 3D Reconstruction Software based on the AliceVision framework.

[PhotoModeler](https://www.photomodeler.com/) is a software extracts Measurements and Models from photographs taken with an ordinary camera. A cost-effective way for accurate 2D or 3D measurement, photo-digitizing, surveying, 3D scanning, and reality capture.

[ODM](https://www.opendronemap.org/odm/) is an open source command line toolkit to generate maps, point clouds, 3D models and DEMs from drone, balloon or kite images.

[WebODM](https://www.opendronemap.org/webodm/) is a user-friendly, commercial grade software for drone image processing. Generate georeferenced maps, point clouds, elevation models and textured 3D models from aerial images. It supports multiple engines for processing, currently [ODM](https://github.com/OpenDroneMap/ODM) and [MicMac](https://github.com/dronemapper-io/NodeMICMAC/).

[NodeODM](https://www.opendronemap.org/nodeodm/) is a [standard API specification](https://github.com/OpenDroneMap/NodeODM/blob/master/docs/index.adoc) for processing aerial images with engines such as [ODM](https://github.com/OpenDroneMap/ODM). The API is used by clients such as [WebODM](https://github.com/OpenDroneMap/WebODM), [CloudODM](https://github.com/OpenDroneMap/CloudODM) and [PyODM](https://github.com/OpenDroneMap/PyODM).

[ClusterODM]https://www.opendronemap.org/clusterodm/) is a reverse proxy, load balancer and task tracker with optional cloud autoscaling capabilities for NodeODM API compatible nodes. In a nutshell, it's a program to link together multiple NodeODM API compatible nodes under a single network address.

[FIELDimageR](https://www.opendronemap.org/fieldimager/) is an R package to analyze orthomosaic images from agricultural field trials.

[Regard3D](https://www.regard3d.org/) is a free and open source structure-from-motion program. It converts photos of an object, taken from different angles, into a 3D model of this object.

# LiDAR Development
[Back to the Top](https://github.com/mikeroyal/ISP-Guide#table-of-contents)

<p align="center">
 <img src="https://user-images.githubusercontent.com/45159366/121950812-f5ae2900-cd0e-11eb-8989-9188bd18a68c.png">
  <br />
</p>

## LiDAR Learning Resources
[Back to the Top](https://github.com/mikeroyal/LiDAR-Guide#table-of-contents)

[Introduction to Lidar Course - NOAA](https://coast.noaa.gov/digitalcoast/training/intro-lidar.html)

[Lidar 101:An Introduction to Lidar Technology, Data, and Applications(PDF) - NOAA](https://coast.noaa.gov/data/digitalcoast/pdf/lidar-101.pdf)

[Understanding LiDAR Technologies - GIS Lounge](https://www.gislounge.com/understanding-lidar-technologies/)

[LiDAR University Free Lidar Training Courses on MODUS AI](https://www.modus-ai.com/lidar-university-2/)

[LiDAR | Learning Plan on ERSI](https://www.esri.com/training/catalog/5bccd52a6e9c0f01fb49e85d/lidar/#!)

[Light Detection and Ranging Sensors Course on Coursera](https://www.coursera.org/lecture/state-estimation-localization-self-driving-cars/lesson-1-light-detection-and-ranging-sensors-3NXgp)

[Quick Introduction to Lidar and Basic Lidar Tools(PDF)](https://training.fws.gov/courses/references/tutorials/geospatial/CSP7304/documents/Lidar.pdf)

[LIDAR - GIS Wiki](http://wiki.gis.com/wiki/index.php/Lidar)

[OpenStreetMap Wiki](https://wiki.openstreetmap.org/wiki/Main_Page)

[OpenStreetMap Frameworks](https://wiki.openstreetmap.org/wiki/Frameworks)

## LiDAR Tools & Frameworks

[Light Detection and Ranging (lidar)](https://www.usgs.gov/news/earthword-lidar) is a technology used to create high-resolution models of ground elevation with a vertical accuracy of 10 centimeters (4 inches). Lidar equipment, which includes a laser scanner, a Global Positioning System (GPS), and an Inertial Navigation System (INS), is typically mounted on a small aircraft. The laser scanner transmits brief pulses of light to the ground surface. Those pulses are reflected or scattered back and their travel time is used to calculate the distance between the laser scanner and the ground.  Lidar data is initially collected as a “point cloud” of individual points reflected from everything on the surface, including structures and vegetation. To produce a “bare earth” Digital Elevation Model (DEM), structures and vegetation are stripped away.

 <p align="center">
 <img src="https://user-images.githubusercontent.com/45159366/121950840-fe9efa80-cd0e-11eb-9a12-57c4799d63b5.png">
  <br />
</p>

**3D Data Visualization of Golden Gate Bridge. Source: [USGS](https://www.usgs.gov/core-science-systems/ngp/tnm-delivery)**

[Mola](https://docs.mola-slam.org/latest/) is a Modular Optimization framework for Localization and mApping (MOLA).

 <p align="center">
 <img src="https://user-images.githubusercontent.com/45159366/121950850-01015480-cd0f-11eb-9fa6-1f93d6d87cd1.gif">
  <br />
</p>

**3D LiDAR SLAM from KITTI dataset. Source: [MOLA](https://docs.mola-slam.org/latest/demo-kitti-lidar-slam.html)**

[Lidar Toolbox™](https://www.mathworks.com/products/lidar.html) is a MATLAB tool that provides algorithms, functions, and apps for designing, analyzing, and testing lidar processing systems. You can perform object detection and tracking, semantic segmentation, shape fitting, lidar registration, and obstacle detection. Lidar Toolbox supports lidar-camera cross calibration for workflows that combine computer vision and lidar processing.

[Automated Driving Toolbox™](https://www.mathworks.com/products/automated-driving.html) is a MATLAB tool that provides algorithms and tools for designing, simulating, and testing ADAS and autonomous driving systems. You can design and test vision and lidar perception systems, as well as sensor fusion, path planning, and vehicle controllers. Visualization tools include a bird’s-eye-view plot and scope for sensor coverage, detections and tracks, and displays for video, lidar, and maps. The toolbox lets you import and work with HERE HD Live Map data and OpenDRIVE® road networks. It also provides reference application examples for common ADAS and automated driving features, including FCW, AEB, ACC, LKA, and parking valet. The toolbox supports C/C++ code generation for rapid prototyping and HIL testing, with support for sensor fusion, tracking, path planning, and vehicle controller algorithms.

[Microsoft AirSim](https://microsoft.github.io/AirSim/lidar.html) is a simulator for drones, cars and more, built on Unreal Engine (with an experimental Unity release). AirSim is open-source, cross platform, and supports [software-in-the-loop simulation](https://www.mathworks.com/help///ecoder/software-in-the-loop-sil-simulation.html) with popular flight controllers such as PX4 & ArduPilot and [hardware-in-loop](https://www.ni.com/en-us/innovations/white-papers/17/what-is-hardware-in-the-loop-.html) with PX4 for physically and visually realistic simulations. It is developed as an Unreal plugin that can simply be dropped into any Unreal environment. AirSim is being developed  as a platform for AI research to experiment with deep learning, computer vision and reinforcement learning algorithms for autonomous vehicles.

<p align="center">
 <img src="https://user-images.githubusercontent.com/45159366/121950853-02328180-cd0f-11eb-9459-1b31d084bd3f.png">
  <br />
</p>

**3D Autonomous Vehicle Simulation in AirSim. Source: [Microsoft](https://microsoft.github.io/AirSim)**

[LASer(LAS)](https://www.asprs.org/divisions-committees/lidar-division/laser-las-file-format-exchange-activities) is a public file format for the interchange of 3-dimensional point cloud data data between data users. Although developed primarily for exchange of lidar point cloud data, this format supports the exchange of any 3-dimensional x,y,z tuplet. This binary file format is an alternative to proprietary systems or a generic ASCII file interchange system used by many companies. The problem with proprietary systems is obvious in that data cannot be easily taken from one system to another. There are two major problems with the ASCII file interchange. The first problem is performance because the reading and interpretation of ASCII elevation data can be very slow and the file size can be extremely large even for small amounts of data. The second problem is that all information specific to the lidar data is lost. The LAS file format is a binary file format that maintains information specific to the lidar nature of the data while not being overly complex.

[3D point cloud](https://www.onyxscan-lidar.com/point-cloud/) is a set of data points defined in a given three-dimensional coordinates system.. Point clouds can be produced directly by 3D scanner which records a large number of points returned from the external surfaces of objects or earth surface. These data are exchanged between LiDAR users mainly through LAS format files (.las).

[ArcGIS Desktop](https://www.esri.com/en-us/arcgis/products/arcgis-desktop/overview) is powerful and cost-effective desktop geographic information system (GIS) software. It is the essential software package for GIS professionals. ArcGIS Desktop users can create, analyze, manage, and share geographic information so decision-makers can make intelligent, informed decisions.

[USGS 3DEP Lidar Point Cloud Now Available as Amazon Public Dataset](https://www.usgs.gov/news/usgs-3dep-lidar-point-cloud-now-available-amazon-public-dataset)

[National Geospatial Program](https://www.usgs.gov/core-science-systems/national-geospatial-program)

[National Map Data Download and Visualization Services](https://www.usgs.gov/core-science-systems/ngp/tnm-delivery)

[USGS Lidar Base Specification(LBS) online edition](https://www.usgs.gov/core-science-systems/ngp/ss/lidar-base-specification-online)

# Bioinformatics
[Back to the Top](https://github.com/mikeroyal/ISP-Guide#table-of-contents)

<p align="center">
 <img src="https://user-images.githubusercontent.com/45159366/126912438-49cc660e-90c5-4cbc-828b-10e807b99767.png">
  <br />
</p>

## Bioinformatics Learning Resources

[Bioinformatics](https://www.genome.gov/genetics-glossary/Bioinformatics) is a field of computational science that has to do with the analysis of sequences of biological molecules. This usually refers to genes, DNA, RNA, or protein, and is particularly useful in comparing genes and other sequences in proteins and other sequences within an organism or between organisms, looking at evolutionary relationships between organisms, and using the patterns that exist across DNA and protein sequences to figure out what their function is.

[European Bioinformatics Institute](https://www.ebi.ac.uk/)

[National Center for Biotechnology Information](https://www.ncbi.nlm.nih.gov)

[Online Courses in Bioinformatics |ISCB - International Society for Computational Biology](https://www.iscb.org/cms_addon/online_courses/index.php)

[Bioinformatics | Coursera](https://www.coursera.org/specializations/bioinformatics)

[Top Bioinformatics Courses | Udemy](https://www.udemy.com/topic/Bioinformatics/)

[Biometrics Courses | Udemy](https://www.udemy.com/course/biometrics/)

[Learn Bioinformatics with Online Courses and Lessons | edX](https://www.edx.org/learn/bioinformatics)

[Bioinformatics Graduate Certificate | Harvard Extension School](https://extension.harvard.edu/academics/programs/bioinformatics-graduate-certificate/)

[Bioinformatics and Biostatistics | UC San Diego Extension](https://extension.ucsd.edu/courses-and-programs/bioinformatics-and-biostatistics)

[Bioinformatics and Proteomics - Free Online Course Materials | MIT](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-092-bioinformatics-and-proteomics-january-iap-2005/)

[Introduction to Biometrics course - Biometrics Institute](https://www.biometricsinstitute.org/event/introduction-to-biometrics-short-course/)

## Bioinformatics Tools, Libraries, and Frameworks

[Bioconductor](https://bioconductor.org/) is an open source project that provides tools for the analysis and comprehension of high-throughput genomic data. Bioconductor uses the [R statistical programming language](https://www.r-project.org/about.html), and is open source and open development. It has two releases each year, and an active user community. Bioconductor is also available as an [AMI (Amazon Machine Image)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html) and [Docker images](https://docs.docker.com/engine/reference/commandline/images/).

[Bioconda](https://bioconda.github.io) is a channel for the conda package manager specializing in bioinformatics software. It has a repository of packages containing over 7000 bioinformatics packages ready to use with conda install.

[UniProt](https://www.uniprot.org/) is a freely accessible database that provide users with a comprehensive, high-quality and freely accessible set of protein sequences annotated with functional information.

[Bowtie 2](https://bio.tools/bowtie2#!) is an ultrafast and memory-efficient tool for aligning sequencing reads to long reference sequences. It is particularly good at aligning reads of about 50 up to 100s or 1,000s of characters, and particularly good at aligning to relatively long (mammalian) genomes.

[Biopython](https://biopython.org/) is a set of freely available tools for biological computation written in Python by an international team of developers. It is a distributed collaborative effort to develop Python libraries and applications which address the needs of current and future work in bioinformatics.

[BioRuby](https://bioruby.open-bio.org/) is a toolkit that has components for sequence analysis, pathway analysis, protein modelling and phylogenetic analysis; it supports many widely used data formats and provides easy access to databases, external programs and public web services, including BLAST, KEGG, GenBank, MEDLINE and GO.

[BioJava](https://biojava.org/) is a toolkit that provides an API to maintain local installations of the PDB, load and manipulate structures, perform standard analysis such as sequence and structure alignments and visualize them in 3D.

[BioPHP](https://biophp.org/) is an open source project that provides a collection of open source PHP code, with classes for DNA and protein sequence analysis, alignment, database parsing, and other bioinformatics tools.

[Avogadro](https://avogadro.cc/) is an advanced molecule editor and visualizer designed for cross-platform use in computational chemistry, molecular modeling, bioinformatics, materials science, and related areas. It offers flexible high quality rendering and a powerful plugin architecture.

[Ascalaph Designer](https://www.biomolecular-modeling.com/Ascalaph/Ascalaph_Designer.html) is a program for molecular dynamic simulations. Under a single graphical environment are represented as their own implementation of molecular dynamics as well as the methods of classical and quantum mechanics of popular programs.

[Anduril](https://www.anduril.org/site/) is a workflow platform for analyzing large data sets. Anduril provides facilities for analyzing high-thoughput data in biomedical research, and the platform is fully extensible by third parties. Ready-made tools support data visualization, DNA/RNA/ChIP-sequencing, DNA/RNA microarrays, cytometry and image analysis.

[Galaxy](https://melbournebioinformatics.github.io/MelBioInf_docs/tutorials/galaxy_101/galaxy_101/) is an open source, web-based platform for accessible, reproducible, and transparent computational biomedical research. It allows users without programming experience to easily specify parameters and run individual tools as well as larger workflows. It also captures run information so that any user can repeat and understand a complete computational analysis.

[PathVisio](https://pathvisio.github.io/) is a free open-source pathway analysis and drawing software which allows drawing, editing, and analyzing biological pathways. It is developed in Java and can be extended with plugins.

[Orange](https://orangedatamining.com/) is a powerful data mining and machine learning toolkit that performs data analysis and visualization.

[Basic Local Alignment Search Tool](https://blast.ncbi.nlm.nih.gov/Blast.cgi) is a tool that finds regions of similarity between biological sequences. The program compares nucleotide or protein sequences to sequence databases and calculates the statistical significance.

[OSIRIS](https://www.ncbi.nlm.nih.gov/osiris/) is public-domain, free, and open source STR analysis software designed for clinical, forensic, and research use, and has been validated for use as an expert system for single-source samples.

[NCBI BioSystems](https://www.ncbi.nlm.nih.gov/biosystems/) is a  Database that provides integrated access to biological systems and their component genes, proteins, and small molecules, as well as literature describing those biosystems and other related data throughout Entrez.

# AR/VR Development
[Back to the Top](https://github.com/mikeroyal/ISP-Guide#table-of-contents)

<p align="center">
 <img src="https://user-images.githubusercontent.com/45159366/130368380-37b7c0cd-ed71-4a52-8b16-4ac802e059d4.png">
  <br />
</p>

## Augmented Reality (AR) & Virtual Reality (VR) Learning Resources

[Augmented Reality (AR)](https://en.wikipedia.org/wiki/Augmented_reality) is an interactive experience of a real-world environment where the objects that reside in the real world are enhanced by computer-generated perceptual information.

[Virtual Reality (VR)](https://en.wikipedia.org/wiki/Virtual_reality) is a simulated experience that can be similar to or completely different from the real world. The applications of virtual reality include entertainment (video games), education (medical or military training) and business (virtual meetings).

[Mixed Reality (MR)](https://en.wikipedia.org/wiki/Mixed_reality) is the merging of real and virtual worlds to produce new environments and visualizations, where physical and digital objects co-exist and interact in real time.

[Extended Reality (XR)](https://en.wikipedia.org/wiki/Extended_reality) is a concept referring to all real-and-virtual combined environments and human-machine interactions generated by computer technology and wearables. Including augmented reality (AR), mixed reality (MR) and virtual reality (VR).

[Virtual Reality - Experiences and Devices](https://www.microsoft.com/en-us/mixed-reality/windows-mixed-reality)

[Oculus | VR Headsets, Games & Equipment](https://www.oculus.com/)

[Virtual Reality on Steam](https://store.steampowered.com/vr/)

[Valve Index® VR Headset](https://store.steampowered.com/valveindex)

[PlayStation VR](https://www.playstation.com/explore/playstation-vr/)

[HTC Vive VR Headset](https://www.vive.com/us/)

[Augmented Reality applications - Apple](https://www.apple.com/augmented-reality/)

[Unity Learn Training Program](https://learn.unity.com)

[Unity Manual: XR](https://docs.unity3d.com/Manual/XR.html)

[Intro to XR: VR, AR, and MR Foundations - Unity Learn](https://learn.unity.com/course/introduction-to-xr-vr-ar-and-mr-foundations)

[Unity XR: Build VR and AR Apps](https://unity3d.com/learn/unity-xr-apps)

[Top Virtual Reality Courses Online | Udemy](https://www.udemy.com/topic/virtual-reality/)

[Top Augmented Reality Courses Online | Udemy](https://www.udemy.com/topic/augmented-reality/)

[Google AR & VR Online Courses | Coursera](https://www.coursera.org/googlearvr)

[Top Augmented Reality Courses | Coursera](https://www.coursera.org/courses?query=augmented%20reality)

[Learn Augmented Reality with Online Courses and Lessons | edX](https://www.edx.org/learn/augmented-reality)

## Augmented Reality (AR) & Virtual Reality (VR) Tools and Frameworks

[ARKit](https://developer.apple.com/augmented-reality/arkit/) is a set set of software development tools to enable developers to build augmented-reality apps for iOS developed by Apple. The latest version ARKit 3.5 takes advantage of the new LiDAR Scanner and depth sensing system on iPad Pro(2020) to support a new generation of AR apps that use Scene Geometry for enhanced scene understanding and object occlusion.

[RealityKit](https://developer.apple.com/documentation/realitykit) is a framework to implement high-performance 3D simulation and rendering with information provided by the ARKit framework to seamlessly integrate virtual objects into the real world.

[SceneKit](https://developer.apple.com/scenekit/) is a high-level 3D graphics framework that helps you create 3D animated scenes and effects in your iOS apps.

[GPUImage framework](https://github.com/BradLarson/GPUImage) is a BSD-licensed iOS library that lets you apply GPU-accelerated filters and other effects to images, live camera video, and movies. In comparison to Core Image (part of iOS 5.0), GPUImage allows you to write your own custom filters, supports deployment to iOS 4.0, and has a simpler interface. However, it currently lacks some of the more advanced features of Core Image, such as facial detection.

[GPUImage3](https://github.com/BradLarson/GPUImage3) is the third generation of the [GPUImage framework](https://github.com/BradLarson/GPUImage), an open source project for performing GPU-accelerated image and video processing on Mac and iOS. The original GPUImage framework was written in Objective-C and targeted Mac and iOS, the second iteration rewritten in Swift using OpenGL to target Mac, iOS, and Linux, and now this third generation is redesigned to use [Apple's Metal](https://developer.apple.com/metal/) in place of OpenGL.

[ARCore](https://developers.google.com/ar/) is a software development kit developed by Google that allows for augmented reality applications in the real world. These tools include environmental understanding, which allows devices to detect horizontal and vertical surfaces and planes. It also includes motion tracking, which lets phones understand and track their positions relative to the world. Also ARCore’s Light Estimation API lets your digital objects appear realistically as if they’re actually part of the physical world.

[Adobe Aero](https://www.adobe.com/products/aero.html) is a powerful new [augmented reality (AR)](https://en.wikipedia.org/wiki/Augmented_reality) authoring tool that makes it easier for designers to create immersive content.

[Vuforia](https://developer.vuforia.com/) is a comprehensive, scalable enterprise AR platform. Our wide-ranging solution suite ensures that we can provide the right AR technology to every customer based on their business needs.

[Vuforia Studio](https://www.ptc.com/en/products/vuforia/vuforia-studio) is a tool that allows anyone to create beautiful 3D augmented reality (AR) experiences in a matter of minutes with no coding required.

[OpenVX™](https://www.khronos.org/openvx/) is an open-source, royalty-free standard for cross platform acceleration of computer vision applications. OpenVX enables performance and power-optimized computer vision processing, especially important in embedded and real-time use cases such as face, body and gesture tracking, smart video surveillance, advanced driver assistance systems (ADAS), object and scene reconstruction, augmented reality, visual inspection, robotics and more.

[NVIDIA Flex](https://github.com/NVIDIAGameWorks/FleX) is a particle-based simulation library designed for real-time applications.

[ARToolKit](https://artoolkit.org) is a fast and modern open source tracking and recognition SDK which enables computers to see and understand more in the environment around them. It's built from the ground up using modern computer vision techniques.

[ARmedia](https://www.inglobetechnologies.com/ar-media/) is a plugin tool that makes it easy to develop and create AR experiences without coding.

[Kundan](https://www.kudan.io/) is a tool that provides proprietary Artificial Perception technologies based on SLAM to enable use cases with significant market potential and impact on our lives such as autonomous driving, robotics, AR/VR and smart cities.

[OVR Toolkit](https://store.steampowered.com/app/1068820/OVR_Toolkit/) is a utility application designed to make viewing the desktop in VR simple and fast, it allows for viewing the desktop within VR, placing desktop windows around the world, mouse input, typing with a virtual keyboard, and quickly switching between windows.

<p align="center">
<img src="https://user-images.githubusercontent.com/45159366/117720758-e843d300-b193-11eb-9796-bde15aebed71.png">
<br />
</p>

Microsoft HoloLens Headset. Source: [Microsoft](https://www.microsoft.com/en-us/hololens/buy)

<p align="center">
<img src="https://user-images.githubusercontent.com/45159366/117720763-e9750000-b193-11eb-888a-e4bccd6c30eb.png">
<br />
</p>

PlayStation VR Headset. Source: [PlayStation](https://www.playstation.com/en-us/ps-vr/)

[SteamVR](https://store.steampowered.com/steamvr) is the ultimate tool for experiencing VR content on the hardware of your choice. SteamVR supports the Valve Index, HTC Vive, Oculus Rift, Windows Mixed Reality headsets, and others.

<p align="center">
<img src="https://user-images.githubusercontent.com/45159366/110881514-543db400-8295-11eb-9543-fd5d385ddb05.png">
<br />

SteamVR Home
</p>

<p align="center">
<img src="https://user-images.githubusercontent.com/45159366/117720776-ed088700-b193-11eb-8538-9831999b5104.png">
<br />
</p>
Valve Index VR Headset. Source: [Steam](https://store.steampowered.com/valveindex)


[OpenVR](https://github.com/ValveSoftware/openvr) is an API and runtime that allows access to VR hardware(Steam Index, HTC Vive, and Oculus Rift) from multiple vendors without requiring that applications have specific knowledge of the hardware they are targeting.

[OpenVR Benchmark on Steam](https://store.steampowered.com/app/955610/OpenVR_Benchmark/) is the first benchmark tool for reproducibly testing your real VR performance, rendering inside of your VR headset.

[OpenHMD](http://www.openhmd.net/) is open source API and drivers that supports a wide range of HMD(head-mounted display) devices such as Oculus Rift, HTC Vive, Sony PSVR, and others.

[openXR](https://www.khronos.org/OpenXR/) is a free, open standard that provides high-performance access to Augmented Reality (AR) and Virtual Reality (VR) collectively known as XR—platforms and devices.

[Monado](https://monado.dev/) is the first OpenXR™ runtime for GNU/Linux. Monado aims to jump-start development of an open source XR ecosystem and provide the fundamental building blocks for device vendors to target the GNU/Linux platform.

[Libsurvive](https://github.com/cntools/libsurvive) is a set of tools and libraries that enable 6 dof tracking on lighthouse and vive based systems that is completely open source and can run on any device. It currently supports both SteamVR 1.0 and SteamVR 2.0 generation of devices and should support any tracked object commercially available.

[Simula](https://github.com/SimulaVR/Simula) is a VR window manager for Linux that runs on top of Godot. It takes less than 1 minute to install. Simula is officially compatible with SteamVR headsets equipped with Linux drivers (e.g. HTC Vive, HTC Vive Pro, & Valve Index). We have also added experimental support to OpenXR headsets that have Monado drivers (e.g. North Star, OSVR HDK, and PSVR). Some people have gotten the Oculus Rift S to run Simula via OpenHMD ([see here](https://github.com/OpenHMD/OpenHMD/issues/225#issuecomment-638454156)).

# Game Development
[Back to the Top](https://github.com/mikeroyal/ISP-Guide#table-of-contents)

<p align="center">
 <img src="https://user-images.githubusercontent.com/45159366/97361059-45151700-185c-11eb-9d12-dae51c79eb8a.png">
  <br />
</p>

<p align="center">
 <img src="https://user-images.githubusercontent.com/45159366/119279021-ea6b5000-bbdd-11eb-9f59-5251fc3ac751.png">
  <br />
</p>

## Game Engines

**[Checkout the Unity Engine](https://unity.com/)**

<img src="https://user-images.githubusercontent.com/45159366/104788113-3432be00-5746-11eb-99b1-49360669f327.png">


**[Checkout the Unreal Engine 4](https://www.unrealengine.com/)**

<img src="https://user-images.githubusercontent.com/45159366/104788122-37c64500-5746-11eb-8f61-48a69b94582d.png">


**[Checkout the CryEngine](https://www.cryengine.com/)**

<img src="https://user-images.githubusercontent.com/45159366/104788177-680de380-5746-11eb-9fc2-6d6f0bdc0a82.png">


**[Checkout the Godot Engine](https://godotengine.org/)**

[If you would like to Donate to the Godot Project](https://www.patreon.com/godotengine)

<img src="https://user-images.githubusercontent.com/45159366/104788134-3f85e980-5746-11eb-94c4-d97165ee888b.jpeg">


**[Checkout Blender](https://www.blender.org/)**

[If you would like to Donate to the Blender Project](https://fund.blender.org/)

<img src="https://user-images.githubusercontent.com/45159366/104788139-401e8000-5746-11eb-9647-058dee01a00e.png">


**[Checkout AWS Lumberyard(based on CryEngine)](https://aws.amazon.com/lumberyard/)**

<img src="https://user-images.githubusercontent.com/45159366/104788145-43b20700-5746-11eb-82f1-1351c3b7e380.png">


**[Checkout Game Maker Studio 2](https://www.yoyogames.com/gamemaker)**

<img src="https://user-images.githubusercontent.com/45159366/104788147-44e33400-5746-11eb-879a-bc6239c98ce4.jpg">


## Game Development Learning Resources

[Unreal Online Learning](https://www.unrealengine.com/en-US/onlinelearning-courses) is a free learning platform that offers hands-on video courses and guided learning paths.

[Unreal Engine Authorized Training Program](https://www.unrealengine.com/en-US/training-partners)

[Unreal Engine for education](https://www.unrealengine.com/en-US/education/)

[Unreal Engine Training & Simulation](https://www.unrealengine.com/en-US/industry/training-simulation)

[Unity Certifications](https://unity.com/products/unity-certifications)

[Autodesk for Games](https://www.autodesk.com/campaigns/autodesk-for-games)

[Getting Started with DirectX 12 Ultimate](https://devblogs.microsoft.com/directx/directx-12-ultimate-getting-started-guide/)

[Getting Started with Vulkan](https://www.khronos.org/vulkan/)

[Getting Started with Apple Metal](https://developer.apple.com/metal/)

[Game Design Online Courses from Udemy](https://www.udemy.com/courses/Design/Game-Design/)

[Game Design Online Courses from Skillshare](https://www.skillshare.com/browse/game-design)

[Learn Game Design with Online Courses and Classes from edX](https://www.edx.org/learn/game-design)

[Game Design Courses from Coursera](https://www.coursera.org/courses?query=game%20design)

[Game Design and Development Specialization Course from Coursera](https://www.coursera.org/specializations/game-development)

## Game Development Tools

[Unreal Engine](https://www.unrealengine.com) is a game engine developed by Epic Games with the world's most open and advanced real-time 3D creation tool. Continuously evolving to serve not only its original purpose as a state-of-the-art game engine, today it gives creators across industries the freedom and control to deliver cutting-edge content, interactive experiences, and immersive virtual worlds.

[Unity](https://unity.com) is a cross-platform game development platform. Use Unity to build high-quality 3D and 2D games, deploy them across mobile, desktop, VR/AR, consoles or the Web, and connect with loyal and enthusiastic players and customers.

[Unigine](https://unigine.com) is a cross-platform game engine designed for development teams (C++/C# programmers, 3D artists) working on interactive 3D apps.

[Frostbite](https://www.ea.com/frostbite/engine) is a game engine developed by [DICE](https://www.dice.se/), designed for cross-platform use on Microsoft Windows and game consoles such as PlayStation 3 Xbox 360,  PlayStation 4, Xbox One, Nintendo Switch, PlayStation 5, and Xbox Series X/S.

[Panda3D](https://www.panda3d.org/) is a game engine, a framework for 3D rendering and game development for Python and C++ programs, developed by Disney and CMU. Panda3D is open-source and free for any purpose, including commercial ventures.

[Source 2](https://developer.valvesoftware.com/wiki/Source_2) is a 3D video game engine in development by Valve as a successor to Source. It is used in Dota 2, Artifact, Dota Underlords, parts of The Lab, SteamVR Home, and Half-Life: Alyx.

[Havok](https://www.havok.com/) is a middleware software suite that provides a realistic physics engine component and related functions to video games. It is supported  and optimized across all major platforms, including Nintendo Switch, PlayStation®, Stadia, and Xbox. Along with integrations for Unity and Unreal Engine and are used in countless proprietary game engines.

[AutoDesk 3ds Max](https://www.autodesk.com/products/3ds-max/overview) is a professional software program for 3D modeling, animation, rendering, and visualization. 3ds Max allows you to create stunning game environments, design visualizations, and virtual reality experiences.

[Houdini](https://www.sidefx.com/) is a 3D procedural software for modeling, rigging, animation, VFX, look development, lighting and rendering in film, TV, advertising and video game pipelines.

[A-Frame](https://aframe.io) is a web framework for building virtual reality experiences in WebVR with HTML and Entity-Component. A-Frame works on Vive, Rift, desktop, mobile platforms.

[AppGameKit](https://www.appgamekit.com) is a powerful game development engine, ideal for Hobbyist and Indie developers. Where you can start coding in the easy to learn AppGameKit BASIC or use the libraries in C++ & XCode.

[Amazon Lumberyard](https://aws.amazon.com/lumberyard/) is an open source, AAA game engine(based on CryEngine) that gives you the tools you need to create high quality games. Deeply integrated with AWS and Twitch, Amazon Lumberyard includes full source code, allowing you to customize your project at any level.

[Blender](https://www.blender.org) is the free and open source 3D creation suite. It supports the entirety of the 3D pipeline—modeling, rigging, animation, simulation, rendering, compositing and motion tracking, video editing and 2D animation pipeline.

[CryEngine](https://www.cryengine.com) is a powerful real-time game development platform created by Crytek.

[GameMaker Studio 2](https://www.yoyogames.com/gamemaker) is the latest and greatest incarnation of GameMaker. It has everything you need to take your idea from concept to finished game. With no barriers to entry and powerful functionality, GameMaker Studio 2 is the ultimate 2D development environment.

[Godot](https://godotengine.org) is a feature-packed, cross-platform game engine to create 2D and 3D games from a unified interface. It provides a comprehensive set of common tools, so that users can focus on making games without having to reinvent the wheel. Games can be exported in one click to a number of platforms, including the major desktop platforms (Linux, Mac OSX, Windows) as well as mobile (Android, iOS) and web-based (HTML5) platforms.

[Open Graphics Library(OpenGL)](https://www.opengl.org/) is an API used acrossed mulitple  programming languages and platforms for hardware-accelerated rendering of 2D/3D vector graphics currently developed by the [Khronos Group](https://www.khronos.org/).

[Open Computing Language (OpenCL)](https://www.khronos.org/opencl/) is an open standard for [parallel programming](https://www.coursera.org/lecture/parprog1/introduction-to-parallel-computing-zNrIS) of heterogeneous platforms consisting of CPUs, GPUs, and other hardware accelerators found in supercomputers, cloud servers, personal computers, mobile devices and embedded platforms.

[OpenGL Shading Language(GLSL)](https://www.khronos.org/opengl/wiki/Core_Language_(GLSL)) is a High Level Shading Language based on the C-style language, so it covers most of the features a user would expect with such a language.  Such as control structures (for-loops, if-else statements, etc) exist in GLSL, including the switch statement.

[High Level Shading Language(HLSL)](https://docs.microsoft.com/en-us/windows/win32/direct3dhlsl/dx-graphics-hlsl) is the High Level Shading Language for DirectX. Using HLSL, the user can create C-like programmable shaders for the Direct3D pipeline. HLSL was first created with DirectX 9 to set up the programmable 3D pipeline.

[DirectX 12 Ultimate](https://github.com/Microsoft/DirectX-Graphics-Samples) is an API(for high performance 2D & 3D graphics) from Microsoft. DirectX 12 Ultimate brings support for ray tracing, mesh shaders, variable rate shading, and sampler feedback. Available in Windows 2004 version(May 2020 Update).

[Vulkan](https://www.khronos.org/vulkan/) is a modern cross-platform graphics and compute API that provides high-efficiency, cross-platform access to modern GPUs used in a wide variety of devices from PCs and consoles to mobile phones and embedded platforms. Vulkan is currently in development by the Khronos consortium.

[Metal](https://developer.apple.com/metal/) is a low-level GPU programming framework used for rendering 2D and 3D graphics on Apple platforms such as iOS, iPadOS, macOS, watchOS and tvOS.

[MoltenVK](https://moltengl.com/moltenvk) is an implementation of Vulkan running on iOS and macOS using Apple's [Metal](https://developer.apple.com/metal/) graphics framework.

[MoltenGL](https://moltengl.com) is an implementation of the OpenGL ES 2.0 API that runs on Apple's [Metal](https://developer.apple.com/metal/) graphics framework.

[Mesa 3D Graphics Library](https://docs.mesa3d.org/index.html) is a project began as an open-source implementation of the OpenGL specification. A system for rendering interactive 3D graphics. Mesa ties into several other open-source projects: the [Direct Rendering Infrastructure](https://dri.freedesktop.org/), [X.org](https://x.org/), and [Wayland](https://wayland.freedesktop.org/) to provide OpenGL support on Linux, FreeBSD, and other operating systems.

[OpenGL ES](https://www.khronos.org/opengles/) is the mobile subset of OpenGL. It's supported on all major mobile platforms, and is also the base for WebGL.

[OpenCL](https://www.khronos.org/opencl/) is a framework for writing programs that execute across heterogeneous platforms consisting of CPUs, GPUs, DSPs, FPGAs and other processors or hardware accelerators.

[EGL](https://www.khronos.org/egl/) is an interface between Khronos rendering APIs such as OpenGL or OpenVG and the underlying native platform window system.

[VDPAU](https://www.freedesktop.org/wiki/Software/VDPAU/) is the Video Decode and Presentation API for UNIX. It provides an interface to video decode acceleration and presentation hardware present in modern GPUs.

[VA API](https://freedesktop.org/wiki/Software/vaapi/) is an open-source library and API specification, which provides access to graphics hardware acceleration capabilities for video processing.

[XvMC](https://en.wikipedia.org/wiki/X-Video_Motion_Compensation) is an extension of the X video extension (Xv) for the X Window System. The XvMC API allows video programs to offload portions of the video decoding process to the GPU hardware.

[AMD Radeon ProRender](https://www.amd.com/en/technologies/radeon-prorender) is a powerful physically-based rendering engine that enables creative professionals to produce stunningly photorealistic images on virtually any GPU, any CPU, and any OS in over a dozen leading digital content creation and CAD applications.

[NVIDIA Omniverse](https://developer.nvidia.com/nvidia-omniverse-platform) is a powerful, multi-GPU, real-time simulation and collaboration platform for 3D production pipelines based on Pixar's Universal Scene Description and NVIDIA RTX.

[LibGDX](https://github.com/libgdx/libgdx) is a cross-platform Java game development framework based on OpenGL (ES) that works on Windows, Linux, Mac OS X, Android, your WebGL enabled browser and iOS.

[cocos2d-x](https://github.com/cocos2d/cocos2d-x) is a multi-platform framework for building 2d games, interactive books, demos and other graphical applications. It is based on cocos2d-iphone, but instead of using Objective-C, it uses C++. It works on iOS, Android, macOS, Windows and Linux.

[MonoGame](https://github.com/MonoGame/MonoGame) is a framework for creating powerful cross-platform games. The spiritual successor to XNA with thousands of titles shipped across desktop, mobile, and console platforms. MonoGame is a fully managed .NET open source game framework without any black boxes.

[Three.js](https://threejs.org) is a cross-browser JavaScript library and application programming interface used to create and display animated 3D computer graphics in a web browser using WebGL.

[Superpowers](http://superpowers-html5.com/) is a downloadable HTML5 app for real-time collaborative projects . You can use it solo like a regular offline game maker, or setup a password and let friends join in on your project through their Web browser.

[URHO3D](https://urho3d.github.io/) is a free lightweight, cross-platform 2D and 3D game engine implemented in C++ and released under the MIT license. Greatly inspired by OGRE and Horde3D.

[Vivox](https://www.vivox.com/) is a voice & text chat platform that's trusted by the world's biggest gaming brands and titles such as Fortnite, PUBG, League of Legends, and Rainbow Six Siege.

[HGIG](https://www.hgig.org/) is a volunteer group of companies from the game and TV display industries that meet to specify and make available for the public guidelines to improve consumer gaming experiences in HDR.

[GameBlocks](https://www.gameblocks.com/) is a Server Side Anti-Cheat & Middleware software.


# CUDA Development
[Back to the Top](https://github.com/mikeroyal/ISP-Guide#table-of-contents)

<p align="center">
 <img src="https://user-images.githubusercontent.com/45159366/94306481-e17b8f00-ff27-11ea-832f-c85374acb3b1.png">
  <br />
</p>


<p align="center">
 <img src="https://user-images.githubusercontent.com/45159366/117718735-55a23480-b191-11eb-874d-e690d09cd490.png">
  <br />
</p>

**CUDA Toolkit. Source: [NVIDIA Developer CUDA](https://developer.nvidia.com/cuda-zone)**

## CUDA Learning Resources

[CUDA](https://developer.nvidia.com/cuda-zone) is a parallel computing platform and programming model developed by NVIDIA for general computing on graphical processing units (GPUs). With CUDA, developers are able to dramatically speed up computing applications by harnessing the power of GPUs. In GPU-accelerated applications, the sequential part of the workload runs on the CPU, which is optimized for single-threaded. The compute intensive portion of the application runs on thousands of GPU cores in parallel. When using CUDA, developers can program in popular languages such as C, C++, Fortran, Python and MATLAB.

[CUDA Toolkit Documentation](https://docs.nvidia.com/cuda/index.html)

[CUDA Quick Start Guide](https://docs.nvidia.com/cuda/cuda-quick-start-guide/index.html)

[CUDA on WSL](https://docs.nvidia.com/cuda/wsl-user-guide/index.html)

[CUDA GPU support for TensorFlow](https://www.tensorflow.org/install/gpu)

[NVIDIA Deep Learning cuDNN Documentation](https://docs.nvidia.com/deeplearning/cudnn/api/index.html)

[NVIDIA GPU Cloud Documentation](https://docs.nvidia.com/ngc/ngc-introduction/index.html)

[NVIDIA NGC](https://ngc.nvidia.com/) is a hub for GPU-optimized software for deep learning, machine learning, and high-performance computing (HPC) workloads.

[NVIDIA NGC Containers](https://www.nvidia.com/en-us/gpu-cloud/containers/) is a registry that provides researchers, data scientists, and developers with simple access to a comprehensive catalog of GPU-accelerated software for AI, machine learning and HPC. These containers take full advantage of NVIDIA GPUs on-premises and in the cloud.

## CUDA Tools Libraries, and Frameworks

[CUDA Toolkit](https://developer.nvidia.com/cuda-downloads) is a collection of tools & libraries that provide a development environment for creating high performance GPU-accelerated applications. The CUDA Toolkit allows you can develop, optimize, and deploy your applications on GPU-accelerated embedded systems, desktop workstations, enterprise data centers, cloud-based platforms and HPC supercomputers. The toolkit includes GPU-accelerated libraries, debugging and optimization tools, a C/C++ compiler, and a runtime library to build and deploy your application on major architectures including x86, Arm and POWER.

[NVIDIA cuDNN](https://developer.nvidia.com/cudnn) is a GPU-accelerated library of primitives for [deep neural networks](https://developer.nvidia.com/deep-learning). cuDNN provides highly tuned implementations for standard routines such as forward and backward convolution, pooling, normalization, and activation layers. cuDNN accelerates widely used deep learning frameworks, including [Caffe2](https://caffe2.ai/), [Chainer](https://chainer.org/), [Keras](https://keras.io/), [MATLAB](https://www.mathworks.com/solutions/deep-learning.html), [MxNet](https://mxnet.incubator.apache.org/), [PyTorch](https://pytorch.org/), and [TensorFlow](https://www.tensorflow.org/).

[CUDA-X HPC](https://www.nvidia.com/en-us/technologies/cuda-x/) is a collection of libraries, tools, compilers and APIs that help developers solve the world's most challenging problems. CUDA-X HPC includes highly tuned kernels essential for high-performance computing (HPC).

[NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-docker) is a collection of tools & libraries that allows users to build and run GPU accelerated Docker containers. The toolkit includes a container runtime [library](https://github.com/NVIDIA/libnvidia-container) and utilities to automatically configure containers to leverage NVIDIA GPUs.

[Minkowski Engine](https://nvidia.github.io/MinkowskiEngine) is an auto-differentiation library for sparse tensors. It supports all standard neural network layers such as convolution, pooling, unpooling, and broadcasting operations for sparse tensors.

[CUTLASS](https://github.com/NVIDIA/cutlass) is a collection of CUDA C++ template abstractions for implementing high-performance matrix-multiplication (GEMM) at all levels and scales within CUDA. It incorporates strategies for hierarchical decomposition and data movement similar to those used to implement cuBLAS.

[CUB](https://github.com/NVIDIA/cub) is a cooperative primitives for CUDA C++ kernel authors.

[Tensorman](https://github.com/pop-os/tensorman) is a utility for easy management of Tensorflow containers by developed by [System76]( https://system76.com).Tensorman allows Tensorflow to operate in an isolated environment that is contained from the rest of the system. This virtual environment can operate independent of the base system, allowing you to use any version of Tensorflow on any version of a Linux distribution that supports the Docker runtime.

[Numba](https://github.com/numba/numba) is an open source, NumPy-aware optimizing compiler for Python sponsored by Anaconda, Inc. It uses the LLVM compiler project to generate machine code from Python syntax. Numba can compile a large subset of numerically-focused Python, including many NumPy functions. Additionally, Numba has support for automatic parallelization of loops, generation of GPU-accelerated code, and creation of ufuncs and C callbacks.

[Chainer](https://chainer.org/) is a Python-based deep learning framework aiming at flexibility. It provides automatic differentiation APIs based on the define-by-run approach (dynamic computational graphs) as well as object-oriented high-level APIs to build and train neural networks. It also supports CUDA/cuDNN using [CuPy](https://github.com/cupy/cupy) for high performance training and inference.

[CuPy](https://cupy.dev/) is an implementation of NumPy-compatible multi-dimensional array on CUDA. CuPy consists of the core multi-dimensional array class, cupy.ndarray, and many functions on it. It supports a subset of numpy.ndarray interface.

[CatBoost](https://catboost.ai/) is a fast, scalable, high performance [Gradient Boosting](https://en.wikipedia.org/wiki/Gradient_boosting) on Decision Trees library, used for ranking, classification, regression and other machine learning tasks for Python, R, Java, C++. Supports computation on CPU and GPU.

[cuDF](https://rapids.ai/) is a GPU DataFrame library for loading, joining, aggregating, filtering, and otherwise manipulating data. cuDF provides a pandas-like API that will be familiar to data engineers & data scientists, so they can use it to easily accelerate their workflows without going into the details of CUDA programming.

[cuML](https://github.com/rapidsai/cuml) is a suite of libraries that implement machine learning algorithms and mathematical primitives functions that share compatible APIs with other RAPIDS projects. cuML enables data scientists, researchers, and software engineers to run traditional tabular ML tasks on GPUs without going into the details of CUDA programming. In most cases, cuML's Python API matches the API from scikit-learn.

[ArrayFire](https://arrayfire.com/) is a general-purpose library that simplifies the process of developing software that targets parallel and massively-parallel architectures including CPUs, GPUs, and other hardware acceleration devices.

[Thrust](https://github.com/NVIDIA/thrust) is a C++ parallel programming library which resembles the C++ Standard Library. Thrust's high-level interface greatly enhances programmer productivity while enabling performance portability between GPUs and multicore CPUs.

[AresDB](https://eng.uber.com/aresdb/) is a GPU-powered real-time analytics storage and query engine. It features low query latency, high data freshness and highly efficient in-memory and on disk storage management.

[Arraymancer](https://mratsim.github.io/Arraymancer/) is a tensor (N-dimensional array) project in Nim. The main focus is providing a fast and ergonomic CPU, Cuda and OpenCL ndarray library on which to build a scientific computing ecosystem.

[Kintinuous](https://github.com/mp3guy/Kintinuous) is a real-time dense visual SLAM system capable of producing high quality globally consistent point and mesh reconstructions over hundreds of metres in real-time with only a low-cost commodity RGB-D sensor.

[GraphVite](https://graphvite.io/) is a general graph embedding engine, dedicated to high-speed and large-scale embedding learning in various applications.

# MATLAB Development
[Back to the Top](https://github.com/mikeroyal/ISP-Guide#table-of-contents)

<p align="center">
 <img src="https://user-images.githubusercontent.com/45159366/94306473-de809e80-ff27-11ea-924b-0a6947ae38bc.png">
  <br />
</p>

## MATLAB Learning Resources

[MATLAB](https://www.mathworks.com/products/matlab.html) is a programming language that does numerical computing such as expressing matrix and array mathematics directly.

[MATLAB Documentation](https://www.mathworks.com/help/matlab/)

[Getting Started with MATLAB ](https://www.mathworks.com/help/matlab/getting-started-with-matlab.html)

[MATLAB and Simulink Training from MATLAB Academy](https://matlabacademy.mathworks.com)

[MathWorks Certification Program](https://www.mathworks.com/services/training/certification.html)

[Apache Spark Basics | MATLAB & Simulink](https://www.mathworks.com/help//compiler/spark/apache-spark-basics.html)

[MATLAB Hadoop and Spark | MATLAB & Simulink](https://www.mathworks.com/products/compiler/hadoop-and-spark.html)

[MATLAB Online Courses from Udemy](https://www.udemy.com/topic/matlab/)

[MATLAB Online Courses from Coursera](https://www.coursera.org/courses?query=matlab)

[MATLAB Online Courses from edX](https://www.edx.org/learn/matlab)

[Building a MATLAB GUI](https://www.mathworks.com/discovery/matlab-gui.html)

[MATLAB Style Guidelines 2.0](https://www.mathworks.com/matlabcentral/fileexchange/46056-matlab-style-guidelines-2-0)

[Setting Up Git Source Control with MATLAB & Simulink](https://www.mathworks.com/help/matlab/matlab_prog/set-up-git-source-control.html)

[Pull, Push and Fetch Files with Git with MATLAB & Simulink](https://www.mathworks.com/help/matlab/matlab_prog/push-and-fetch-with-git.html)

[Create New Repository with MATLAB & Simulink](https://www.mathworks.com/help/matlab/matlab_prog/add-folder-to-source-control.html)

[PRMLT](http://prml.github.io/) is Matlab code for machine learning algorithms in the PRML book.

## MATLAB Tools, Libraries, Frameworks

**[MATLAB and Simulink Services & Applications List](https://www.mathworks.com/products.html)**

[MATLAB in the Cloud](https://www.mathworks.com/solutions/cloud.html) is a service that allows you to run in cloud environments from [MathWorks Cloud](https://www.mathworks.com/solutions/cloud.html#browser) to [Public Clouds](https://www.mathworks.com/solutions/cloud.html#public-cloud) including [AWS](https://aws.amazon.com/) and [Azure](https://azure.microsoft.com/).

[MATLAB Online™](https://matlab.mathworks.com) is a service that allows to users to uilitize MATLAB and Simulink through a web browser such as Google Chrome.

[Simulink](https://www.mathworks.com/products/simulink.html) is a block diagram environment for Model-Based Design. It supports simulation, automatic code generation, and continuous testing of embedded systems.

[Simulink Online™](https://www.mathworks.com/products/simulink-online.html) is a service that provides access to Simulink through your web browser.

[MATLAB Drive™](https://www.mathworks.com/products/matlab-drive.html) is a service that gives you the ability to store, access, and work with your files from anywhere.

[MATLAB Parallel Server™](https://www.mathworks.com/products/matlab-parallel-server.html) is a tool that lets you scale MATLAB® programs and Simulink® simulations to clusters and clouds. You can prototype your programs and simulations on the desktop and then run them on clusters and clouds without recoding. MATLAB Parallel Server supports batch jobs, interactive parallel computations, and distributed computations with large matrices.

[MATLAB Schemer](https://github.com/scottclowe/matlab-schemer) is a MATLAB package makes it easy to change the color scheme (theme) of the MATLAB display and GUI.

[LRSLibrary](https://github.com/andrewssobral/lrslibrary) is a Low-Rank and Sparse Tools for Background Modeling and Subtraction in Videos. The library was designed for moving object detection in videos, but it can be also used for other computer vision and machine learning problems.

[Image Processing Toolbox™](https://www.mathworks.com/products/image.html) is a tool that provides a comprehensive set of reference-standard algorithms and workflow apps for image processing, analysis, visualization, and algorithm development. You can perform image segmentation, image enhancement, noise reduction, geometric transformations, image registration, and 3D image processing.

[Computer Vision Toolbox™](https://www.mathworks.com/products/computer-vision.html) is a tool that provides algorithms, functions, and apps for designing and testing computer vision, 3D vision, and video processing systems. You can perform object detection and tracking, as well as feature detection, extraction, and matching. You can automate calibration workflows for single, stereo, and fisheye cameras. For 3D vision, the toolbox supports visual and point cloud SLAM, stereo vision, structure from motion, and point cloud processing.

[Statistics and Machine Learning Toolbox™](https://www.mathworks.com/products/statistics.html) is a tool that provides functions and apps to describe, analyze, and model data. You can use descriptive statistics, visualizations, and clustering for exploratory data analysis; fit probability distributions to data; generate random numbers for Monte Carlo simulations, and perform hypothesis tests. Regression and classification algorithms let you draw inferences from data and build predictive models either interactively, using the Classification and Regression Learner apps, or programmatically, using AutoML.

[Lidar Toolbox™](https://www.mathworks.com/products/lidar.html) is a tool that provides algorithms, functions, and apps for designing, analyzing, and testing lidar processing systems. You can perform object detection and tracking, semantic segmentation, shape fitting, lidar registration, and obstacle detection. Lidar Toolbox supports lidar-camera cross calibration for workflows that combine computer vision and lidar processing.

[Mapping Toolbox™](https://www.mathworks.com/products/mapping.html) is a tool that provides algorithms and functions for transforming geographic data and creating map displays. You can visualize your data in a geographic context, build map displays from more than 60 map projections, and transform data from a variety of sources into a consistent geographic coordinate system.

[UAV Toolbox](https://www.mathworks.com/products/uav.html) is an application that provides tools and reference applications for designing, simulating, testing, and deploying unmanned aerial vehicle (UAV) and drone applications. You can design autonomous flight algorithms, UAV missions, and flight controllers. The Flight Log Analyzer app lets you interactively analyze 3D flight paths, telemetry information, and sensor readings from common flight log formats.

[Parallel Computing Toolbox™](https://www.mathworks.com/products/matlab-parallel-server.html) is a tool that lets you solve computationally and data-intensive problems using multicore processors, GPUs, and computer clusters. High-level constructs such as parallel for-loops, special array types, and parallelized numerical algorithms enable you to parallelize MATLAB® applications without CUDA or MPI programming. The toolbox lets you use parallel-enabled functions in MATLAB and other toolboxes. You can use the toolbox with Simulink® to run multiple simulations of a model in parallel. Programs and models can run in both interactive and batch modes.

[Partial Differential Equation Toolbox™](https://www.mathworks.com/products/pde.html) is a tool that provides functions for solving structural mechanics, heat transfer, and general partial differential equations (PDEs) using finite element analysis.

[ROS Toolbox](https://www.mathworks.com/products/ros.html) is a tool that provides an interface connecting MATLAB® and Simulink® with the Robot Operating System (ROS and ROS 2), enabling you to create a network of ROS nodes. The toolbox includes MATLAB functions and Simulink blocks to import, analyze, and play back ROS data recorded in rosbag files. You can also connect to a live ROS network to access ROS messages.

[Robotics Toolbox™](https://www.mathworks.com/products/robotics.html) provides a toolbox that brings robotics specific functionality(designing, simulating, and testing manipulators, mobile robots, and humanoid robots) to MATLAB, exploiting the native capabilities of MATLAB (linear algebra, portability, graphics). The toolbox also supports mobile robots with functions for robot motion models (bicycle), path planning algorithms (bug, distance transform, D*, PRM), kinodynamic planning (lattice, RRT), localization (EKF, particle filter), map building (EKF) and simultaneous localization and mapping (EKF), and a Simulink model a of non-holonomic vehicle. The Toolbox also including a detailed Simulink model for a quadrotor flying robot.

[Deep Learning Toolbox™](https://www.mathworks.com/products/deep-learning.html) is a tool that provides a framework for designing and implementing deep neural networks with algorithms, pretrained models, and apps. You can use convolutional neural networks (ConvNets, CNNs) and long short-term memory (LSTM) networks to perform classification and regression on image, time-series, and text data. You can build network architectures such as generative adversarial networks (GANs) and Siamese networks using automatic differentiation, custom training loops, and shared weights. With the Deep Network Designer app, you can design, analyze, and train networks graphically. It can exchange models with TensorFlow™ and PyTorch through the ONNX format and import models from TensorFlow-Keras and Caffe. The toolbox supports transfer learning with DarkNet-53, ResNet-50, NASNet, SqueezeNet and many other pretrained models.

[Reinforcement Learning Toolbox™](https://www.mathworks.com/products/reinforcement-learning.html) is a tool that provides an app, functions, and a Simulink® block for training policies using reinforcement learning algorithms, including DQN, PPO, SAC, and DDPG. You can use these policies to implement controllers and decision-making algorithms for complex applications such as resource allocation, robotics, and autonomous systems.

[Deep Learning HDL Toolbox™](https://www.mathworks.com/products/deep-learning-hdl.html) is a tool that provides functions and tools to prototype and implement deep learning networks on FPGAs and SoCs. It provides pre-built bitstreams for running a variety of deep learning networks on supported Xilinx® and Intel® FPGA and SoC devices. Profiling and estimation tools let you customize a deep learning network by exploring design, performance, and resource utilization tradeoffs.

[Model Predictive Control Toolbox™](https://www.mathworks.com/products/model-predictive-control.html) is a tool that provides functions, an app, and Simulink® blocks for designing and simulating controllers using linear and nonlinear model predictive control (MPC). The toolbox lets you specify plant and disturbance models, horizons, constraints, and weights. By running closed-loop simulations, you can evaluate controller performance.

[Vision HDL Toolbox™](https://www.mathworks.com/products/vision-hdl.html) is a tool that provides pixel-streaming algorithms for the design and implementation of vision systems on FPGAs and ASICs. It provides a design framework that supports a diverse set of interface types, frame sizes, and frame rates. The image processing, video, and computer vision algorithms in the toolbox use an architecture appropriate for HDL implementations.

[SoC Blockset™](https://www.mathworks.com/products/soc.html) is a tool that provides Simulink® blocks and visualization tools for modeling, simulating, and analyzing hardware and software architectures for ASICs, FPGAs, and systems on a chip (SoC). You can build your system architecture using memory models, bus models, and I/O models, and simulate the architecture together with the algorithms.

[Wireless HDL Toolbox™](https://www.mathworks.com/products/wireless-hdl.html) is a tool that provides pre-verified, hardware-ready Simulink® blocks and subsystems for developing 5G, LTE, and custom OFDM-based wireless communication applications. It includes reference applications, IP blocks, and gateways between frame and sample-based processing.

[ThingSpeak™](https://www.mathworks.com/products/thingspeak.html) is an IoT analytics service that allows you to aggregate, visualize, and analyze live data streams in the cloud. ThingSpeak provides instant visualizations of data posted by your devices to ThingSpeak. With the ability to execute MATLAB® code in ThingSpeak, you can perform online analysis and process data as it comes in. ThingSpeak is often used for prototyping and proof-of-concept IoT systems that require analytics.

[SEA-MAT](https://sea-mat.github.io/sea-mat/) is a collaborative effort to organize and distribute Matlab tools for the Oceanographic Community.

[Gramm](https://github.com/piermorel/gramm) is a complete data visualization toolbox for Matlab. It provides an easy to use and high-level interface to produce publication-quality plots of complex data with varied statistical visualizations. Gramm is inspired by R's ggplot2 library.

[hctsa](https://hctsa-users.gitbook.io/hctsa-manual) is a software package for running highly comparative time-series analysis using Matlab.

[Plotly](https://plot.ly/matlab/) is a Graphing Library for MATLAB.

[YALMIP](https://yalmip.github.io/) is a MATLAB toolbox for optimization modeling.

[GNU Octave](https://www.gnu.org/software/octave/) is a high-level interpreted language, primarily intended for numerical computations. It provides capabilities for the numerical solution of linear and nonlinear problems, and for performing other numerical experiments. It also provides extensive graphics capabilities for data visualization and manipulation.

# C/C++ Development
[Back to the Top](https://github.com/mikeroyal/ISP-Guide#table-of-contents)

<p align="center">
 <img src="https://user-images.githubusercontent.com/45159366/115297894-961e0d80-a111-11eb-81c3-e2bd2ac9a7cd.png">
  <br />
</p>

## C/C++ Learning Resources

[C++](https://www.cplusplus.com/doc/tutorial/) is a cross-platform language that can be used to build high-performance applications developed by Bjarne Stroustrup, as an extension to the C language.

[C](https://www.iso.org/standard/74528.html) is a general-purpose, high-level language that was originally developed by Dennis M. Ritchie to develop the UNIX operating system at Bell Labs. It supports structured programming, lexical variable scope, and recursion, with a static type system. C also provides constructs that map efficiently to typical machine instructions, which makes it one was of the most widely used programming languages today.

[Embedded C](https://en.wikipedia.org/wiki/Embedded_C) is a set of language extensions for the C programming language by the [C Standards Committee](https://isocpp.org/std/the-committee) to address issues that exist between C extensions for different [embedded systems](https://en.wikipedia.org/wiki/Embedded_system). The extensions hep enhance microprocessor features such as fixed-point arithmetic, multiple distinct memory banks, and basic I/O operations. This makes Embedded C the most popular embedded software language in the world.

[C & C++ Developer Tools from JetBrains](https://www.jetbrains.com/cpp/)

[Open source C++ libraries on cppreference.com](https://en.cppreference.com/w/cpp/links/libs)

[C++ Graphics libraries](https://cpp.libhunt.com/libs/graphics)

[C++ Libraries in MATLAB](https://www.mathworks.com/help/matlab/call-cpp-library-functions.html)

[C++ Tools and Libraries Articles](https://www.cplusplus.com/articles/tools/)

[Google C++ Style Guide](https://google.github.io/styleguide/cppguide.html)

[Introduction C++ Education course on Google Developers](https://developers.google.com/edu/c++/)

[C++ style guide for Fuchsia](https://fuchsia.dev/fuchsia-src/development/languages/c-cpp/cpp-style)

[C and C++ Coding Style Guide by OpenTitan](https://docs.opentitan.org/doc/rm/c_cpp_coding_style/)

[Chromium C++ Style Guide](https://chromium.googlesource.com/chromium/src/+/master/styleguide/c++/c++.md)

[C++ Core Guidelines](https://github.com/isocpp/CppCoreGuidelines/blob/master/CppCoreGuidelines.md)

[C++ Style Guide for ROS](http://wiki.ros.org/CppStyleGuide)

[Learn C++](https://www.learncpp.com/)

[Learn C : An Interactive C Tutorial](https://www.learn-c.org/)

[C++ Institute](https://cppinstitute.org/free-c-and-c-courses)

[C++ Online Training Courses on LinkedIn Learning](https://www.linkedin.com/learning/topics/c-plus-plus)

[C++ Tutorials on W3Schools](https://www.w3schools.com/cpp/default.asp)

[Learn C Programming Online Courses on edX](https://www.edx.org/learn/c-programming)

[Learn C++ with Online Courses on edX](https://www.edx.org/learn/c-plus-plus)

[Learn C++ on Codecademy](https://www.codecademy.com/learn/learn-c-plus-plus)

[Coding for Everyone: C and C++ course on Coursera](https://www.coursera.org/specializations/coding-for-everyone)

[C++ For C Programmers on Coursera](https://www.coursera.org/learn/c-plus-plus-a)

[Top C Courses on Coursera](https://www.coursera.org/courses?query=c%20programming)

[C++ Online Courses on Udemy](https://www.udemy.com/topic/c-plus-plus/)

[Top C Courses on Udemy](https://www.udemy.com/topic/c-programming/)

[Basics of Embedded C Programming for Beginners on Udemy](https://www.udemy.com/course/embedded-c-programming-for-embedded-systems/)

[C++ For Programmers Course on Udacity](https://www.udacity.com/course/c-for-programmers--ud210)

[C++ Fundamentals Course on Pluralsight](https://www.pluralsight.com/courses/learn-program-cplusplus)

[Introduction to C++ on MIT Free Online Course Materials](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-096-introduction-to-c-january-iap-2011/)

[Introduction to C++ for Programmers | Harvard ](https://online-learning.harvard.edu/course/introduction-c-programmers)

[Online C Courses | Harvard University](https://online-learning.harvard.edu/subject/c)


## C/C++ Tools and Frameworks

[AWS SDK for C++](https://aws.amazon.com/sdk-for-cpp/)

[Azure SDK for C++](https://github.com/Azure/azure-sdk-for-cpp)

[Azure SDK for C](https://github.com/Azure/azure-sdk-for-c)

[C++ Client Libraries for Google Cloud Services](https://github.com/googleapis/google-cloud-cpp)

[Visual Studio](https://visualstudio.microsoft.com/) is an integrated development environment (IDE) from Microsoft; which is a feature-rich application that can be used for many aspects of software development. Visual Studio makes it easy to edit, debug, build, and publish your app. By using Microsoft software development platforms such as Windows API, Windows Forms, Windows Presentation Foundation, and Windows Store.

[Visual Studio Code](https://code.visualstudio.com/) is a code editor redefined and optimized for building and debugging modern web and cloud applications.

[Vcpkg](https://github.com/microsoft/vcpkg) is a C++ Library Manager for Windows, Linux, and MacOS.

[ReSharper C++](https://www.jetbrains.com/resharper-cpp/features/) is a Visual Studio Extension for C++ developers developed by JetBrains.

[AppCode](https://www.jetbrains.com/objc/) is constantly monitoring the quality of your code. It warns you of errors and smells and suggests quick-fixes to resolve them automatically. AppCode provides lots of code inspections for Objective-C, Swift, C/C++, and a number of code inspections for other supported languages. All code inspections are run on the fly.

[CLion](https://www.jetbrains.com/clion/features/) is a cross-platform IDE for C and C++ developers developed by JetBrains.

[Code::Blocks](https://www.codeblocks.org/) is a free C/C++ and Fortran IDE built to meet the most demanding needs of its users. It is designed to be very extensible and fully configurable. Built around a plugin framework, Code::Blocks can be extended with plugins.

[CppSharp](https://github.com/mono/CppSharp) is a tool and set of libraries which facilitates the usage of native C/C++ code with the .NET ecosystem. It consumes C/C++ header and library files and generates the necessary glue code to surface the native API as a managed API. Such an API can be used to consume an existing native library in your managed code or add managed scripting support to a native codebase.

[Conan](https://conan.io/) is an Open Source Package Manager for C++ development and dependency management into the 21st century and on par with the other development ecosystems.

[High Performance Computing (HPC) SDK](https://developer.nvidia.com/hpc) is a comprehensive toolbox for GPU accelerating HPC modeling and simulation applications. It includes the C, C++, and Fortran compilers, libraries, and analysis tools necessary for developing HPC applications on the NVIDIA platform.

[Thrust](https://github.com/NVIDIA/thrust) is a C++ parallel programming library which resembles the C++ Standard Library. Thrust's high-level interface greatly enhances programmer productivity while enabling performance portability between GPUs and multicore CPUs. Interoperability with established technologies such as CUDA, TBB, and OpenMP integrates with existing software.

[Boost](https://www.boost.org/) is an educational opportunity focused on cutting-edge C++. Boost has been a participant in the annual Google Summer of Code since 2007, in which students develop their skills by working on Boost Library development.

[Automake](https://www.gnu.org/software/automake/) is a tool for automatically generating Makefile.in files compliant with the GNU Coding Standards. Automake requires the use of GNU Autoconf.

[Cmake](https://cmake.org/) is an open-source, cross-platform family of tools designed to build, test and package software. CMake is used to control the software compilation process using simple platform and compiler independent configuration files, and generate native makefiles and workspaces that can be used in the compiler environment of your choice.

[GDB](http://www.gnu.org/software/gdb/) is a debugger, that allows you to see what is going on `inside' another program while it executes or what another program was doing at the moment it crashed.

[GCC](https://gcc.gnu.org/) is a compiler Collection that includes front ends for C, C++, Objective-C, Fortran, Ada, Go, and D, as well as libraries for these languages.

[GSL](https://www.gnu.org/software/gsl/) is a numerical library for C and C++ programmers. It is free software under the GNU General Public License. The library provides a wide range of mathematical routines such as random number generators, special functions and least-squares fitting. There are over 1000 functions in total with an extensive test suite.

[OpenGL Extension Wrangler Library (GLEW)](https://www.opengl.org/sdk/libs/GLEW/) is a cross-platform open-source C/C++ extension loading library. GLEW provides efficient run-time mechanisms for determining which OpenGL extensions are supported on the target platform.

[Libtool](https://www.gnu.org/software/libtool/) is a generic library support script that hides the complexity of using shared libraries behind a consistent, portable interface. To use Libtool, add the new generic library building commands to your Makefile, Makefile.in, or Makefile.am.

[Maven](https://maven.apache.org/) is a software project management and comprehension tool. Based on the concept of a project object model (POM), Maven can manage a project's build, reporting and documentation from a central piece of information.

[TAU (Tuning And Analysis Utilities)](http://www.cs.uoregon.edu/research/tau/home.php) is capable of gathering performance information through instrumentation of functions, methods, basic blocks, and statements as well as event-based sampling. All C++ language features are supported including templates and namespaces.

[Clang](https://clang.llvm.org/) is a production quality C, Objective-C, C++ and Objective-C++ compiler when targeting X86-32, X86-64, and ARM (other targets may have caveats, but are usually easy to fix). Clang is used in production to build performance-critical software like Google Chrome or Firefox.

[OpenCV](https://opencv.org/) is a highly optimized library with focus on real-time applications. Cross-Platform C++, Python and Java interfaces support Linux, MacOS, Windows, iOS, and Android.

[Libcu++](https://nvidia.github.io/libcudacxx) is the NVIDIA C++ Standard Library for your entire system. It provides a heterogeneous implementation of the C++ Standard Library that can be used in and between CPU and GPU code.

[ANTLR (ANother Tool for Language Recognition)](https://www.antlr.org/) is a powerful parser generator for reading, processing, executing, or translating structured text or binary files. It's widely used to build languages, tools, and frameworks. From a grammar, ANTLR generates a parser that can build parse trees and also generates a listener interface that makes it easy to respond to the recognition of phrases of interest.

[Oat++](https://oatpp.io/) is a light and powerful C++ web framework for highly scalable and resource-efficient web application. It's zero-dependency and easy-portable.

[JavaCPP](https://github.com/bytedeco/javacpp) is a program that provides efficient access to native C++ inside Java, not unlike the way some C/C++ compilers interact with assembly language.

[Cython](https://cython.org/) is a language that makes writing C extensions for Python as easy as Python itself. Cython is based on Pyrex, but supports more cutting edge functionality and optimizations such as calling C functions and declaring C types on variables and class attributes.

[Spdlog](https://github.com/gabime/spdlog) is a very fast, header-only/compiled, C++ logging library.

[Infer](https://fbinfer.com/) is a static analysis tool for Java, C++, Objective-C, and C. Infer is written in [OCaml](https://ocaml.org/).

# Java Development
[Back to the Top](https://github.com/mikeroyal/ISP-Guide#table-of-contents)

<p align="center">
 <img src="https://user-images.githubusercontent.com/45159366/93925952-c0b6fd80-fccb-11ea-9f90-21c4148e3c86.png">
  <br />
</p>


## Java Learning Resources

[Java](https://www.oracle.com/java/) is a popular programming language and development platform(JDK). It reduces costs, shortens development timeframes, drives innovation, and improves application services. With millions of developers running more than 51 billion Java Virtual Machines worldwide.

[The Eclipse Foundation](https://www.eclipse.org/downloads/) is home to a worldwide community of developers, the Eclipse IDE, Jakarta EE and over 375 open source projects, including runtimes, tools and frameworks for Java and other languages.

[Getting Started with Java](https://docs.oracle.com/javase/tutorial/)

[Oracle Java certifications from Oracle University](https://education.oracle.com/java-certification-benefits)

[Google Developers Training](https://developers.google.com/training/)

[Google Developers Certification](https://developers.google.com/certification/)

[Java Tutorial by W3Schools](https://www.w3schools.com/java/)

[Building Your First Android App in Java](codelabs.developers.google.com/codelabs/build-your-first-android-app/)

[Getting Started with Java in Visual Studio Code](https://code.visualstudio.com/docs/java/java-tutorial)

[Google Java Style Guide](https://google.github.io/styleguide/javaguide.html)

[AOSP Java Code Style for Contributors](https://source.android.com/setup/contribute/code-style)

[Chromium Java style guide](https://chromium.googlesource.com/chromium/src/+/master/styleguide/java/java.md)

[Get Started with OR-Tools for Java](https://developers.google.com/optimization/introduction/java)

[Getting started with Java Tool Installer task for Azure Pipelines](https://docs.microsoft.com/en-us/azure/devops/pipelines/tasks/tool/java-tool-installer)

[Gradle User Manual](https://docs.gradle.org/current/userguide/userguide.html)

## Java Tools, Libraries, and Frameworks

[Java SE](https://www.oracle.com/java/technologies/javase/tools-jsp.html) contains several tools to assist in program development and debugging, and in the monitoring and troubleshooting of production applications.

[JDK Development Tools](https://docs.oracle.com/javase/7/docs/technotes/tools/) includes the Java Web Start Tools (javaws) Java Troubleshooting, Profiling, Monitoring and Management Tools (jcmd, jconsole, jmc, jvisualvm); and Java Web Services Tools (schemagen, wsgen, wsimport, xjc).

[Android Studio](https://developer.android.com/studio/) is the official integrated development environment for Google's Android operating system, built on JetBrains' IntelliJ IDEA software and designed specifically for Android development. Availble on Windows, macOS, Linux, Chrome OS.

[IntelliJ IDEA](https://www.jetbrains.com/idea/) is an IDE for Java, but it also understands and provides intelligent coding assistance for a large variety of other languages such as Kotlin, SQL, JPQL, HTML, JavaScript, etc., even if the language expression is injected into a String literal in your Java code.

[NetBeans](https://netbeans.org/features/java/index.html) is an IDE provides Java developers with all the tools needed to create professional desktop, mobile and enterprise applications. Creating, Editing, and Refactoring. The IDE provides wizards and templates to let you create Java EE, Java SE, and Java ME applications.

[Java Design Patterns ](https://github.com/iluwatar/java-design-patterns) is a collection of the best formalized practices a programmer can use to solve common problems when designing an application or system.

[Elasticsearch](https://www.elastic.co/products/elasticsearch) is a distributed RESTful search engine built for the cloud written in Java.

[RxJava](https://github.com/ReactiveX/RxJava) is a Java VM implementation of [Reactive Extensions](http://reactivex.io/): a library for composing asynchronous and event-based programs by using observable sequences. It extends the [observer pattern](http://en.wikipedia.org/wiki/Observer_pattern) to support sequences of data/events and adds operators that allow you to compose sequences together declaratively while abstracting away concerns about things like low-level threading, synchronization, thread-safety and concurrent data structures.

[Guava](https://github.com/google/guava) is a set of core Java libraries from Google that includes new collection types (such as multimap and multiset), immutable collections, a graph library, and utilities for concurrency, I/O, hashing, caching, primitives, strings, and more! It is widely used on most Java projects within Google, and widely used by many other companies as well.

[okhttp](https://square.github.io/okhttp/) is a HTTP client for Java and Kotlin developed by Square.

[Retrofit](https://square.github.io/retrofit/) is a type-safe HTTP client for Android and Java develped by Square.

[LeakCanary](https://square.github.io/leakcanary/) is a memory leak detection library for Android develped by Square.

[Apache Spark](https://spark.apache.org/) is a unified analytics engine for large-scale data processing. It provides high-level APIs in Scala, Java, Python, and R, and an optimized engine that supports general computation graphs for data analysis. It also supports a rich set of higher-level tools including Spark SQL for SQL and DataFrames, MLlib for machine learning, GraphX for graph processing, and Structured Streaming for stream processing.

[Apache Flink](https://flink.apache.org/) is an open source stream processing framework with powerful stream- and batch-processing capabilities with elegant and fluent APIs in Java and Scala.

[Fastjson](https://github.com/alibaba/fastjson/wiki) is a Java library that can be used to convert Java Objects into their JSON representation. It can also be used to convert a JSON string to an equivalent Java object.

[libGDX](https://libgdx.com/) is a cross-platform Java game development framework based on OpenGL (ES) that works on Windows, Linux, Mac OS X, Android, your WebGL enabled browser and iOS.

[Jenkins](https://www.jenkins.io/) is the leading open-source automation server. Built with Java, it provides over 1700 [plugins](https://plugins.jenkins.io/) to support automating virtually anything, so that humans can actually spend their time doing things machines cannot.

[DBeaver](https://dbeaver.io/) is a free multi-platform database tool for developers, SQL programmers, database administrators and analysts. Supports any database which has JDBC driver (which basically means - ANY database). EE version also supports non-JDBC datasources (MongoDB, Cassandra, Redis, DynamoDB, etc).

[Redisson](https://redisson.pro/) is a Redis Java client with features of In-Memory Data Grid. Over 50 Redis based Java objects and services: Set, Multimap, SortedSet, Map, List, Queue, Deque, Semaphore, Lock, AtomicLong, Map Reduce, Publish / Subscribe, Bloom filter, Spring Cache, Tomcat, Scheduler, JCache API, Hibernate, MyBatis, RPC, and local cache.

[GraalVM](https://www.graalvm.org/) is a universal virtual machine for running applications written in JavaScript, Python, Ruby, R, JVM-based languages like Java, Scala, Clojure, Kotlin, and LLVM-based languages such as C and C++.

[Gradle](https://gradle.org/) is a build automation tool for multi-language software development. From mobile apps to microservices, from small startups to big enterprises, Gradle helps teams build, automate and deliver better software, faster. Write in Java, C++, Python or your language of choice.

[Apache Groovy](http://www.groovy-lang.org/) is a powerful, optionally typed and dynamic language, with static-typing and static compilation capabilities, for the Java platform aimed at improving developer productivity thanks to a concise, familiar and easy to learn syntax. It integrates smoothly with any Java program, and immediately delivers to your application powerful features, including scripting capabilities, Domain-Specific Language authoring, runtime and compile-time meta-programming and functional programming.

[JaCoCo](https://www.jacoco.org/jacoco/) is a free code coverage library for Java, which has been created by the EclEmma team based on the lessons learned from using and integration existing libraries for many years.

[Apache JMeter](http://jmeter.apache.org/) is  used to test performance both on static and dynamic resources, Web dynamic applications. It also used to simulate a heavy load on a server, group of servers, network or object to test its strength or to analyze overall performance under different load types.

[Junit](https://junit.org/) is a simple framework to write repeatable tests. It is an instance of the xUnit architecture for unit testing frameworks.

[Mockito](https://site.mockito.org/) is the most popular Mocking framework for unit tests written in Java.

[SpotBugs](https://spotbugs.github.io/) is a program which uses static analysis to look for bugs in Java code.

[SpringBoot](https://spring.io/projects/spring-boot) is a great tool that helps you to create Spring-powered, production-grade applications and services with absolute minimum fuss. It takes an opinionated view of the Spring platform so that new and existing users can quickly get to the bits they need.

[YourKit](https://www.yourkit.com/) is a technology leader, creator of the most innovative and intelligent tools for profiling Java & .NET applications.

# Python Development
[Back to the Top](https://github.com/mikeroyal/ISP-Guide#table-of-contents)

<p align="center">
 <img src="https://user-images.githubusercontent.com/45159366/93133273-ce490380-f68b-11ea-81d0-7f6a3debe6c0.png">
  <br />

</p>

## Python Learning Resources

[Python](https://www.python.org) is an interpreted, high-level programming language. Python is used heavily in the fields of Data Science and Machine Learning.

[Python Developer’s Guide](https://devguide.python.org) is a comprehensive resource for contributing to Python – for both new and experienced contributors. It is maintained by the same community that maintains Python.

[Azure Functions Python developer guide](https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-python) is an introduction to developing Azure Functions using Python. The content below assumes that you've already read the [Azure Functions developers guide](https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference).

[CheckiO](https://checkio.org/) is a programming learning platform and a gamified website that teaches Python through solving code challenges and competing for the most elegant and creative solutions.

[Python Institute](https://pythoninstitute.org)

[PCEP – Certified Entry-Level Python Programmer certification](https://pythoninstitute.org/pcep-certification-entry-level/)

[PCAP – Certified Associate in Python Programming certification](https://pythoninstitute.org/pcap-certification-associate/)

[PCPP – Certified Professional in Python Programming 1 certification](https://pythoninstitute.org/pcpp-certification-professional/)

[PCPP – Certified Professional in Python Programming 2](https://pythoninstitute.org/pcpp-certification-professional/)

[MTA: Introduction to Programming Using Python Certification](https://docs.microsoft.com/en-us/learn/certifications/mta-introduction-to-programming-using-python)

[Getting Started with Python in Visual Studio Code](https://code.visualstudio.com/docs/python/python-tutorial)

[Google's Python Style Guide](https://google.github.io/styleguide/pyguide.html)

[Google's Python Education Class](https://developers.google.com/edu/python/)

[Real Python](https://realpython.com)

[The Python Open Source Computer Science Degree by Forrest Knight](https://github.com/ForrestKnight/open-source-cs-python)

[Intro to Python for Data Science](https://www.datacamp.com/courses/intro-to-python-for-data-science)

[Intro to Python by W3schools](https://www.w3schools.com/python/python_intro.asp)

[Codecademy's Python 3 course](https://www.codecademy.com/learn/learn-python-3)

[Learn Python with Online Courses and Classes from edX](https://www.edx.org/learn/python)

[Python Courses Online from Coursera](https://www.coursera.org/courses?query=python)

## Python Frameworks and Tools

[Python Package Index (PyPI)](https://pypi.org/) is a repository of software for the Python programming language. PyPI helps you find and install software developed and shared by the Python community.

[PyCharm](https://www.jetbrains.com/pycharm/) is the best IDE I've ever used. With PyCharm, you can access the command line, connect to a database, create a virtual environment, and manage your version control system all in one place, saving time by avoiding constantly switching between windows.

[Python Tools for Visual Studio(PTVS)](https://microsoft.github.io/PTVS/) is a free, open source plugin that turns Visual Studio into a Python IDE. It supports editing, browsing, IntelliSense, mixed Python/C++ debugging, remote Linux/MacOS debugging, profiling, IPython, and web development with Django and other frameworks.

[Pylance](https://github.com/microsoft/pylance-release) is an extension that works alongside Python in Visual Studio Code to provide performant language support. Under the hood, Pylance is powered by Pyright, Microsoft's static type checking tool.

[Pyright](https://github.com/Microsoft/pyright) is a fast type checker meant for large Python source bases. It can run in a “watch” mode and performs fast incremental updates when files are modified.

[Django](https://www.djangoproject.com/) is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.

[Flask](https://flask.palletsprojects.com/) is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries.

[Web2py](http://web2py.com/) is an open-source web application framework written in Python allowing allows web developers to program dynamic web content. One web2py instance can run multiple web sites using different databases.

[AWS Chalice](https://github.com/aws/chalice) is a framework for writing serverless apps in python. It allows you to quickly create and deploy applications that use AWS Lambda.

[Tornado](https://www.tornadoweb.org/) is a Python web framework and asynchronous networking library. Tornado uses a non-blocking network I/O, which can scale to tens of thousands of open connections.

[HTTPie](https://github.com/httpie/httpie) is a command line HTTP client that makes CLI interaction with web services as easy as possible. HTTPie is designed for testing, debugging, and generally interacting with APIs & HTTP servers.

[Scrapy](https://scrapy.org/) is a fast high-level web crawling and web scraping framework, used to crawl websites and extract structured data from their pages. It can be used for a wide range of purposes, from data mining to monitoring and automated testing.

[Sentry](https://sentry.io/) is a service that helps you monitor and fix crashes in realtime. The server is in Python, but it contains a full API for sending events from any language, in any application.

[Pipenv](https://github.com/pypa/pipenv) is a tool that aims to bring the best of all packaging worlds (bundler, composer, npm, cargo, yarn, etc.) to the Python world.

[Python Fire](https://github.com/google/python-fire) is a library for automatically generating command line interfaces (CLIs) from absolutely any Python object.

[Bottle](https://github.com/bottlepy/bottle) is a fast, simple and lightweight [WSGI](https://www.wsgi.org/) micro web-framework for Python. It is distributed as a single file module and has no dependencies other than the [Python Standard Library](https://docs.python.org/library/).

[CherryPy](https://cherrypy.org) is a minimalist Python object-oriented HTTP web framework.

[Sanic](https://github.com/huge-success/sanic) is a Python 3.6+ web server and web framework that's written to go fast.

[Pyramid](https://trypyramid.com) is a small and fast open source Python web framework. It makes real-world web application development and deployment more fun and more productive.

[TurboGears](https://turbogears.org) is a hybrid web framework able to act both as a Full Stack framework or as a Microframework.

[Falcon](https://falconframework.org/) is a reliable, high-performance Python web framework for building large-scale app backends and microservices with support for MongoDB, Pluggable Applications and autogenerated Admin.

[Neural Network Intelligence(NNI)](https://github.com/microsoft/nni) is an open source AutoML toolkit for automate machine learning lifecycle, including [Feature Engineering](https://github.com/microsoft/nni/blob/master/docs/en_US/FeatureEngineering/Overview.md), [Neural Architecture Search](https://github.com/microsoft/nni/blob/master/docs/en_US/NAS/Overview.md), [Model Compression](https://github.com/microsoft/nni/blob/master/docs/en_US/Compressor/Overview.md) and [Hyperparameter Tuning](https://github.com/microsoft/nni/blob/master/docs/en_US/Tuner/BuiltinTuner.md).

[Dash](https://plotly.com/dash) is a popular Python framework for building ML & data science web apps for Python, R, Julia, and Jupyter.

[Luigi](https://github.com/spotify/luigi) is a Python module that helps you build complex pipelines of batch jobs. It handles dependency resolution, workflow management, visualization etc. It also comes with Hadoop support built-in.

[Locust](https://github.com/locustio/locust) is an easy to use, scriptable and scalable performance testing tool.

[spaCy](https://github.com/explosion/spaCy) is a library for advanced Natural Language Processing in Python and Cython.

[NumPy](https://www.numpy.org/) is the fundamental package needed for scientific computing with Python.

[Pillow](https://python-pillow.org/) is a friendly PIL(Python Imaging Library) fork.

[IPython](https://ipython.org/) is a command shell for interactive computing in multiple programming languages, originally developed for the Python programming language, that offers enhanced introspection, rich media, additional shell syntax, tab completion, and rich history.

[GraphLab Create](https://turi.com/) is a Python library, backed by a C++ engine, for quickly building large-scale, high-performance machine learning models.

[Pandas](https://pandas.pydata.org/) is a fast, powerful, and easy to use open source data structrures, data analysis and manipulation tool, built on top of the Python programming language.

[PuLP](https://coin-or.github.io/pulp/) is an Linear Programming modeler written in python. PuLP can generate LP files and call on use highly optimized solvers, GLPK, COIN CLP/CBC, CPLEX, and GUROBI, to solve these linear problems.

[Matplotlib](https://matplotlib.org/) is a 2D plotting library for creating static, animated, and interactive visualizations in Python. Matplotlib produces publication-quality figures in a variety of hardcopy formats and interactive environments across platforms.

[Scikit-Learn](https://scikit-learn.org/stable/index.html) is a simple and efficient tool for data mining and data analysis. It is built on NumPy,SciPy, and mathplotlib.

# Scala Development
[Back to the Top](https://github.com/mikeroyal/ISP-Guide#table-of-contents)

<p align="center">
 <img src="https://user-images.githubusercontent.com/45159366/95688293-09bcec00-0bbe-11eb-8d0d-d75706856673.png">
  <br />
</p>


## Scala Learning Resources

[Scala](https://scala-lang.org/) is a combination of object-oriented and functional programming in one concise, high-level language. Scala's static types help avoid bugs in complex applications, and its JVM and JavaScript runtimes let you build high-performance systems with easy access to huge ecosystems of libraries.

[Scala Style Guide](https://docs.scala-lang.org/style/)

[Databricks Scala Style Guide](https://github.com/databricks/scala-style-guide)

[Data Science using Scala and Spark on Azure](https://docs.microsoft.com/en-us/azure/machine-learning/team-data-science-process/scala-walkthrough)

[Creating a Scala Maven application for Apache Spark in HDInsight using IntelliJ](https://docs.microsoft.com/en-us/azure/hdinsight/spark/apache-spark-create-standalone-application)

[Intro to Spark DataFrames using Scala with Azure Databricks](https://docs.microsoft.com/en-us/azure/databricks/spark/latest/dataframes-datasets/introduction-to-dataframes-scala)

[Using Scala to Program AWS Glue ETL Scripts](https://docs.aws.amazon.com/glue/latest/dg/glue-etl-scala-using.html)

[Using Flink Scala shell with Amazon EMR clusters](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/flink-scala.html)

[AWS EMR and Spark 2 using Scala from Udemy](https://www.udemy.com/course/aws-emr-and-spark-2-using-scala/)

[Using the Google Cloud Storage connector with Apache Spark](https://cloud.google.com/dataproc/docs/tutorials/gcs-connector-spark-tutorial)

[Write and run Spark Scala jobs on Cloud Dataproc for Google Cloud](https://cloud.google.com/dataproc/docs/tutorials/spark-scala)

[Scala Courses and Certifications from edX](https://www.edx.org/learn/scala)

[Scala Courses from Coursera](https://www.coursera.org/courses?query=scala)

[Top Scala Courses from Udemy](https://www.udemy.com/topic/scala/)

## Scala Tools

[Apache Spark](https://spark.apache.org/) is a unified analytics engine for large-scale data processing. It provides high-level APIs in Scala, Java, Python, and R, and an optimized engine that supports general computation graphs for data analysis. It also supports a rich set of higher-level tools including Spark SQL for SQL and DataFrames, MLlib for machine learning, GraphX for graph processing, and Structured Streaming for stream processing.

[Apache Spark Connector for SQL Server and Azure SQL](https://github.com/microsoft/sql-spark-connector) is a high-performance connector that enables you to use transactional data in big data analytics and persists results for ad-hoc queries or reporting. The connector allows you to use any SQL database, on-premises or in the cloud, as an input data source or output data sink for Spark jobs.

[Azure Databricks](https://azure.microsoft.com/en-us/services/databricks/) is a fast and collaborative Apache Spark-based big data analytics service designed for data science and data engineering. Azure Databricks, sets up your Apache Spark environment in minutes, autoscale, and collaborate on shared projects in an interactive workspace. Azure Databricks supports Python, Scala, R, Java, and SQL, as well as data science frameworks and libraries including TensorFlow, PyTorch, and scikit-learn.

[Apache PredictionIO](https://predictionio.apache.org/) is an open source machine learning framework for developers, data scientists, and end users. It supports event collection, deployment of algorithms, evaluation, querying predictive results via REST APIs. It is based on scalable open source services like Hadoop, HBase (and other DBs), Elasticsearch, Spark and implements what is called a Lambda Architecture.

[Cluster Manager for Apache Kafka(CMAK)](https://github.com/yahoo/CMAK) is a tool for managing [Apache Kafka](https://kafka.apache.org/) clusters.

[BigDL](https://bigdl-project.github.io/) is a distributed deep learning library for Apache Spark. With BigDL, users can write their deep learning applications as standard Spark programs, which can directly run on top of existing Spark or Hadoop clusters.

[Eclipse Deeplearning4J (DL4J)](https://deeplearning4j.konduit.ai/) is a set of projects intended to support all the needs of a JVM-based(Scala, Kotlin, Clojure, and Groovy) deep learning application. This means starting with the raw data, loading and preprocessing it from wherever and whatever format it is in to building and tuning a wide variety of simple and complex deep learning networks.

[Play Framework](https://github.com/playframework/playframework) is a web framework combines productivity and performance making it easy to build scalable web applications with Java and Scala.

[Dotty](https://github.com/lampepfl/dotty) is a research compiler that will become Scala 3.

[AWScala](https://github.com/seratch/AWScala) is a tool that enables Scala developers to easily work with Amazon Web Services in the Scala way.

[Scala.js](https://www.scala-js.org/) is a compiler that converts Scala to JavaScript.

[Polynote](https://polynote.org/) is an experimental polyglot notebook environment. Currently, it supports Scala and Python (with or without Spark), SQL, and Vega.

[Scala Native](http://scala-native.org/) is an optimizing ahead-of-time compiler and lightweight managed runtime designed specifically for Scala.

[Gitbucket](https://gitbucket.github.io/) is a Git platform powered by Scala with easy installation, high extensibility & GitHub API compatibility.

[Finagle](https://twitter.github.io/finagle) is a fault tolerant, protocol-agnostic RPC system

[Gatling](https://gatling.io/) is a load test tool. It officially supports HTTP, WebSocket, Server-Sent-Events and JMS.

[Scalatra](https://scalatra.org/) is a tiny Scala high-performance, async web framework, inspired by [Sinatra](https://www.sinatrarb.com/).


# R Development
[Back to the Top](https://github.com/mikeroyal/ISP-Guide#table-of-contents)

<p align="center">
 <img src="https://user-images.githubusercontent.com/45159366/126080648-b515b7c0-e1bd-481b-92d2-c9cdd98ac30c.png">
  <br />
</p>

## R Learning Resources

[R](https://www.r-project.org/) is an open source software environment for statistical computing and graphics. It compiles and runs on a wide variety of  platforms such as Windows and MacOS.

[An Introduction to R](https://cran.r-project.org/doc/manuals/r-release/R-intro.pdf)

[Google's R Style Guide](https://google.github.io/styleguide/Rguide.html)

[R developer's guide to Azure](https://docs.microsoft.com/en-us/azure/architecture/data-guide/technology-choices/r-developers-guide)

[Running R at Scale on Google Compute Engine](https://cloud.google.com/solutions/running-r-at-scale)

[Running R on AWS](https://aws.amazon.com/blogs/big-data/running-r-on-aws/)

[RStudio Server Pro for AWS](https://aws.amazon.com/marketplace/pp/RStudio-RStudio-Server-Pro-for-AWS/B06W2G9PRY)

[Learn R by Codecademy](https://www.codecademy.com/learn/learn-r)

[Learn R Programming with Online Courses and Lessons by edX](https://www.edx.org/learn/r-programming)

[R Language Courses by Coursera](https://www.coursera.org/courses?query=r%20language)

[Learn R For Data Science by Udacity](https://www.udacity.com/course/programming-for-data-science-nanodegree-with-R--nd118)

## R Tools, Libraries, and Frameworks

[Visual Studio Code](https://code.visualstudio.com/) is a code editor redefined and optimized for building and debugging modern web and cloud applications.

[Code Server](https://coder.com/) is a tool that allows you to run [VS Code](https://code.visualstudio.com/) on any machine anywhere and access it in the browser.

[VSCode-R](https://marketplace.visualstudio.com/items?itemName=Ikuyadeu.r) is a VS Code extension provides support for the [R programming language](https://www.r-project.org/), including features such as extended syntax highlighting, R language service based on code analysis, interacting with R terminals, viewing data, plots, workspace variables, help pages, managing packages, and working with [R Markdown](https://rmarkdown.rstudio.com/) documents.

[R Debugger](https://marketplace.visualstudio.com/items?itemName=RDebugger.r-debugger) is an extension that adds debugging capabilities for the R programming language to Visual Studio Code and depends on the R package [vscDebugger (documentation)](https://github.com/ManuelHentschel/vscDebugger).

[Language Server Protocol (LSP)](https://microsoft.github.io/language-server-protocol/) is a tool that defines the protocol used between an editor or IDE and a language server that provides language features like auto complete, go to definition, find all references.

[RStudio](https://rstudio.com/) is an integrated development environment for R and Python, with a console, syntax-highlighting editor that supports direct code execution, and tools for plotting, history, debugging and workspace management.

[Shiny](https://shiny.rstudio.com/) is a newer package from RStudio that makes it incredibly easy to build interactive web applications with R.

[Rmarkdown](https://rmarkdown.rstudio.com/) is a package helps you create dynamic analysis documents that combine code, rendered output (such as figures), and prose.

[R Host](https://github.com/microsoft/R-Host) is a host process for R that provides access and extensibility to it remotely over WebSocket and JSON.

[Rplugin](https://github.com/JetBrains/Rplugin) is R Language supported plugin for the IntelliJ IDE.

[Plotly](https://plotly-r.com/) is an R package for creating interactive web graphics via the open source JavaScript graphing library [plotly.js](https://github.com/plotly/plotly.js).

[Metaflow](https://metaflow.org/) is a Python/R library that helps scientists and engineers build and manage real-life data science projects. Metaflow was originally developed at Netflix to boost productivity of data scientists who work on a wide variety of projects from classical statistics to state-of-the-art deep learning.

[Prophet](https://facebook.github.io/prophet) is a procedure for forecasting time series data based on an additive model where non-linear trends are fit with yearly, weekly, and daily seasonality, plus holiday effects. It works best with time series that have strong seasonal effects and several seasons of historical data.

[LightGBM](https://lightgbm.readthedocs.io/) is a gradient boosting framework that uses tree based learning algorithms, used for ranking, classification and many other machine learning tasks.

[Dash](https://plotly.com/dash) is a Python framework for building analytical web applications in Python, R, Julia, and Jupyter.

[MLR](https://mlr.mlr-org.com/) is Machine Learning in R.

[ML workspace](https://github.com/ml-tooling/ml-workspace) is an all-in-one web-based IDE specialized for machine learning and data science. It is simple to deploy and gets you started within minutes to productively built ML solutions on your own machines. ML workspace is the ultimate tool for developers preloaded with a variety of popular data science libraries (Tensorflow, PyTorch, Keras, and MXnet) and dev tools (Jupyter, VS Code, and Tensorboard) perfectly configured, optimized, and integrated.

[CatBoost](https://catboost.ai/) is a fast, scalable, high performance Gradient Boosting on Decision Trees library, used for ranking, classification, regression and other machine learning tasks for Python, R, Java, C++. Supports computation on CPU and GPU.

[Plumber](https://www.rplumber.io/) is a tool that allows you to create a web API by merely decorating your existing R source code with special comments.

[Drake](https://docs.ropensci.org/drake) is an R-focused pipeline toolkit for reproducibility and high-performance computing.

[DiagrammeR](https://visualizers.co/diagrammer/) is a package you can create, modify, analyze, and visualize network graph diagrams. The output can be incorporated into R Markdown documents, integrated with Shiny web apps, converted to other graph formats, or exported as image files.

[Knitr](https://yihui.org/knitr/) is a general-purpose literate programming engine in R, with lightweight API's designed to give users full control of the output without heavy coding work.

[Broom](https://broom.tidymodels.org/) is a tool that converts statistical analysis objects from R into tidy format.


## Contribute

- [x] If would you like to contribute to this guide simply make a [Pull Request](https://github.com/mikeroyal/ISP-Guide/pulls).


## License

[Back to the Top](https://github.com/mikeroyal/ISP-Guide#table-of-contents)

Distributed under the [Creative Commons Attribution 4.0 International (CC BY 4.0) Public License](https://creativecommons.org/licenses/by/4.0/).

