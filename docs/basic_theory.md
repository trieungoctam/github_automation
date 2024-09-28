# Multicast vs. Broadcast vs. Anycast vs. Unicast

##  1. Introduction

- Mạng máy tính cho phép các thiết bị liên lạc với nhau trên toàn thế giới. Tuy nhiên việc giao tiếp này không đơn giản và phải dựa vào nhiều nguồn lực kỹ thuật khác nhau (từ vật lý đén logic) để thực hiện được. Ví dụ về các tài nguyên này là cáp, protocols, addressing methods, ... Đặc biệt, việc giải quyết các thông điệp bằng phương pháp phù hợp là rất quan trọng trong việc thiết kế và phát triển hệ thống truyền thông. Việc áp dụng đầy đủ các phương pháp này có thể đảm bảo liên lạc hiệu quả giữa các thiết bị được kết nối. Tuy nhiên việc sử dụng không đúng cách có thể dẫn đến mạng quá tải và các vấn đề bảo mật.

- Chúng ta sẽ nghiên cứu các phương pháp đánh địa chỉ tin nhắn khác nhau. Đầu tiên, ta xem các đặc điểm hoạt động và cách sử dụng trong thế giới thực của các phương pháp đánh địa chỉ tin nhắn hiện có. Cuối cùng, xem xét các phương pháp trong một bản tóm tắt có hệ thống, đặt chúng trực tiếp và nếu bật những điểm tương đồng và khác biệt của chúng.

## Addressing Methods

- Việc đánh địa chỉ công việc có nghĩa là xác định đích đến nào mà nguồn muốn truyền đạt. 

- Xem xét các mạng hiện đại, chúng ta có thể mô tả một số phương pháp đánh địa chỉ tin nhắn bằng cách điều tra người nhận tin nhắn đã gửi. Các phương pháp phù hợp nhất trong số này là unicast, Broadcast, Multicast và Anycast. Mỗi phương pháp đánh địa chỉ có những đặc điểm cụ thể liên quan đến số lượng người nhận, địa chỉ dành riêng trong giao thức mạng, chiến lược định tuyến và ứng dụng cuối cùng.

### 2.1 Unicast

- Unicast addressing method chỉ ra rằng giao tiếp qua mạng bao gồm một người gửi (nguồn) duy nhất và một người nhận (đích). Tương tự, chúng ta có thể coi giao tiếp unicast là một cuộc trò chuyện cụ thể với một người (unicast) tại một bữa tiệc có nhiều người (mạng). Do đó, việc giải quyết các tin nhắn bằng phương pháp unicast đòi hỏi phải có giảo tiếp riêng tư. Tuy nhiên, vì các thực thể khác có thể chặn tin nhắn nên việc sử dụng địa chỉ unicast không đảm bảo liên lạc riêng tư trong mạng. Tương tự, tương tự như một bữa tiệc, việc nói chuyện với một người không có nghĩa là những người khác ở gần bạn sẽ không lắng nghe cuộc trò chuyện.

- Dưới đây là mô tả giao tiếp sử dụng tin nhắn có địa chỉ unicast:

![Unicast](/assets/Unicast.webp)

- Việc định tuyến các thông điệp của một giao tiếp unicast khá đơn giản. Lưu ý rằng đích đến được xác định rõ ràng trong các tin nhắn unicast. Do đó, các bộ định tuyến chỉ tra cứu bảng định tuyến để chuyển tiếp tin nhắn đến nút định tuyến tiếp theo hoặc chính đích đến đó.

- Một số giao thức ứng dụng sử dụng unicast làm phương pháp đánh địa chỉ mặc định. Một số ví dụ về các giao thức này là HTTP, Telnet, FTP và SMTP. Theo cách đó, chúng ta có thể thấy rõ ràng các giao tiếp unicast xảy ra trong quá trình sử dụng mạng hàng ngày, chẳng hạn như khi chúng ta duyệt các trang web hoặc tải xuống các tệp trên Internet.

### 2.2 Broadcast

- Phương pháp đánh địa chỉ quảng bá xem xét việc truyền thông qua mạng bao gồm một người gửi (nguồn) và nhiều người nhận (đích). Theo mặc định, máy thu quảng bá là mọi thiết bị được kết nối với cùng một mạng với người gửi. Vì vậy, bằng cách sử dụng sự tương tự tương tự như đối với unicast, chúng ta có thể hiểu giao tiếp quảng bá là một người nào đó (người gửi) trong một nhóm (mạng) đứng lên bàn và hét lên một tin nhắn cho mọi người (người nhận) đang nghe.

- Dưới đây là mô tả giao tiếp sử dụng tin nhắn có địa chỉ broadcasting:

![Broadcast](/assets/Broadcast.webp)

- Trong hầu hết các trường hợp, tin nhắn quảng bá không được định tuyến mà bị giới hạn trong một mạng logic duy nhất. Tuy nhiên, đôi khi các miền quảng bá có thể cần thiết. Vì vậy, trong những trường hợp này, bộ định tuyến có thể chuyển tiếp các tin nhắn quảng bá đến từng máy chủ của miền quảng bá bằng cách sử dụng một số tin nhắn unicast. Ngoài ra, các bộ định tuyến cũng có thể tràn ngập tất cả các giao diện của chúng bằng các tin nhắn quảng bá.

