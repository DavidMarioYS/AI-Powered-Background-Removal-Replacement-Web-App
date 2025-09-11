# # import streamlit as st
# # from rembg import remove
# # from PIL import Image
# # import io

# # # Mengatur konfigurasi halaman agar terlihat lebih profesional
# # st.set_page_config(
# #     page_title="Editor Latar Belakang Gambar",
# #     page_icon="🖼️",
# #     layout="centered",
# #     initial_sidebar_state="auto",
# # )

# # def process_image(image_bytes, operation, color=None):
# #     """
# #     Fungsi utama untuk memproses gambar.
# #     - Menghapus background.
# #     - Mengubah warna background.
# #     """
# #     try:
# #         # Buka gambar dari bytes
# #         original_image = Image.open(io.BytesIO(image_bytes)).convert("RGBA")

# #         # Hapus background menggunakan rembg
# #         image_no_bg = remove(original_image)

# #         if operation == "remove_only":
# #             # Jika hanya hapus background, kembalikan gambar dengan bg transparan
# #             return image_no_bg

# #         elif operation == "change_color":
# #             # Buat background baru dengan warna yang dipilih
# #             background = Image.new("RGBA", image_no_bg.size, color)
            
# #             # Tempelkan gambar tanpa background (foreground) ke atas background berwarna
# #             # Menggunakan alpha_composite untuk blending yang lebih baik
# #             final_image = Image.alpha_composite(background, image_no_bg)
# #             return final_image

# #     except Exception as e:
# #         st.error(f"Terjadi kesalahan saat memproses gambar: {e}")
# #         return None

# # def image_to_bytes(image):
# #     """Mengubah objek gambar PIL menjadi bytes untuk diunduh."""
# #     buf = io.BytesIO()
# #     image.save(buf, format="PNG")
# #     byte_im = buf.getvalue()
# #     return byte_im

# # # --- UI Streamlit ---

# # st.title("🖼️ Editor Latar Belakang Gambar")
# # st.caption("Dibuat dengan Streamlit & Rembg")

# # st.markdown("""
# # Aplikasi ini memungkinkan Anda untuk melakukan dua hal:
# # 1.  **Menghapus Latar Belakang**: Membuat latar belakang gambar menjadi transparan.
# # 2.  **Mengubah Warna Latar Belakang**: Mengganti latar belakang dengan warna solid (merah atau biru).
# # """)

# # # Area untuk mengunggah file
# # uploaded_file = st.file_uploader(
# #     "Pilih sebuah gambar...", 
# #     type=["png", "jpg", "jpeg"],
# #     help="Unggah gambar yang ingin Anda edit latar belakangnya."
# # )

# # if uploaded_file is not None:
# #     # Tampilkan gambar asli dalam dua kolom agar rapi
# #     col1, col2 = st.columns(2)
# #     with col1:
# #         st.subheader("Gambar Asli")
# #         st.image(uploaded_file, use_container_width=True)

# #     # Dapatkan bytes dari file yang diunggah
# #     image_bytes = uploaded_file.getvalue()

# #     # Pilihan operasi di kolom kedua
# #     with col2:
# #         st.subheader("Pilih Operasi")
        
# #         operation = st.radio(
# #             "Pilih tindakan yang ingin Anda lakukan:",
# #             ('Hapus Latar Belakang', 'Ubah Warna Latar Belakang'),
# #             key="operation_choice"
# #         )

# #         processed_image = None
# #         file_name = "hasil.png"

# #         if operation == 'Hapus Latar Belakang':
# #             if st.button("🚀 Proses Sekarang!", key="remove_btn"):
# #                 with st.spinner('Menghapus latar belakang...'):
# #                     processed_image = process_image(image_bytes, "remove_only")
# #                     file_name = "gambar_tanpa_background.png"
        
# #         elif operation == 'Ubah Warna Latar Belakang':
# #             color_name = st.selectbox(
# #                 'Pilih warna baru:',
# #                 ('Biru', 'Merah'),
# #                 key="color_select"
# #             )
            
# #             color_map = {
# #                 "Biru": (0, 102, 255, 255),  # Biru (R, G, B, A)
# #                 "Merah": (255, 0, 0, 255)    # Merah (R, G, B, A)
# #             }
# #             selected_color = color_map[color_name]

