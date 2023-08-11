number_system = {
    'nol': 0,
    'kosong': 0,
    'pertama': 1,
    'satu': 1, 
    'dua': 2, 
    'tiga': 3, 
    'empat': 4,
    'lima': 5, 
    'enam': 6, 
    'tujuh': 7,
    'delapan': 8, 
    'sembilan': 9,
    'sepuluh': 10, 
    'sebelas': 11, 
    'belas': 10,
    'puluh': 10, 
    'seratus': 100, 
    'ratus': 100, 
    'seribu': 1000, 
    'sejuta': 1000000, 
    'ribu': 1000, 
    'juta': 1000000,
    'miliar': 1000000000, 
    'milyar': 1000000000, 
    'setengah': 0.5
}

multiplier_system = ['puluh', 'ratus', 'ribu', 'juta', 'milyar', 'trilyun', 'miliar']

def add_leading_zero(number):
    num_digits = len(str(number))
    decimal_value = number / 10 ** num_digits
    return decimal_value

def word_to_num(number_sentence):
    """
    Konversi kalimat angka dalam bentuk kata menjadi angka dalam bentuk numerik.

    Args:
    number_sentence (str): Kalimat angka dalam bentuk kata.

    Returns:
    int: Angka yang sudah dikonversi.

    Raises:
    ValueError: Jika tipe input bukan string atau tidak ada kata angka yang valid.

    Example:
    >>> word_to_num("seratus dua puluh lima")
    125
    """

    if type(number_sentence) is not str:
        raise ValueError("Tipe input bukan string! Silakan masukkan kata angka yang valid (contoh: 'dua juta dua puluh tiga ribu empat puluh sembilan')")

    number_sentence = number_sentence.replace('-', ' ')
    number_sentence = number_sentence.lower()  # mengonversi input menjadi huruf kecil

    if number_sentence.isdigit():  # mengembalikan angka jika pengguna memasukkan string angka
        return int(number_sentence)

    if 'koma' in number_sentence:
        split_koma = number_sentence.split("koma")
        split_words = split_koma[0].strip().split()
        point_words = split_koma[1].strip().split()
    else:
        split_words = number_sentence.strip().split()
        point_words = []
    

    clean_numbers = []
    clean_decimal_numbers = []
    point_clean_numbers = []
    point_numbers = []

    for word in split_words:
        if word.startswith("ke"):
            word = word.replace("ke", "")
        if word in number_system:
            clean_numbers.append(word)


    for word in point_words:
        if word.startswith("ke"):
            word = word.replace("ke", "")
        if word in number_system:
            point_clean_numbers.append(word)

    if len(clean_numbers) == 0:
        raise ValueError("Tidak ditemukan kata angka yang valid! Silakan masukkan kata angka yang valid (contoh: 'dua juta dua puluh tiga ribu empat puluh sembilan')")

    if len(clean_numbers) > 0:
        tmp_number = 1
        biggest_multiplier = 1
        for i, w in enumerate(reversed(clean_numbers)):
            if w in multiplier_system:
                if number_system[w] > biggest_multiplier:
                    biggest_multiplier = number_system[w]
                    tmp_number = tmp_number * number_system[w]
                else:
                    tmp_number = number_system[w] * biggest_multiplier
            else:
                if tmp_number == 1:
                    clean_decimal_numbers.append(number_system[w])
                else:
                    tmp_number = tmp_number * number_system[w]
                    clean_decimal_numbers.append(tmp_number)
                    tmp_number = 1
        
        if len(point_clean_numbers) > 0:
            tmp_number = 1
            biggest_multiplier = 1
            for i, w in enumerate(reversed(point_clean_numbers)):
                if w in multiplier_system:
                    if number_system[w] > biggest_multiplier:
                        biggest_multiplier = number_system[w]
                        tmp_number = tmp_number * number_system[w]
                    else:
                        tmp_number = number_system[w] * biggest_multiplier
                else:
                    if tmp_number == 1:
                        point_numbers.append(number_system[w])
                    else:
                        tmp_number = tmp_number * number_system[w]
                        point_numbers.append(tmp_number)
                        tmp_number = 1
            zero_prefix = 0
            for w in point_clean_numbers:
                if number_system[w] == 0:
                    zero_prefix = zero_prefix + 1
                else:
                    break
            
            # print(sum(point_numbers))
            # print(clean_decimal_numbers)
            # print(zero_prefix)
            if(zero_prefix > 0):
                stri = str(add_leading_zero(sum(point_numbers)))
                stri = stri.split(".")
                stri[1] =  (zero_prefix * "0") + stri[1]
                # print(stri)
                stri = ".".join(stri)
                # print(stri)
                clean_decimal_numbers.append(float(stri))
            else:
                clean_decimal_numbers.append(add_leading_zero(sum(point_numbers)))
            
        neg_words = ["-", "minus", "negatif"]
        for w in neg_words:
            if w in number_sentence:
                return sum(clean_decimal_numbers) * -1
        return sum(clean_decimal_numbers)