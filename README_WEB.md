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

##### **1.1. Tạo tài khoản GitHub** (nếu chưa có):
   - Truy cập: https://github.com
   - Click "Sign up" và làm theo hướng dẫn
   - Xác nhận email

##### **1.2. Tạo repository mới**:
   - Đăng nhập GitHub
   - Click nút "**+**" góc phải trên > "**New repository**"
   - **Repository name**: `furnace-monitoring-dashboard` (hoặc tên bạn thích, không dấu)
   - **Description** (tùy chọn): "Glass Furnace Monitoring Dashboard"
   - Chọn **Public** (bắt buộc cho Streamlit Cloud free tier)
   - ✅ Check "**Add a README file**"
   - Click "**Create repository**" màu xanh

##### **1.3. Tạo cấu trúc thư mục trên GitHub**

**📁 Cấu trúc cần thiết:**
```
furnace-monitoring-dashboard/
├── web_dashboard.py          # File chính (BẮT BUỘC)
├── requirements.txt          # Dependencies (BẮT BUỘC)
├── README.md                 # Mô tả (tự động tạo)
├── Data_result/              # Folder database (BẮT BUỘC)
│   └── analysis.db          # SQLite database
└── Result_Img/              # Folder ảnh (khuyến nghị)
    ├── original_*.jpg
    └── result_*.jpg
```

**⚠️ QUAN TRỌNG**: Folder `Data_result/` và `Result_Img/` phải được tạo trước khi deploy!

##### **1.4. Upload file bằng GitHub Web Interface** (Dễ nhất cho người mới):

**Bước 1: Tạo file `requirements.txt`**
   - Trong repository, click "**Add file**" > "**Create new file**"
   - Tên file: `requirements.txt`
   - Copy và paste nội dung sau:
     ```
     streamlit>=1.28.0
     pandas>=2.0.0
     pillow>=10.0.0
     ```
   - Kéo xuống dưới, click "**Commit new file**" (nút màu xanh)

**Bước 2: Upload file `web_dashboard.py`**
   - Click "**Add file**" > "**Upload files**"
   - Kéo thả file `web_dashboard.py` từ máy tính vào
   - Đường dẫn file local: `d:\Ralaco\In progress\Binh phich\AI\AI_lo_phich\analysis_color\web_dashboard.py`
   - Click "**Commit changes**"

**Bước 3: Tạo folder `Data_result/` và upload database**
   - Click "**Add file**" > "**Upload files**"
   - Kéo thả file `analysis.db` vào
   - **QUAN TRỌNG**: Trước khi commit, sửa đường dẫn file thành:
     ```
     Data_result/analysis.db
     ```
     (GitHub tự động tạo folder khi bạn thêm `/` trong tên file)
   - Click "**Commit changes**"
   
   **❌ Nếu file database > 100MB:**
   - GitHub không cho upload file > 100MB
   - **Giải pháp**: Tạo database mẫu nhỏ hơn:
     ```bash
     # Chạy trên máy local để tạo database mẫu
     sqlite3 analysis_sample.db
     # Copy cấu trúc bảng, chỉ giữ 10-20 dòng data gần nhất
     ```
   - Hoặc dùng Git LFS (Large File Storage) - xem phần 1.5

**Bước 4: Tạo folder `Result_Img/` (tùy chọn nhưng khuyến nghị)**
   - Click "**Add file**" > "**Upload files**"
   - Chọn 2-3 ảnh mẫu (không quá 10MB/ảnh)
   - Sửa tên file thành: `Result_Img/result_001.jpg`, `Result_Img/original_001.jpg`, etc.
   - Click "**Commit changes**"

**Kiểm tra sau khi upload xong:**
- Repository của bạn phải có cấu trúc:
  ```
  ✅ web_dashboard.py
  ✅ requirements.txt
  ✅ Data_result/analysis.db
  ✅ Result_Img/ (ít nhất 1 ảnh)
  ```