# #             if st.button("🚀 Proses Sekarang!", key="change_color_btn"):
# #                 with st.spinner(f'Mengubah latar belakang menjadi {color_name.lower()}...'):
# #                     processed_image = process_image(image_bytes, "change_color", color=selected_color)
# #                     file_name = f"gambar_background_{color_name.lower()}.png"

# #         # Tampilkan hasil jika proses selesai
# #         if processed_image:
# #             st.subheader("Hasil")
# #             st.image(processed_image, use_container_width=True)
            
# #             # Tombol untuk mengunduh hasil
# #             st.download_button(
# #                 label="📥 Unduh Hasil Gambar",
# #                 data=image_to_bytes(processed_image),
# #                 file_name=file_name,
# #                 mime="image/png"
# #             )
# # else:
# #     st.info("Silakan unggah sebuah gambar untuk memulai.")

# import streamlit as st
# from rembg import remove
# from PIL import Image
# import io

# # --- KONFIGURASI HALAMAN ---
# st.set_page_config(
#     page_title="Magic Background Editor",
#     page_icon="✨",
#     layout="wide",
#     initial_sidebar_state="collapsed",
# )

# # --- CSS KUSTOM UNTUK TAMPILAN ELEGAN ---
# st.markdown("""
# <style>
# /* Style untuk container utama (kartu) */
# .card-container {
#     border: 1px solid rgba(255, 255, 255, 0.2);
#     background: rgba(255, 255, 255, 0.05);
#     border-radius: 10px;
#     padding: 20px;
#     margin-bottom: 20px;
#     box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
#     backdrop-filter: blur(5px);
#     -webkit-backdrop-filter: blur(5px);
# }

# /* Style untuk tombol utama */
# .stButton>button {
#     background-color: #4F8BF9;
#     color: white;
#     border-radius: 50px;
#     padding: 10px 25px;
#     border: none;
#     font-weight: bold;
#     transition: all 0.3s ease;
# }
# .stButton>button:hover {
#     background-color: #3A6DC2;
#     transform: scale(1.05);
#     box-shadow: 0px 5px 15px rgba(79, 139, 249, 0.4);
# }

# /* Style untuk tombol download minimalis */
# .stDownloadButton>button {
#     background-color: transparent;
#     color: #FFFFFF;
#     border: 1px solid #FFFFFF;
#     border-radius: 5px;
#     padding: 8px 16px;
#     font-weight: normal;
# }
# .stDownloadButton>button:hover {
#     background-color: rgba(255, 255, 255, 0.1);
#     color: #FFFFFF;
# }

# /* Style untuk file uploader */
# [data-testid="stFileUploader"] {
#     border: 2px dashed #4F8BF9;
#     background-color: rgba(79, 139, 249, 0.05);
#     padding: 20px;
#     border-radius: 10px;
# }
# </style>
# """, unsafe_allow_html=True)


# # --- FUNGSI HELPER ---
# def process_image(image_bytes, operation, color=None):
#     try:
#         original_image = Image.open(io.BytesIO(image_bytes)).convert("RGBA")
#         if operation == "remove_only":
#             return remove(original_image)
#         elif operation == "change_color":
#             image_no_bg = remove(original_image)
#             background = Image.new("RGBA", image_no_bg.size, color)
#             final_image = Image.alpha_composite(background, image_no_bg)
#             return final_image
#     except Exception as e:
#         st.error(f"Oops! Terjadi kesalahan: {e}")
#         return None

# def crop_image(image, aspect_ratio_str):
#     """Fungsi untuk memotong gambar dari tengah sesuai rasio aspek."""
#     aspect_map = {"2x3": 2/3, "3x4": 3/4, "4x6": 4/6}
#     target_aspect = aspect_map[aspect_ratio_str]
    
#     img_width, img_height = image.size
#     original_aspect = img_width / img_height

#     if original_aspect > target_aspect:
#         new_width = int(target_aspect * img_height)
#         new_height = img_height
#     else:
#         new_width = img_width
#         new_height = int(img_width / target_aspect)

