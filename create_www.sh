rm -r www
sphinx-build -b html source www
sh create_epub.sh
mkdir www/data
mv ebook/estspolenk.epub www/data/sest-spolecniku-hanpari.epub