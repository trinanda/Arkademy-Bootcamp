def gantiString(string_awal, string_lama, string_baru):
    for i in range(len(string_awal)):
        if string_lama == string_awal[i:i+len(string_lama)]:
            string_awal = string_awal[:i] + string_baru + string_awal[i+len(string_lama):]
    return string_awal


print(gantiString('Lembah Harau', 'a', 'o'))