#     left = (img_width - new_width) / 2
#     top = (img_height - new_height) / 2
#     right = (img_width + new_width) / 2
#     bottom = (img_height + new_height) / 2

#     return image.crop((left, top, right, bottom))

# def image_to_bytes(image):
#     buf = io.BytesIO()
#     image.save(buf, format="PNG")
#     return buf.getvalue()

# # --- INISIALISASI SESSION STATE ---
# if 'processed_image' not in st.session_state:
#     st.session_state.processed_image = None
# if 'original_filename' not in st.session_state:
#     st.session_state.original_filename = "hasil"

# # --- UI APLIKASI ---
# st.title("✨ Magic Background Editor")
# st.markdown("Unggah gambar, hapus atau ubah latar belakang, lalu unduh dalam berbagai ukuran pas foto.")

# # 1. KARTU UNTUK UPLOAD GAMBAR
# with st.container():
#     st.markdown('<div class="card-container">', unsafe_allow_html=True)
#     uploaded_file = st.file_uploader(
#         "Pilih sebuah gambar...", 
#         type=["png", "jpg", "jpeg"],
#         label_visibility="collapsed"
#     )
#     st.markdown('</div>', unsafe_allow_html=True)


# if uploaded_file is not None:
#     st.session_state.original_filename = uploaded_file.name.split('.')[0]
    
#     col1, col2 = st.columns(2)

#     # 2. KARTU UNTUK GAMBAR ASLI DAN KONTROL
#     with col1:
#         st.markdown('<div class="card-container">', unsafe_allow_html=True)
#         st.subheader("🖼️ Gambar Asli")
#         st.image(uploaded_file, use_container_width=True, caption="Gambar yang Anda unggah")
#         st.markdown('</div>', unsafe_allow_html=True)

#     with col2:
#         st.markdown('<div class="card-container">', unsafe_allow_html=True)
#         st.subheader("⚙️ Panel Kontrol Utama")
#         operation = st.radio(
#             "Pilih tindakan utama:",
#             ('Hapus Latar Belakang', 'Ubah Warna Latar Belakang'),
#             key="operation_choice",
#             horizontal=True
#         )

#         selected_color = None
#         if operation == 'Ubah Warna Latar Belakang':
#             color_name = st.selectbox('Pilih warna baru:', ('Merah', 'Hijau', 'Biru'), key="color_select")
#             color_map = {"Merah": (255, 0, 0, 255), "Hijau": (0, 255, 0, 255), "Biru": (0, 0, 255, 255)}
#             selected_color = color_map[color_name]

#         if st.button("🚀 Proses Sekarang!", use_container_width=True):
#             with st.spinner('Sedang memproses...'):
#                 image_bytes = uploaded_file.getvalue()
#                 if operation == 'Hapus Latar Belakang':
#                     st.session_state.processed_image = process_image(image_bytes, "remove_only")
#                 elif operation == 'Ubah Warna Latar Belakang':
#                     st.session_state.processed_image = process_image(image_bytes, "change_color", color=selected_color)
#             st.success("Gambar berhasil diproses!")
#         st.markdown('</div>', unsafe_allow_html=True)

# # 4. KARTU UNTUK HASIL GAMBAR
# if st.session_state.processed_image:
#     st.markdown("---")
    
#     with st.container():
#         st.markdown('<div class="card-container">', unsafe_allow_html=True)
#         st.subheader("🎉 Hasil Akhir & Pilihan Ukuran Pas Foto")
#         st.write("Pilih dan unduh ukuran yang Anda inginkan di bawah ini.")
        
#         # Membuat kolom dengan lebar yang berbeda untuk merepresentasikan rasio
#         col_ratios = st.columns([2, 3, 4]) 
#         crop_ratios = ['2x3', '3x4', '4x6']

#         for i, ratio in enumerate(crop_ratios):
#             with col_ratios[i]:
#                 st.markdown(f"**Ukuran {ratio}**")
                
#                 # Proses crop untuk preview
#                 cropped_img = crop_image(st.session_state.processed_image, ratio)
#                 st.image(cropped_img, use_container_width=True)
                
