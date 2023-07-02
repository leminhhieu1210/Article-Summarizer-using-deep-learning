from utils import *

def predict2(text):
    text = rdrsegmenter.tokenize(text)
    text = ' '.join([' '.join(x) for x in text])

    inputs = tokenizer(text, padding="max_length", truncation=True, max_length=256, return_tensors="pt")
    input_ids = inputs.input_ids
    attention_mask = inputs.attention_mask

    outputs = model.generate(input_ids, 
                             attention_mask=attention_mask,
                             max_length=configs['decoder_max_length'],
                             early_stopping=configs['early_stopping'],
                             num_beams=configs['num_beams'],
                             no_repeat_ngram_size=configs['no_repeat_ngram_size'])

    # all special tokens including will be removed
    output_str = tokenizer.batch_decode(outputs, skip_special_tokens=True)

    return output_str[0]


def predict(text):
    inputs = tokenizer(text, padding="max_length", truncation=True, max_length=256, return_tensors="pt")
    input_ids = inputs.input_ids.to("cpu")
    attention_mask = inputs.attention_mask.to("cpu")

    outputs = model.generate(input_ids, attention_mask=attention_mask)

    # all special tokens including will be removed
    output_str = tokenizer.batch_decode(outputs, skip_special_tokens=True)

    return output_str[0]



# st.title("Vietnamese text summarization")
# st.subheader("Enter the text you'd like to summarize.")
# text = st.text_input('Enter text')


# text = "Theo lời khai của Huy tại phiên_toà, để có tiền sử_dụng cá_nhân, Huy “nổ” là sĩ_quan cục Phòng_chống ma_tuý của bộ Công_an đóng tại TP. Đà_Nẵng, có nguồn mua ô_tô thanh_lý giá rẻ, và khả_năng chạy việc vào ngành công_an."

