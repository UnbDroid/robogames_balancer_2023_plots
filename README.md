# robogames_balancer_2023_plots

Repo com codigo pra plotar dados e debugar controlador do balancer.

## Repo Principal

- [Balancer 2023](https://github.com/UnbDroid/Robogames_balancer_2023)

## Dependencias

Python:

```bash
pip install numpy matplotlib pandas
```

## Comandos

Comando para copiar csvs para seu diretorio atual:

```bash
scp debian@192.168.8.1:/home/debian/ros_catkin_ws/vai31.csv .
```

Para rodar:
0. na linha 4 de `teste_colunas_com_referencias.py` mude para o arquivo que quiser ler.
1. rode com `python teste_colunas_com_referencias.py`
