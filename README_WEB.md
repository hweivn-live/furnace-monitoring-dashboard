# 🔥 Glass Furnace Monitoring - Web Dashboard

Web dashboard để giám sát trực tuyến trạng thái lò nấu phích.

## 📸 Screenshot

![Dashboard Preview](https://via.placeholder.com/800x400.png?text=Dashboard+Preview)

## ✨ Tính năng

- ✅ Hiển thị trạng thái real-time lò nấu phích
- ✅ Xem ảnh gốc và ảnh phân tích
- ✅ Bảng lịch sử phân tích chi tiết
- ✅ Tự động cập nhật khi có dữ liệu mới
- ✅ Responsive - xem được trên mobile
- ✅ Không cần cài đặt - chỉ cần browser

## 🚀 Chạy nhanh

### Cách 1: Double-click file .bat
```
RUN_WEB_DASHBOARD.bat
```

### Cách 2: Command line
```bash
pip install -r requirements_web.txt
streamlit run web_dashboard.py
```

Dashboard sẽ mở tại: http://localhost:8501

## ☁️ Deploy lên Internet (MIỄN PHÍ)

### 🌐 Deploy trên Streamlit Cloud - Hướng dẫn chi tiết

Streamlit Cloud là dịch vụ hosting MIỄN PHÍ của Streamlit, cho phép bạn chia sẻ dashboard với bất kỳ ai qua Internet. Không giới hạn người xem, tự động cập nhật khi code thay đổi!

#### **Bước 1: Chuẩn bị code trên GitHub**

1. **Tạo tài khoản GitHub** (nếu chưa có):
   - Truy cập: https://github.com
   - Click "Sign up" và làm theo hướng dẫn

2. **Tạo repository mới**:
   - Click nút "+" góc phải > "New repository"
   - Repository name: `furnace-monitoring-dashboard` (hoặc tên bạn thích)
   - Chọn **Public** (bắt buộc cho Streamlit Cloud free tier)
   - ✅ Check "Add a README file"
   - Click "Create repository"

3. **Upload các file cần thiết** lên GitHub:
   
   Cách 1 - Dùng GitHub Web Interface:
   - Click "Add file" > "Upload files"
   - Kéo thả các file sau vào:
     ```
     web_dashboard.py
     requirements_web.txt
     README_WEB.md
     ```
   - Click "Commit changes"

   Cách 2 - Dùng Git Command Line:
   ```bash
   cd "d:\Ralaco\In progress\Binh phich\AI\AI_lo_phich\analysis_color"
   git init
   git add web_dashboard.py requirements_web.txt README_WEB.md
   git commit -m "Initial commit - Furnace monitoring dashboard"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/furnace-monitoring-dashboard.git
   git push -u origin main
   ```

4. **Tạo file `requirements.txt`** (nếu chưa có):
   - Click "Add file" > "Create new file"
   - Tên file: `requirements.txt`
   - Nội dung:
     ```
     streamlit>=1.28.0
     pandas>=2.0.0
     pillow>=10.0.0
     ```
   - Click "Commit changes"

5. **Upload dữ liệu mẫu** (tùy chọn):
   - Tạo folder `Data_result/` và upload file `analysis.db`
   - Tạo folder `Result_Img/` và upload một vài ảnh mẫu
   - Hoặc tạo database rỗng để test trước

#### **Bước 2: Tạo tài khoản Streamlit Cloud**

1. **Truy cập Streamlit Cloud**:
   - Vào: https://share.streamlit.io
   - Click "Sign up" hoặc "Continue with GitHub"

2. **Kết nối với GitHub**:
   - Chọn "Continue with GitHub"
   - Đăng nhập GitHub nếu chưa đăng nhập
   - Click "Authorize streamlit" để cho phép Streamlit truy cập GitHub của bạn

#### **Bước 3: Deploy Dashboard**

1. **Tạo app mới**:
   - Sau khi đăng nhập Streamlit Cloud, click "New app"
   - Hoặc truy cập: https://share.streamlit.io/deploy

2. **Cấu hình deployment**:
   
   **Repository, branch, and file path:**
   - **Repository**: Chọn `YOUR_USERNAME/furnace-monitoring-dashboard`
   - **Branch**: `main` (hoặc `master`)
   - **Main file path**: `web_dashboard.py`
   
   **App URL (optional):**
   - Để mặc định: `furnace-monitoring-dashboard`
   - Hoặc đặt tên tùy chỉnh: `lo-nau-phich-monitoring`
   - URL cuối cùng sẽ là: `https://YOUR_USERNAME-furnace-monitoring-dashboard.streamlit.app`

3. **Advanced settings** (tùy chọn):
   - Click "Advanced settings" nếu cần:
     - **Python version**: `3.10` (khuyến nghị)
     - **Secrets**: Để trống (hoặc thêm config nếu cần)
   - Thường không cần thay đổi gì

4. **Deploy**:
   - Click nút **"Deploy!"**
   - Chờ 2-5 phút để Streamlit Cloud:
     - Clone repository
     - Cài đặt dependencies
     - Khởi động app
   
   **Quan sát log deployment:**
   - Bạn sẽ thấy log real-time:
     ```
     Cloning repository...
     Installing requirements...
     Running app...
     Your app is now live! 🎉
     ```

5. **Nhận link public**:
   - Sau khi deploy thành công, bạn sẽ thấy dashboard chạy
   - URL dạng: `https://YOUR_USERNAME-furnace-monitoring-dashboard.streamlit.app`
   - Copy link này để chia sẻ!

#### **Bước 4: Cập nhật dữ liệu**

Dashboard đã chạy nhưng chưa có dữ liệu thật? Có 3 cách sync dữ liệu:

**Cách 1: Upload database lên GitHub (đơn giản nhất)**
```bash
# Trên máy local, copy database mới nhất
cd "d:\Ralaco\In progress\Binh phich\AI\AI_lo_phich\analysis_color"
git add Data_result/analysis.db Result_Img/*.jpg
git commit -m "Update analysis data"
git push
```
- Streamlit Cloud tự động deploy lại sau 1-2 phút
- Lưu ý: File > 100MB không upload được GitHub

**Cách 2: Dùng Cloud Database (cho production thật sự)**
- Chuyển từ SQLite sang PostgreSQL/MySQL
- Dùng dịch vụ free như:
  - Supabase (https://supabase.com) - PostgreSQL miễn phí
  - PlanetScale (https://planetscale.com) - MySQL miễn phí
  - Neon (https://neon.tech) - PostgreSQL serverless
- Sửa code `web_dashboard.py` để kết nối cloud database

**Cách 3: Dùng Cloud Storage cho ảnh**
- Upload ảnh lên Imgur, Cloudinary, hoặc Google Drive
- Lưu link ảnh trong database thay vì đường dẫn local

#### **Bước 5: Quản lý và theo dõi**

**Dashboard Streamlit Cloud:**
- Truy cập: https://share.streamlit.io
- Xem danh sách apps của bạn
- Mỗi app có:
  - 📊 **Analytics**: Số lượt view, visitors
  - ⚙️ **Settings**: Cấu hình, reboot app
  - 📝 **Logs**: Xem lỗi, debug
  - 🔄 **Reboot**: Khởi động lại app

**Auto-update:**
- Mỗi khi push code mới lên GitHub:
  ```bash
  git add .
  git commit -m "Update dashboard UI"
  git push
  ```
- Streamlit Cloud tự động deploy lại trong 1-2 phút

**Giới hạn Free Tier:**
- ✅ Unlimited viewers
- ✅ HTTPS tự động
- ✅ 1 private app
- ✅ Unlimited public apps
- ⚠️ 1GB RAM per app
- ⚠️ 1 CPU core per app

#### **💡 Tips & Best Practices**

**Tối ưu hiệu năng:**
- Sử dụng `@st.cache_data` cho những hàm đọc database nhiều lần
- Giới hạn số lượng ảnh hiển thị
- Tránh tự động refresh quá nhanh (khuyến nghị 30-60s)

**Bảo mật:**
- Thêm authentication nếu cần:
  ```python
  # Thêm vào đầu web_dashboard.py
  import streamlit_authenticator as stauth
  ```
- Hoặc dùng Streamlit Secrets để lưu password
- Với dữ liệu nhạy cảm, nên dùng private repository + trả phí

**Custom domain:**
- Free tier chỉ có subdomain: `*.streamlit.app`
- Muốn custom domain (vd: `monitor.ralaco.com`):
  - Cần nâng lên Teams/Enterprise plan ($$$)
  - Hoặc deploy trên nền tảng khác (Heroku, AWS, Azure)

**Monitoring:**
- Theo dõi logs thường xuyên
- Set up email alert khi app down
- Test trên nhiều thiết bị (desktop, mobile, tablet)

#### **🔧 Troubleshooting**

**❌ Lỗi: "No module named 'streamlit'"**
- Kiểm tra file `requirements.txt` có `streamlit` chưa
- Format đúng: mỗi package một dòng

**❌ Lỗi: "File not found: Data_result/analysis.db"**
- Upload folder `Data_result/` lên GitHub
- Hoặc sửa code để tạo database mẫu:
  ```python
  if not os.path.exists(db_path):
      # Create sample database
      conn = sqlite3.connect(db_path)
      # ... tạo bảng mẫu
  ```

**❌ App chạy chậm hoặc crash:**
- Giảm refresh rate
- Giảm số lượng data load
- Optimize queries
- Check RAM usage trong Streamlit Cloud dashboard

**❌ Ảnh không hiển thị:**
- Đảm bảo ảnh đã upload lên GitHub
- Check đường dẫn trong database
- Hoặc dùng cloud storage (Imgur, Cloudinary)

**❌ Database không update:**
- GitHub push thành công chưa?
- Streamlit Cloud có rebuild không?
- Check logs trong Streamlit Cloud dashboard

**🆘 Cần trợ giúp thêm?**
- Streamlit docs: https://docs.streamlit.io/streamlit-community-cloud
- Community forum: https://discuss.streamlit.io
- Liên hệ: huyralaco@live.com

## 📁 Cấu trúc File

```
analysis_color/
├── web_dashboard.py          # Main dashboard code
├── requirements_web.txt      # Python dependencies
├── RUN_WEB_DASHBOARD.bat    # Quick start script
├── DEPLOY_GUIDE.md          # Hướng dẫn deploy chi tiết
├── Data_result/
│   └── analysis.db          # SQLite database
└── Result_Img/              # Thư mục chứa ảnh kết quả
```

## ⚙️ Cấu hình

Dashboard tự động đọc dữ liệu từ:
- Database: `Data_result/analysis.db`
- Ảnh: `Result_Img/result_*.jpg`

Không cần config gì thêm!

## 🔄 Tự động cập nhật dữ liệu

Data tự động refresh mỗi 5-60 giây (tùy chỉnh trong sidebar).

Để sync dữ liệu mới từ phần mềm chính sang web:

**Cách 1: Local Network**
- Chạy dashboard trên cùng máy với app chính
- Dashboard tự động đọc database mới nhất

**Cách 2: Cloud Deploy**
- Upload file `analysis.db` mới lên GitHub
- Streamlit Cloud tự động deploy lại
- Hoặc dùng cloud database (PostgreSQL)

## 📱 Mobile Access

Dashboard responsive, xem tốt trên mọi thiết bị:
- Desktop: Full features
- Tablet: Responsive layout
- Mobile: Optimized view

Tạo shortcut trên mobile:
- iOS: Safari > Share > Add to Home Screen
- Android: Chrome > Menu > Add to Home Screen

## 🔒 Bảo mật

Nếu muốn thêm password protection, xem hướng dẫn trong [DEPLOY_GUIDE.md](DEPLOY_GUIDE.md).

## 🐛 Troubleshooting

**Q: Dashboard không hiển thị dữ liệu?**
- Kiểm tra file `Data_result/analysis.db` có tồn tại không
- Chạy app chính để tạo dữ liệu mẫu

**Q: Không thấy ảnh?**
- Kiểm tra folder `Result_Img/` có ảnh không
- Đảm bảo đường dẫn trong database đúng

**Q: Dashboard chạy chậm?**
- Giảm số dòng hiển thị (sidebar)
- Xóa ảnh cũ trong Result_Img
- Giảm tần suất auto-refresh

## 💻 Tech Stack

- **Framework**: Streamlit
- **Database**: SQLite
- **Images**: PIL/Pillow
- **Data**: Pandas

## 📧 Contact

Developer: huyralaco@live.com
Version: 1.0

## 📝 License

Proprietary - Ralaco Company
