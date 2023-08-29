# COBRA - Processamento de imagens

Ecosystem | Processing | COBRA

---

### Sobre o projeto

O Projeto Cobra é um algoritmo de processamento de imagens que realiza a extração de teor de um material a partir de imagens. Este projeto é desenvolvido em Python e permite a análise e tratamento de imagens para obter informações valiosas como o teor de carbono.


---
### Detalhes do Projeto
#### Pastas
| Pasta  | Descrição  |
| :-- | :-- |
| **cobra/**  |  Pasta principal e os scripts |
| **cobra/Images**  |  A pasta onde as imagens para analisar são localizadas |
| **cobra/DATA BASE**  |  Onde o resto das imagens se encontram |


---
### Output
| Formato  | Descrição  |	Exemplo	| Nome do Output |
| :-- | :-- | :-- | :-- |
| CSV  |  .csv será salvo na pasta principal do projeto   |	<code>csv</code>	| carbon_content.csv [Default Mode] |


### Instalação

### **1. Abra o shell e clone este repositótio**

```bash
git clone 
```

### **2. Criar o ambiente Cobra.**

#### **2.1 Instalação do make.**
* **Para windows:**

  1- Abra o PowerShell (Windows + x)

  2- Instalação do Chocolatey

```bash
Set-ExecutionPolicy Bypass -Scope Process -Force; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```

  3- Verifica se o Chocolatey foi instalado

```bash
choco
```

  4- Instalação do Make

```bash
choco install make
```
 5- Instalação do Anaconda
 
Go to https://www.anaconda.com/products/distribution,  donwload and execute the file


* **Para linux:**

  1- Instalação do Make

```bash
sudo apt install make
```

 2- Instalação do Anaconda
 
Caso nâo tenha o Anaconda instalado, siga o passo a passo neste link: https://docs.anaconda.com/anaconda/install/linux/

### **3. Vá no cobra/ .**

### **4. Criação do ambiente "Cobra" dentro do Anaconda**

* **Para windows:**

**Execute a próxima linha de comando no prompt ou terminal do Anaconda**

```bash
make setup
```

* **Para linux:**

```bash
make setup
```

### **5. Ativação do Ambiente Conda**

```bash
conda activate cobra
```

**Remember to activate the environment every time you run the cobra**

### **6. Executar cobra.**

Após instalar as dependências, você pode executar o script principal do projeto. Certifique-se de ter uma pasta chamada "Images" no diretório do projeto contendo as imagens que deseja analisar.

No prompt de comando, dentro do diretório do projeto, execute o seguinte comando:

```bash
python cobra.py
```

------------
### Todo

- [ ] Token for automation.
