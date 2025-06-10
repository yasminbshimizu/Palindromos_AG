<div align="center">
  <img src="https://github.com/user-attachments/assets/ccb6f5f1-0e07-4eb2-aa7c-5f681c57a59c" alt="Descrição da imagem" width="1000"/>
</div>

<h1 align="center">👹Oto come mocotÓ👹</h1>

<h3 align="center">Encontrando novos palíndromos com algoritmos genéticos</h3>

<p align="center"><strong>Autores:</strong> Júlia Guedes A. Santos e Yasmin Barbosa Shimizu</p>
<p align="center"><strong>Orientador:</strong> Prof. Dr. Daniel R. Cassar</p>

<p align="center">
<img loading="lazy" src="http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN&style=for-the-badge"/>
</p>

## 📝 Descrição

Algortmos genéticos são importantes ferramentas para resolução de problemas de otimização, baseando-se na evolução Darwiniana. Um problema simples para o qual tal estrtura pode ser aplicada é para a descoberta de palíndromos --- "Uma palavra ou frase que pode ser lida no seu sentido normal, da esquerda para a direita, bem como no sentido contrário, da direita para a esquerda, sem que haja mudança nas palavras que a formam e no seu significado" (Dicionário Online da Língua Portuguesa). [1] 

Neste trabalho, 10 palíndromos, formados por 5 letras cada, serão encontrados. A única restrição é que todos precisam ter pelo menos uma vogal. Para que isso aconteça, a função objetivo atribuirá uma penalização proporcional a maior distância entre uma letra da palavra e uma vogal. Para o fitness total do palíndromo, será considerada a distância entre o primeiro e o último elemento somada a distância entre o segundo e o penúltimo, somada a essa penalização. Ademais, todos os indivíduos criados inicialmente pela função de criação da população precisarão ser compostos por uma vogal.

Além dos operadores de seleção (seleção por torneio), cruzamento (cruzamento de ponto duplo) e mutação (mutação de salto), foi implementada uma nova função de mutação. Essa, caso a função não tenha nenhuma letra repetida, irá sortear um determinado gene e mudará seu valor para um igual a outro gene sorteado. Dessa forma, o conceito de letras repetidas na palavra será introduzido, o que pode auxiliar na convergência.

## 📔 Notebooks e arquivos do projeto
* `4.12 - Novos palíndromos.ipynb`: otimização do problema dos múltiplos caixeiros viajantes através de um algoritmo genético.
* `funcoes_palindromos.py`: script com as funções construídas, necessárias para a evolução dos algoritmos genéticos
* `README.md`: descrição geral do projeto.

## 🖇️ Informações técnicas
* Linguagem de programação: `Python 3.9`
* Software:  `Visual Studio Code`, `Jupyter Notebook`
* Bibliotecas e Módulos: `random`, `functools`, `itertools`, `string`

### Como executar o algoritmo?
Os algoritmos genéticos desenvolvidos neste trabalho podem ser executados em compiladores de Python como Jupyter Notebook, Visual Studio Code e Google Colab. Para tal, é necessário:
1. A instalação das bibliotecas citadas acima, utilizando, por exemplo, o método `!pip install <nome_da_biblioteca>`;
2. O download do *script* `funcoes_palindromos.py` e do notebook `4.12 - Novos palíndromos.ipynb` no mesmo diretório;
3. Execução do notebook em um compilador de Python.


## 🧬 Evoluindo o algoritmo genético

Além dos operadores de seleção, cruzamento e mutação clássico de algoritmos genéticos --- aqui implementados como seleção por torneio, cruzamento de ponto duplo e mutação por salto ---, desenvolvemos adaptações específicas para o problema de geração de palíndromos:

* **Função objetivo:** Avalia a qualidade de um indivíduo com base na soma das distâncias entre o primeiro e o último caracteres, e entre o segundo e o penúltimo. Como penalização adicional, caso o indivíduo não contenha nenhuma vogal, é aplicada uma penalidade proporcional — 10 vezes a maior distância entre uma letra da palavra e uma vogal (calculada a partir do produto cartesiano entre as vogais existentes e as letras da palavra).

