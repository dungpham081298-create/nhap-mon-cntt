def diem_trung_binh(ds_diem):
    if not ds_diem:            # danh sach rong
        return 0.0
    return round(sum(ds_diem) / len(ds_diem), 2)

def xep_loai(dtb):
    if dtb >= 8.5:
        return "Giỏi"
    elif dtb >= 7.0:
        return "Khá"
    elif dtb >= 5.0:
        return "Trung bình"
    return "Yếu"

for diem in [[7.5, 8.0, 9.0], [10, 10], [5, 5], []]:
    tb = diem_trung_binh(diem)
    print(diem, "->", tb, xep_loai(tb))
