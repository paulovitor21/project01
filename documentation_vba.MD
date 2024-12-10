Documentação do Código VBA para Atualização de Planos

Este documento descreve a funcionalidade e o funcionamento do código VBA que atualiza informações de produção e montagem em várias planilhas no Excel. O objetivo do código é consolidar, calcular e atualizar dados relacionados a "PlanAssy", "PlanPPH", "Onhand", "BOM" e "Summary_Master" de maneira automatizada.

Visão Geral do Código

O código utiliza um botão chamado Up_PlanAssy para disparar a macro. Ele realiza as seguintes etapas:

Atualização de datas em cabeçalhos de tabelas.

Atualização de dados de "Onhand" com base em condições e somatórias.

Cálculos de planos de montagem em diferentes níveis (Assy nivel 1, Assy nivel 2).

Identificação de "shortages" (faltas) com base em "onhand" e planos.

Atualização de planos de montagem em "BOM" e "Summary_Master".

Cada etapa é descrita em detalhes a seguir.

Estrutura e Funcionamento do Código

Declaração de Variáveis

RgR1, RgR2, RgR3: Armazenam o último número de linha preenchido nas planilhas correspondentes.

WsPlanAssy, WsPlanPPH, WsOnhand, WsBOM, WsSumMaster: Objetos Worksheet para referenciar as planilhas.

Atualização do Plano de Produção

Seleciona a planilha PlanAssy e remove filtros ativos.

Calcula o último número de linha na coluna "A".

Atualiza datas no cabeçalho (colunas 16 a 46) com valores provenientes da planilha PlanPPH.

Atualização de Dados de "Onhand"

Para cada linha na planilha PlanAssy:

Identifica linhas onde a coluna "J" tem o valor "Onhand".

Calcula os valores nas colunas "K" a "P" com base em somatórias condicionais (é usado Application.SumIfs).

Atualização de Assy Nível 1

Para cada linha na planilha PlanAssy:

Identifica linhas onde a coluna "J" tem o valor "Plano".

Calcula os valores nas colunas 16 a 46 com base na planilha PlanPPH.

Cálculo de "Shortages" (1X, 2X, 3X)

Para cada linha na planilha PlanAssy:

Identifica linhas onde a coluna "J" tem o valor "Onhand" ou "Shortage".

Calcula o valor do "shortage" com base em somatórias condicionais e verifica se os valores são negativos.

Atualização de Assy Nível 2

Para cada linha na planilha PlanAssy:

Identifica linhas onde a coluna "J" tem o valor "Plano1".

Realiza cálculos usando valores de "Shortage" da planilha PlanAssy e aplica fatores multiplicadores.

Atualização do Plano BOM

Seleciona a planilha BOM e remove filtros ativos.

Calcula o último número de linha na coluna "A".

Atualiza datas no cabeçalho (colunas 16 a 45) com valores da planilha PlanPPH.

Para cada linha na planilha BOM:

Identifica linhas onde a coluna "O" tem o valor "Plano" ou "Plano1".

Realiza cálculos baseados nas planilhas PlanPPH e PlanAssy.

Atualização do Plano Summary Master

Seleciona a planilha Summary_Master e remove filtros ativos.

Calcula o último número de linha na coluna "A".

Atualiza datas no cabeçalho (colunas 20 a 49) com valores da planilha BOM.

Para cada linha na planilha Summary_Master:

Identifica linhas onde a coluna "S" tem o valor "Plan".

Realiza cálculos baseados na planilha BOM com múltiplos critérios.

Finalização

Exibe uma mensagem de confirmação (MsgBox) informando que o plano foi atualizado.

Fecha o formulário Master_Local.

Melhorias Sugeridas

Modularização:

Separar códigos repetitivos em funções ou procedimentos, como "Atualizar Datas", "Calcular Shortages", etc.

Desempenho:

Usar arrays para processar grandes volumes de dados em vez de iterar linha a linha diretamente nas planilhas.

Validações:

Adicionar verificacões para evitar erros, como verificar se as planilhas ou colunas contêm os dados esperados.

Comentários:

Melhorar a documentação interna do código para facilitar a compreensão e a manutenção.

Conclusão

Este código automatiza várias tarefas de processamento de dados relacionados a planos de produção e montagem. Embora funcional, ele pode ser otimizado para melhorar a manutenção, desempenho e robustez. Implementar melhorias sugeridas pode tornar o código mais eficiente e fácil de usar em outros contextos.

