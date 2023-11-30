<!-- #region -->
# Climate_HMA_course

Computing climate trends of surface temperature in the Himalaya Mountain Area with observations and General Circulation Model (GCM) outputs over the last century and in future projections.

This folder contain the french course from Martin Ménégoz, about climate modelling activities over mountainous areas, with a focus on High-Mountain Asia.

**General description of this github repository:**

You can download this repository by using the commande git clone https://github.com/mmenegoz/climate_HMA_course.git

1. Document of the course: menegoz_climate_models_nepal_2023.pdf

2. A Script to do the training, aiming at computing temperature trends in HMA: HMA_climate_trends_CRU.ipynb

See the sections below to download the data, install your environment and run the script

Steps during the 13/12/2023 training:
-------------------------------------

2.1 Launch and run the script HMA_climate_trends_CRU.ipynb

2.2 Copy this script and adapt it yourself to compute tas trend over historical (1850-2014) and futur (2014-2020) periods


3. Data (downloadable on the UGA cloud).

The data used in this training is:

* The CRU temperature gridded observational dataset (1901-2021).
* IPSL experiments: one historical simulation over 1850-2014 and one projection over 2014-2100 under SSP2-45 scenario. Only one member (r1i1p1f1) is provided here from a 32-member ensemble experiment.
* Surface elevation data estimated from GMTED2010.

Documentation and repositories related to these data are described below.

*CRU temperature dataset*

A subset of the data over HMA can be downloaded on the [UGA cloud climate repository](https://cloud.univ-grenoble-alpes.fr/apps/files/?dir=/2023_TU_winter_school/Data/05_climate/CRU&fileid=792557848) in the file HMA_cru_ts4.06.1901.2021.tmp.dat.nc

The Origina data globally available can be downloaded at: https://crudata.uea.ac.uk/cru/data/hrg/cru_ts_4.06/cruts.2205201912.v4.06/tmp/cru_ts4.06.1901.2021.tmp.dat.nc.gz (October 2022)

*Topography data (global data)*

[UGA cloud dem GEMTED repository](https://cloud.univ-grenoble-alpes.fr/apps/files/?dir=/2023_TU_winter_school/Data/03_dem/GMTED2010&fileid=792549724), original data available at [GMTED2010](https://www.temis.nl/data/gmted2010/index.php) (December 2023)

*IPSL GCM experiments; temperature data (tas)*

The IPSL-CM6A-LR model have been used to simulate the global climate system over 1850-2014 (historical experiment) and in future projections extended unntil 2100 and following different emission scenarios. The model is described in Boucher et al. (2020, available [online](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2019MS002010)). Here, one subset extracted over HMA is available for the historical period and in one future projection available over 2014-20100 under the SSP2_45 scenario. For this short training, only one member is provided (r1i1p1f1), availablefor in two files for the two experiments on the [UGA cloud climate data IPSL repository](https://cloud.univ-grenoble-alpes.fr/apps/files/?dir=/2023_TU_winter_school/Data/05_climate/IPSL_r1i1p1f1&fileid=792576253):

HMA_tas_Amon_IPSL-CM6A-LR_historical_r1i1p1f1_gr_185001-201412.nc
HMA_tas_Amon_IPSL-CM6A-LR_ssp245_r1i1p1f1_gr_201501-210012.nc

Please, consider that the original data is a 32-member ensemble experiment than can be used to investigate the uncertainties related to climate internal variability inherent to the global climate system.

4. Python environment and main packages

To install the environement on your machine, you can do it with:

mamba env create -f environment_2023.yml

or alternatively with

conda env create -f environment_2023.yml

Then, activate your environment. Some details about conda environments and python packages used in this tutorial are described below.

**Python environement details**

- [xarray](http://xarray.pydata.org/en/stable/): is an open-source project and Python package that makes working with labelled multi-dimensional arrays simple, efficient, and fun! ([Xarray Tutorial](https://xarray-contrib.github.io/xarray-tutorial/) / [Xarray | SciPy 2020](https://www.youtube.com/watch?v=mecN-Ph_-78&list=PLYx7XA2nY5Gde-6QO98KUJ9iL_WW4rgYf&index=4))
- [jupyter](https://jupyter.org/): for using jupyter-notebook / lab
- [matplotlib](https://matplotlib.org/): back-end for making plots
- [cartopy](https://scitools.org.uk/cartopy/docs/latest/): replace basemap, back-end for map projections
- [proplot](https://proplot.readthedocs.io/en/stable/): a lightweight matplotlib wrapper for making beautiful, publication-quality graphics (still in development)

If you want to install an environment on your machine, you can do it directly by typing the command conda env create -f environment_2023.yml (or alternatively with mamba) using the environment file environment_2023.yml from this repository. You need to have Anaconda or Minconda already pre-installed on your machine. For managing your conda environments always come back to the official documentation: https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file.

The package versions can be found in the environment.yml file. Be careful if you want to upgrade this environment, because there are often conflicts between some packages (e.g., version 0.6.4 of proplot does not work with version 3.3 of matplotlib, or cartopy does not work with the latest version 3.9 of python... but this can have already evolved at the time of this session). Be particularly careful with Proplot which is a package under development and which evolves very quickly, including changes of syntax, thus refer to version 0.6.4 for these practical works: https://proplot.readthedocs.io/en/v0.6.4/.

Some issues related with this environment:

    Proplot colormaps: https://github.com/lukelbd/proplot/issues/123
    Proplot colorbar: https://github.com/lukelbd/proplot/issues/124
<!-- #endregion -->
