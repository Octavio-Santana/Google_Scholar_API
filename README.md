# Google Scholar API

  API que retorna informações referente ao tema de busca no site google scholar em formato json.
  
  As informações obtidas são:
  
    -> Titulo,
    -> Autores,
    -> Nome da revista,
    -> Ano da publicação,
    -> Número de citações,
    -> Link do abstract,
    -> Link dos artigos citados,
    -> Link dos artigos relacionados
    
------------------------------------
  
### Guia

  Após executar o programa api.py, acesse com o navegador de sua preferência o link, 
    
    localhost:5000/
    
  Existe três formas de requisição:
    
    localhost:5000/<nome da busca> 
    
        Vai retornar as informações referente as 5 primerias páginas do site google scholar.
    
    
    localhost:5000/<nome da busca>/pg=<numero> 
    
        Retorna a informação referente a página escolhida, sendo que a primeira página refere-se ao numero 0.
    
    
    localhost:5000/<nome da busca>/inicio=<n_i>&fim<n_f> 
    
        Retorna as informações contidas entre as páginas n_i e n_f.
    
  Exemplo de busca:
    
    localhost:5000/Goos Hanchen Shift
    localhost:5000/Goos Hanchen Shift/pg=0
    localhost:5000/Goos Hanchen Shift/inicio=3&fim=5
    
##### Observação:

  Pode ocorre de algumas requisições retornar nulo, isso ocorre quando é feito varias requisições no site.
  Esse problema ainda está em aberto.
