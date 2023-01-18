#!/bash
# Download the CRU data from a temporary FileSender archive.
# The link is found by downloading it with a browser, then in Download, right-click on the data and copy download URL.
# See https://www.forbesconrad.com/blog/download-wetransfer-to-linux-server-wget/

wget -U Mozilla/5.0 'https://filesender.renater.fr/?s=download&token=42e674b9-ab1a-4ec8-b463-53eafdd5e588' -O HMA_cru_ts4.06.1901.2021.tmp.dat.nc.gz
wget -U Mozilla/5.0 'https://filesender.renater.fr/?s=download&token=e28cefb8-91e5-48c2-a538-b1a3c5193311' -O elev.0.25-deg.nc
mkdir -p data
mv elev.0.25-deg.nc data/.
gunzip HMA_cru_ts4.06.1901.2021.tmp.dat.nc.gz
mv HMA_cru_ts4.06.1901.2021.tmp.dat.nc data/.
