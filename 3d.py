e1, e2, e3 = map(int, input("Masukan Panjang a, b dan c : ").split())
B = input("Masukan Posisi Awal Index (B) : ")
L = int(input("Masukan Ukuran Type Data (L) : "))
m, n, p= map(int, input("Masukan Index Yang Dicari i, j, k : ").split())

rumus1a = (m - 1) * (e2 * e3)
rumus1b = (n - 1) * e3
rumus1c = (p - 1)
rumus1 = (rumus1a + rumus1b + rumus1c) * L
rumus2 = hex(rumus1)[2:]
rumus3 = str(hex(rumus1 + int(B, 16))[2:]).rjust(len(B), '0')

print(f'''
Penyelesaian:
1. Tentukan jumlah elemen array A[{e1}][{e2}][{e3}]
    = {e1} * {e2} * {e3}    = {e1 * e2 * e3}
2. @M[m][n][p] = M[0][0][0] + {{((m - 1) * (juml.elemen2 * jum.elemen3)) + ((n - 1) * e3) + (p - 1)}} * L
    A[{m}][{n}][{p}] = {B}(h) + {{(({m} - 1) * {e2 * e3}) + (({n} - 1) * {e3}) + ({p} - 1)}} * {L}
                = {B}(h) + {{ {rumus1a} + {rumus1b} + {rumus1c} }}(d) * {L}
                = {B}(h) + {rumus1}(d)
                = {B}(h) + {rumus2}(h)
                = {rumus3}(h) # {rumus1} desimal = {rumus2}
''')