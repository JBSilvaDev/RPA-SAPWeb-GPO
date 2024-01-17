import pandas as pd
from pathlib import Path
import colorama
from colorama import Fore
from colorama import Style


# E:\Development\WorkStation
# C:\Users\julianobs\Dev


class DbFilter:
    def __init__(self):
        colorama.init()
        self.path = r"C:\Users\julianobs\Dev"
        # Path('./').resolve().parents[0]

    def data_processing(self):
        self.log("Processando dados estoque fábrica")
        self.sap_balance()
        self.log("Processando dados estoque porto")
        self.gpo_balance()
        self.log("Processando dados fatudado D-1")
        self.sap_d_1()
        self.log("Processando dados faturado mês")
        self.sap_month()
        self.log("Processando dados de produção")
        self.sap_product()

    def sap_balance(self):
        sap_stoke_balance = pd.read_csv(
            rf"{self.path}\Report-Logistc\Arquivos\BDEstoque.CSV",
            sep="\t",
            encoding="utf-8",
            header=2,
        )
        sap_stoke_balance = sap_stoke_balance[
            ["Material", "Dep.", "Texto breve material", "Lote", "PosDepósit"]
        ].dropna()

        sap_stoke_balance["Linha"] = sap_stoke_balance["Lote"].apply(
            lambda x: "L1" if "S1" in x else "L2"
        )
        ESTOQUE_TOTAL = sap_stoke_balance["Material"].shape[0] * 2
        TOTAL_PERC = f"{ESTOQUE_TOTAL  / 38000:.0%}"
        EST_L1 = (sap_stoke_balance["Linha"] == "L1").sum() * 2
        L1_PERC = f"{EST_L1  / 8000:.0%}"
        EST_L2 = (sap_stoke_balance["Linha"] == "L2").sum() * 2
        L2_PERC = f"{EST_L2  / 30000:.0%}"
        return ESTOQUE_TOTAL, TOTAL_PERC, EST_L1, L1_PERC, EST_L2, L2_PERC

    def gpo_balance(self):
        gpo_stoke_balance = pd.read_csv(
            f"{self.path}\Report-Logistc\Arquivos\Report.csv", sep=";", encoding="UTF-8"
        )
        rename = {
            "DatalgReport_COD_MERCADORIA": "Mercadoria",
            "Text3": "Qtde",
        }

        gpo_stoke_balance = gpo_stoke_balance[["DatalgReport_COD_MERCADORIA", "Text3"]]
        gpo_stoke_balance.rename(columns=rename, inplace=True)

        gpo_stoke_balance["Unidade"] = gpo_stoke_balance["Mercadoria"].apply(
            lambda x: "Mucuri" if "MSP" in x else "Anothers"
        )
        gpo_stoke_balance = gpo_stoke_balance[["Unidade", "Qtde"]]
        gpo_stoke_balance = (
            gpo_stoke_balance[["Unidade", "Qtde"]].groupby(["Unidade"]).sum()
        )

        TOTAL_PORTO = int(f"{gpo_stoke_balance['Qtde'][1] * 2}")
        TOTAL_PERC = f"{(int(TOTAL_PORTO) / 60000):.0%}"
        return TOTAL_PORTO, TOTAL_PERC

    def sap_d_1(self):
        sap_d_1 = pd.read_csv(
            f"{self.path}\Report-Logistc\Arquivos\BDFaturamentoD-1.csv",
            sep="\t",
            encoding="UTF-8",
            header=2,
        )
        sap_d_1.columns = sap_d_1.columns.str.strip()
        sap_d_1 = sap_d_1[["Descrição do Cliente", "Peso bruto"]]
        sap_d_1.fillna("Total", inplace=True)
        sap_d_1["Peso bruto"] = sap_d_1["Peso bruto"].apply(
            lambda x: int(x.replace(".", "").replace(",", "")) / 1000
        )
        FAT_D_1_MI = 0
        FAT_D_1_ME = 0
        FAT_D_1_TOTAL = 0

        for i, item in enumerate(sap_d_1["Descrição do Cliente"]):
            if "Portocel" in item:
                FAT_D_1_ME += int(sap_d_1["Peso bruto"][i])
            elif "Total" in item:
                FAT_D_1_TOTAL += int(sap_d_1["Peso bruto"][i])
            else:
                FAT_D_1_MI += int(sap_d_1["Peso bruto"][i])
        return FAT_D_1_MI, FAT_D_1_ME, FAT_D_1_TOTAL

    def sap_month(self):
        sap_month = pd.read_csv(
            f"{self.path}\Report-Logistc\Arquivos\BDfaturamentoMes.csv",
            sep="\t",
            encoding="UTF-8",
            header=2,
        )
        sap_month.columns = sap_month.columns.str.strip()
        sap_month = sap_month[["Descrição do Cliente", "Peso bruto"]]
        sap_month.fillna("Total", inplace=True)
        sap_month["Peso bruto"] = sap_month["Peso bruto"].apply(
            lambda x: int(x.replace(".", "").replace(",", "")) / 1000
        )
        FAT_MES_ME = 0
        FAT_MES_MI = 0
        FAT_MES_TOTAL = 0

        for i, item in enumerate(sap_month["Descrição do Cliente"]):
            if "Portocel" in item:
                FAT_MES_ME += int(sap_month["Peso bruto"][i])
            elif "Total" in item:
                FAT_MES_TOTAL += int(sap_month["Peso bruto"][i])
            else:
                FAT_MES_MI += int(sap_month["Peso bruto"][i])

        return FAT_MES_ME, FAT_MES_MI, FAT_MES_TOTAL

    def sap_product(self):
        sap_product = pd.read_csv(
            f"{self.path}\Report-Logistc\Arquivos\BDProducaoD-1.csv",
            sep="\t",
            encoding="UTF-8",
            header=1,
        )
        sap_product.columns = sap_product.columns.str.strip()
        sap_product = sap_product[["Data doc.", "Lote"]]
        sap_product["Lote"].dropna()
        sap_product["Linha"] = (
            sap_product["Lote"]
            .dropna()
            .apply(lambda x: "L1" if "S1" in str(x) else "L2")
        )
        PROD_L1 = (sap_product["Linha"] == "L1").sum() * 2
        PROD_L2 = (sap_product["Linha"] == "L2").sum() * 2

        PROD_TOTAL = PROD_L1 + PROD_L2
        return PROD_L1, PROD_L2, PROD_TOTAL

    def log(self, msg: str):
        # format_text  = '\033[33;40;1;4m'
        # reset_format  = '\033[0m'
        # print(f"{'=' * 100}\n{format_text}{msg}\n{reset_format}{'=' * 100}")
        # print(f"{'=' * 100}\n{msg}\n{'=' * 100}")
        print(f"{'=' * 100}\n{Fore.YELLOW}{msg}{Style.RESET_ALL}\n{'=' * 100}")
