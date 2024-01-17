from data.controller import DbFilter


df = DbFilter()


class MsgModel:
    def __init__(
        self,
    ):
        self.estoque_total = df.sap_balance()[0]
        self.total_perc = df.sap_balance()[1]
        self.estoque_l1 = df.sap_balance()[2]
        self.l1_perc = df.sap_balance()[3]
        self.estoque_l2 = df.sap_balance()[4]
        self.l2_perc = df.sap_balance()[5]
        self.estoque_porto = df.gpo_balance()[0]
        self.porto_perc = df.gpo_balance()[1]
        self.fat_d_1_mi = df.sap_d_1()[0]
        self.fat_d_1_me = df.sap_d_1()[1]
        self.fat_d_1_total = df.sap_d_1()[2]
        self.fat_mes_me = df.sap_month()[0]
        self.fat_mes_mi = df.sap_month()[1]
        self.fat_mes_total = df.sap_month()[2]
        self.prod_l1 = df.sap_product()[0]
        self.prod_l2 = df.sap_product()[1]
        self.prod_total = df.sap_product()[2]
        self.logo = (
            "https://logodownload.org/wp-content/uploads/2014/07/suzano-logo-0.png"
        )
        self.title_msg = "Segue dados sobre estoque faturamento e produção:"
        self.activityText = "Automation created by: JB Silva!"
        self.msg_final = {
            "Total estoque fábrica ": f"{self.estoque_total:,} - ({self.total_perc})".replace(
                ",", "."
            ),
            "Total estoque porto ": f"{self.estoque_porto:,} - ({self.porto_perc})".replace(
                ",", "."
            ),
            "Total estoque linha 1 ": f"{self.estoque_l1:,} - ({self.l1_perc})".replace(
                ",", "."
            ),
            "Total estoque linha 2 ": f"{self.estoque_l2:,} - ({self.l2_perc})".replace(
                ",", "."
            ),
            "Produção L1 (D-1) ": f"{self.prod_l1:,}".replace(",", "."),
            "Produção L2 (D-1) ": f"{self.prod_l2:,}".replace(",", "."),
            "Produção Total (D-1) ": f"{self.prod_total:,}".replace(",", "."),
            "Faturamento ME (D-1) ": f"{self.fat_d_1_me:,}".replace(",", "."),
            "Faturamento MI (D-1) ": f"{self.fat_d_1_mi:,}".replace(",", "."),
            "Faturamento Total (D-1) ": f"{self.fat_d_1_total:,}".replace(",", "."),
            "Faturamento ME MTD ": f"{self.fat_mes_me:,}".replace(",", "."),
            "Faturamento MI MTD ": f"{self.fat_mes_mi:,}".replace(",", "."),
            "Faturamento TOTAL Mês ": f"{self.fat_mes_total:,}".replace(",", "."),
        }
        self.msg_final_zap = f"""

Total estoque fábrica : {self.estoque_total:,} - ({self.total_perc})
Total estoque porto : {self.estoque_porto:,} - ({self.porto_perc})
Total estoque linha 1 : {self.estoque_l1:,} - ({self.l1_perc})
Total estoque linha 2 : {self.estoque_l2:,} - ({self.l2_perc})
Produção L1 (D-1) : {self.prod_l1:,}
Produção L2 (D-1) : {self.prod_l2:,}
Produção Total (D-1) : {self.prod_total:,}
Faturamento ME (D-1) : {self.fat_d_1_me:,}
Faturamento MI (D-1) : {self.fat_d_1_mi:,}
Faturamento Total (D-1) : {self.fat_d_1_total:,}
Faturamento ME MTD : {self.fat_mes_me:,}
Faturamento MI MTD : {self.fat_mes_mi:,}
Faturamento TOTAL Mês : {self.fat_mes_total:,}
        """.replace(
            ",", "."
        )
