# main.py
import logging
from scripts.process_data import processar_arquivo

# Configuração de logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    try:
        # Caminho do arquivo .xlsb de origem
        #xlsb_file = r"C:\Users\Paulo\Documents\data_g\ref\1213_Bom_Master.xlsb"
        xlsb_file = r"C:\Users\Paulo\Downloads\Downloads-1\1210_Bom_Master.xlsb"
        # Processar o arquivo
        processar_arquivo(xlsb_file)
    except Exception as e:
        logging.error(f"Ocorreu um erro na execução do processo: {e}")
        logging.exception("Detalhes do erro: ")

if __name__ == "__main__":
    main()
