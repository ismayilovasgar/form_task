import pdfkit

config = pdfkit.configuration(
    wkhmtltopdf=r"C:/Program Files/wkhtmltox/bin/wkhtmltopdf.exe"
)
pdfkit.from_string("Hello World", "example.pdf")