- Broadcast có nhiều ứng dụng. Một ví dụ có liên quan là ARP, ánh xạ các địa chỉ IP động được xác định thành địa chỉ vật lý cố định của thiết bị. DHCP là một ví dụ khác sử dụng tính năng phát sóng để cho phép khách hàng định vị và nhận các ưu đãi IP từ máy chủ DHCP trong mạng. Chúng tôi có thể xác định các ví dụ khác trong các giao thức duyệt máy và NTP của Microsoft.

### 2.3 Multicast

- Thông báo địa chỉ multicasting cho một nhóm thiết bị cụ thể trong mạng. Lưu ý rằng, ngay cả khi một nhóm chứa tất cả các thiết bị trong mạng, về mặt lý thuyết, phát đa hướng vẫn khác với broadcast. Sự khác biệt này bao gồm ở chỗ, trong trường hợp phát đa hướng, các thiết bị đăng ký nhận tin nhắn một cách hiệu quả. Tuy nhiên, trong trường hợp broadcast, các thiết bị sẽ nhận được tin nhắn bất kể chúng có muốn hay không.

- Trong ví dụ về nhóm (mạng), chúng ta có thể thấy giao tiếp đa hướng là một nhóm người đang trò chuyện. Một thành viên trong nhóm có thể nói chuyện (người gửi) và nghe (người nhận) các thành viên khác. Hơn nữa, mọi người có thể lựa chọn trở thành thành viên của nhóm và họ có thể từ bỏ cuộc trò chuyện nếu không còn hứng thú nữa. Trong bữa tiệc, những người khác trò chuyện trong nhóm khác, trò chuyện riêng tư hoặc im lặng trong quán bar. Những người này không chú ý đến nhóm được giới thiệu đầu tiên.

- Dưới đây là mô tả giao tiếp sử dụng tin nhắn có địa chỉ  Multicast:

![Multicast](/assets/Multicast.webp)

- Chúng ta có thể hiểu định tuyến multicast như một trường hợp cụ thể của định tuyến quảng bá. Tuy nhiên, thách thức ở đây là các bộ định tuyến chỉ phải truyền tin nhắn cho các máy chủ muốn nhận chúng (thành viên của nhóm multicast). Do đó, các chiến lược dựa trên cây bao trùm tạo ra các tuyến không lặp từ một nguồn đến tất cả các đích. Với các tuyến này, các bộ định tuyến sẽ truyền một thông báo đồng thời tới tất cả các thành viên của một nhóm multicast.

- Một số hệ thống sử dụng multicast với các mục đích khác nhau. Một ví dụ có liên quan là hệ thống phân phối đa phương tiện. Trong trường hợp này, các ứng dụng IPTV và hội nghị video thường xuyên sử dụng multicast để truyền dữ liệu. Một ví dụ khác là truyền phát đa hướng trong Dịch vụ triển khai Windows (WDS). Multicast trong WDS cho phép máy chủ triển khai nhiều máy khách Windows với một luồng dữ liệu duy nhất, sử dụng hiệu quả mạng có sẵn.

### 2.4 Anycast

- Phương thức đánh địa chỉ Anycast chuyển tiếp tin nhắn đến một thiết bị của một nhóm thiết bị cụ thể. Thông thường, xem xét vị trí của người gửi, thiết bị gần nhất về mặt cấu trúc của nhóm Anycast sẽ nhận được tin nhắn. Trong ví dụ về nhóm (mạng) của chúng tôi, chúng tôi có thể hiểu giao tiếp Anycast khi một người (người gửi) sẽ rời khỏi nhóm nhưng trước tiên muốn nói lời tạm biệt với máy chủ (nhóm Anycast). Khi bữa tiệc đang diễn ra và hầu hết những người chủ trì đều có nhiều khách, bạn có thể tạm biệt một người duy nhất. Vì vậy, người đó nhìn xung quanh và tìm người tổ chức bữa tiệc (điểm đến) gần nhất, cảm ơn vì bữa tiệc và rời đi.

- Dưới đây là mô tả giao tiếp sử dụng tin nhắn có địa chỉ  Anycast:

![Anycast](/assets/Anycast.webp)

- Các ứng dụng thực tế của địa chỉ Anycast bao gồm truy vấn DNS và phân phối nội dung hiệu quả. Một số máy chủ DNS sử dụng địa chỉ Anycast để cung cấp dịch vụ dự phòng với hiệu suất được cải thiện khi truy vấn địa chỉ. Mạng phân phối nội dung có mục đích tương tự khi sử dụng Anycast. Trong trường hợp này, máy chủ nội dung được bố trí ở các vị trí chiến lược theo nhu cầu của khách hàng. Vì vậy, các yêu cầu phát sóng bất kỳ cho phép truy cập vào máy chủ nội dung phù hợp nhất theo vị trí hiện tại của khách hàng.

## 3. Systematic Summary

Nói chung, đặc điểm nổi bật nhất của các phương pháp đánh địa chỉ khác nhau là cách một nguồn liên quan đến một hoặc nhiều đích. Do đó, chúng ta có thể phân loại các phương pháp đánh địa chỉ dựa trên số lượng đích tiềm năng có sẵn cho một thông báo cụ thể và số lượng đích thực sự nhận được thông báo. Bảng sau đây tóm tắt lại các phương pháp đánh địa chỉ được nghiên cứu thông qua các đặc điểm sau:


| Method | Source-to- Destination | How many potential destinations? | How many destinations receive the message?|
|--------------|-----------|------------|------------|
| Unicast | One-to-One | One | One |
| Broadcast | One-to-All | Multiple | Multiple |
| Multicast | One-to-Many | Multiple | Multiple |
| Anycast | One-to-Any | Multiple | One |