import pandas as pd
from fpdf import FPDF
from pathlib import Path
import glob

filepaths = glob.glob('texts/*.txt')
pdf = FPDF(orientation="P", unit="mm", format="A4")
for filepath in filepaths:
    df = pd.read_csv(filepath)
    pdf.add_page()
    filename = Path(filepath).stem.capitalize()
    pdf.set_font(family="Times", size=16, style = "B")
    pdf.cell(w=50, h=8, txt= f"{filename}")
pdf.output("animals.pdf")



