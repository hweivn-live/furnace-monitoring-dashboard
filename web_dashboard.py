#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
WEB DASHBOARD - FURNACE MONITORING SYSTEM
Real-time monitoring dashboard for glass furnace analysis
Giám sát trực tuyến trạng thái lò nấu phích
"""

import streamlit as st
import sqlite3
import pandas as pd
import os
import sys
from datetime import datetime
from PIL import Image
import time

# ============================
# PAGE CONFIGURATION
# ============================
st.set_page_config(
    page_title="Giám sát Lò Nấu Phích",
    page_icon="🔥",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================
# CUSTOM CSS
# ============================
st.markdown("""
<style>
    /* Header styling */
    .main-header {
        background: linear-gradient(90deg, #1e3c72 0%, #2a5298 100%);
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 20px;
    }
    .main-header h1 {
        color: white;
        font-size: 28px;
        font-weight: bold;
        margin: 0;
    }
    
    /* Status banner styling */
    .status-banner {
        padding: 15px;
        border-radius: 8px;
        margin: 10px 0;
        font-size: 16px;
        font-weight: bold;
        text-align: center;
    }
    .status-success {
        background-color: #d4edda;
        color: #155724;
        border-left: 5px solid #28a745;
    }
    .status-warning {
        background-color: #fff3cd;
        color: #856404;
        border-left: 5px solid #ffc107;
    }
    .status-danger {
        background-color: #f8d7da;
        color: #721c24;
        border-left: 5px solid #dc3545;
    }
    
    /* Metrics styling */
    .metric-container {
        background-color: #f8f9fa;
        padding: 15px;
        border-radius: 8px;
        text-align: center;
        border: 2px solid #e9ecef;
    }
    
    /* Image section styling */
    .image-section {
        border: 2px solid #dee2e6;
        border-radius: 8px;
        padding: 10px;
        background-color: white;
    }
    .image-title {
        text-align: center;
        font-weight: bold;
        margin-bottom: 10px;
        color: #495057;
    }
    
    /* Table styling */
    .dataframe {
        font-size: 14px;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        padding: 20px;
        color: #6c757d;
        font-size: 14px;
        margin-top: 30px;
        border-top: 1px solid #dee2e6;
    }
</style>
""", unsafe_allow_html=True)

# ============================
# HELPER FUNCTIONS
# ============================

def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        # Not running as .exe, use script directory
        try:
            base_path = os.path.dirname(os.path.abspath(__file__))
        except NameError:
            base_path = os.path.dirname(os.path.abspath(sys.argv[0]))
    
    return os.path.join(base_path, relative_path)

def get_app_directory():
    """Get the directory where .exe or script is located"""
    try:
        # If running as .exe, use executable directory
        if getattr(sys, 'frozen', False):
            return os.path.dirname(sys.executable)
        else:
            # Running as script
            return os.path.dirname(os.path.abspath(__file__))
    except:
        return os.getcwd()

@st.cache_resource
def get_database_connection():
    """Get SQLite database connection with caching"""
    # Use app directory (where .exe or script is) for Data_result folder
    app_dir = get_app_directory()
    db_path = os.path.join(app_dir, "Data_result", "analysis.db")
    if not os.path.exists(db_path):
        st.error(f"❌ Không tìm thấy database: {db_path}")
        return None
    return db_path

def load_latest_analysis():
    """Load the latest analysis result from database"""
    db_path = get_database_connection()
    if db_path is None:
        return None
    
    try:
        conn = sqlite3.connect(db_path, timeout=5.0)
        query = """
            SELECT 
                timestamp,
                temperature,
                ratio,
                status,
                result,
                image_path,
                result_image_path,
                operator_name,
                glass_capacity,
                power_consumption
            FROM analysis_results
            ORDER BY timestamp DESC
            LIMIT 1
        """
        df = pd.read_sql_query(query, conn)
        conn.close()
        
        if len(df) == 0:
            return None
        return df.iloc[0]
    except Exception as e:
        st.error(f"❌ Lỗi đọc database: {e}")
        return None

def load_history_data(limit=10):
    """Load historical analysis data"""
    db_path = get_database_connection()
    if db_path is None:
        return pd.DataFrame()
    
    try:
        conn = sqlite3.connect(db_path, timeout=5.0)
        query = f"""
            SELECT 
                timestamp AS 'Thời gian',
                ratio AS 'Điểm hồng',
                temperature AS 'T° nóc',
                status AS 'Tan chảy',
                result AS 'Trạng thái',
                glass_capacity AS 'Tấn/ngày',
                power_consumption AS 'kWh/kg',
                operator_name AS 'Vận hành'
            FROM analysis_results
            ORDER BY timestamp DESC
            LIMIT {limit}
        """
        df = pd.read_sql_query(query, conn)
        conn.close()
        
        # Format các cột
        if 'Điểm hồng' in df.columns:
            df['Điểm hồng'] = df['Điểm hồng'].apply(lambda x: f"{x:.3f}" if pd.notnull(x) else "")
        if 'Tấn/ngày' in df.columns:
            df['Tấn/ngày'] = df['Tấn/ngày'].apply(lambda x: f"{x:.1f}" if pd.notnull(x) else "")
        if 'kWh/kg' in df.columns:
            df['kWh/kg'] = df['kWh/kg'].apply(lambda x: f"{x:.3f}" if pd.notnull(x) else "")
            
        return df
    except Exception as e:
        st.error(f"❌ Lỗi đọc lịch sử: {e}")
        return pd.DataFrame()

def load_image_safe(image_path):
    """Load image safely with error handling"""
    if not image_path or not os.path.exists(image_path):
        return None
    try:
        return Image.open(image_path)
    except Exception as e:
        st.warning(f"⚠️ Không thể tải ảnh: {e}")
        return None

def count_total_records():
    """Count total number of analysis records"""
    db_path = get_database_connection()
    if db_path is None:
        return 0
    
    try:
        conn = sqlite3.connect(db_path, timeout=5.0)
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM analysis_results")
        count = cursor.fetchone()[0]
        conn.close()
        return count
    except:
        return 0

# ============================
# MAIN DASHBOARD
# ============================

def main():
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>🔥 AI - PHÂN TÍCH TRẠNG THÁI PHỐI LIỆU LÒ PHÍCH</h1>
        <p style="color: #e9ecef; margin: 5px 0 0 0;">Glass Furnace Status Analysis System - Real-time Monitoring</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Auto-refresh sidebar
    with st.sidebar:
        st.title("⚙️ Cài đặt")
        auto_refresh = st.checkbox("🔄 Tự động làm mới", value=True)
        refresh_interval = st.slider("Chu kỳ cập nhật (giây)", 5, 60, 10)
        history_limit = st.slider("Số dòng hiển thị", 5, 50, 10)
        
        st.divider()
        st.caption("📊 Thống kê")
        total_records = count_total_records()
        st.metric("Tổng số phân tích", total_records)
        
    # Load latest data
    latest = load_latest_analysis()
    
    if latest is None:
        st.warning("⚠️ Chưa có dữ liệu phân tích. Vui lòng chạy phần mềm chính để thu thập dữ liệu.")
        return
    
    # Status Banner
    status_text = latest.get('status', 'Không xác định')
    result_text = latest.get('result', '')
    
    if 'ĐẠT' in result_text.upper() or 'ĐẠT YÊU CẦU' in result_text.upper():
        banner_class = "status-success"
        icon = "✅"
    elif 'CẢNH BÁO' in result_text.upper() or 'XU HƯỚNG' in result_text.upper():
        banner_class = "status-warning"
        icon = "⚠️"
    else:
        banner_class = "status-danger"
        icon = "❌"
    
    st.markdown(f"""
    <div class="status-banner {banner_class}">
        {icon} {result_text}
    </div>
    """, unsafe_allow_html=True)
    
    # Metrics Row
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
        <div class="metric-container">
            <div style="font-size: 14px; color: #6c757d;">📊 Số tin hiệu đã nhận</div>
            <div style="font-size: 24px; font-weight: bold; color: #007bff;">{total_records}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="metric-container">
            <div style="font-size: 14px; color: #6c757d;">📸 Lần chụp</div>
            <div style="font-size: 24px; font-weight: bold; color: #28a745;">{total_records}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        temp = latest.get('temperature', 'N/A')
        st.markdown(f"""
        <div class="metric-container">
            <div style="font-size: 14px; color: #6c757d;">🌡️ T° nóc lò nấu</div>
            <div style="font-size: 24px; font-weight: bold; color: #dc3545;">{temp}</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Images Section
    col_img1, col_img2, col_recommendation = st.columns([1, 1, 1])
    
    with col_img1:
        st.markdown('<div class="image-section">', unsafe_allow_html=True)
        st.markdown('<div class="image-title">📷 ẢNH GỐC</div>', unsafe_allow_html=True)
        original_img_path = latest.get('image_path', '')
        if original_img_path and os.path.exists(original_img_path):
            img = load_image_safe(original_img_path)
            if img:
                st.image(img, width='stretch')
        else:
            st.info("Không có ảnh gốc")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col_img2:
        st.markdown('<div class="image-section">', unsafe_allow_html=True)
        st.markdown('<div class="image-title">🔍 ẢNH ĐÃ PHÂN TÍCH</div>', unsafe_allow_html=True)
        result_img_path = latest.get('result_image_path', '')
        if result_img_path and os.path.exists(result_img_path):
            img = load_image_safe(result_img_path)
            if img:
                st.image(img, width='stretch')
        else:
            st.info("Không có ảnh kết quả")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col_recommendation:
        st.markdown('<div class="image-section">', unsafe_allow_html=True)
        st.markdown('<div class="image-title">💡 ĐỀ XUẤT</div>', unsafe_allow_html=True)
        
        # Hiển thị thông tin phân tích
        ratio = latest.get('ratio', 0)
        if ratio:
            st.markdown(f"**Điểm hồng:** {ratio:.3f}")
        
        st.markdown(f"**Trạng thái:** {status_text}")
        st.markdown(f"**Kết luận:** {result_text}")
        
        # Thêm thông tin vận hành
        if latest.get('operator_name'):
            st.markdown(f"**Vận hành:** {latest.get('operator_name')}")
        
        capacity = latest.get('glass_capacity')
        if capacity:
            st.markdown(f"**Sản lượng:** {capacity:.1f} tấn/ngày")
        
        power = latest.get('power_consumption')
        if power:
            st.markdown(f"**Điện năng:** {power:.3f} kWh/kg")
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # History Table
    st.subheader("📊 LỊCH SỬ PHÂN TÍCH")
    history_df = load_history_data(limit=history_limit)
    
    if not history_df.empty:
        st.dataframe(
            history_df,
            width='stretch',
            hide_index=True,
            height=400
        )
    else:
        st.info("Chưa có dữ liệu lịch sử")
    
    # Footer
    st.markdown(f"""
    <div class="footer">
        <p>🕐 Cập nhật lần cuối: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
        <p>💻 Developed by huyralaco@live.com | Version 1.0</p>
        <p style="font-size: 12px; color: #adb5bd;">Vì trí camera lò nấu luôn để ở vị trí 1/4 phía trên bên phải của phần mềm SmartPSS</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Auto-refresh
    if auto_refresh:
        time.sleep(refresh_interval)
        st.rerun()

# ============================
# RUN APP
# ============================

if __name__ == "__main__":
    main()