##### **1.5. Upload bằng Git Command Line** (Cho người quen Git):

**Cài đặt Git** (nếu chưa có):
- Download: https://git-scm.com/download/win
- Install với cài đặt mặc định

**Các bước chi tiết:**

```bash
# Bước 1: Mở PowerShell/CMD, di chuyển vào thư mục dự án
cd "d:\Ralaco\In progress\Binh phich\AI\AI_lo_phich\analysis_color"

# Bước 2: Khởi tạo Git repository local
git init

# Bước 3: Cấu hình Git (lần đầu tiên)
git config --global user.name "Tên của bạn"
git config --global user.email "email@example.com"

# Bước 4: Thêm remote repository (thay YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/furnace-monitoring-dashboard.git

# Bước 5: Tạo file .gitignore để loại trừ file không cần
# Tạo file .gitignore với nội dung:
echo "__pycache__/" > .gitignore
echo "*.pyc" >> .gitignore
echo ".vscode/" >> .gitignore

# Bước 6: Thêm các file cần thiết
git add web_dashboard.py
git add requirements.txt
git add README_WEB.md

# Bước 7: Thêm dữ liệu (nếu < 100MB)
git add Data_result/analysis.db
git add Result_Img/*.jpg

# Bước 8: Commit
git commit -m "Initial commit: Glass furnace monitoring dashboard"

# Bước 9: Đổi tên branch thành main
git branch -M main

# Bước 10: Push lên GitHub (lần đầu tiên)
git push -u origin main
# Nhập username và password (hoặc Personal Access Token)
```

**❓ Nếu gặp lỗi authentication:**
- GitHub không còn hỗ trợ password từ 2021
- Cần dùng **Personal Access Token**:
  1. Vào GitHub > Settings > Developer settings > Personal access tokens > Tokens (classic)
  2. Click "Generate new token (classic)"
  3. Chọn scope: `repo` (full control)
  4. Copy token (chỉ hiện 1 lần!)
  5. Dùng token này thay cho password khi git push

**🔄 Cập nhật dữ liệu sau này:**
```bash
# Copy database mới từ app chính
cd "d:\Ralaco\In progress\Binh phich\AI\AI_lo_phich\analysis_color"

# Thêm các file thay đổi
git add Data_result/analysis.db Result_Img/*.jpg

# Commit với message mô tả
git commit -m "Update analysis data $(Get-Date -Format 'yyyy-MM-dd HH:mm')"

# Push lên GitHub
git push

# Streamlit Cloud tự động deploy lại sau 1-2 phút!
```

##### **1.6. Xử lý khi chưa có dữ liệu (Deploy lần đầu)**

Nếu bạn chưa có file `analysis.db` hoặc muốn tạo database mẫu:

**Option A: Chạy app chính để tạo dữ liệu**
- Chạy phần mềm phân tích chính 1 lần
- Sẽ tự động tạo `Data_result/analysis.db` với dữ liệu thật

**Option B: Tạo database mẫu bằng script**
- Tạo file `create_sample_db.py`:

```python
import sqlite3
import os
from datetime import datetime

# Tạo folder nếu chưa có
os.makedirs("Data_result", exist_ok=True)

# Tạo database
conn = sqlite3.connect("Data_result/analysis.db")
cursor = conn.cursor()

# Tạo bảng
cursor.execute("""
CREATE TABLE IF NOT EXISTS analysis_results (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    temperature REAL,
    ratio REAL,
    status TEXT,
    result TEXT,
    image_path TEXT,
    result_image_path TEXT,
    operator_name TEXT,
    glass_capacity REAL,
    power_consumption REAL
)
""")

# Thêm dữ liệu mẫu
sample_data = [
    (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 1450.5, 0.234, 
     'TAN ĐỀU', '✅ ĐẠT YÊU CẦU', 
     'Result_Img/original_001.jpg', 'Result_Img/result_001.jpg',
     'Nguyễn Văn A', 25.5, 0.875),
    (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 1425.3, 0.189,
     'TAN CHẬM', '⚠️ CẢNH BÁO - Xu hướng giảm',
     'Result_Img/original_002.jpg', 'Result_Img/result_002.jpg',
     'Trần Văn B', 24.2, 0.892),
]

cursor.executemany("""
INSERT INTO analysis_results 
(timestamp, temperature, ratio, status, result, image_path, 
 result_image_path, operator_name, glass_capacity, power_consumption)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
""", sample_data)

conn.commit()
conn.close()
print("✅ Created sample database: Data_result/analysis.db")
```

