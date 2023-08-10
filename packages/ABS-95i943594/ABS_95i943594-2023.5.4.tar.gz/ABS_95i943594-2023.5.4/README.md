# Pacote principal Absolute Investimentos

Pacote principal com funções básicas para uso interno na Absolute Investimentos


## Instalando pacote no Windows

- Substituir arquivos na rede, na pasta `P:/sistemas/Python`
- Alterar versão no setup.py para a data da publicação
- Caso necessário, incluir novas dependências no requirements.txt
- Enviar email respondendo "Documentação Pacote ABS (python)" avisando que
 há uma nova versão disponível


## Instalando pacote no linux

Para instalação do pacote, é recomendado ter o conda configurado na máquina.
Também é necessário instalar os drivers compatíveis do [Microsoft ODBC](https://bit.ly/3Bsn0Pz).
 Depois de ambos instalados, em um terminal, navegue para a pasta raiz deste
 projeto, `PackageABS`, e digite:

```bash
> sudo apt-get install unixodbc-dev
> conda install pyodbc
> cd Pacotes/
> pip install -r requirements.txt
> pip install .
> python -c "import ABS; print(ABS.__name__)"
```
