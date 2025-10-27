import streamlit as st 
import pandas as pd 
 
# 设置页面标题 
st.title("Excel  文件读取器")
 
# 方法1：通过文件上传器上传Excel文件 
st.header(" 方法1：上传Excel文件")
uploaded_file = st.file_uploader(" 选择Excel文件", type=["xlsx", "xls"])
 
if uploaded_file is not None:
    try:
        # 读取Excel文件
        df = pd.read_excel(uploaded_file) 
        st.success(" 文件读取成功！")
        
        # 显示数据
        st.subheader(" 文件内容预览")
        st.dataframe(df) 
        
        # 显示统计信息 
        st.subheader(" 数据统计信息")
        st.write(df.describe()) 
        
    except Exception as e:
        st.error(f" 读取文件时出错: {e}")
 
# 方法2：直接读取固定路径的Excel文件 
st.header(" 方法2：读取固定路径的Excel文件")
 
# 在这里设置你的固定文件路径（示例路径，请替换成你的实际路径）
fixed_file_path = r"C:\Users\Administrator\Desktop\PH.xlsx"
 
if st.button(" 读取固定路径的文件"):
    try:
        # 读取Excel文件 
        df = pd.read_excel(fixed_file_path) 
        st.success(f" 文件读取成功！路径: {fixed_file_path}")
        
        # 显示数据
        st.subheader(" 文件内容预览")
        st.dataframe(df) 
        
        # 显示统计信息
        st.subheader(" 数据统计信息")
        st.write(df.describe()) 
        
    except FileNotFoundError:
        st.error(f" 文件未找到，请检查路径: {fixed_file_path}")
    except Exception as e:
        st.error(f" 读取文件时出错: {e}")
 
# 添加一些说明
st.markdown(""" 
### 使用说明 
- **方法1**：直接上传Excel文件（支持.xlsx和.xls格式）
- **方法2**：读取代码中预设路径的Excel文件（请确保路径正确）
""")