Chạy script:
```bash
python create_sample_db.py
```

**Option C: Sửa code để tạo database tự động**
Thêm vào đầu hàm `get_database_connection()` trong `web_dashboard.py`:

```python
def get_database_connection():
    app_dir = get_app_directory()
    db_path = os.path.join(app_dir, "Data_result", "analysis.db")
    
    # TẠO DATABASE MẪU NẾU CHƯA CÓ
    if not os.path.exists(db_path):
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE analysis_results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT,
                temperature REAL,
                ratio REAL,
                status TEXT,
                result TEXT,
                image_path TEXT,
                result_image_path TEXT,
                operator_name TEXT,
                glass_capacity REAL,
                power_consumption REAL
            )
        """)
        # Thêm 1 dòng mẫu
        cursor.execute("""
            INSERT INTO analysis_results VALUES 
            (1, datetime('now'), 1450.0, 0.25, 'TAN ĐỀU', 
             '✅ ĐẠT YÊU CẦU - Dữ liệu mẫu', '', '', 
             'Demo User', 25.0, 0.85)
        """)
        conn.commit()
        conn.close()
        st.info("📝 Đã tạo database mẫu. Hãy kết nối với app chính để có dữ liệu thật.")
    
    return db_path
```

**Sau khi có database**, upload lên GitHub theo hướng dẫn ở bước 1.4 hoặc 1.5.

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

#### **🔧 Troubleshooting - Xử lý lỗi khi Deploy**

---

### **❌ LỖI 1: "Không tìm thấy database: /mount/src/furnace-monitoring-dashboard/Data_result/analysis.db"**

**Nguyên nhân:** 
- Folder `Data_result/` hoặc file `analysis.db` chưa được upload lên GitHub
- Streamlit Cloud không tìm thấy file ở đường dẫn tương đối

**✅ GIẢI PHÁP CHI TIẾT:**

**Cách 1: Upload database lên GitHub (Khuyến nghị cho lần đầu)**

Trên máy local, mở PowerShell/Terminal:

```bash
# Bước 1: Di chuyển vào thư mục dự án
cd "d:\Ralaco\In progress\Binh phich\AI\AI_lo_phich\analysis_color"

# Bước 2: Kiểm tra file có tồn tại không
dir Data_result\analysis.db
# Nếu không có, chạy app chính để tạo dữ liệu hoặc dùng script tạo mẫu ở Bước 1.6

# Bước 3: Khởi tạo Git (nếu chưa làm)
git init

# Bước 4: Add remote (thay YOUR_USERNAME bằng username GitHub của bạn)
git remote add origin https://github.com/YOUR_USERNAME/furnace-monitoring-dashboard.git
# Hoặc nếu đã có remote, kiểm tra bằng: git remote -v

# Bước 5: Pull code hiện tại từ GitHub để tránh conflict
git pull origin main --allow-unrelated-histories

# Bước 6: Thêm database và ảnh
git add Data_result/analysis.db
git add Result_Img/*.jpg

# Bước 7: Commit
git commit -m "Add database and image files"

# Bước 8: Push lên GitHub
git push origin main

# Nếu gặp lỗi authentication:
# - Dùng Personal Access Token thay vì password
# - Tạo token tại: https://github.com/settings/tokens
# - Scope cần chọn: repo
```

