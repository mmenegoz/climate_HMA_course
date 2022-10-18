# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.0
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# **High-Mountain Asia climate analysis based on gridded observations**
#
# **Katmandhu course, October, 2022**
#
# Topography, temperature

# **1. Environment**

# +
# To reload external files automatically (ex: utils)
# %load_ext autoreload
# %autoreload 2

import xarray as xr
import pandas as pd
import numpy as np
import calendar as cld
import matplotlib.pyplot as plt
import proplot as plot # New plot library (https://proplot.readthedocs.io/en/latest/)
plot.rc['savefig.dpi'] = 300 # 1200 is too big! #https://proplot.readthedocs.io/en/latest/basics.html#Creating-figures
from scipy import stats

# Import some extra functions from utils folder
import sys
sys.path.insert(1, 'utils') # to include the util directory
import utils as u # my personal functions
u.check_python_version()
u.check_virtual_memory()

# Library not used here
#import dask
#import xesmf as xe # For regridding (https://xesmf.readthedocs.io/en/latest/)
#from scipy.interpolate import griddata # Other package for regridding
# -

# Where are the data files?
path="/Users/mmenegoz/cours/nepal_2022/"

# Domain study
lon1=60;lon2=110
lat1=25;lat2=45


# function for seasonal mean
def season_mean(ds, calendar="standard"):
    # Make a DataArray with the number of days in each month, size = len(time)
    month_length = ds.time.dt.days_in_month

    # Calculate the weights by grouping by 'time.season'
    weights = (
        month_length.groupby("time.season") / month_length.groupby("time.season").sum()
    )

    # Test that the sum of the weights for each season is 1.0
    np.testing.assert_allclose(weights.groupby("time.season").sum().values, np.ones(4))

    # Calculate the weighted average
    return (ds * weights).groupby("time.season").sum(dim="time")


# **2. Open temperature data file (CRU)**

# CRU dataset (https://crudata.uea.ac.uk/cru/data/hrg/cru_ts_4.06/cruts.2205201912.v4.06/tmp/cru_ts4.06.1901.2021.tmp.dat.nc.gz)
# https://www.nature.com/articles/s41597-020-0453-3
file='cru_ts4.06.1901.2021.tmp.dat.nc'
ds = xr.open_dataset(path+file)
ds

# **3. Extracting regional data and computing seasonal means**

# Extracting the data over HMA
longitudes=slice(lon1,lon2)
latitudes=slice(lat1,lat2)
temp_HMA=ds.sel(lat=latitudes,lon=longitudes)
temp_HMA

# Computing seasonal mean and ordering properly the seasons
seasonal_mean=season_mean(temp_HMA.tmp).sortby(xr.DataArray(['DJF','MAM','JJA', 'SON'],dims=['season']))

seasonal_mean.shape

# Levels of temperature for the plot
levels=np.arange(-26,28,2)

# +
# Producing the map of the seasonal mean, excluding the borders of the domain.
f, axs = plot.subplots(proj='cyl',ncols=2, nrows=2, share=1, axwidth=5)
for i, ax in enumerate(axs):
    print('i='+str(i))
    print('ax='+str(ax))
    m = ax.pcolormesh(
        temp_HMA.lon,temp_HMA.lat,
        seasonal_mean[i,:,:],
        levels=levels,
        cmap='coolwarm'
    )
    ax.format(title=seasonal_mean.season.data[i],large='20px')
    
f.colorbar(m, label= '°C')

axs.format(
    geogridlinewidth=0.1, geogridcolor='gray8', geogridalpha=0.5, labels=True, 
    coast=True, ocean=False, oceancolor='gray3', borders=True,
    suptitle="Seasonal mean of temperature, CRU observations",
    lonlines=4, latlines=4, abc=False, latlim=[lat1,lat2],lonlim=[lon1,lon2]
)
# -

# **4. Trends**
#
# Choose the period that you want!

# Period over which computing the trends
date1="1901-01"; date2="2021-12"
date3="2022-12" # One year after date2
dates=pd.date_range(start=date1, end=date3, freq='Y')
dates.year

# Extract seasonal timeseries
Temp=temp_HMA.tmp.sel(time=slice(date1,date2))

# **4.1 Check the trend and its level of significance in the location of your choice**

# location study
lon_loc=87; lat_loc=28 # Everest location!!!
#lon_loc=84; lat_loc=28
#lon_loc2=72; lat_loc2=32

# Extraction of the data at the point
temp_loc=Temp.sel(lon=lon_loc, lat=lat_loc, method="nearest")
#temp_loc2=Temp.sel(lon=lon_loc2, lat=lat_loc2, method="nearest")

