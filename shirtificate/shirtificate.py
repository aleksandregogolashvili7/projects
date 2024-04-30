from fpdf import FPDF
class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 26)
        self.cell(210, 30,"CS50 shirtificate", align="C")
        self.ln(20)
def main():
    name=input("name: ")
    pdf=PDF()
    pdf.add_page()
    pdf.image("shirtificate.png",x=20,y=60,w=170,h=200)
    pdf.set_text_color(150,150,102)
    pdf.set_font("helvetica", "B", 20)
    pdf.cell(200, 150, f"{name} took CS50", align='C')
    pdf.output("shirtificate.pdf")
if __name__=="__main__":
    main()