text = "Ngày_mai có_thể sẽ đưa đồng_hồ nước đi kiểm_định Chiều ngày 19/5 , trao_đổi với chúng_tôi , bà Hoàng_Thị_Hoà ( 60 tuổi , trú tại Tân_Triều , xã Triều_Khúc , Thanh_Trì , Hà_Nội ) cho biết , sáng nay , gia_đình bà đã ra Hợp_tác_xã Dịch_vụ sản_xuất Nông_nghiệp Triều_Khúc để xem_lại hoá_đơn tiền nước các 3 tháng đầu năm . ‘ Tại buổi làm_việc có cả các phóng_viên báo_chí tham_dự nhưng ông kế_toán_trưởng chỉ đưa ra hoá_đơn tiền nước trong tháng 1 , 2 , 3 của gia_đình tôi chứ không trả_lời thêm các ý_kiến gì . Khi gia_đình tôi đề_nghị cho xem_lại cuống hoá_đơn nước của các năm trước cũng không được đồng_ý ' , bà Hoà cho_hay . Theo bà Hoà , cả gia_đình bà có 6 nhân_khẩu gồm vợ_chồng bà , vợ_chồng người con trai và hai cháu nhỏ . Trước khi nhận được hoá_đơn tiền nước tháng 4/2016 với mức sử_dụng hơn 1.000 m3 , tổng_số tiền lên đến 19.125.036 đồng thì mỗi tháng , gia_đình bà chỉ dùng trong khoảng trên_dưới 100m3 mỗi tháng . ‘ Nghe thấy anh chốt nước thông_báo hết đến hơn 1.000 m3 , tính ra bằng hơn 19 triệu đồng mà tôi gần như không tin đó là thật , mắt hoa hết cả , chân không còn đứng vững . Gia_đình tôi có 6 người , hàng tháng vẫn dùng chỉ khoảng 90 - 100m3 là nhiều , tính ra độ hơn 200.000 - 300.000 đồng mỗi tháng . Có một_vài tháng phao trong bể bị hỏng thì tiền nước cũng chỉ lên cùng lắm đến hơn 1 triệu / tháng , thế_mà đùng cái nghe thông_báo thế , thực_sự là hoảng quá ' , bà Hoà cho_hay . Cũng theo bà Hoà , ngay sau khi nhận được thông_báo về tiền nước , gia_đình bà đã lên Hợp_tác_xã gặp lãnh_đạo đơn_vị để hỏi và giải_quyết nhưng đến nay , đã có hơn 5 cuộc gặp diễn ra nhưng vẫn không được giải_quyết chính_đáng . Phía Hợp_tác_xã giữ nguyên quan_điểm không sai mà cái này thuộc về trách_nhiệm của gia_đình bà và họ cho rằng việc hoá_đơn tiền nước tăng đột_biến là do vỡ đường_ống nước hoặc do bể nước , phao nước có vấn_đề . ‘ Nhưng thực_tế thì đường_ống nước_nhà tôi vẫn bình_thường , không sao cả , nước xả ra để rửa . Nếu ống nước mà vỡ thì hơn 1.000 m3 như_thế mỗi ngày phải chảy ra đến vài chục m3 , như_vậy , nó phải lênh_láng nước ra chứ đâu có như thế_này . Gia_đình tôi cho rằng không đúng và đề_nghị được đem đồng_hồ đi kiểm_tra nhưng phía Hợp_tác_xã đã ra 3 điều_kiện . Nếu bây_giờ nhà tôi chấp_nhận đóng tiền nước thì chỉ phải đóng 10.800.000 đồng theo mức tính hữu_nghị làng_xóm như lần trước đã thông_báo thôi . Còn nếu mang đồng_hồ đi giám_định thì gia_đình phải chịu hoàn_toàn trách_nhiệm . Nếu đồng_hồ đúng , chất_lượng đạt yêu_cầu thì gia_đình tôi phải đóng toàn_bộ hoá_đơn tiền nước là 19.125.036 đồng . Nếu đồng_hồ bị sai theo nghi_vấn thì phía hợp_tác_xã sẽ lấy 3 tháng tiền nước gần đây cộng vào chia trung_bình 3 tháng , tức_là tháng 1 , tháng 2 và tháng 3 . Nếu đúng như_vậy thì chúng_tôi chỉ phải đóng khoảng hơn 200.000 đồng ' , bà Hoà nói . Còn theo ông Trần_Công_Ứng , chồng bà Hoà thì , sau buổi làm_việc vào sáng 19/5 , theo thông_báo mới nhất của Hợp_tác_xã thì có_thể trong ngày_mai ( 20/5 ) , Hợp_tác_xã sẽ cùng gia_đình đưa đồng_hồ nước của gia_đình đi kiểm_định để làm rõ . Sụt cân vì quá suy_nghĩ Bà Hoà cho biết thêm , do sơ_suất của gia_đình nên toàn_bộ hoá_đơn tiền nước đã không còn được lưu lại , cộng thêm với việc bị Hợp_tác_xã gây khó nên ông_bà rất lo_lắng , suy_nghĩ nhiều . ‘ Từ lúc nghe thông_báo tiền nước đến nay , xong lên đề_nghị nhiều lần không được nên vợ_chồng tôi lúc_nào cũng lo_lắng , mấy đêm mất_ngủ liền , cứ chợp mắt vào là lại nghĩ . Trước tôi 46kg mà mấy ngày suy_nghĩ sụt mất cả 1kg , giờ còn 45kg . Còn ông nhà tôi thì mấy năm trước bị tai_biến nên mấy hôm_nay , sự_việc xảy ra như_thế , ông ấy bức_xúc , đôi_khi nổi_nóng nên gia_đình cũng rất lo_lắng . Cứ thế_này thì không biết sẽ còn thế_nào nữa đây . Chúng_tôi già rồi nên cũng chẳng muốn thế_này đâu ' , bà Hoà chia_sẻ . Cũng theo bà Hoà , ông_bà trước_đây đều làm_ruộng , sau chuyển sang buôn_bán nhỏ , không có lương hưu nên tất_cả đều trông nhờ vào vợ_chồng anh con trai và các con . Trong khi đó , vợ_chồng anh con trai đang phải nuôi con nhỏ , thu_nhập cũng không quá cao so với các gia_đình xung_quanh . ‘ Gia_đình không phải khó_khăn quá , cũng đủ ăn nhưng_mà giờ bảo bỏ ra đủ là hơn 19 triệu hay giảm rồi là hơn 10 triệu để đóng tiền nước này thì chắc_chắn là chúng_tôi phải đi vay_mượn thêm chứ không có ngay được . Nhưng thực_sự là nếu gia_đình tôi dùng nhiều thì tôi dù vay_mượn cũng sẵn_sàng đóng , tuy_nhiên , tôi cũng đã trình_bày , gia_đình tôi có thế , bán hàng ăn_uống thì không , rửa xe cũng không mà nước lên đến vậy là không đúng . Giờ chúng_tôi chỉ mong sao sự_việc được giải_quyết rõ_ràng xem nguyên_nhân là do đâu , chứ cứ thế_này mệt_mỏi lắm ' , bà Hoà bày_tỏ . Trong chiều nay , chúng_tôi đã có_mặt tại trụ_sở Hợp_tác_xã dịch_vụ sản_xuất Nông_nghiệp Triều_Khúc để tìm_hiểu thêm sự_việc nhưng theo ông Nguyễn_Trung_Dũng - Kế_toán_trưởng cho biết , lãnh_đạo đều đã đi vắng hết nên không_thể trả_lời thêm gì . Chúng_tôi cũng liên_lạc thêm vào số máy của ông Triệu_Đình_Nhã , Chủ_nhiệm HTX Dịch_vụ sản_xuất nông_nghiệp Triều_Khúc nhưng tắt máy . Chúng_tôi sẽ tiếp_tục thông_tin về sự_việc này ..."