**Sau khi push thành công:**
1. Đợi 1-2 phút
2. Vào https://share.streamlit.io
3. Click vào app của bạn
4. Nếu không tự động rebuild, click "⚙️ Manage app" > "⋮" > "Reboot app"
5. Chờ app restart và kiểm tra lại

**Cách 2: Upload qua GitHub Web (Nếu chưa quen Git)**

1. Truy cập repository trên GitHub: `https://github.com/YOUR_USERNAME/furnace-monitoring-dashboard`

2. **Upload database:**
   - Click "Add file" > "Upload files"
   - Kéo file `analysis.db` vào
   - ⚠️ **QUAN TRỌNG**: Trước khi commit, đổi tên file thành:
     ```
     Data_result/analysis.db
     ```
     (Thêm `Data_result/` vào trước tên file để tạo folder)
   - Click "Commit changes"

3. **Upload ảnh:**
   - Click "Add file" > "Upload files"
   - Kéo các file ảnh vào
   - Đổi tên thành: `Result_Img/original_001.jpg`, `Result_Img/result_001.jpg`, etc.
   - Click "Commit changes"

4. **Kiểm tra cấu trúc:**
   - Repository phải có:
     ```
     ✅ web_dashboard.py
     ✅ requirements.txt
     ✅ Data_result/
     │   └── analysis.db
     ✅ Result_Img/
         └── *.jpg
     ```

5. **Reboot app:**
   - Vào Streamlit Cloud dashboard
   - Click "Reboot app"
   - Đợi 2-5 phút để rebuild

**Cách 3: Tạo database tự động trong code (Best practice)**

Sửa file `web_dashboard.py`:

```python
import sqlite3
import os

def get_database_connection():
    """Get SQLite database connection with caching"""
    app_dir = get_app_directory()
    db_path = os.path.join(app_dir, "Data_result", "analysis.db")
    
    # ===== THÊM ĐOẠN NÀY =====
    # Tự động tạo database nếu chưa có
    if not os.path.exists(db_path):
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        
        # Tạo database và bảng
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS analysis_results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT NOT NULL,
                temperature REAL,
                ratio REAL,
                status TEXT,
                result TEXT,
                image_path TEXT,
                result_image_path TEXT,
                operator_name TEXT,
                glass_capacity REAL,
                power_consumption REAL
            )
        """)
        
        # Thêm dữ liệu mẫu để test
        from datetime import datetime
        cursor.execute("""
            INSERT INTO analysis_results 
            (timestamp, temperature, ratio, status, result, operator_name, glass_capacity, power_consumption)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            1450.0,
            0.250,
            'TAN ĐỀU',
            '✅ ĐẠT YÊU CẦU - Dữ liệu mẫu',
            'Demo User',
            25.0,
            0.850
        ))
        
        conn.commit()
        conn.close()
        
        st.warning("⚠️ Dashboard đang hiển thị dữ liệu mẫu. Kết nối với app chính để có dữ liệu thật.")
    # ===== HẾT ĐOẠN THÊM =====
    
    return db_path
```

Sau khi sửa:
```bash
git add web_dashboard.py
git commit -m "Auto-create database if not exists"
git push
```

---

### **❌ LỖI 2: "No module named 'streamlit'" hoặc ImportError**

**Nguyên nhân:** File `requirements.txt` không đúng format hoặc thiếu package

**✅ GIẢI PHÁP:**

1. **Kiểm tra file `requirements.txt` trên GitHub:**
   - Vào repository > Click vào file `requirements.txt`
   - Xem nội dung có đúng không:
     ```
     streamlit>=1.28.0
     pandas>=2.0.0
     pillow>=10.0.0
     ```

2. **Format đúng:**
   - Mỗi package một dòng
   - Không có dấu phẩy `,` giữa các dòng
   - Không có khoảng trắng thừa
   - Phải có version (hoặc dùng `>=` để lấy version mới nhất)

