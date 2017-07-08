import argparse
import urllib.request as u
parser = argparse.ArgumentParser(description="descarga fracciones de video de xvideos")
parser.add_argument('--video', help='url del video')
parser.add_argument('--rf', help="rango final")
parser.add_argument('--nombre', help="nombre del video")
args = parser.parse_args()

with open(args.nombre,"ab") as v:
	for parte in range(1,int(args.rf) + 1):
		url = str(args.video) + str(parte) + ".ts"
		video = u.urlopen(url)
		v.write(video.read())
