#!/bash
# Download the CRU, IPSL and GMTED2010 data from a cloud archive.
# The link is found by downloading it with a browser, then in Download, right-click on the data and copy download URL.
# See https://www.forbesconrad.com/blog/download-wetransfer-to-linux-server-wget/

#wget -U Mozilla/5.0 'https://cloud.univ-grenoble-alpes.fr/remote.php/webdav/2023_TU_winter_school/Data/05_climate/CRU/HMA_cru_ts4.06.1901.2021.tmp.dat.nc' -O CRU/HMA_cru_ts4.06.1901.2021.tmp.dat.nc
#wget -U Mozilla/5.0 'https://cloud.univ-grenoble-alpes.fr/remote.php/webdav/2023_TU_winter_school/Data/05_climate/IPSL_r1i1p1f1/HMA_tas_Amon_IPSL-CM6A-LR_ssp245_r1i1p1f1_gr_201501-210012.nc' -O HMA_tas_Amon_IPSL-CM6A-LR_ssp245_r1i1p1f1_gr_201501-210012.nc
#wget -U Mozilla/5.0 'https://cloud.univ-grenoble-alpes.fr/remote.php/webdav/2023_TU_winter_school/Data/05_climate/IPSL_r1i1p1f1/HMA_tas_Amon_IPSL-CM6A-LR_historical_r1i1p1f1_gr_185001-201412.nc' -O HMA_tas_Amon_IPSL-CM6A-LR_historical_r1i1p1f1_gr_185001-201412.nc
#wget -U Mozilla/5.0 'https://cloud.univ-grenoble-alpes.fr/remote.php/webdav/2023_TU_winter_school/Data/03_dem/GMTED2010/GMTED2010_15n060_0250deg.nc' -O GMTED2010_15n060_0250deg.nc

wget -U Mozilla/5.0 'https://drive.google.com/file/d/13l6HHYdBtPPp_t2aQ1qh7pHoxVdQDhea/view?usp=drive_link' HMA_cru_ts4.06.1901.2021.tmp.dat.nc.gz

mkdir -p data
#mv *nc data/.
gunzip HMA_cru_ts4.06.1901.2021.tmp.dat.nc.gz
mv HMA_cru_ts4.06.1901.2021.tmp.dat.nc data/.