3. **Nếu sai format:**
   - Edit file trên GitHub:
     - Click vào `requirements.txt`
     - Click biểu tượng bút chì (Edit)
     - Sửa lại content
     - "Commit changes"
   
4. **Reboot app:**
   - Streamlit Cloud > Your app > "Reboot"

**Requirements.txt template đầy đủ:**
```txt
streamlit>=1.28.0
pandas>=2.0.0
pillow>=10.0.0
openpyxl>=3.1.0
```

---

### **❌ LỖI 3: "Chưa có dữ liệu phân tích. Vui lòng chạy phần mềm chính..."**

**Nguyên nhân:** Database đã có nhưng bảng trống hoặc không có records

**✅ GIẢI PHÁP:**

**Option A: Thêm dữ liệu mẫu vào database:**

Chạy script Python này trên máy local:

```python
import sqlite3
from datetime import datetime, timedelta
import random

# Kết nối database
conn = sqlite3.connect("Data_result/analysis.db")
cursor = conn.cursor()

# Tạo dữ liệu mẫu (10 records)
for i in range(10):
    timestamp = (datetime.now() - timedelta(hours=i)).strftime('%Y-%m-%d %H:%M:%S')
    temp = random.uniform(1400, 1500)
    ratio = random.uniform(0.15, 0.30)
    
    if ratio < 0.20:
        status = 'TAN CHẬM'
        result = '⚠️ CẢNH BÁO - Xu hướng giảm'
    elif ratio > 0.28:
        status = 'TAN QUÁ NHANH'
        result = '❌ KHÔNG ĐẠT - Cần giảm nhiệt độ'
    else:
        status = 'TAN ĐỀU'
        result = '✅ ĐẠT YÊU CẦU'
    
    cursor.execute("""
        INSERT INTO analysis_results 
        (timestamp, temperature, ratio, status, result, operator_name, glass_capacity, power_consumption)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (timestamp, temp, ratio, status, result, f'Vận hành {i+1}', 
          random.uniform(24.0, 26.0), random.uniform(0.85, 0.92)))

conn.commit()
conn.close()

print("✅ Đã thêm 10 records mẫu vào database")
```

Sau đó push database mới lên GitHub:
```bash
git add Data_result/analysis.db
git commit -m "Add sample data"
git push
```

**Option B: Kết nối với app chính:**
- Chạy phần mềm phân tích chính 1 lần
- Database sẽ được tạo tự động với dữ liệu thật
- Push lên GitHub

---

### **❌ LỖI 4: Ảnh không hiển thị**

**Nguyên nhân:** 
- Ảnh chưa được upload
- Đường dẫn trong database không khớp với file thực tế

**✅ GIẢI PHÁP:**

**Bước 1: Kiểm tra đường dẫn trong database:**
```python
import sqlite3
conn = sqlite3.connect("Data_result/analysis.db")
cursor = conn.cursor()
cursor.execute("SELECT image_path, result_image_path FROM analysis_results LIMIT 5")
for row in cursor.fetchall():
    print(row)
conn.close()
```

**Bước 2: Đường dẫn phải dạng tương đối:**
```
✅ ĐÚNG: Result_Img/original_001.jpg
❌ SAI: d:\Ralaco\...\Result_Img\original_001.jpg
❌ SAI: C:\Users\...\original_001.jpg
```

**Bước 3: Update đường dẫn nếu sai:**
```python
import sqlite3
conn = sqlite3.connect("Data_result/analysis.db")
cursor = conn.cursor()

# Update tất cả đường dẫn về dạng tương đối
cursor.execute("""
    UPDATE analysis_results
    SET image_path = 'Result_Img/' || 
        (CASE 
            WHEN image_path LIKE '%\\%' THEN substr(image_path, instr(image_path, '\\') + 1)
            ELSE image_path
        END)
""")

conn.commit()
conn.close()
```

**Bước 4: Upload ảnh lên GitHub:**
```bash
git add Result_Img/*.jpg
git add Data_result/analysis.db
git commit -m "Add images and fix paths"
git push
```

