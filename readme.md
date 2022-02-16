O Web-Interface-GCP-Finder é um projeto que pretende simplificar a utilização da ferramenta GCP Finder, que em sí é um programa capaz de identificar Aruco Markers em imagens.

Este programa surgiu no âmbito de uma dissertação de Mestrado do Departamento de Informática da Faculdade de Ciência e Tecnologia da Universidade NOVA de Lisboa em colaboração com o Laboratório Nacional de Engenharia Civil, com o intuito de tornar o levantamento topográfico de estruturas de engenharia, nomeadamente barragens, mais prático, preciso e rápido.

O programa começa por separar as imagens que contêm um ponto de controlo daquelas que nâo contêm um ponto de controlo. Após essa operação, o programa identifica o centro dos pontos de controlo nas imagens que foram selecionadas e gera um ficheiro gcp_list.txt que irá conter a localização dos pontos de controlo em pixeis para cada imagem, já com o formato correto para ser utilizado como ficheiro de configuração no Open Drone Map.

Setup:

$ git clone https://github.com/octaviojardim/Web-Interface-GCP-Finder

$ cd Web-Interface-GCP-Finder/

$ make install

$ make run

$ http://127.0.0.1:5000


FCT/UNL-LNEC
