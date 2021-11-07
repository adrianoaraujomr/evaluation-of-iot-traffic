# Detecção de Anomaliasem Redes Domésticas

## Notebooks

* AnalisesResultados: notebook com códigos usados para montar as analises
* AnomalyFilter: notebook com processo de filtro de trafegos anomalos
* DataExploration: notebook com processo de data exploration, usado para montar script de data cleaning
* FeaturesAnalysis: notebook para analise de features
* TesteHipoteses: notebook com teste de hipoteses para os 2 primeiros experimentos
* TrafficClassification: notebook de classificação de trafego, usado para gerar resultados, base para script de run classification

## Diretorios

* code: scripts para tratamento de dados, e versão em código para não usar os notebooks
* datasets: diretorio com datasets de cada experimento
* resultados: diretorio com os resultados de cada experimento

## Instalar pocote pip

* Os códigos do processo de classificação e teste ficam no direotorio code/evaluation-iot-traffic-pipelin
* Para rodar os notebooks deve instalar o pacote local que ficam os codigo de classificação e teste
    * cd code/evaluation-iot-traffic-pipeline
    * pip install .