# Creating an empty array with the seasonal data
seasonal_T_loc=np.empty(shape=(int(temp_loc.shape[0]/12),4), dtype=float)
seasonal_T_loc.shape

# Seasonal spatial data
seasonal_T_loc [:,0] = temp_loc.where(Temp['time.season'] == 'DJF').groupby('time.year').mean(dim='time')
seasonal_T_loc [:,1] = temp_loc.where(Temp['time.season'] == 'MAM').groupby('time.year').mean(dim='time')
seasonal_T_loc [:,2] = temp_loc.where(Temp['time.season'] == 'JJA').groupby('time.year').mean(dim='time')
seasonal_T_loc [:,3] = temp_loc.where(Temp['time.season'] == 'SON').groupby('time.year').mean(dim='time')

# Computing trends
slope_T_loc=np.full(seasonal_T_loc.shape[1:4],np.nan)
pvalue_T_loc=np.full(seasonal_T_loc.shape[1:4],np.nan)
intercept_T_loc=np.full(seasonal_T_loc.shape[1:4],np.nan)
for season in range(4):
    linregress_T_loc = stats.linregress(range(seasonal_T_loc.shape[0]-1), seasonal_T_loc[1:,season])
    slope_T_loc[season] = linregress_T_loc.slope
    intercept_T_loc[season] = linregress_T_loc.intercept
    pvalue_T_loc[season] = linregress_T_loc.pvalue

seasonal_T_loc.shape

index=np.arange(0,dates.shape[0])
index.shape

# +
#Plotting temperature timeseries
f, axs = plot.subplots(ncols=2, nrows=2)
for i, ax in enumerate(axs):
    print('i='+str(i))
    print('ax='+str(ax))
    if pvalue_T_loc[i]<0.05:
        signif='solid'
    else:
        signif='dashed'
    m = ax.scatter(dates,seasonal_T_loc[:,i]-np.mean(seasonal_T_loc[:,i]))
    m = ax.plot(dates,intercept_T_loc[i]+slope_T_loc[i]*index-np.mean(seasonal_T_loc[:,i]),linestyle=signif)
    ax.format(title=seasonal_mean.season.data[i]+' trend='+str(round(slope_T_loc[i]*10,2))+'°C.decade-1; '+'pvalue='+str(round(pvalue_T_loc[i],3)),large='10px')

axs.format(
    suptitle='Seasonal temperature at lon='+str(lon_loc)+' lat='+str(lat_loc),
    xlabel='year',
    ylabel='temperature anomaly'
)
# -

# **4.2. HMA trend maps**

# Getting the total number of years
int(Temp.shape[0]/12)

# Creating an empty array with the total seasonal data
seasonal_T=np.empty(shape=(int(Temp.shape[0]/12),4,Temp.shape[1],Temp.shape[2]), dtype=float)
seasonal_T.shape

Temp.where(Temp['time.season'] == 'DJF').groupby('time.year').mean(dim='time').shape

# Seasonal spatial data
seasonal_T [:,0,:,:] = Temp.where(Temp['time.season'] == 'DJF').groupby('time.year').mean(dim='time')
seasonal_T [:,1,:,:] = Temp.where(Temp['time.season'] == 'MAM').groupby('time.year').mean(dim='time')
seasonal_T [:,2,:,:] = Temp.where(Temp['time.season'] == 'JJA').groupby('time.year').mean(dim='time')
seasonal_T [:,3,:,:] = Temp.where(Temp['time.season'] == 'SON').groupby('time.year').mean(dim='time')

# Computing trends
slope_T=np.full(seasonal_T.shape[1:4],np.nan)
pvalue_T=np.full(seasonal_T.shape[1:4],np.nan)
for lon in range(seasonal_T.shape[3]):
    print('longitude='+str(lon)+'/'+str(seasonal_T.shape[3]))
    for lat in range(seasonal_T.shape[2]):
        for season in range(4):
            linregress_T = stats.linregress(range(seasonal_T.shape[0]-1), seasonal_T[1:,season,lat,lon])
            slope_T[season][lat][lon] = linregress_T.slope
            pvalue_T[season][lat][lon] = linregress_T.pvalue

# Masking non-significative signals
signif=np.where(pvalue_T<0.05,True,False)

# Levels of temperature for the plot
levels=np.arange(-0.5,0.5,0.05)
factor=10 # degree per decade

