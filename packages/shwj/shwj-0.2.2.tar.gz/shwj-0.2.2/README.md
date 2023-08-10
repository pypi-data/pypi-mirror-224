# pypi_utils_4_shwj
我发现把常用的utils打包成库文件就十分方便

使用
````
python setup.py sdist bdist_wheel
pip install dist/shwj
````

## environment
这部分库是为了打印环境 使用sys和platform两个原生库
## plot
为了绘制简单
## audio
和音频处理相关的函数 需要用到librosa
## torch_utils