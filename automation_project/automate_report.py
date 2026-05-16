import pandas as pd
import matplotlib.pyplot as plt
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Image,
)

from reportlab.platypus.flowables import KeepTogether
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet

df = pd.read_csv("sales_data.csv")

total_sales = df["Sales"].sum()
average_sales = df["Sales"].mean()
max_sales = df["Sales"].max()
min_sales = df["Sales"].min()

print("Sales Summary Report")
print("--------------------")
print("Total sales: ", total_sales)
print("Average sales: ", average_sales)
print("Maximum sales: ", max_sales)
print("Minimum sales: ", min_sales)

plt.figure()
plt.bar(df["Month"], df["Sales"])
plt.title("Monthly Sales Report")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("sales_chart.png")
plt.close()
print("Chart saved successfully as sales_chart.png")

# Create a PDF report
pdf = SimpleDocTemplate(
    "sales_report.pdf",
    pagesize = A4,
    rightMargin=40,
    leftMargin=40,
    topMargin=40,
    bottomMargin=40,
)
styles = getSampleStyleSheet()
story =[]

story.append(Paragraph("Automated Sales Report" , styles["Title"]))
story.append(Spacer(1, 12))

summary_text =f"""
Total Sales: {total_sales}<br/>
Average Sales: {average_sales:.2f}<br/>
Highest Sales: {max_sales}<br/>
Lowest Sales: {min_sales}<br/>

"""

story.append(Paragraph(summary_text, styles["Normal"]))
story.append(Spacer(1, 12))
chart = Image("sales_chart.png", width=400, height=300)
story.append(KeepTogether([chart]))
pdf.build(story)
print("PDF report generated successfully as sales_report.pdf")