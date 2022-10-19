<!-- #region -->
# Climate_HMA_course

Computing climate trends in the Himalaya Mountain Area with the CRU temperature dataset

This folder contain the french course from Martin Ménégoz, about climate modelling activities over mountainous areas.

The students can use this binder session to create a python notebook to compute seasonal trends of temperature, just clicking there:

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/mmenegoz/climate_HMA_course/HEAD)

If you want to run the script on your own machine, you can download the github repository, and use the script *ipynb (or *py if you prefer).

Then, you can download the data available at:

**Reduced version of the CRU dataset: https://filesender.renater.fr/?s=download&token=1f0c251e-096f-4038-b5c0-4f3a7b10f46c** (available until November, the 3rd)

**Surface elevation dataset: https://filesender.renater.fr/?s=download&token=c274a574-1116-44d7-878d-b74e33258f3d** (available until November, the 3rd)

The Origina data globally available can be downloaded at:

Temperature data: https://crudata.uea.ac.uk/cru/data/hrg/cru_ts_4.06/cruts.2205201912.v4.06/tmp/cru_ts4.06.1901.2021.tmp.dat.nc.gz (October 2022)

Topography data: [http://research.jisao.washington.edu/data_sets/elevation/](http://research.jisao.washington.edu/data_sets/elevation/elev.0.25-deg.nc) (October 2022)

**General description of this github repository:**

1. Python packages

- [xarray](http://xarray.pydata.org/en/stable/): is an open-source project and Python package that makes working with labelled multi-dimensional arrays simple, efficient, and fun! ([Xarray Tutorial](https://xarray-contrib.github.io/xarray-tutorial/) / [Xarray | SciPy 2020](https://www.youtube.com/watch?v=mecN-Ph_-78&list=PLYx7XA2nY5Gde-6QO98KUJ9iL_WW4rgYf&index=4))
- [jupyter](https://jupyter.org/): for using jupyter-notebook / lab
- [matplotlib](https://matplotlib.org/): back-end for making plots
- [cartopy](https://scitools.org.uk/cartopy/docs/latest/): replace basemap, back-end for map projections
- [proplot](https://proplot.readthedocs.io/en/stable/): a lightweight matplotlib wrapper for making beautiful, publication-quality graphics (still in development)

Check the Environment section at the end of this README if you want to know more about the environment and/or to install it on your local machine.

2. Script

HMA_climate_trends.ipynb is a basic script from which you can start working on the CRU data with python libraries.

3. Environment

Note that we will be working with an already pre-installed environment with binder. If you want to install the same environment on your machine, you can do it directly by typing the command conda env create -f environment.yml using the environment file environment.yml from this repository. You need to have Anaconda or Minconda already pre-installed on your machine. If not, for Linux users, you can check this (steps 2, 3, and 4; the rest is to install it on a server — to adapt for non-Linux machines): https://mickaellalande.github.io/post/tutorial/how-to-install-jupyter-notebook-on-a-server/. For managing your conda environments always come back to the official documentation: https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file.

The package versions can be found in the environment.yml file. Be careful if you want to upgrade this environment, because there are often conflicts between some packages (e.g., version 0.6.4 of proplot does not work with version 3.3 of matplotlib, or cartopy does not work with the latest version 3.9 of python... but this can have already evolved at the time of this session). Be particularly careful with Proplot which is a package under development and which evolves very quickly, including changes of syntax, thus refer to version 0.6.4 for these practical works: https://proplot.readthedocs.io/en/v0.6.4/.

Some issues related with this environment:

    Proplot colormaps: https://github.com/lukelbd/proplot/issues/123
    Proplot colorbar: https://github.com/lukelbd/proplot/issues/124
<!-- #endregion -->
