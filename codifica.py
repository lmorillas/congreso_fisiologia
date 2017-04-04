#/usr/bin/env python
# coding: utf-8

import os
import codecs

# traverse root directory, and list directories as dirs and files as files
for root, dirs, files in os.walk("output"):

	for file in files:
		if file.endswith('.html'):
			filename = os.path.join( root, file )
			print (filename)

			f = codecs.open( filename, encoding='utf-8')
			texto = f.read()
			f.close()
			f = codecs.open(filename, 'w', encoding='iso-8859-1')
			texto = texto.replace('<meta charset="UTF-8">', '<meta charset="ISO-8859-1">')

			f.write(texto)
			f.close()

