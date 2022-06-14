B = input("Masukan Posisi Awal Index (B) : ")
L = int(input("Masukan Ukuran Type Data (L) : "))
i = int(input("Masukan Index Yang Dicari (i) : "))

rumus1 = (i - 1) * L
rumus2 = hex(rumus1)[2:]
rumus3 = str(hex(rumus1 + int(B, 16))[2:]).rjust(len(B), '0')

print(f'''
Rumus : @A[i] = B + (i - 1) * L
Diketahui :
@A[i] = A[{i}]
    B = {B}(h)
    i = {i}
    L = {L}

Penyelesaian :
A[{i}] = {B}(h) + ({i} - 1) * {L}
     = {B}(h) + {rumus1}(d)
     = {B}(h) + {rumus2}(h)
     = {rumus3}(h)  # {rumus1} desimal = {rumus2}
       ^
''')
