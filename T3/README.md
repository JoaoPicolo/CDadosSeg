## Exploração de Dados

### Que tipos de dados você tem, majoritariamente (atributos numéricos, textuais)?

O _dataset_ apresenta 170 colunas divididas da seguintes maneira:

- 90 colunas de números decimais (aproximadamente 53% das colunas);
- 70 colunas de números inteiros (aproximadamente 41% das colunas);
- 9 colunas do tipo _string_ (aproximadamente 5% das colunas);
- 1 coluna do tipo _timestamp_ (menos de 1% das colunas);


Desta forma é fácil perceber que o _dataset_ é composto majoritariamente por colunas númericas, as quais correspondem a aproximadamente 94% de todas as colunas.


### Qual seu objetivo com esse dataset?

O objetivo é treinar uma rede artificial que seja capaz de identificar se uma determinada comunicação configura-se como ataque _DDoS_ ou não. Provalvemente isto pode ser feito utilizando-se um classificador visto que no _dataset_ existe a coluna **_Label_** que identifica se uma determinada linha é benigna ou faz parte de um ataque deste tipo.

Como análise posterior é possível utilizar a coluna **_Timestamp_** para identificar quais os horários ou até mesmo datas (como feriados, por exemplo) em que ataques deste tipo podem acontecer. Caso seja possível realizar isso pode-se tentar melhorar a detecção em datas de grande movimento, como a _Black Friday_.

Também será possível inferir sobre qual protocolo de rede ocorrem o maior número de ataques através da coluna **_Protocol_**.


### Seu dataset é rotulado de que maneira?

O _dataset_ foi gerado e rotulado automaticamente utilizando [CICFlow](https://www.unb.ca/cic/research/applications.html#CICFlowMeter), desta forma é possível a extração de estatísticas sobre características de tráfico de rede.

O _dataset_ foi dividio então em duas classes: benignos e DDoS. No primeiro caso o fluxo de rede analisado não representa um ataque, enquanto no segundo sim.


### Como é a distribuição dos dados do dataset?

Os dados são bem distrbuídos, podemos ver isso ao analisar as estatísticas da coluna **_Label_** onde 51% dos registros representam ataques DDoS e os outros 49% representam fluxos de rede benignos.


Por estarmos lidando com um _dataset_ balanceado é possível perceber que a completude dos dados referentes as colunas restantes, onde quase todas apresentam 100% dos dados válidos. Apenas a coluna **_Timestamp_** difere-se do restante, neste caso temos 4% dos dados válido e 96% dos dados estão incompatíveis com o tipo da coluna. Desta forma é possível concluirmos que caso a análise de tempo proposta anteriormente seja realizada será preciso uma normalização da forma de apresentar estes dados no _dataset_.


### Quais colunas/atributos você julga ser interessante manter e remover? Por quê?

Naturalmente deve-se manter as colunas **_Label_**, **_Timestamp_** e **_Protocol_** como forma de se atingir o objetivo proposto anteriormente, pois estas colunas possuem as informações centrais relativas a ele.

Para auxiliar neste objetivo acredito ser importante manter-se os endereços que realizam conunicações bem como o ID da comunicação entre estes endereços, então mantêm-se as seguintes colunas: Flow ID, Src Ip, Src Port, Dest Ip, Dest Port.

Como um ataque DDoS tem forte relação com o tempo no qual ocorre o fluxo de dados também deve-se manter algumas colunas com estas informações, são estas: Flow Duration e Flow IAT Min (tempo mínimo entre o envio de dois pacotes).

O ataque também tem forte relação com a quantidade de dados enviados em um único fluxo, adiciona-se então as colunas: Tot Fwd Pkts (total de pacotes enviados da origem para o destino).


A princípio as outras colunas parecem ser passíveis de descarte por não apresentarem informações tão diretas como as citadas anteriormente.
