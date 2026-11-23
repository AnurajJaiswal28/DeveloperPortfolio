from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable

file_path = "Portfolio/resume.pdf"

doc = SimpleDocTemplate(
    file_path,
    pagesize=A4,
    rightMargin=45,
    leftMargin=45,
    topMargin=35,
    bottomMargin=35
)

styles = getSampleStyleSheet()

name_style = ParagraphStyle(
    "Name",
    parent=styles["Title"],
    fontSize=21,
    textColor=colors.HexColor("#17365D"),
    alignment=TA_CENTER,
    spaceAfter=5
)

subtitle_style = ParagraphStyle(
    "Subtitle",
    parent=styles["Normal"],
    fontSize=10,
    alignment=TA_CENTER,
    spaceAfter=8
)

heading_style = ParagraphStyle(
    "Heading",
    parent=styles["Heading2"],
    fontSize=11,
    textColor=colors.HexColor("#17365D"),
    spaceBefore=8,
    spaceAfter=4
)

body_style = ParagraphStyle(
    "Body",
    parent=styles["BodyText"],
    fontSize=9,
    leading=12,
    spaceAfter=3
)

story = []

story.append(Paragraph("ANURAJ JAISWAL", name_style))
story.append(Paragraph(
    "B.Tech Computer Science and Engineering Student",
    subtitle_style
))
story.append(HRFlowable(width="100%", color=colors.HexColor("#17365D")))
story.append(Spacer(1, 8))

sections = [
    ("CAREER OBJECTIVE",
     "Motivated B.Tech CSE student interested in software development "
     "and computer technologies. Eager to learn programming, "
     "problem-solving and practical development skills."),

    ("EDUCATION",
     "<b>Bachelor of Technology (B.Tech)</b><br/>"
     "Computer Science and Engineering<br/>"
     "K.R. Mangalam University<br/>"
     "Currently Pursuing"),

    ("TECHNICAL SKILLS",
     "<b>Programming:</b> Python, C, C++ (basic)<br/>"
     "<b>Web Technologies:</b> HTML, CSS (basic)<br/>"
     "<b>Tools:</b> Linux, Git, GitHub, VS Code<br/>"
     "<b>Other:</b> Bash Scripting, REST API, JSON, jq"),

    ("ACADEMIC PROJECTS",
     "<b>Developer Ecosystem Portfolio</b><br/>"
     "- Created a structured Git repository.<br/>"
     "- Practiced Linux commands and Bash scripting.<br/>"
     "- Retrieved REST API data using curl.<br/>"
     "- Processed JSON data using jq."),

    ("AREAS OF INTEREST",
     "Software Development | Web Development | Problem Solving | "
     "Computer Science Fundamentals"),

    ("PERSONAL DETAILS",
     "<b>Name:</b> Anuraj Jaiswal<br/>"
     "<b>Location:</b> India")
]

for heading, content in sections:
    story.append(Paragraph(heading, heading_style))
    story.append(Paragraph(content, body_style))

doc.build(story)

print("Resume PDF created successfully:", file_path)
