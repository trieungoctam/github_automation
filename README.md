# Công cụ quản lý/automation GitHub Classroom với GitHub API

## Author
1. Trieu Ngoc Tam

- Email: tamtn.dynamite.work@gmail.com

- GitHub: trieungoctam

- MSV: B21DCCN658

2. Hoang Quoc Anh

- Email: 

- GitHub: 

- MSV: B21DCCN146

3. Dinh Hoang Anh

- Email: 

- GitHub: 

- MSV: B21DCCN142

## Mô tả dự án

Công cụ này được thiết kế để tự động hóa quá trình quản lý lớp học trên GitHub Classroom, hỗ trợ giáo viên quản lý các bài tập lập trình của sinh viên một cách hiệu quả hơn. Công cụ sử dụng GitHub API để tự động tạo repository, theo dõi tiến độ sinh viên, gửi thông báo tự động và hỗ trợ chấm bài tự động.

## Mục tiêu chính
- **Tự động tạo bài tập**: Tạo các repository riêng cho từng sinh viên, sao chép template bài tập để sinh viên có thể bắt đầu làm bài.
- **Theo dõi tiến độ sinh viên**: Theo dõi số lượng commit của sinh viên để biết được tiến độ hoàn thành bài tập.
- **Gửi thông báo tự động**: Tạo issue nhắc nhở trên GitHub hoặc gửi email tự động khi sinh viên chưa nộp bài đúng hạn.
- **Tự động chấm bài**: Sử dụng GitHub Actions để kiểm tra cú pháp code và unit test khi sinh viên push bài tập lên repository.

## Các tính năng chính

### 1. Tạo bài tập tự động
- Công cụ sẽ tạo repository cho từng sinh viên trong tổ chức GitHub Classroom.
- Sao chép một template bài tập có sẵn và push lên repository của sinh viên.

### 2. Theo dõi tiến độ sinh viên
- Công cụ lấy danh sách tất cả các repository trong lớp học và kiểm tra số lượng commit của sinh viên.
- Hiển thị thông tin về tiến độ của sinh viên, giúp giáo viên theo dõi quá trình nộp bài dễ dàng.

### 3. Gửi thông báo tự động
- Nếu sinh viên chưa nộp bài đúng hạn, công cụ sẽ tạo một issue trên GitHub hoặc gửi email nhắc nhở.
- Tích hợp SMTP để gửi email tự động thông báo sinh viên hoàn thành bài tập đúng hạn.

### 4. Tự động chấm bài
- Sử dụng GitHub Actions để tự động kiểm tra mã nguồn của sinh viên khi họ push bài tập lên.
- Chạy các kiểm tra cú pháp và unit test để đảm bảo chất lượng code.
- Gửi phản hồi tự động cho sinh viên qua GitHub Issues nếu bài tập đạt yêu cầu hoặc có lỗi cần sửa.

## Hướng dẫn cài đặt

### Yêu cầu hệ thống
- Python 3.x hoặc Node.js
- GitHub API Personal Access Token (PAT)
- Một tổ chức GitHub để quản lý GitHub Classroom

## Project Structure
```bash
github-classroom-automation/
│
├── src/
│   ├── api/
│   │   ├── github_client.py       # Xử lý kết nối với GitHub API
│   │   └── notifications.py       # Xử lý việc gửi email hoặc tạo GitHub Issues
│   │
│   ├── core/
│   │   ├── create_assignment.py   # Logic tạo bài tập tự động
│   │   ├── track_progress.py      # Theo dõi tiến độ sinh viên (commits, PRs)
│   │   └── auto_grading.py        # Xử lý tự động chấm bài
│   │
│   ├── utils/
│   │   ├── config.py              # Lưu trữ cấu hình dự án (API keys, email server)
│   │   └── logger.py              # Xử lý logging và thông báo lỗi
│   │
│   └── app.py                     # Tệp chính để chạy dự án, tích hợp các tính năng
│
├── tests/
│   ├── test_create_assignment.py   # Kiểm tra chức năng tạo bài tập
│   ├── test_track_progress.py      # Kiểm tra chức năng theo dõi tiến độ sinh viên
│   └── test_auto_grading.py        # Kiểm tra chức năng tự động chấm bài
│
├── .github/
│   └── workflows/
│       └── main.yml                # Cấu hình GitHub Actions cho CI/CD
│
├── .gitignore                      # Các tệp cần loại bỏ khi commit lên Git
├── README.md                       # Tài liệu mô tả dự án
├── requirements.txt                # Danh sách các thư viện cần thiết (Python)
├── package.json                    # Thông tin dự án (nếu sử dụng Node.js)
└── LICENSE                         # Thông tin bản quyền dự án
```
## Documentation
Here are links to the detailed documentation for this project:
- [Architecture Documentation](/docs/architechture.md): Learn more about the overall system architecture, communication patterns, and design decisions.
- [API Documentation](docs/api_docs.md): Find detailed descriptions of the API endpoints, request/response formats, and usage examples for both FastAPI and Spring Boot services.
- [Deployment Strategies](docs/deployment.md): Review strategies for deploying this project in different environments (local, cloud, Kubernetes).
- [Troubleshooting Guide](docs/troubleshooting.md): Common issues and their solutions for both services.

## Prerequisites

- **Docker** and **Docker Compose** installed on your machine.

- **Python 3.9+** for FastAPI development (optional if using Docker).

## Sử dụng
### Tạo bài tập lập trình
- Công cụ sẽ tự động tạo repository cho từng sinh viên trong lớp học và push template bài tập lên.
### Theo dõi tiến độ sinh viên
- Theo dõi số lượng commit trên mỗi repository để cập nhật tiến độ hoàn thành bài tập.
### Gửi thông báo tự động
- Tạo GitHub Issues hoặc gửi email nhắc nhở sinh viên hoàn thành bài tập.
### Tự động chấm bài
- Sử dụng GitHub Actions để tự động kiểm tra bài tập khi sinh viên push code lên repository.

## License
This project is licensed under the MIT License - see the [LICENSE](/License) file for details.

## Contributing

- Fork the repository.

- Create your feature branch (git checkout -b feature/my-feature).

- Commit your changes (git commit -am 'Add my feature').

- Push to the branch (git push origin feature/my-feature).

- Create a new Pull Request.
