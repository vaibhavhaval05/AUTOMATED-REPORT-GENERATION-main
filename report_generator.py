import csv
from fpdf import FPDF

# -----------------------------
# STEP 1: READ DATA FROM FILE
# -----------------------------
def read_data(filename):
    students = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append({
                "name": row["Name"],
                "marks": int(row["Marks"])
            })
    return students


# -----------------------------
# STEP 2: ANALYZE DATA
# -----------------------------
def analyze_data(students):
    total = sum(s["marks"] for s in students)
    highest = max(students, key=lambda x: x["marks"])
    lowest = min(students, key=lambda x: x["marks"])
    average = total / len(students)

    return {
        "total_students": len(students),
        "average_marks": round(average, 2),
        "highest": highest,
        "lowest": lowest
    }


# -----------------------------
# STEP 3: GENERATE PDF REPORT
# -----------------------------
def generate_pdf(students, analysis):
    pdf = FPDF()
    pdf.add_page()

    # Title
    pdf.set_font("Helvetica", "B", 16)
    pdf.cell(0, 10, "Student Performance Report", ln=True, align="C")
    pdf.ln(10)

    # Student Table
    pdf.set_font("Helvetica", "B", 12)
    pdf.cell(80, 10, "Name", border=1)
    pdf.cell(40, 10, "Marks", border=1)
    pdf.ln()

    pdf.set_font("Helvetica", size=12)
    for s in students:
        pdf.cell(80, 10, s["name"], border=1)
        pdf.cell(40, 10, str(s["marks"]), border=1)
        pdf.ln()

    pdf.ln(10)

    # Analysis Section
    pdf.set_font("Helvetica", "B", 14)
    pdf.cell(0, 10, "Analysis Summary", ln=True)

    pdf.set_font("Helvetica", size=12)
    pdf.cell(0, 8, f"Total Students: {analysis['total_students']}", ln=True)
    pdf.cell(0, 8, f"Average Marks: {analysis['average_marks']}", ln=True)
    pdf.cell(
        0, 8,
        f"Highest Marks: {analysis['highest']['name']} "
        f"({analysis['highest']['marks']})",
        ln=True
    )
    pdf.cell(
        0, 8,
        f"Lowest Marks: {analysis['lowest']['name']} "
        f"({analysis['lowest']['marks']})",
        ln=True
    )

    pdf.output("student_report.pdf")


# -----------------------------
# MAIN PROGRAM
# -----------------------------
students = read_data("data.csv")
analysis = analyze_data(students)
generate_pdf(students, analysis)

print("PDF report generated successfully.")
