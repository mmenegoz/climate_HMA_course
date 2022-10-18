#!/bash
# Download the CRU data from a temporary FileSender archive.
# The link is found by downloading it with a browser, then in Download, right-click on the data and copy download URL.
# See https://www.forbesconrad.com/blog/download-wetransfer-to-linux-server-wget/

wget --user-agent Mozilla/4.0 '' -O HMA_data.tgz
tar xzvf HMA_data.tgz
rm HMA_data.tgz
