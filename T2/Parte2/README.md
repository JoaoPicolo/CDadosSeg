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

- Nome: RiotGames Client; Hash MD4:7e85f67a509e5bdaa52fb1cfb67e2cd5;
- Nome: Steam; Hash MD4:90f93293f2cb7868bfb5c039394d503a;
