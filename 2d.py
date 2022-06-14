print('''
1. Cara Pandang Baris per Baris
2. Cara Pandang Kolom per Kolom
''')

jenis = input("Masukan Jenis Pandang : ")
K, N = map(int, input("Masukan Panjang Kolom dan Panjang Baris : ").split())
B = input("Masukan Posisi Awal Index (B) : ")
L = int(input("Masukan Ukuran Type Data (L) : "))
i, j = map(int, input("Masukan Index Yang Dicari i dan j : ").split())

if jenis == "1":
  rumus1 = (((i - 1) * N) + (j - 1)) * L
  rumus2 = hex(rumus1)[2:]
  rumus3 = str(hex(rumus1 + int(B, 16))[2:]).rjust(len(B), '0')

  print(f'''
  @M[i][j]    = @M[0][0] + {{(i - 1) * N + (j - 1)}} * L
  X[{i}][{j}]     = {B}(h) + {{({i} - 1) * {N} + ({j} - 1)}} * {L}
              = {B}(h) + {rumus1}(d)
              = {B}(h) + {rumus2}(h)
              = {rumus3}(h) # {rumus1} desimal = {rumus2}
  ''')
elif jenis == "2":
  rumus1 = (((j - 1) * K) + (i - 1)) * L
  rumus2 = hex(rumus1)[2:]
  rumus3 = str(hex(rumus1 + int(B, 16))[2:]).rjust(len(B), '0')

  print(f'''
  @M[i][j]    = @M[0][0] + {{(j - 1) * K + (i - 1)}} * L
  X[{i}][{j}]     = {B}(h) + {{({j} - 1) * {K} + ({i} - 1)}} * {L}
              = {B}(h) + {rumus1}(d)
              = {B}(h) + {rumus2}(h)
              = {rumus3}(h) # {rumus1} desimal = {rumus2}
  ''')