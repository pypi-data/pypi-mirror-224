#!/usr/bin/env python3

import argparse
from . import main
from . import args	

if __name__ == '__main__':

	parser = argparse.ArgumentParser(description='This is CLI for simple paragraph recoginitive based on morphological operator')
		
	parser.add_argument('--image', type=str, help="""Entrer l\'image de que tu souhaite reconnaitre""")

	parser.add_argument('--image_reco', type=str, help="""enter le nom de l\'image une fois reconnu""")
		
	args = parser.parse_args()
	
	main(args.image, args.image_reco)
