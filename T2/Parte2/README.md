# Parte 2: Análise de arquivos PE


Esta parte se divide em duas tarefas: análise de seções executáveis de arquivos PE e comparação de seções entre dois arquivos PE.

### Tarefa 1: Análise das seções executáveis de arquivos PE

Nesta tarefa o programa espera em seu primeiro argumento o caminho para um arquivo PE **ou** o caminho para um diretório contendo um ou mais arquivos PE. Seja **_pe_** a pasta que contêm dois arquivos (bin1.exe e bin2.exe). O programa pode ser executado da seguinte maneira para a análise de um arquivo:
``` bash
python3 executable.py pe/bin1.exe
```

E deve ser executado da seguite maneira como forma de analisar todos os arquivos da pasta:
``` bash
python3 executable.py pe/
```


### Tarefa 2: Comparação de seções entre dois arquivos PE

Nesta tarefa o programa espera como seu primeiro e segundo argumento o caminho para um arquivo PE. Seja **_pe_** a pasta descrita na **Tarefa 1**, o programa deve ser executado da seguinte maneira:
``` bash
python3 compare.py pe/bin1.exe pe/bin2.exe
```

### Testes

Para os testes foram utilizados dois arquivos PE:

- Nome: RiotGames Client; Hash MD5:D476FB65C0E3CFC1A6D06DC9F359776B;
- Nome: Steam; Hash MD5:29A0D4F99B2AD92BC67D276C0C43D603;
