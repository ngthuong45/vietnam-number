from vietnam_number.data import units_words, word_multiplier
from vietnam_number.w2n import process_w2n


def w2n(number_sentence):
    if type(number_sentence) is not str:
        raise ValueError(
            "Không phải là một chuỗi (string)! Vui lòng truyền vảo chuỗi chử số (eg. \'bốn trăm năm mươi nghìn\')")

    number_sentence = number_sentence.replace('-', ' ')  # replace ký tự đặt biệt "-" sang khoản trắng
    number_sentence = number_sentence.lower()  # converting chuổi đầu vào thành chuổi viết thường

    if number_sentence.isdigit():  # trả về chuổi số nếu người dùng nhập chuổi số
        return int(number_sentence)

    split_words = number_sentence.strip().split()  # xóa khoảng trắng thừa và chia câu thành các từ

    clean_numbers = []

    # xóa các từ không có trong vietnam_number_system va muoi, tram, nghin, trieu, ty
    for word in split_words:
        if word in units_words or word in word_multiplier:
            clean_numbers.append(word)

    # Thông báo lỗi nếu người dùng nhập đầu vào không hợp lệ!
    if len(clean_numbers) == 0:
        raise ValueError(
            "không có chử số hợp lệ! vui lòng nhập chữ số hợp lệ (eg. bốn trăm năm mươi nghìn)")

    if len(clean_numbers) > 0:
        return int(process_w2n(clean_numbers))