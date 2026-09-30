print("====================================")
print("       LegalEase Document Generator")
print("====================================")

name = input("Enter your name: ")
address = input("Enter your address: ")
document_type = input("Enter document type: ")
duration = input("Enter duration: ")

document = f"""
LEGAL DOCUMENT
==============

Document Type: {document_type}

Name: {name}
Address: {address}
Duration: {duration}

This document is generated using the
LegalEase AI-Powered Legal Document Generator.

This is a basic document template for
educational and project demonstration purposes.
It is not a substitute for professional legal advice.
"""

with open("generated_document.txt", "w") as file:
    file.write(document)

print("\nDocument generated successfully!")
print("Saved as: generated_document.txt")