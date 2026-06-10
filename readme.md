<p align="center">
  <img src="images\CISP - CUDA Image Signal Processor.png" width="900">
</p>

A High-Performance GPU-accelerated Cuda based Image Signal Processor(ISP) that transforms RAW Bayer data to high quality RGB output. This is a modular pipeline with tunable parameter for each operation. CISP explores the parallel nature of image processing algorithms.


# Features 
- GPU accelerated modules
- End-to-end Bayer RAW to RGB image conversion.
- Real-time parameter tuning through a graphical user interface.
- Support for High-bit Depth images
- Hybrid CUDA/C++ and Python architecture combining GPU-accelerated performance with the flexibility of a Python-based workflow.

# ISP Operations Integrated

## Bayer Domain
* Defective pixel correction
* Lens Shading Correction
* Black Level Correction
* Automatic White Balance Gain Adjustment (Gray world assumption)
* De-Mosaicing
## RGB Domain
* Color Correction Matrix 
* Color Space Conversion to YCbCr
* Gamma Correction

## YCbCr Domain
### Tone and Color Adjustments
- Brightness
- Saturation
- Hue
- Tint
- Contrast
- Vibrance

### Image Enhancement
- Bilateral Filter
- Highboost filtering

# Tech Stack

- Cuda
- C++
- Python
- TKinter and TTKBootStrap (For Ui)
- Pybind11
- Rawpy
- numpy
- opencv ( For basic file operations )

# Data Flow
<p align="center">
  <img src="images\1.png" width="900">
</p>


# User Interface
<p align="center">
  <img src="images\ui.jpg" width="900">
</p>


# How To Use

clone repository : 
```bash
git clone https://github.com/mjithujanardhanan/CISP---Cuda-ISP-Pipeline.git
cd CISP---Cuda-ISP-Pipeline
pip install -r requirements.txt
```
app.exe executes the ISP application

### supported Formats

```bash
    ".dng", ".nef", ".nrw",
    ".cr2", ".cr3", ".crw",
    ".arw", ".raf", ".orf",
    ".rw2", ".pef", ".CR2"
 ```

input the path to the raw image and press enter to load. The toogle button can be used to activate and deactivate each block. Once the parameters are set click the run button to activate the pipeline. You can also save the processed image by clicking save.


### Files:
- app.exe       :: application
- app.py        :: UI code
- ISP.cu        :: Pipeline Code
- Sample_input  :: contains a few raw images for testing
- src           :: contains individual kernels for each operation

# Future work

- Guided Filter
- chroma denoising
- histogram equilization
- image compression

# References

1. Gonzalez, R. C., & Woods, R. E. *Digital Image Processing* (4th ed.). Pearson, 2018.
2. Szeliski, R. *Computer Vision: Algorithms and Applications* (2nd ed.). Springer, 2022.
3. Nayar, S. *First Principles of Computer Vision Specialization*. Columbia University, Coursera. Available at: https://www.coursera.org/specializations/firstprinciplesofcomputervision  PS.... check this out... its gold
4.  Holm, J. *Image Sensors and Signal Processing for Digital Still Cameras*. CRC Press, 2011.
5. Langseth, R., Gaddam, V. R., Stensland, H. K., Griwodz, C., Halvorsen, P., & Johansen, D. 
   *An Experimental Evaluation of Debayering Algorithms on GPUs for Recording Panoramic Video in Real-Time*. 
   International Journal of Multimedia Data Engineering and Management (IJMDEM), 6(3), 1–16, 2015.
   DOI: 10.4018/IJMDEM.2015070101
6. Huang, B.-C., & Fuh, C.-S.
   *Image Pipeline Algorithms for Standard Mobile Imaging Architecture Sensors*.
   Proceedings of the 18th IPPR Conference on Computer Vision, Graphics and Image Processing (CVGIP), Taipei, Taiwan, 2005.
7. NVIDIA Corporation. *CUDA C++ Best Practices Guide*. NVIDIA Developer Documentation. Available at: https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/
8. NVIDIA Corporation. *CUDA C++ Programming Guide*. NVIDIA Developer Documentation. Available at: https://docs.nvidia.com/cuda/cuda-c-programming-guide/
9. Kuo, K.-T. *openISP: Open Image Signal Processor*. GitHub repository. Available at: https://github.com/cruxopen/openISP
10. AI Plays. *AI Plays YouTube Channel*. YouTube. Available at: https://www.youtube.com/@AISpeedrunners