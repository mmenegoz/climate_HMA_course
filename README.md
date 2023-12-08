<!-- #region -->
# Climate_HMA_course, Katmandhu, December 2023

Computing climate trends of surface temperature in the Himalaya Mountain Area with observations and General Circulation Model (GCM) outputs over the last century and in future projections.

This folder contain the french course from Martin Ménégoz, about climate modelling activities over mountainous areas, with a focus on High-Mountain Asia.

You can download this repository by using the commande git clone https://github.com/mmenegoz/climate_HMA_course.git

**General description of the files available for this course**

* This README.md file descibing yhe content of the course as well as the steps of the training.

* Document of the course: menegoz_climate_models_nepal_2023.pdf

* A training script: HMA_climate_trends_CRU.ipynb (with a *py version of the script)

This script allows to compute temperature trends in HMA. See the sections below to discover the data, install your python environment and run the script

* A python environment file common with the other sessions: environment.yml

-----------------------------------------------------------------------

Steps during the 13/12/2023 training:
-------------------------------------

1. Copy the three datasets described below on your machine.

2. Create your python environment (or use those that you got from the previous python sessions), and activate this environment before launching the notebook (either with jupyter-notebook or jupyter-lab)

3. Launch and run the script HMA_climate_trends_CRU.ipynb

4. Make one or several copies of this script and adapt it/them yourself to compute temperature trend over historical (1850-2014) and futur (2014-2020) periods with the IPSL GCM outputs (variable tas)

You will need to change the names of some files/variables and to adapt the date corresponding to the new dataset.

-----------------------------------------------------------------------

**Data**

The 3 datasets used in this training are :

* The CRU temperature gridded observational dataset (1901-2021)
* Surface elevation data estimated from GMTED2010.
* IPSL experiments: one historical simulation over 1850-2014 and one projection over 2014-2100 under SSP2-45 scenario. Only one member (r1i1p1f1) is provided here from a 32-member ensemble experiment.

Documentation and repositories related to these data are described below.

*CRU temperature dataset*

A subset of the CRU data over HMA is provided in the file HMA_cru_ts4.06.1901.2021.tmp.dat.nc

The Origina data globally available can be downloaded at: https://crudata.uea.ac.uk/cru/data/hrg/cru_ts_4.06/cruts.2205201912.v4.06/tmp/cru_ts4.06.1901.2021.tmp.dat.nc.gz (October 2022)

*Topography data (global data)*

The file GMTED2010_15n060_0250deg.nc is a topography global dataset at 0.25° resolution. The original data is available at [GMTED2010](https://www.temis.nl/data/gmted2010/index.php) (December 2023)

*IPSL GCM experiments; temperature data (tas)*

The IPSL-CM6A-LR model have been used to simulate the global climate system over 1850-2014 (historical experiment) and in future projections extended unntil 2100 and following different emission scenarios. The model is described in Boucher et al. (2020, available [online](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2019MS002010)). Here, one subset extracted over HMA is available for the historical period and in one future projection available over 2014-20100 under the SSP2_45 scenario. For this short training, only one member is provided (r1i1p1f1), availablefor in two files for the two experiments on the [UGA cloud climate data IPSL repository](https://cloud.univ-grenoble-alpes.fr/apps/files/?dir=/2023_TU_winter_school/Data/05_climate/IPSL_r1i1p1f1&fileid=792576253):

HMA_tas_Amon_IPSL-CM6A-LR_historical_r1i1p1f1_gr_185001-201412.nc

HMA_tas_Amon_IPSL-CM6A-LR_ssp245_r1i1p1f1_gr_201501-210012.nc

Please, consider that the original data is a 32-member ensemble experiment than can be used to investigate the uncertainties related to climate internal variability inherent to the global climate system.

-----------------------------------------------------------------------

**Python environment and main packages**

*Commands*

To check existing environments

	conda info --envs

To install the environement on your machine, you can do it with:

	mamba env create -f environment.yml

or alternatively with

	conda env create -f environment.yml

Then, activate your environment. Some details about conda environments and python packages used in this tutorial are described below.

*Python packages*

- [xarray](http://xarray.pydata.org/en/stable/): is an open-source project and Python package that makes working with labelled multi-dimensional arrays simple, efficient, and fun! ([Xarray Tutorial](https://xarray-contrib.github.io/xarray-tutorial/) / [Xarray | SciPy 2020](https://www.youtube.com/watch?v=mecN-Ph_-78&list=PLYx7XA2nY5Gde-6QO98KUJ9iL_WW4rgYf&index=4))
- [jupyter](https://jupyter.org/): for using jupyter-notebook / lab
- [matplotlib](https://matplotlib.org/): back-end for making plots
- [cartopy](https://scitools.org.uk/cartopy/docs/latest/): replace basemap, back-end for map projections
- [proplot](https://proplot.readthedocs.io/en/stable/): a lightweight matplotlib wrapper for making beautiful, publication-quality graphics (still in development)

You need to have Anaconda or Minconda already pre-installed on your machine. For managing your conda environments always come back to the official documentation: https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file.

The package versions have not been set in the environment.yml file. Be careful if you want to upgrade this environment, because you can get conflicts between some packages (e.g., version 0.6.4 of proplot does not work with version 3.3 of matplotlib, or cartopy does not work with the version 3.9 of python... but this can have already evolved at the time of this session). Be particularly careful with Proplot which is a package under development and which evolves very quickly, including changes of syntax, thus refer to version 0.6.4 for these practical works: https://proplot.readthedocs.io/en/v0.6.4/.

<!-- #endregion -->