---

### **❌ LỖI 5: App chạy chậm, crash, hoặc "exceeded resource limits"**

**Nguyên nhân:** 
- Database quá lớn (>100MB)
- Quá nhiều ảnh
- Auto-refresh quá nhanh
- RAM vượt quá 1GB (giới hạn free tier)

**✅ GIẢI PHÁP:**

**1. Giảm kích thước database:**
```python
import sqlite3

conn = sqlite3.connect("Data_result/analysis.db")
cursor = conn.cursor()

# Chỉ giữ lại 100 records gần nhất
cursor.execute("""
    DELETE FROM analysis_results 
    WHERE id NOT IN (
        SELECT id FROM analysis_results 
        ORDER BY timestamp DESC 
        LIMIT 100
    )
""")

conn.commit()
conn.close()
```

**2. Giảm số lượng ảnh:**
- Chỉ giữ 20-30 ảnh gần nhất
- Nén ảnh xuống < 500KB/ảnh:
```python
from PIL import Image

def compress_image(input_path, output_path, max_size_kb=500):
    img = Image.open(input_path)
    
    # Resize nếu quá lớn
    max_dimension = 1024
    if max(img.size) > max_dimension:
        img.thumbnail((max_dimension, max_dimension), Image.Resampling.LANCZOS)
    
    # Lưu với quality thấp hơn
    quality = 85
    img.save(output_path, "JPEG", quality=quality, optimize=True)
```

**3. Tối ưu code:**

Thêm caching vào `web_dashboard.py`:
```python
import streamlit as st

@st.cache_data(ttl=60)  # Cache 60 seconds
def load_latest_analysis():
    # ... code hiện tại

@st.cache_data(ttl=300)  # Cache 5 minutes
def load_history_data(limit=10):
    # ... code hiện tại
```

**4. Điều chỉnh auto-refresh:**
- Trong sidebar, set refresh interval lên 30-60 giây
- Hoặc tắt auto-refresh nếu không cần realtime

**5. Check RAM usage:**
- Streamlit Cloud dashboard > Your app > "⋮" > "View logs"
- Tìm dòng "Memory usage"
- Nếu > 900MB, cần tối ưu thêm

---

### **❌ LỖI 6: Database không cập nhật sau khi push**

**Nguyên nhân:** 
- GitHub push chưa hoàn tất
- Streamlit Cloud chưa rebuild
- Cache browser

**✅ GIẢI PHÁP:**

**1. Kiểm tra GitHub:**
```bash
# Kiểm tra push đã thành công chưa
git log --oneline -n 5
git status
```

**2. Force rebuild Streamlit Cloud:**
- Vào https://share.streamlit.io
- Click vào app
- Click "⚙️ Manage app" > "⋮ More options" > "Reboot app"
- Chờ 2-5 phút

**3. Clear browser cache:**
- Ctrl + Shift + R (Windows)
- Cmd + Shift + R (Mac)
- Hoặc mở Incognito/Private window

**4. Check deployment logs:**
- Streamlit Cloud > Your app > "⋮" > "View logs"
- Xem có lỗi gì không
- Tìm dòng "Successfully deployed"

---

### **🆘 Checklist cho Deploy thành công:**

```
☐ Repository GitHub đã tạo (public)
☐ File web_dashboard.py đã upload
☐ File requirements.txt đã upload (format đúng)
☐ Folder Data_result/ đã tạo
☐ File analysis.db đã upload (hoặc code tự tạo)
☐ Folder Result_Img/ đã tạo (tùy chọn)
☐ Ảnh mẫu đã upload (tùy chọn)
☐ Đã connect Streamlit Cloud với GitHub
☐ Đã deploy app trên Streamlit Cloud
☐ App status = "Running" (màu xanh)
☐ Không có lỗi trong logs
☐ Dashboard hiển thị dữ liệu
```

**🆘 Vẫn gặp vấn đề?**
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
