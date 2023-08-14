import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path
import os
import math


# import time

def generate(invoices_path, pdfs_path,image_path, total_price):
    """
    Converts invoice Excel files into PDFs
    :param invoices_path:
    :param pdfs_path:
    :param image_path:
    :param total_price:
    :return:
    """
    filepaths = glob.glob(f"{invoices_path}/*.xlsx")
    total_due = 0.0
    # try:
    for filepath in filepaths:
        total_due = 0.0
        df = pd.read_excel(filepath, sheet_name="Sheet 1")

        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()

        filename = Path(filepath).stem
        invoice_num = filename.split("-")[0]

        # filepath.split("\\")[1].split("-")[0]
        invoice_dt = filename.split("-")[1].split(".pdf")[0]
        pdf.set_font(family="Times", size=16, style="B")

        pdf.cell(w=50, h=8, txt=f"Invoice: {invoice_num}", ln=1)
        pdf.cell(w=50, h=8, txt=f"Date: {invoice_dt}", ln=1)
        pdf.ln(h=20)

        for column in df.columns:
            pdf.set_font(family="Times", size=8, style="B")
            pdf.cell(w=40, h=8, txt=str(column).title().replace("_", ' ')
                     , border=1)

        pdf.ln()

        for index, row in df.iterrows():
            for col, val in row.items():
                pdf.set_font(family="Times", size=8)
                pdf.cell(w=40, h=8, txt=str(val), border=1)
                if col == f"{total_price}":
                    total_due += float("{:.2f}".format(val))
            pdf.ln()
        pdf.ln(20)
        pdf.set_font(family="Times", size=12, style="B")
        pdf.cell(w=40, h=8, align="L", txt=f"Total amount due ${total_due}")
        pdf.image(image_path, w=10)

        if not os.path.exists(f"{pdfs_path}"):
            os.mkdir(f"{pdfs_path}")
        pdf.output(f"{pdfs_path}/{filename}.pdf")
    # except Exception as ex:
    #    print(ex)
