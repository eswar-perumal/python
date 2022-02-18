# 1st way - use %
x=10
printer="Dell"
print("Print %s pages from %s printer"%(x,printer))

#Print 10 pages from Dell printer

# 2nd way
print("Print {0} pages from {1} printer".format(x,printer))
print("Print {page} pages from {printer_type} printer".format(page=21,printer_type="Canon"))

# 3rd way
print(f"Print {x} pages from {printer} printer")