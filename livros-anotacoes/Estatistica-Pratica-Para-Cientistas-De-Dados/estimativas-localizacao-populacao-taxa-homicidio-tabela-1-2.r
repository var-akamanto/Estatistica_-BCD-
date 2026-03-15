##Calcule a média, a média aparada e a mediana para a população utilizando R:

state <- read.csv(file='livros-anotacoes/Estatistica-Pratica-Para-Cientistas-De-Dados/tabela-1-2.csv')
print(mean(state[["População"]]))
print(mean(state[["População"]], trim=0.2))
print(median(state[["População"]]))
