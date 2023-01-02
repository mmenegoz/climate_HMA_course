#!/bash
# Download the CRU data from a temporary FileSender archive.
# The link is found by downloading it with a browser, then in Download, right-click on the data and copy download URL.
# See https://www.forbesconrad.com/blog/download-wetransfer-to-linux-server-wget/

wget -U Mozilla/5.0 'https://filesender.renater.fr/download.php?token=0c9741dd-cb6f-4a4e-8bae-37ca24a93f09&files_ids=20570999' -O HMA_cru_ts4.06.1901.2021.tmp.dat.nc.gz
wget -U Mozilla/5.0 'https://filesender.renater.fr/download.php?token=863294df-3c3f-40d8-945a-55400710e8dc&files_ids=20570949' -O elev.0.25-deg.nc
mkdir -p data
mv elev.0.25-deg.nc data/.
gunzip HMA_cru_ts4.06.1901.2021.tmp.dat.nc.gz
mv HMA_cru_ts4.06.1901.2021.tmp.dat.nc data/.
