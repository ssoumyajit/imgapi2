# imgapiv1

# brew install graphviz     necessary for mac, pip install graphviz won't work coz that is just the python wrapper,
# need some build C dependacy, so go with brew install. Thank you.

# To get that django model graph
# # Create a dot file
python3 manage.py graph_models -a > imgapiV1.dot
python3 manage.py graph_models --pydot -a -g -o imgapiV1.png