* **Função de mutação por letra repetida:** Se um indivíduo for sorteado para mutação e não possuir letras repetidas, um de seus genes será alterado para copiar o valor de outro gene aleatório do mesmo indivíduo. Essa abordagem favorece a formação de estruturas repetidas, essenciais para a construção de palíndromos, especialmente nas primeiras gerações.

Para encontrar 10 palíndromos diferentes, o algoritmo foi construído com loops `while`, executando um algoritmo até que um novo palíndromo fosse encontrado, e parando apenas quando 10 palíndromos fossem registrados, cada um em evoluções diferentes.

## 🔤 Resultados Obtidos
Como resultado, grande parte dos palíndromos foram gerados em poucas gerações (por volta de 50), o que demonstra uma boa performance do algoritmo genético implementado. Abaixo, é possível observar os palíndromos gerados pelo algoritmo, nas respectivas gerações em que foram formados:

* ***focof*** (Geração 51)
* ***imkmi*** (Geração 63)
* ***idldi*** (Geração 61)
* ***lgugl*** (Geração 57)
* ***uyryu*** (Geração 152)
* ***mokom*** (Geração 11)
* ***innni*** (Geração 42)
* ***ihjhi*** (Geração 37)
* ***efsfe*** (Geração 41)
* ***efvfe*** (Geração 112)

## 😁 Conclusão

A partir do desenvolvimento e evolução do algoritmo genético, foi possível concluir que o procedimento demonstrou alta performance, sendo capaz de gerar 10 palíndromos válidos (com 5 letras e ao menos uma vogal) em cerca de 50 gerações na maioria dos casos. Isso evidencia a eficácia das estratégias escolhidas de seleção, cruzamento e mutação adotadas na resolução do problema, bem como boa estruturação da função objetivo e da função responsável por criar letras repetidas, feitas de forma autoral.

## 🗃️ Referências
[1] Palíndromos: o que são e mais de 100 exemplos. Dicio, Dicionário Online de Português. Disponível em: https://www.dicio.com.br/lista-palindromos/. Acesso em: 6 jun. 2025.

## 🧠 Contribuições dos Colaboradores

#### Para o Projeto:

* Júlia Guedes: Construção da resolução do problema, implementação das funções necessárias para a resolução do problema, comentários descritivos no código.
* Yasmin Shimizu: Construção da resolução do problema, implementação das funções necessárias para a resolução do problema.

#### Para o Repositório GitHub:
* Júlia Guedes: Upload de arquivos.
* Yasmin Shimizu: Documentação do README.

**Orientação e Revisão:** Prof. Dr. Daniel R. Cassar.

| [<img loading="lazy" src="https://avatars.githubusercontent.com/u/172424779?v=4" width=115><br><sub> Júlia Guedes </sub>](https://github.com/JuliaGuedesASantos)<br> [<sub>Ilum - CNPEM</sub>](https://ilum.cnpem.br/)<br> [<sub>Currículo Lattes</sub>](http://lattes.cnpq.br/9504021537643847)<br> [<sub>Linkedin</sub>](https://www.linkedin.com/in/j%C3%BAlia-guedes-546542283/) | [<img loading="lazy" src="https://avatars.githubusercontent.com/u/171518829?v=4" width=115><br><sub>Yasmin Shimizu</sub>](https://github.com/yasminbshimizu)<br> [<sub>Ilum - CNPEM</sub>](https://ilum.cnpem.br/)<br> [<sub>Currículo Lattes</sub>](https://wwws.cnpq.br/cvlattesweb/PKG_MENU.menu?f_cod=B946BED44B4E2F555F7290AF3E8AF4F3#)<br> [<sub>Linkedin</sub>](https://www.linkedin.com/in/yasminbshimizu/) | [<img loading="lazy" src="https://github.com/user-attachments/assets/463d4753-7fa4-4a42-aa54-409e4150bb51" width=115><br> <sub> Prof. Dr. Daniel R. Cassar </sub>](https://github.com/drcassar)<br> [<sub>Ilum - CNPEM</sub>](https://ilum.cnpem.br/)<br> [<sub>Currículo Lattes</sub>](http://lattes.cnpq.br/1717397276752482) <br> [<sub>Linkedin</sub>](https://www.linkedin.com/in/drcassar/)| 
| :---: | :---: | :---: | 