# +
# Producing the map of the trends, excluding the borders of the domain.
f, axs = plot.subplots(proj='cyl',ncols=2, nrows=2, share=1, axwidth=5)
for i, ax in enumerate(axs):
    print('i='+str(i))
    print('ax='+str(ax))
    m = ax.pcolormesh(
        temp_HMA.lon,temp_HMA.lat,
        slope_T[i,:,:]*factor,
        levels=levels,
        cmap='coolwarm'
    )
    ax.format(title=seasonal_mean.season.data[i],large='20px')
    
    p = ax.contourf(
    temp_HMA.lon,temp_HMA.lat,
    signif[i,:,:],
    hatches=["", "."], alpha=0
    )
    
f.colorbar(m, label= '°C')

axs.format(
    geogridlinewidth=0.1, geogridcolor='gray8', geogridalpha=0.5, labels=True, 
    coast=True, ocean=False, oceancolor='gray3', borders=True,
    suptitle="Seasonal trend of temperature, CRU dataset over "+date1+" - "+date2,
    lonlines=4, latlines=4, abc=False, latlim=[lat1,lat2],lonlim=[lon1,lon2]
)
# -

# **Now, you can invent your own analysis, e.g:**
# * Computing trends where you want and over any period.
# * Computing trends as a function of the elevation using the topography in the file below.
# * Etc...
#

# Topography at 0.25° (http://research.jisao.washington.edu/data_sets/elevation/)
# -> 0.25-degree latitude-longitude resolution elevation (TBASE)
file_topo="elev.0.25-deg.nc"
ds_topo = xr.open_dataset(path+file_topo)
ds_topo # ds_topo as dataset

# Extracting the data over HMA
# be careful to reversed latitudes in the original file
topo_HMA=ds_topo.isel(time=0).sel(lon=slice(lon1,lon2),lat=slice(lat2,lat1))

fig, ax = plt.subplots()
m=ax.pcolormesh(topo_HMA.lon,topo_HMA.lat,topo_HMA.data)
fig.colorbar(m,label= 'm.asl')
ax.set_title('Topography TBASE with a 0.25° resolution')

# Interpolation of the topography on the CRU grid
ds_topo_HMA_out=topo_HMA.interp(lat=temp_HMA.lat,lon=temp_HMA.lon)

fig, ax = plt.subplots()
m=ax.pcolormesh(ds_topo_HMA_out.lon,ds_topo_HMA_out.lat,ds_topo_HMA_out.data)
fig.colorbar(m,label= 'm.asl')
ax.set_title('Topography TBASE interpolated on a 0.5° resolution')

# Levels of temperature for the plot
#levels=np.arange(-0.5,0.5,0.05)
factor_trend=10 # degree per decade
bins=100
levels=np.logspace(0,1,25)

# We keep only the elevation area > limit m.asl
limit=1000
topo_high=ds_topo_HMA_out.data.where(ds_topo_HMA_out.data > limit)
trends_high=np.zeros(slope_T.shape)
for i in np.arange(4):
    trends_high[i,:,:]=np.where(ds_topo_HMA_out.data > limit,slope_T[i,:,:],np.nan)

fig, ax = plt.subplots()
m=ax.pcolormesh(topo_high)
fig.colorbar(m,label= 'm.asl')
ax.set_title('Topography TBASE interpolated on a 0.5° resolution, masking area above '+str(limit)+'m asl')

# +
#Plotting trends as a function of elevation
f, axs = plot.subplots(ncols=2, nrows=2,share=1)
for i, ax in enumerate(axs):
    print('i='+str(i))
    print('ax='+str(ax))
    m = ax.scatter(topo_high.values.flatten(),trends_high[i,:,:].flatten()*factor_trend,alpha=0.1)
    #m = ax.hist2d(topo_high.values.flatten(),trends_high[i,:,:].flatten()*factor_trend,bins=bins,cmap='Spectral_r',levels=levels,cmin=1)
    #m = ax.hist2d(ds_topo_HMA_out.data.values.flatten(),slope_T[i,:,:].flatten()*factor_trend,bins=bins,cmap='Spectral_r',levels=levels,cmin=1)
    #m = ax.scatter(ds_topo_HMA_out.data,slope_T[i,:,:]*factor_trend,alpha=0.1)
    ax.format(title=seasonal_mean.season.data[i],large='15px',ylim=(-0.05,0.25))

    #f.colorbar(m[3],ticks=np.logspace(0,1,2))    

axs.format(
    suptitle='Temperature trend as a function of the topography',
    xlabel='Elevation',
    ylabel='trends (°C.decade-1)',
    large='15px'
)
# -




