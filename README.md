<!-- #region -->
# M2_climat_MAR
Computing climate trends in the Himalaya Mountain Area with the CRU temperature dataset

This folder contain the french course from Martin Ménégoz, about climate modelling activities over mountainous areas.

The students can use this binder session to create a python notebook to compute seasonal trends of temperature, using the data available at:

**Temperature data: https://crudata.uea.ac.uk/cru/data/hrg/cru_ts_4.06/cruts.2205201912.v4.06/tmp/cru_ts4.06.1901.2021.tmp.dat.nc.gz** (October 2022)

**Topography data: [http://research.jisao.washington.edu/data_sets/elevation/](http://research.jisao.washington.edu/data_sets/elevation/elev.0.25-deg.nc)** (October 2022)

[![Binder](https://mybinder.org/badge_logo.svg)]https://hub.gke2.mybinder.org/user/mmenegoz-climate_hma_course-genqi7jk/doc/tree/HMA_climate_trends.ipynb

1. General description:

Downloading CRU data to investigate climate trends over the HMA.
For this we will use several classic Python packages:

    xarray: is an open-source project and Python package that makes working with labelled multi-dimensional arrays simple, efficient, and fun! (Xarray Tutorial / Xarray | SciPy 2020)
    jupyter: for using jupyter-notebook / lab
    matplotlib: back-end for making plots
    cartopy: replace basemap, back-end for map projections
    proplot: a lightweight matplotlib wrapper for making beautiful, publication-quality graphics (still in development)

Check the Environment section at the end of this README if you want to know more about the environment and/or to install it on your local machine.

2. Script

HMA_climate_trends.ipynb is a basic script from which you can start working on the CRU data with python libraries.

The package https://zenodo.org/record/4458780#.YeSjVGAo_OQ could be used to compute the statistical significance of the trends with the Mann Kendall criteria with more efficiency.

3. Environment

Note that we will be working with an already pre-installed environment with binder. If you want to install the same environment on your machine, you can do it directly by typing the command conda env create -f environment.yml using the environment file environment.yml from this repository. You need to have Anaconda or Minconda already pre-installed on your machine. If not, for Linux users, you can check this (steps 2, 3, and 4; the rest is to install it on a server — to adapt for non-Linux machines): https://mickaellalande.github.io/post/tutorial/how-to-install-jupyter-notebook-on-a-server/. For managing your conda environments always come back to the official documentation: https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file.

The package versions can be found in the environment.yml file. Be careful if you want to upgrade this environment, because there are often conflicts between some packages (e.g., version 0.6.4 of proplot does not work with version 3.3 of matplotlib, or cartopy does not work with the latest version 3.9 of python... but this can have already evolved at the time of this session). Be particularly careful with Proplot which is a package under development and which evolves very quickly, including changes of syntax, thus refer to version 0.6.4 for these practical works: https://proplot.readthedocs.io/en/v0.6.4/.

Some issues related with this environment:

    Proplot colormaps: https://github.com/lukelbd/proplot/issues/123
    Proplot colorbar: https://github.com/lukelbd/proplot/issues/124
<!-- #endregion -->
