
#### Patch del comando DD

$$\text{dc3dd if= /dev/sda ofs=/mnt/dest/dd\_image/sda.000 ofsz=2G bufsz=2k hash=md5}$$
  
  
- OFS= output diviso in più file (in sda.000).
- OFSZ= dimensione massima dei file (2gb).
- BUFSZ= BS = blocksize in byte (512 default) (dimensione 2048byte).
- HASH= \[ MD5 | SHA1 | SHA256 | SHA512 ] calcola dell'Hash indicato \[**MD5 e SHA256**].
- LOG = salva il report dell' elaborazione in un file \[sda.log].
- VERB=ON indica di generare un report dettagliato (verbose).
	

