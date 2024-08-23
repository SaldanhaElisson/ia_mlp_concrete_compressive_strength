
# Projeto de Regressão para Previsão da Resistência do Concreto

## Descrição
Este projeto utiliza uma rede neural MLP (Perceptron Multicamadas) para prever a resistência à compressão do concreto. O projeto está organizado em diferentes módulos para facilitar a análise de dados, limpeza de dados e criação de modelos.

## Estrutura de Pastas e Arquivos

### Pasta `data_handling`
1. **`analizy_datas.py`**:
   - **Descrição**: Contém a classe `AnalizeyDatas` com métodos para calcular a assimetria (`skew_datas`) e a curtose (`kurt_datas`) dos dados.
   - **Funções**:
     - `skew_datas(datas)`: Calcula a assimetria dos dados.
     - `kurt_datas(datas)`: Calcula a curtose dos dados.

2. **`charts.py`**:
   - **Descrição**: Inclui a classe `Charts` com métodos para criar histogramas e calcular a quantidade de classes usando a Lei de Sturges.
   - **Funções**:
     - `law_sturges(data)`: Calcula a quantidade de classes usando a Lei de Sturges.
     - `histogram(data, name_data)`: Cria um histograma para os dados fornecidos.

3. **`cleasing_datas.py`**:
   - **Descrição**: Contém a classe `CleasingDatas` com métodos para remover outliers dos dados.
   - **Funções**:
     - `remove_outliers(df)`: Remove outliers dos dados usando o método do intervalo interquartil (IQR).

4. **`data_main.py`**:
   - **Descrição**: A classe `DataMain` é responsável por carregar os dados de um arquivo Excel ou DataFrame e criar histogramas para diferentes componentes do concreto.
   - **Funções**:
     - `create_histogram_cement()`: Cria um histograma para o cimento.
     - `create_histogram_blast_fumace_slag()`: Cria um histograma para a escória de alto-forno.
     - `create_histogram_fly_ash()`: Cria um histograma para as cinzas volantes.
     - `create_histogram_water()`: Cria um histograma para a água.
     - `create_histogram_superplasticizer()`: Cria um histograma para o superplastificante.
     - `create_histogram_course_aggregate()`: Cria um histograma para os agregados graúdos.
     - `create_histogram_fine_aggregate()`: Cria um histograma para os agregados miúdos.
     - `create_histogram_age()`: Cria um histograma para a idade do concreto.

### Pasta `models_ia`
1. **Subpasta `linear`**:
   - **Descrição**: Contém arquivos relacionados a modelos lineares para regressão.

2. **Subpasta `mlp`**:
   - **Descrição**: Contém arquivos relacionados a modelos de Perceptron Multicamadas (MLP) para regressão.

## Como Usar
1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute o script principal:
   ```bash
   python data_main.py
   ```

## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença
Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
