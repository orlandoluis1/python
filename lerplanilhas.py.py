import xlrd
book = xlrd.open_workbook("Pasta de trabalho 5.xls")
print "Número de abas: ", book.nsheets
print "Nomes das Planilhas:", book.sheet_names()
sh = book.sheet_by_index(0)
print(sh.name, sh.nrows, sh.ncols)
print("Valor da célula c3 é ", sh.cell_value(rowx=3, colx=3))
for rx in range(sh.nrows):
    print(sh.row(rx))
