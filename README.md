# wrf-python
使用wrfout进行绘图练习
使用的库有numpy、matplotlib、netCDF4

read data 使用netCDF4的variables['Name'][:]方法

对数据进行插值，插值方法见： https://wiki.openwfm.org/wiki/How_to_interpret_WRF_variables
插值后统一了数据维度（39，59 ），39为z方向的格点数，59为x方向的格点数
potential temperature = T + 300K    T为扰动位温
H = （ph+phb）/9.81 真实高度为 （扰动位势+基态位势）/9.81

主要的绘图函数为plt.contourf(),plt.quiver(),
plt.contourf()，leves为一个列表，表示色带的范围，extend="both"，代表其余范围如何表示，cmap为可用plt.cm.bwr,自带的调色方案，colorbar添加色带，给colorbar一个变量名，
使用set_label设置色带的标签。
quiver（）函数，绘制风速矢量，quiverkey（）函数给定标准矢量，及其所在位置。

$^abc$  设置上标，$_sss$ 设置下表