#                 # Tombol download untuk setiap ukuran
#                 st.download_button(
#                     label=f"Unduh {ratio}",
#                     data=image_to_bytes(cropped_img),
#                     file_name=f"{st.session_state.original_filename}_pas_foto_{ratio}.png",
#                     mime="image/png",
#                     use_container_width=True,
#                     key=f"download_{ratio}"
#                 )
#         st.markdown('</div>', unsafe_allow_html=True)

# else:
#     st.info("☝️ Silakan unggah gambar untuk memulai proses editing.")

import streamlit as st
from rembg import remove
from PIL import Image
import io

# --- KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="Magic Background Editor",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# --- CSS KUSTOM UNTUK TAMPILAN ELEGAN ---
st.markdown("""
<style>
.card-container {
    border: 1px solid rgba(255, 255, 255, 0.2);
    background: rgba(255, 255, 255, 0.05);
    border-radius: 10px;
    padding: 20px;
    margin-bottom: 20px;
    box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
    backdrop-filter: blur(5px);
    -webkit-backdrop-filter: blur(5px);
}
.stButton>button {
    background-color: #4F8BF9;
    color: white;
    border-radius: 50px;
    padding: 10px 25px;
    border: none;
    font-weight: bold;
    transition: all 0.3s ease;
}
.stButton>button:hover {
    background-color: #3A6DC2;
    transform: scale(1.05);
    box-shadow: 0px 5px 15px rgba(79, 139, 249, 0.4);
}
.stDownloadButton>button {
    background-color: transparent;
    color: #FFFFFF;
    border: 1px solid #FFFFFF;
    border-radius: 5px;
    padding: 8px 16px;
    font-weight: normal;
}
.stDownloadButton>button:hover {
    background-color: rgba(255, 255, 255, 0.1);
    color: #FFFFFF;
}
[data-testid="stFileUploader"] {
    border: 2px dashed #4F8BF9;
    background-color: rgba(79, 139, 249, 0.05);
    padding: 20px;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# --- FUNGSI HELPER ---
def process_image(image_bytes, operation, color=None):
    """
    operation:
      - 'remove_only'   : hapus latar, transparan
      - 'solid_bg'      : jadikan latar solid (Red/Blue/White)
    """
    try:
        original_image = Image.open(io.BytesIO(image_bytes)).convert("RGBA")

        if operation == "remove_only":
            # PNG transparan (tanpa latar)
            return remove(original_image)

        elif operation == "solid_bg":
            # 1) Hapus latar
            image_no_bg = remove(original_image)  # RGBA, foreground dgn alpha
            # 2) Siapkan kanvas warna solid penuh (alpha 255)
            solid = Image.new("RGBA", image_no_bg.size, color)
            # 3) Tempelkan foreground pakai alpha sebagai mask -> hasil latar solid total
            solid.paste(image_no_bg, (0, 0), mask=image_no_bg.split()[-1])
            return solid.convert("RGBA")

    except Exception as e:
        st.error(f"Oops! Terjadi kesalahan: {e}")
        return None

def crop_image(image, aspect_ratio_str):
    """Potong dari tengah sesuai rasio aspek (opsional saat unduh)."""
    aspect_map = {"2x3": 2/3, "3x4": 3/4, "4x6": 4/6}
    target_aspect = aspect_map[aspect_ratio_str]

    img_width, img_height = image.size
    original_aspect = img_width / img_height

    if original_aspect > target_aspect:
        new_width = int(target_aspect * img_height)
        new_height = img_height
    else:
        new_width = img_width
        new_height = int(img_width / target_aspect)

    left = (img_width - new_width) / 2
    top = (img_height - new_height) / 2
    right = (img_width + new_width) / 2
    bottom = (img_height + new_height) / 2

    return image.crop((left, top, right, bottom))

def image_to_bytes(image, fmt="PNG"):
    buf = io.BytesIO()
    image.save(buf, format=fmt)
    return buf.getvalue()

# --- INISIALISASI SESSION STATE ---
if 'processed_image' not in st.session_state:
    st.session_state.processed_image = None
if 'original_filename' not in st.session_state:
    st.session_state.original_filename = "hasil"

# --- UI APLIKASI ---
st.title("✨ Magic Background Editor")
st.markdown("Unggah gambar, hapus/ubah latar belakang **tanpa harus crop**, lalu (opsional) unduh versi pas foto.")

# 1) Upload
with st.container():
    st.markdown('<div class="card-container">', unsafe_allow_html=True)
    uploaded_file = st.file_uploader(
        "Pilih sebuah gambar...",
        type=["png", "jpg", "jpeg"],
        label_visibility="collapsed"
    )
    st.markdown('</div>', unsafe_allow_html=True)

if uploaded_file is not None:
    st.session_state.original_filename = uploaded_file.name.split('.')[0]

    col1, col2 = st.columns(2)

    # 2) Preview asli
    with col1:
        st.markdown('<div class="card-container">', unsafe_allow_html=True)
        st.subheader("🖼️ Gambar Asli")
        st.image(uploaded_file, use_container_width=True, caption="Gambar yang Anda unggah")
        st.markdown('</div>', unsafe_allow_html=True)

    # 3) Panel kontrol (tanpa wajib crop)
    with col2:
        st.markdown('<div class="card-container">', unsafe_allow_html=True)
        st.subheader("⚙️ Panel Kontrol Utama")

        operation = st.radio(
            "Pilih tindakan:",
            ('Hapus Latar (Transparan)', 'Ubah ke Warna Solid'),
            key="operation_choice",
            horizontal=True
        )

        selected_color = None
        if operation == 'Ubah ke Warna Solid':
            color_name = st.selectbox('Pilih warna latar:', ('Red', 'Blue', 'White'), key="color_select")
            color_map = {
                "Red":   (255, 0,   0,   255),
                "Blue":  (0,   0,   255, 255),
                "White": (255, 255, 255, 255),
            }
            selected_color = color_map[color_name]

        if st.button("🚀 Proses Sekarang!", use_container_width=True):
            with st.spinner('Sedang memproses...'):
                image_bytes = uploaded_file.getvalue()
                if operation == 'Hapus Latar (Transparan)':
                    st.session_state.processed_image = process_image(image_bytes, "remove_only")
                else:
                    st.session_state.processed_image = process_image(image_bytes, "solid_bg", color=selected_color)
            if st.session_state.processed_image is not None:
                st.success("Gambar berhasil diproses!")
        st.markdown('</div>', unsafe_allow_html=True)

# 4) Hasil (tanpa harus crop dulu)
if st.session_state.processed_image:
    st.markdown("---")
    with st.container():
        st.markdown('<div class="card-container">', unsafe_allow_html=True)
        st.subheader("🎉 Hasil Akhir")

        # Tampilkan hasil langsung (full size, tanpa crop)
        st.image(st.session_state.processed_image, use_container_width=True, caption="Hasil tanpa crop")

        # Unduh hasil tanpa crop (asli)
        st.download_button(
            label="Unduh (Tanpa Crop)",
            data=image_to_bytes(st.session_state.processed_image, fmt="PNG"),
            file_name=f"{st.session_state.original_filename}_final.png",
            mime="image/png",
            use_container_width=True,
            key="download_original"
        )

        st.markdown("### 📐 Opsi Pas Foto (opsional)")
        st.write("Silakan pilih ukuran jika ingin pas foto. Jika tidak perlu, lewati saja bagian ini.")
        col_ratios = st.columns([2, 3, 4])
        crop_ratios = ['2x3', '3x4', '4x6']

        for i, ratio in enumerate(crop_ratios):
            with col_ratios[i]:
                st.markdown(f"**Ukuran {ratio}**")
                cropped_img = crop_image(st.session_state.processed_image, ratio)
                st.image(cropped_img, use_container_width=True)
                st.download_button(
                    label=f"Unduh {ratio}",
                    data=image_to_bytes(cropped_img, fmt="PNG"),
                    file_name=f"{st.session_state.original_filename}_pas_foto_{ratio}.png",
                    mime="image/png",
                    use_container_width=True,
                    key=f"download_{ratio}"
                )
        st.markdown('</div>', unsafe_allow_html=True)
else:
    st.info("☝️ Silakan unggah dan proses gambar terlebih dahulu.")
