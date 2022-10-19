#!/bash
# Download the CRU data from a temporary FileSender archive.
# The link is found by downloading it with a browser, then in Download, right-click on the data and copy download URL.
# See https://www.forbesconrad.com/blog/download-wetransfer-to-linux-server-wget/

wget --user-agent Mozilla/4.0 'https://filesender.renater.fr/?s=download&token=1f0c251e-096f-4038-b5c0-4f3a7b10f46c/HMA_cru_ts4.06.1901.2021.tmp.dat.nc' -O HMA_cru_ts4.06.1901.2021.tmp.dat.nc.gz
gunzip HMA_cru_ts4.06.1901.2021.tmp.dat.nc.gz
wget --user-agent Mozilla/4.0 'https://filesender.renater.fr/?s=download&token=c274a574-1116-44d7-878d-b74e33258f3d' -O elev.0.25-deg.nc
mkdir -p data
mv elev.0.25-deg.nc data/.
mv HMA_cru_ts4.06.1901.2021.tmp.dat.nc data/.
