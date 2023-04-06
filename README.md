# robogames_balancer_2023_plots

Repo com codigo pra plotar dados e debugar controlador do balancer.

## Repo Principal

- [Balancer 2023](https://github.com/UnbDroid/Robogames_balancer_2023)

## Dependencias

Python:

```bash
sudo apt-get install sshpass
pip install numpy matplotlib pandas
```

## Comandos

Comando para copiar csvs para seu diretorio atual:

## Baixar CSV

```bash
scp debian@192.168.8.1:/home/debian/ros_catkin_ws/nomearquivo.csv ./csv/
```

## Para rodar

### Manual

0. importe `usecase_N_cols` no inicio do arquivo `main.py`, `N` sendo o número de colunas do arquivo csv que quiser ler.
1. sete a variavel como `column_names = usecase_N_cols.column_names`
2. rode com `python main.py nomearquivo.csv`

# Auto

1. TODO