# text = "Hầm Gothard gồm 2 hầm đơn , mỗi hầm tương_ứng với một tuyến đường_ray . Sau 17 năm thi_công , công_trình thế_kỷ với chi_phí xây_dựng hơn 12 tỷ Francs_Thuỵ_Sĩ này được khoan sâu trong lòng núi với mục_tiêu trở_thành một trong những tuyến đường xuyên núi Alpe quan_trọng nhất nối_liền Bắc và Nam_Âu . Ước_tính , đường_hầm tàu_hoả này sau khi được đưa vào vận_hành sẽ đón trung_bình 6,5 triệu lượt khách mỗi năm . Mỗi ngày , sẽ có từ 50 đến 80 chuyến tàu chở khách và hơn 200 chuyến tàu hàng qua hầm ."

text = '''
 Ngày 4/2, lãnh đạo thị xã Hoàng Mai (Nghệ An) cho biết, cơ quan chức năng thị xã vừa phối hợp với đơn vị chức năng tỉnh cách ly, lấy mẫu xét nghiệm cho 1 nam sinh viên trường Đại học FPT có biểu hiện ho sốt sau khi đi từ Hà Nội về nhà.

Trước đó vào ngày 31/1 nam sinh C.T.Ph. (20 tuổi, trú TX. Hoàng Mai, Nghệ An; Sinh viên trường Đại học FPT cơ sở Mỹ Đình) cùng 1 người bạn đi xe máy từ Hà Nội về quê nhà.

Lúc 22h ngày 31/1 nam sinh này về đến quê nhà nhưng không khai báo y tế. Từ ngày 1-3/2, nam sinh Ph. có đi một số nơi trên địa bàn thị xã và tiếp xúc với khoảng 12 người.


Khoảng 20h ngày 3/2, nam sinh này có dấu hiệu sốt 39 độ, đau đầu, đau rát họng, đau mỏi cơ, khó thở nhẹ. Nam sinh này sau đó được đưa vào Bệnh viện Phong da liễu (TX. Hoàng Mai) để khám và cách ly y tế.

Nhận được tin báo, Trung tâm Kiểm soát bệnh tật tỉnh Nghệ An đã trực tiếp ra lấy mẫu bệnh phẩm để xét nghiệm Covid-19. Dự kiến trong chiều cùng ngày sẽ có kết quả.

Hiện cơ quan chức năng đang rà soát những người tiếp xúc gần với nam sinh Ph. để có phương án theo dõi, cách ly và lấy mẫu xét nghiệm.

Trước đó vào đêm 31/1, một chuyến xe khách chở 22 người từ Hà Nội về Nghệ An trong đó có nhiều sinh viên Đại học FPT đi về tại phường Lê Lợi, TP. Vinh (Nghệ An). Cơ quan chức năng sau đó đã đưa 1 trường hợp F1 trên xe khách này đi cách ly tại Trung tâm Y tế huyện Nam Đàn. Riêng những trường hợp còn lại được theo dõi tại nhà.

Sau khi cách ly, các trường hợp này đã được lấy mẫu xét nghiệm và cho kết quả âm tính với Covid-19.
 '''


pred = predict(text)
print(pred)


# st.header("Results")
# st.subheader("Summary")
# st.write(pred)