
# -*- coding: utf-8 -*-
import urllib.request

# ������ URL ��� ���������� �����
url = 'https://jenyay.net/uploads/Student/Modelling/task_rcs_01.txt'

# ������ ������ �� URL
with urllib.request.urlopen(url) as response:
    dataread = response.read().decode('utf-8')

# �������������� ����������
D = None
fmin = None
fmax = None

# �������� ��� ������ �� �����
lines = dataread.splitlines()

# ���������, ���� �� ���� �� 9 ����� � �����
if len(lines) >= 9:
    # ��������� 9-� ������ (������ 8, ��� ��� ��������� � ����)
    line = lines[8]
    
    # ��������� ����������� �������� �� ������
    parts = line.split()
    for part in parts:
        if part.startswith('D='):
            D = float(part.split('=')[1])  # ����� ������ ����� ����� '=' � ����������� � float
        elif part.startswith('fmin='):
            fmin = float(part.split('=')[1].replace('e9', '')) * 1e9  # ������� 'e9' � ����������� � float
        elif part.startswith('fmax='):
            fmax = float(part.split('=')[1].replace('e9', '')) * 1e9  # ������� 'e9' � ����������� � float

# ���������� �������� ������
if fmin is not None and fmax is not None:
    freq = range(int(fmin), int(fmax), 100000000)
    print(f"D: {D}, fmin: {fmin}, fmax: {fmax}")
    print(f"�������� ������: {list(freq)}")
else:
    print("�� ������� ������� ������ �� 9-� ������ ��� ������ ��������.")