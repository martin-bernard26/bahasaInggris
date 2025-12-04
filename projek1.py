import streamlit as st
import numpy as np
import pandas as pd
from statistics import mean, median, mode, stdev, multimode
import matplotlib.pyplot as plt
from scipy.stats import norm, f, t, wilcoxon, pearsonr, ttest_rel
import requests
import base64
import math
import seaborn as sns
from scipy import stats
import plotly.graph_objects as go
import plotly.express as px
from io import StringIO
import seaborn as sns
from scipy import stats
from scipy.stats import shapiro, normaltest, anderson, kstest
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from scipy.stats import f_oneway
from itertools import combinations
import warnings

warnings.filterwarnings('ignore')

st.set_page_config(
    page_title="Aplikasi Upload ke Google Drive",
    page_icon="📤",
    layout="wide",
    initial_sidebar_state="expanded"
)

if "tampilan1" not in st.session_state:
    st.session_state.tampilan1 = False

if "tampilan2" not in st.session_state:
    st.session_state.tampilan2 = False

if "tampilan3" not in st.session_state:
    st.session_state.tampilan3 = True

if "tampilan4" not in st.session_state:
    st.session_state.tampilan4 = False

if "tampilan5" not in st.session_state:
    st.session_state.tampilan5 = False

if "tampilan6" not in st.session_state:
    st.session_state.tampilan6 = False

if "tampilan7" not in st.session_state:
    st.session_state.tampilan7 = False
    
if "tampilan8" not in st.session_state:
    st.session_state.tampilan8 = False

if "tampilan9" not in st.session_state:
    st.session_state.tampilan9 = False

if "tampilan10" not in st.session_state:
    st.session_state.tampilan10 = False

if "tampilan11" not in st.session_state:
    st.session_state.tampilan11 = False
if "tampilan12" not in st.session_state:
    st.session_state.tampilan12 = False

if "tampilan13" not in st.session_state:
    st.session_state.tampilan13 = False

if "tampilan14" not in st.session_state:
    st.session_state.tampilan14 = False

if "tampilan15" not in st.session_state:
    st.session_state.tampilan15 = False

if "tampilan16" not in st.session_state:
    st.session_state.tampilan16 = False

if "tampilan17" not in st.session_state:
    st.session_state.tampilan17 = False
if "tampilan18" not in st.session_state:
    st.session_state.tampilan18 = False
if "tampilan19" not in st.session_state:
    st.session_state.tampilan19 = False

if "tampilan20" not in st.session_state:
    st.session_state.tampilan20 = False

if "tampilan21" not in st.session_state:
    st.session_state.tampilan21 = False

if "tampilan22" not in st.session_state:
    st.session_state.tampilan22 = False

if "tampilan23" not in st.session_state:
    st.session_state.tampilan23 = False

if "tampilan24" not in st.session_state:
    st.session_state.tampilan24 = False

if "tampilan25" not in st.session_state:
    st.session_state.tampilan25 = False

if "tampilan26" not in st.session_state:
    st.session_state.tampilan26 = False

if "tampilan27" not in st.session_state:
    st.session_state.tampilan27 = False

if "tampilan28" not in st.session_state:
    st.session_state.tampilan28 = False

if "tampilan29" not in st.session_state:
    st.session_state.tampilan29 = False

if "tampilan30" not in st.session_state:
    st.session_state.tampilan30 = False
    
if "masukan1" not in st.session_state:
    st.session_state.masukan1=""
    
if "kontrol" not in st.session_state:
    st.session_state.kontrol = True
    
def latar():
    koding1='''
    <!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Materi Statistik Penelitian</title>
  <style>
    body {
      margin: 0;
      font-family: 'Georgia', serif;
      background: linear-gradient(135deg, #fceabb, #f8b500);
      color: #2d2d2d;
      line-height: 1.7;
      padding: 40px;
    }
    h1, h2, h3 {
      font-family: 'Palatino Linotype', 'Book Antiqua', Palatino, serif;
      color: #4b2e05;
    }
    h1 {
      text-align: center;
      font-size: 2.5em;
      margin-bottom: 20px;
    }
    h2 {
      font-size: 1.8em;
      margin-top: 30px;
    }
    p {
      margin: 10px 0;
    }
    .example {
      background: rgba(255, 255, 255, 0.8);
      padding: 15px;
      border-left: 5px solid #d97706;
      margin: 10px 0;
      border-radius: 6px;
      font-style: italic;
    }
  </style>
</head>
<body>
  <h1>Materi Statistik Penelitian untuk Mahasiswa Pendidikan Bahasa Inggris</h1>

  <h2>1. Skala Pengukuran Data</h2>
  <p>Dalam penelitian, data dapat dikategorikan ke dalam skala nominal, ordinal, interval, dan rasio.</p>
  <div class="example">Contoh: Jenis kelamin (nominal), tingkat kepuasan (ordinal), skor tes membaca (interval), lama belajar dalam jam (rasio).</div>

  <h2>2. Statistik Deskriptif</h2>
  <p>Statistik deskriptif digunakan untuk merangkum data melalui mean, median, modus, standar deviasi, dan distribusi.</p>
  <div class="example">Contoh: Rata-rata nilai tes kosa kata mahasiswa adalah 75 dengan standar deviasi 5.</div>

  <h2>3. Reliabilitas dan Validitas</h2>
  <p>Reliabilitas mengukur konsistensi instrumen, sedangkan validitas mengukur apakah instrumen benar-benar mengukur apa yang seharusnya diukur.</p>
  <div class="example">Contoh: Angket strategi belajar dinyatakan reliabel jika Cronbach’s Alpha &gt; 0.7.</div>

  <h2>4. Uji Hipotesis</h2>
  <p>Digunakan untuk mengetahui apakah terdapat perbedaan atau hubungan yang signifikan dalam penelitian.</p>
  <div class="example">Contoh: Uji-t berpasangan digunakan untuk membandingkan nilai pre-test dan post-test dalam kelas bahasa Inggris yang sama.</div>

  <h2>5. Ukuran Efek</h2>
  <p>Selain nilai signifikansi, ukuran efek menjelaskan seberapa besar dampak dari perlakuan atau variabel tertentu.</p>
  <div class="example">Contoh: Cohen’s d = 0.5 menunjukkan efek sedang dari penggunaan strategi membaca tertentu.</div>

  <h2>6. Desain Penelitian</h2>
  <p>Desain penelitian mencakup eksperimen, quasi-eksperimen, dan non-eksperimen. Pemilihan desain tergantung pada tujuan penelitian.</p>
  <div class="example">Contoh: Pre-test Post-test Control Group Design digunakan untuk melihat pengaruh metode pengajaran grammar.</div>

  <h2>7. Sampling</h2>
  <p>Sampling adalah teknik pengambilan sampel dari populasi untuk dijadikan subjek penelitian.</p>
  <div class="example">Contoh: Pengambilan 30 mahasiswa secara acak dari total 120 mahasiswa di satu universitas.</div>

</body>
</html>
    '''
    st.components.v1.html(koding1,height=2050)



def tampilkan_materi1():
    koding2='''
    <!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Skala Pengukuran Data</title>
  <style>
    body {
      margin: 0;
      font-family: 'Merriweather', serif;
      background: linear-gradient(120deg, #e0c3fc, #8ec5fc);
      color: #2c2c2c;
      line-height: 1.8;
      padding: 40px;
    }
    h1, h2, h3 {
      font-family: 'Playfair Display', serif;
      color: #2e1065;
    }
    h1 {
      text-align: center;
      font-size: 2.7em;
      margin-bottom: 20px;
      text-shadow: 1px 1px #fff;
    }
    h2 {
      font-size: 1.9em;
      margin-top: 30px;
    }
    p {
      margin: 10px 0;
      font-size: 1.1em;
    }
    .card {
      background: rgba(255, 255, 255, 0.9);
      padding: 20px;
      border-radius: 12px;
      box-shadow: 0 4px 8px rgba(0,0,0,0.1);
      margin: 20px 0;
    }
    .example {
      background: #fdf2f8;
      padding: 15px;
      border-left: 6px solid #be185d;
      margin-top: 10px;
      border-radius: 6px;
      font-style: italic;
    }
    ul {
      margin: 10px 0 10px 20px;
    }
  </style>
</head>
<body>
  <h1>Skala Pengukuran Data dalam Statistik Penelitian</h1>

  <div class="card">
    <h2>Pendahuluan</h2>
    <p>Dalam penelitian, khususnya di bidang pendidikan Bahasa Inggris, data yang dikumpulkan perlu diklasifikasikan berdasarkan <strong>skala pengukuran</strong>. Skala ini menentukan bagaimana data dapat dianalisis dan interpretasi apa yang valid. Terdapat empat jenis utama skala pengukuran: <em>nominal</em>, <em>ordinal</em>, <em>interval</em>, dan <em>rasio</em>.</p>
  </div>

  <div class="card">
    <h2>1. Skala Nominal</h2>
    <p>Skala nominal adalah skala pengukuran paling dasar yang hanya mengelompokkan data ke dalam kategori tanpa urutan tertentu.</p>
    <ul>
      <li><strong>Sifat:</strong> hanya menunjukkan perbedaan kategori, tidak ada urutan.</li>
      <li><strong>Statistik yang bisa digunakan:</strong> modus, frekuensi, persentase.</li>
    </ul>
    <div class="example">Contoh: Jenis kelamin mahasiswa (laki-laki/perempuan), jurusan (Pendidikan Bahasa Inggris, Sastra Inggris, Linguistik).</div>
  </div>

  <div class="card">
    <h2>2. Skala Ordinal</h2>
    <p>Skala ordinal menyajikan data dalam bentuk urutan, tetapi jarak antar kategori tidak dapat diukur secara tepat.</p>
    <ul>
      <li><strong>Sifat:</strong> ada peringkat/urutan, tetapi selisih antar kategori tidak pasti.</li>
      <li><strong>Statistik yang bisa digunakan:</strong> median, modus, ranking, distribusi persentase.</li>
    </ul>
    <div class="example">Contoh: Tingkat kepuasan belajar (sangat puas, puas, kurang puas, tidak puas).</div>
  </div>

  <div class="card">
    <h2>3. Skala Interval</h2>
    <p>Skala interval tidak hanya menunjukkan urutan, tetapi juga memiliki jarak yang sama antar nilai. Namun, tidak ada nol mutlak.</p>
    <ul>
      <li><strong>Sifat:</strong> dapat diurutkan dan selisih antar nilai bermakna, nol bersifat relatif.</li>
      <li><strong>Statistik yang bisa digunakan:</strong> mean, median, modus, standar deviasi, korelasi, regresi.</li>
    </ul>
    <div class="example">Contoh: Skor tes membaca dengan rentang 0–100. Perbedaan skor 10 poin bermakna sama di seluruh skala.</div>
  </div>

  <div class="card">
    <h2>4. Skala Rasio</h2>
    <p>Skala rasio adalah skala tertinggi karena memiliki semua karakteristik skala sebelumnya dan ditambah adanya nol mutlak.</p>
    <ul>
      <li><strong>Sifat:</strong> dapat diurutkan, selisih bermakna, perbandingan valid, ada nol mutlak.</li>
      <li><strong>Statistik yang bisa digunakan:</strong> semua teknik statistik parametrik.</li>
    </ul>
    <div class="example">Contoh: Lama belajar bahasa Inggris dalam jam, jumlah kosakata yang dikuasai mahasiswa.</div>
  </div>

  <div class="card">
    <h2>Penggunaan dalam Penelitian Pendidikan Bahasa Inggris</h2>
    <p>Dalam penelitian pendidikan Bahasa Inggris, pemahaman skala pengukuran data sangat penting untuk memilih analisis yang tepat. Misalnya:</p>
    <ul>
      <li><strong>Nominal:</strong> membedakan kelompok mahasiswa berdasarkan jenis kelamin.</li>
      <li><strong>Ordinal:</strong> mengukur tingkat motivasi belajar siswa.</li>
      <li><strong>Interval:</strong> skor tes TOEFL yang digunakan untuk mengukur kemampuan bahasa.</li>
      <li><strong>Rasio:</strong> menghitung jumlah jam belajar tambahan per minggu.</li>
    </ul>
  </div>

  <div class="card">
    <h2>Kesimpulan</h2>
    <p>Skala pengukuran data menjadi dasar dalam analisis statistik. Pemilihan teknik analisis yang tepat sangat bergantung pada pemahaman jenis skala yang digunakan, sehingga hasil penelitian lebih akurat dan dapat dipertanggungjawabkan.</p>
  </div>

</body>
</html>
    '''
    st.components.v1.html(koding2,height=2950)
    
def tampilkan_materi2():
    koding3='''
        <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Statistik Penelitian R&D untuk Mahasiswa Bahasa Inggris</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        .stat-card {
            transition: transform 0.3s ease;
        }
        .stat-card:hover {
            transform: translateY(-5px);
        }
        .code-block {
            background-color: #f8f9fa;
            border-left: 4px solid #007bff;
            padding: 15px;
            margin: 20px 0;
            font-family: 'Courier New', monospace;
            white-space: pre-wrap;
        }
    </style>
</head>
<body class="bg-gray-50">
    <!-- Navigation -->
    <nav class="bg-blue-600 text-white shadow-lg sticky top-0 z-50">
        <div class="container mx-auto px-4 py-3 flex justify-between items-center">
            <h1 class="text-xl font-bold">Statistik Penelitian R&D</h1>
            <button id="menu-toggle" class="md:hidden">
                <i class="fas fa-bars"></i>
            </button>
        </div>
    </nav>

    <!-- Main Content -->
    <main class="container mx-auto px-4 py-8 max-w-6xl">
        <!-- Introduction Section -->
        <section class="mb-12 bg-white rounded-lg shadow-md p-8">
            <h2 class="text-3xl font-bold mb-6 text-blue-800">Pengantar Statistik dalam Penelitian R&D</h2>
            <p class="text-lg leading-relaxed mb-6">
                Statistika merupakan alat penting dalam penelitian R&D (Research and Development). 
                Bagi mahasiswa bahasa Inggris, pemahaman dasar statistik membantu dalam merancang penelitian, 
                mengumpulkan data, menganalisis hasil, dan menyajikan temuan secara ilmiah.
            </p>
            
            <div class="grid md:grid-cols-3 gap-6 mt-8">
                <div class="stat-card bg-gradient-to-r from-blue-500 to-purple-600 text-white p-6 rounded-lg shadow-md">
                    <i class="fas fa-chart-bar text-3xl mb-4"></i>
                    <h3 class="font-semibold text-xl mb-2">Analisis Data</h3>
                    <p>Mengolah data kuantitatif menjadi informasi berharga</p>
                </div>
                
                <div class="stat-card bg-gradient-to-r from-green-500 to-teal-600 text-white p-6 rounded-lg shadow-md">
                    <i class="fas fa-search text-3xl mb-4"></i>
                    <h3 class="font-semibold text-xl mb-2">Uji Hipotesis</h3>
                    <p>Memvalidasi teori melalui metode statistik</p>
                </div>
                
                <div class="stat-card bg-gradient-to-r from-orange-500 to-red-600 text-white p-6 rounded-lg shadow-md">
                    <i class="fas fa-lightbulb text-3xl mb-4"></i>
                    <h3 class="font-semibold text-xl mb-2">Interpretasi Hasil</h3>
                    <p>Menerjemahkan angka menjadi kesimpulan praktis</p>
                </div>
            </div>
        </section>

        <!-- Types of Statistics Section -->
        <section class="mb-12 bg-white rounded-lg shadow-md p-8">
            <h2 class="text-3xl font-bold mb-6 text-blue-800">Jenis-Jenis Statistika dalam Penelitian</h2>
            
            <div class="grid md:grid-cols-2 gap-8">
                <div>
                    <h3 class="text-2xl font-semibold mb-4 text-green-700">Statistika Deskriptif</h3>
                    <p class="mb-4">Menggambarkan karakteristik data melalui:</p>
                    <ul class="list-disc pl-6 space-y-2">
                        <li><strong>Rata-rata (Mean):</strong> Nilai tengah dari sekumpulan data</li>
                        <li><strong>Median:</strong> Nilai tengah ketika data diurutkan</li>
                        <li><strong>Modus:</strong> Nilai yang paling sering muncul</li>
                        <li><strong>Standar Deviasi:</strong> Ukuran sebaran data</li>
                    </ul>
                    
                    <div class="mt-6 p-4 bg-yellow-100 rounded-lg">
                        <p class="font-medium mb-2"><i class="fas fa-exclamation-triangle mr-2"></i>Konteks R&D:</p>
                        <p>Digunakan untuk mendeskripsikan sampel populasi atau hasil uji coba produk.</p>
                    </div>
                </div>
                
                <div>
                    <h3 class="text-2xl font-semibold mb-4 text-purple-700">Statistika Inferensial</h3>
                    <p class="mb-4">Menarik kesimpulan dari sampel ke populasi dengan:</p>
                    <ul class="list-disc pl-6 space-y-2">
                        <li><strong>Uji T:</strong> Membandingkan rata-rata dua kelompok</li>
                        <li><strong>ANOVA:</strong> Membandingkan rata-rata lebih dari dua kelompok</li>
                        <li><strong>Korelasi:</strong> Mengukur hubungan antara variabel</li>
                        <li><strong>Regresi:</strong> Memprediksi nilai satu variabel berdasarkan variabel lain</li>
                    </ul>
                    
                    <div class="mt-6 p-4 bg-blue-100 rounded-lg">
                        <p class="font-medium mb-2"><i class="fas fa-info-circle mr-2"></i>Konteks R&D:</p>
                        <p>Digunakan untuk menguji efektivitas treatment, prediksi performa produk, dll.</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- Hypothesis Testing Section -->
        <section class="mb-12 bg-white rounded-lg shadow-md p-8">
            <h2 class="text-3xl font-bold mb-6 text-blue-800">Uji Hipotesis dalam Penelitian</h2>
            
            <div class="mb-8">
                <h3 class="text-xl font-semibold mb-4">Langkah-langkah Uji Hipotesis:</h3>
                <ol class="list-decimal pl-6 space-y-2">
                    <li>Buat hipotesis nol (H₀) dan alternatif (H₁)</li>
                    <li>Pilih tingkat signifikansi (α), biasanya 0.05</li>
                    <li>Pilih uji statistik yang sesuai</li>
                    <li>Hitung nilai statistik dan p-value</li>
                    <li>Tentukan apakah tolak H₀ atau tidak</li>
                </ol>
            </div>
            
            <div class="grid md:grid-cols-2 gap-8">
                <div>
                    <h4 class="text-lg font-semibold mb-3">Contoh Kasus:</h4>
                    <p>"Apakah metode pembelajaran baru meningkatkan kemampuan berbahasa Inggris?"</p>
                    <p class="mt-4"><strong>H₀:</strong> Tidak ada perbedaan signifikan</p>
                    <p><strong>H₁:</strong> Ada perbedaan signifikan</p>
                </div>
                
                <div>
                    <h4 class="text-lg font-semibold mb-3">Interpretasi Hasil:</h4>
                    <p>Jika p-value &lt; 0.05, maka tolak H₀ → Metode baru efektif</p>
                    <p>Jika p-value ≥ 0.05, maka gagal tolak H₀ → Tidak cukup bukti</p>
                </div>
            </div>
        </section>

        <!-- Data Analysis Tools Section -->
        <section class="mb-12 bg-white rounded-lg shadow-md p-8">
            <h2 class="text-3xl font-bold mb-6 text-blue-800">Alat Analisis Data</h2>
            
            <div class="grid md:grid-cols-3 gap-6">
                <div class="border rounded-lg p-4 hover:shadow-md transition-shadow">
                    <h3 class="font-semibold text-lg mb-2">SPSS</h3>
                    <p class="text-sm text-gray-600">Software komersial untuk analisis statistik lanjutan</p>
                    <div class="mt-3 flex items-center">
                        <span class="w-3 h-3 bg-green-500 rounded-full mr-2"></span>
                        <span class="text-sm">User-friendly interface</span>
                    </div>
                </div>
                
                <div class="border rounded-lg p-4 hover:shadow-md transition-shadow">
                    <h3 class="font-semibold text-lg mb-2">R/RStudio</h3>
                    <p class="text-sm text-gray-600">Bahasa pemrograman untuk analisis statistik lanjut</p>
                    <div class="mt-3 flex items-center">
                        <span class="w-3 h-3 bg-blue-500 rounded-full mr-2"></span>
                        <span class="text-sm">Gratis dan open-source</span>
                    </div>
                </div>
                
                <div class="border rounded-lg p-4 hover:shadow-md transition-shadow">
                    <h3 class="font-semibold text-lg mb-2">Excel/Google Sheets</h3>
                    <p class="text-sm text-gray-600">Alat dasar untuk analisis statistik sederhana</p>
                    <div class="mt-3 flex items-center">
                        <span class="w-3 h-3 bg-yellow-500 rounded-full mr-2"></span>
                        <span class="text-sm">Cepat dan mudah digunakan</span>
                    </div>
                </div>
            </div>
        </section>

        <!-- Interactive Example Section -->
        <section class="mb-12 bg-white rounded-lg shadow-md p-8">
            <h2 class="text-3xl font-bold mb-6 text-blue-800">Contoh Interaktif: Perhitungan Rata-Rata</h2>
            
            <div class="mb-6">
                <label for="dataInput" class="block text-lg font-medium mb-2">Masukkan data (pisahkan dengan koma):</label>
                <input type="text" id="dataInput" placeholder="Contoh: 85,90,78,92,88" 
                       class="w-full p-3 border rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent">
            </div>
            
            <button onclick="calculateStats()" 
                    class="bg-blue-600 text-white px-6 py-3 rounded-lg hover:bg-blue-700 transition-colors mb-6">
                Hitung Statistik
            </button>
            
            <div id="resultContainer" class="hidden">
                <h3 class="text-xl font-semibold mb-4">Hasil Perhitungan:</h3>
                <div id="resultsDisplay" class="space-y-2"></div>
            </div>
        </section>

        <!-- Conclusion Section -->
        <section class="mb-12 bg-white rounded-lg shadow-md p-8">
            <h2 class="text-3xl font-bold mb-6 text-blue-800">Kesimpulan</h2>
            <p class="text-lg leading-relaxed mb-6">
                Pemahaman statistik adalah keterampilan esensial bagi mahasiswa bahasa Inggris yang melakukan penelitian R&D. 
                Dengan memahami konsep dasar statistik, Anda dapat merancang penelitian yang lebih baik, 
                menganalisis data secara akurat, dan menyajikan temuan penelitian dengan cara yang profesional.
            </p>
            
            <div class="grid md:grid-cols-2 gap-8 mt-8">
                <div class="border-l-4 border-green-500 pl-4">
                    <h3 class="font-semibold text-lg mb-2">Tips Sukses:</h3>
                    <ul class="space-y-2">
                        <li><i class="fas fa-check text-green-500 mr-2"></i>Pahami jenis data Anda</li>
                        <li><i class="fas fa-check text-green-500 mr-2"></i>Pilih uji statistik yang tepat</li>
                        <li><i class="fas fa-check text-green-500 mr-2"></i>Gunakan software yang sesuai</li>
                        <li><i class="fas fa-check text-green-500 mr-2"></i>Interpretasikan hasil dengan hati-hati</li>
                    </ul>
                </div>
                
                <div class="border-l-4 border-blue-500 pl-4">
                    <h3 class="font-semibold text-lg mb-2">Sumber Belajar:</h3>
                    <ul class="space-y-2">
                        <li><i class="fas fa-book text-blue-500 mr-2"></i>Book: "Statistics for Research" by George Argyrous</li>
                        <li><i class="fas fa-link text-blue-500 mr-2"></i>Online Course: Coursera - Basic Statistics</li>
                        <li><i class="fas fa-video text-blue-500 mr-2"></i>YouTube: StatQuest with Josh Starmer</li>
                    </ul>
                </div>
            </div>
        </section>
    </main>

    <!-- Footer -->
    <footer class="bg-gray-800 text-white py-8">
        <div class="container mx-auto px-4 text-center">
            <p>&copy; 2023 Statistik Penelitian R&D. All rights reserved.</p>
            <p class="mt-2 text-gray-400">Didesain untuk mahasiswa bahasa Inggris</p>
        </div>
    </footer>

    <script>
        function calculateStats() {
            const input = document.getElementById('dataInput').value;
            if (!input.trim()) {
                alert('Silakan masukkan data terlebih dahulu!');
                return;
            }

            try {
                // Parse input data
                const data = input.split(',').map(num => parseFloat(num.trim())).filter(n => !isNaN(n));
                
                if (data.length === 0) {
                    throw new Error('Data tidak valid');
                }

                // Calculate statistics
                const sum = data.reduce((acc, val) => acc + val, 0);
                const mean = sum / data.length;
                const sortedData = [...data].sort((a, b) => a - b);
                const median = sortedData.length % 2 === 0 
                    ? (sortedData[sortedData.length/2 - 1] + sortedData[sortedData.length/2]) / 2
                    : sortedData[Math.floor(sortedData.length/2)];
                
                // Count frequency for mode
                const freqMap = {};
                data.forEach(val => {
                    freqMap[val] = (freqMap[val] || 0) + 1;
                });
                let mode = [];
                let maxFreq = 0;
                for (const [val, freq] of Object.entries(freqMap)) {
                    if (freq > maxFreq) {
                        maxFreq = freq;
                        mode = [parseFloat(val)];
                    } else if (freq === maxFreq) {
                        mode.push(parseFloat(val));
                    }
                }

                // Display results
                const resultContainer = document.getElementById('resultContainer');
                const resultsDisplay = document.getElementById('resultsDisplay');
                
                resultsDisplay.innerHTML = `
                    <div class="bg-gray-100 p-4 rounded-lg">
                        <p><strong>Data:</strong> ${data.join(', ')}</p>
                        <p><strong>Jumlah data:</strong> ${data.length}</p>
                        <p><strong>Rata-rata (Mean):</strong> ${mean.toFixed(2)}</p>
                        <p><strong>Median:</strong> ${median.toFixed(2)}</p>
                        <p><strong>Modus:</strong> ${mode.join(', ')}</p>
                    </div>
                `;
                
                resultContainer.classList.remove('hidden');
                
            } catch (error) {
                alert('Terjadi kesalahan saat memproses data. Pastikan formatnya benar.');
            }
        }

        // Add smooth scrolling for navigation links
        document.addEventListener('DOMContentLoaded', () => {
            const navLinks = document.querySelectorAll('nav a[href^="#"]');
            navLinks.forEach(link => {
                link.addEventListener('click', (e) => {
                    e.preventDefault();
                    const targetId = link.getAttribute('href').substring(1);
                    const targetElement = document.getElementById(targetId);
                    if (targetElement) {
                        window.scrollTo({
                            top: targetElement.offsetTop - 80,
                            behavior: 'smooth'
                        });
                    }
                });
            });
        });
    </script>
</body>
</html>
    '''
    st.components.v1.html(koding3,height=3000)

def tampilkan_materi3():
    # Judul Aplikasi
    st.title("📊 Statistik Penelitian Interaktif")
    st.write("Masukkan data penelitian untuk menghitung **Rata-rata, Median, Modus, dan Standar Deviasi**.")
    # Input Data
    data_input = st.text_area(
        "Masukkan data (pisahkan dengan koma atau spasi):",
        "70, 75, 80, 90, 85, 75, 80, 95, 100"
    )

    # Konversi input ke list angka
    try:
        # Hilangkan spasi lalu split dengan koma atau spasi
        data = [float(x) for x in data_input.replace(",", " ").split()]
    
        if len(data) > 0:
            df = pd.DataFrame(data, columns=["Nilai"])
            st.dataframe(df, use_container_width=True)

            # Hitung statistik
            rata2 = mean(data)
            med = median(data)
            try:
                mod = mode(data)  # Jika hanya 1 modus
            except:
                mod = multimode(data)  # Jika ada lebih dari 1 modus
            std_dev = stdev(data)

            # Tampilkan hasil
            st.subheader("📌 Hasil Statistik:")
            st.metric("Rata-rata (Mean)", f"{rata2:.2f}")
            with st.expander("Penjelasan Rata-rata"):
                st.markdown("<div style='text-align:center; font-family:broadway; background-color:yellow; color:black; font-size:25px'>Rata-rata Nilai</div>",unsafe_allow_html=True)
                st.latex("\\bar{x}=\\frac{\\sum{x_{i}}}{n}")
                st.markdown("<div style='text-align:center; font-family:broadway; background-color:cyan; color:black; font-size:20px; width:50%'>Jumlah semua Nilai</div>",unsafe_allow_html=True)
                st.latex("\\sum{x_{i}}="+str(sum(data)))
                st.markdown("<div style='text-align:center; font-family:broadway; background-color:cyan; color:black; font-size:20px; width:50%'>Banyak Siswa</div>",unsafe_allow_html=True)
                st.latex("n="+str(len(data)))
                st.markdown("<div style='text-align:center; font-family:broadway; background-color:cyan; color:black; font-size:20px; width:50%'>Hasil Rata-rata</div>",unsafe_allow_html=True)
                st.latex("\\bar{x}=\\frac{\\sum{x_i}}{n}=\\frac{"+str(sum(data))+"}{"+str(len(data))+"}="+str(mean(data)))
            st.metric("Median", f"{med:.2f}")
            with st.expander("Penjelasan Median"):
                st.markdown("<div style='text-align:center; font-family:broadway; background-color:yellow; color:black; font-size:25px; margin:10px'>Median</div>",unsafe_allow_html=True)
                st.markdown("""<div style='text-align:center; font-family:broadway; background-color:cyan; color:black; font-size:20px; width:50%; margin:10px'>Mengurut Data</div>
                <div>Cari data tengah</div>
                """,unsafe_allow_html=True)
                df1 = pd.DataFrame(sorted(data),columns=['Nilai'])
                st.dataframe(df1,use_container_width=True)
                st.markdown("""<div style='text-align:center; font-family:broadway; background-color:cyan; color:black; font-size:20px; width:50%; margin:10px'>Urutan Data Tengah</div>
                <div>Cari data tengah</div>
                """,unsafe_allow_html=True)
                st.write("Jumlah Ganjil")
                st.latex("i=\\frac{n+1}{2}\\\\u_{t}=u_{\\frac{n+1}{2}}")
                st.write("Jumlah Genap")
                st.latex("i_{1}=\\frac{n}{2}\\\\i_{2}=\\frac{\\frac{n}{2}+1}{2}\\\\u_{t}=\\frac{u_{i_{1}}+u_{i_{2}}}{2}")
                nilai=0
                if len(data)%2==0:
                    st.write("jumlah Data Genap")
                    st.latex("u_[t}="+str(med))
                else:
                    st.write("jumlah Data Ganjil")
                    st.latex("u_{t}="+str(med))
                st.markdown("""<div style='text-align:center; font-family:broadway; background-color:cyan; color:black; font-size:20px; width:50%; margin:10px'>Data Media</div>
                <div>Cari data tengah</div>
                """,unsafe_allow_html=True)
            st.metric("**Modus:**", str(mod))
            with st.expander("Penjelasan Modus"):
                st.markdown("<div style='text-align:center; font-family:broadway; background-color:yellow; color:black; font-size:25px; margin:10px'>Modus</div>",unsafe_allow_html=True)
                data1 = set(data)
                data2 = {}
                for i in data1:
                    data2[int(i)]=data.count(i)
                st.write(data2)
            st.metric("Standar Deviasi", f"{std_dev:.2f}")
            with st.expander("Penjelasan Standar Deviasi"):
                st.markdown("<div style='text-align:center; font-family:broadway; background-color:yellow; color:black; font-size:25px'>Standar Deviasi</div>",unsafe_allow_html=True)
                st.latex("SD=\\sqrt{\\frac{\\sum{(x_i-\\bar{x})^2}}{n-1}}\\\\Standar\\;\\;Deviasi\\;Sampel")
                st.markdown("""<div style='text-align:center; font-family:broadway; background-color:cyan; color:black; font-size:20px; width:80%; margin:10px'>
                                Langkah Pertama: Mencari Rata-rata Nilai</div>""",unsafe_allow_html=True)
                st.latex(f'\\bar{{x}}={rata2:.2f}')
                st.markdown("""<div style='text-align:center; font-family:broadway; background-color:cyan; color:black; font-size:20px; width:80%; margin:10px'>
                                Langkah Kedua: Kurangi masing-masing nilai dengan rata2 lalu hasilnya dikuadratkan </div>""",unsafe_allow_html=True)
                kolom = ['Nilai','rata2','(x_{i}-\\bar{x}','(x_{i}-\\bar{x})^2']
                data_masukan = {'Nilai':[float(i) for i in data_input.replace(",", " ").split()],
                                'Rata-rata':[float(rata2) for i in data_input.replace(",", " ").split()],
                                r'$x_{i}-\bar{x}$':[float(i)-float(rata2) for i in data_input.replace(",", " ").split()]}
                df1 = pd.DataFrame(data_masukan)
                st.markdown(
                    df1.to_html(escape=False),
                    unsafe_allow_html=True
                    )
                st.dataframe(df1,use_container_width=True)
                

            # Visualisasi
            st.subheader("📈 Visualisasi Data")
            st.bar_chart(df)

    except Exception as e:
        st.error("⚠️ Pastikan data hanya berisi angka yang dipisahkan dengan koma atau spasi.")

def tampilkan_materi4():
    st.title("Distribusi Normal dengan Interval Standar Deviasi")

    # Input interaktif
    mu = st.number_input("Rata-rata (μ)", value=0.0)
    sigma = st.number_input("Standar Deviasi (σ)", value=1.0, min_value=0.1)
    max_dev = st.slider("Jumlah Batas Standar Deviasi", 1, 10, 5)

    # Data distribusi normal
    x = np.linspace(mu - (max_dev+1)*sigma, mu + (max_dev+1)*sigma, 1000)
    y = norm.pdf(x, mu, sigma)

    # Plot
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(x, y, label="Distribusi Normal")

    interval = st.number_input("")
    for i in range(1, max_dev + 1):
        ax.axvline(mu + i*sigma, color="blue", linestyle="--", linewidth=1)
        ax.axvline(mu - i*sigma, color="blue", linestyle="--", linewidth=1)
        ax.text(mu + i*sigma, max(y)*0.9, f"+{i}σ", rotation=90, va="bottom", ha="center", fontsize=8)
        ax.text(mu - i*sigma, max(y)*0.9, f"-{i}σ", rotation=90, va="bottom", ha="center", fontsize=8)

    # Garis rata-rata
    ax.axvline(mu, color="black", linestyle="--", linewidth=2, label=f"μ = {mu}")

    ax.set_title("Distribusi Normal dan Interval Standar Deviasi")
    ax.set_xlabel("X")
    ax.set_ylabel("Probabilitas")
    ax.legend()
    st.pyplot(fig)
    
    st.subheader("Batas-batas Interval Standar Deviasi")
    kump_interval=[mu-i*sigma for i in range(-max_dev,max_dev+1)]
    for k in range(1, max_dev + 1):
        st.write(f"±{k}σ: {mu - k*sigma:.2f}  s.d.  {mu + k*sigma:.2f}")
    st.header("Melihat interval nilai")
    try:
        for i in range(len(kump_interval)):
            st.write(f"Kelompok {i}")
            st.write(f'{kump_interval[i]} - {kump_interval[i+1]}')
    except:
        pass
    st.markdown("""
    **Catatan:**  
      - Area di bawah kurva untuk setiap ±σ kira-kira:
      - ±1σ ≈ 68%
      - ±2σ ≈ 95%
      - ±3σ ≈ 99.7%  
    """)
    
def tampilkan_materi5():
    st.title("Uji Z dengan Visualisasi")

    # Input pengguna
    mu_pop = st.number_input("Rata-rata Populasi (μ0)", value=50.0)
    sigma_pop = st.number_input("Standar Deviasi Populasi (σ)", value=10.0)
    n = st.number_input("Ukuran Sampel (n)", value=30, min_value=1)
    mean_sample = st.number_input("Rata-rata Sampel (x̄)", value=52.0)
    alpha = st.number_input("Tingkat Signifikansi (α)", value=0.05, min_value=0.001, max_value=0.5, step=0.01)

    # Hitung Z
    z_hit = (mean_sample - mu_pop) / (sigma_pop / np.sqrt(n))
    z_kritis = norm.ppf(1 - alpha/2)  # uji 2 sisi

    st.write(f"**Z hitung = {z_hit:.3f}**")
    st.write(f"**Z kritis = ±{z_kritis:.3f}**")

    # Buat grafik distribusi normal
    x = np.linspace(-4, 4, 500)
    y = norm.pdf(x, 0, 1)

    fig, ax = plt.subplots()

    # Plot distribusi normal standar
    ax.plot(x, y, label="Distribusi Normal Standar")

    # Area kritis (dua sisi)
    x_crit_left = np.linspace(-4, -z_kritis, 200)
    x_crit_right = np.linspace(z_kritis, 4, 200)
    ax.fill_between(x_crit_left, 0, norm.pdf(x_crit_left), color="red", alpha=0.4, label="Daerah Kritis (α/2)")
    ax.fill_between(x_crit_right, 0, norm.pdf(x_crit_right), color="red", alpha=0.4)

    # Tandai Z hitung
    ax.axvline(z_hit, color="blue", linestyle="--", linewidth=2, label=f"Z hitung = {z_hit:.2f}")

    # Tambahan garis kritis
    ax.axvline(-z_kritis, color="black", linestyle="--", label=f"-Z kritis = {-z_kritis:.2f}")
    ax.axvline(z_kritis, color="black", linestyle="--", label=f"Z kritis = {z_kritis:.2f}")

    ax.legend()
    ax.set_title("Uji Z - Visualisasi Daerah Kritis")
    st.pyplot(fig)

    # Keputusan
    if abs(z_hit) > z_kritis:
        st.error("Tolak H0: Ada perbedaan signifikan.")
    else:
        st.success("Gagal Tolak H0: Tidak ada perbedaan signifikan.")
#===========Tugas============
def tampilkan_tugas():
    GOOGLE_FORM_URL = "https://docs.google.com/forms/u/0/d/e/1FAIpQLSevmMv-SgWK8OoG-WBt04PAJqttBBIu_iavDfus6ABC4MzWgA/formResponse"
    ENTRY_IDS = {
    "nama": "entry.75935386",
    "nim":"entry.1727447679",
    "deskripsi": "entry.1051471251"
    }
   #  KONFIGURASI GOOGLE APPS SCRIPT UNTUK UPLOAD FILE ===
    UPLOAD_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbxCnwMFDRhKEy5h7KRaAHshuQ1JuGBYXwtXmJEVEc3TLSZu7vBvs3idUJImMjTqkOoM/exec"

   # TAMPILAN STREAMLIT ===
    st.title("📤 Kirim Data & File ke Google Sheet dan Drive (Tanpa API)")

    nama = st.text_input("Nama Lengkap")
    nim = st.text_input("NIM")
    deskripsi = st.text_area("Deskripsi / Keterangan Tugas ke berapa")
    uploaded_file = st.file_uploader("Unggah File", type=["pdf", "jpg", "png", "docx"])

    if st.button("Kirim Data"):
        if nama and deskripsi:
            file_url = None
            st.session_state.kontrol = False
            # --- Upload File ke Google Drive ---
            if uploaded_file is not None:
                try:
                    # kirim file sebagai bytes biasa, bukan multipart
                    encoded_file = base64.b64encode(uploaded_file.getvalue()).decode('utf-8')
                    response_upload = requests.post(
                        UPLOAD_SCRIPT_URL,
                        data=encoded_file,
                        params={
                            "filename": uploaded_file.name
                        }
                    )

                    if response_upload.status_code == 200 and "Error" not in response_upload.text:
                        file_url = response_upload.text.strip()
                        st.success(f"📎 File berhasil diupload ke Drive: [Lihat File]({file_url})")
                    else:
                        st.warning(f"⚠️ Upload gagal: {response_upload.text}")

                except Exception as e:
                    st.error(f"❌ Gagal upload file: {e}")

            # --- Kirim data teks ke Google Form ---
            data = {
                ENTRY_IDS["nama"]: nama,
                ENTRY_IDS["nim"]:nim,
                ENTRY_IDS["deskripsi"]: deskripsi,
            }
            if file_url:
                data["entry.1605146254"] = file_url  # tambahkan kolom link file di form

            response = requests.post(GOOGLE_FORM_URL, data=data)
            if response.status_code == 200:
                st.success("✅ Data berhasil dikirim ke Google Sheet!")
                st.session_state.kontrol = True
            else:
                st.warning(f"⚠️ Gagal kirim data ke Sheet! Kode: {response.status_code}")
        else:
            st.error("Mohon isi semua kolom teks sebelum mengirim.")

#==========Akhir Tugas++++++++
#==========Latihan1==========
def tampilkan_latihan1():
    st.markdown("""
    <iframe src="https://martin123-oke.github.io/LatianUjiZ/latihan_distribusi_Z.html" style="width:100%; height:3000px;"></iframe>
    """,unsafe_allow_html=True)
#========Akhir Latihan1=========
#==========Lanjutkan Materi 6=====
def tampilkan_materi6():
    halaman1 = st.tabs(['Pendahuluan','Contoh','Grafik','Latihan'])
    with halaman1[0]:
        st.markdown('''
        <iframe src="https://martin123-oke.github.io/LatianUjiZ/UjiHipotesisZ.html" style="width:100%; height:3000px;"></iframe>
        ''',unsafe_allow_html=True)
    with halaman1[1]:
        with st.expander("📘 Materi: Konsep Dasar Uji Z"):
            st.markdown("""
            ### 🔹 Pengertian
            Uji Z digunakan untuk **menguji hipotesis tentang rata-rata populasi** jika:
            - Standar deviasi populasi (σ) diketahui, dan
            - Ukuran sampel (n) cukup besar (biasanya n ≥ 30).

            ### 🔹 Rumus Statistik Uji Z
            $$
            Z = \\frac{\\bar{X} - \\mu_0}{\\frac{\\sigma}{\\sqrt{n}}}
            $$
            di mana:
            - $ \\bar{X} $: rata-rata sampel  
            - $ \\mu_0 $: rata-rata populasi (hipotesis nol)  
            - $ \\sigma $: standar deviasi populasi  
            - $ n $: jumlah sampel  

            ### 🔹 Langkah-langkah Uji Hipotesis
            1. **Tentukan hipotesis**
                - H₀ : μ = μ₀  
                - H₁ : μ ≠ μ₀ (dua sisi) atau μ > μ₀ / μ < μ₀ (satu sisi)
            2. **Tentukan taraf signifikansi (α)**
            3. **Hitung nilai Z hitung**
            4. **Bandingkan dengan Z tabel**
            5. **Buat keputusan**
                - Tolak H₀ jika |Z hitung| > Z tabel (dua sisi)  
                - Tolak H₀ jika Z hitung > Z tabel (kanan) atau Z hitung < -Z tabel (kiri)
            """)

        # ==============================
        # Input Data Uji Z
        # ==============================
        st.subheader("🔢 Input Data Uji Z")

        col1, col2 = st.columns(2)
        with col1:
            x_bar = st.number_input("Rata-rata sampel (x̄)", value=50.0)
            mu0 = st.number_input("Rata-rata populasi (μ₀)", value=45.0)
            sigma = st.number_input("Standar deviasi populasi (σ)", value=10.0)
        with col2:
            n = st.number_input("Jumlah sampel (n)", min_value=1, value=30)
            alpha = st.selectbox("Taraf signifikansi (α)", [0.10, 0.05, 0.01])
            jenis_uji = st.radio("Jenis Uji", ["Dua sisi", "Satu sisi kanan", "Satu sisi kiri"])

        # ==============================
        # Perhitungan Uji Z
        # ==============================
        if st.button("🔍 Hitung Uji Z"):
            # Hitung Z hitung
            z_hitung = (x_bar - mu0) / (sigma / math.sqrt(n))

            # Nilai kritis (Z tabel)
            if jenis_uji == "Dua sisi":
                z_tabel = norm.ppf(1 - alpha / 2)
                keputusan = "Tolak H₀" if abs(z_hitung) > z_tabel else "Gagal tolak H₀"
            elif jenis_uji == "Satu sisi kanan":
                z_tabel = norm.ppf(1 - alpha)
                keputusan = "Tolak H₀" if z_hitung > z_tabel else "Gagal tolak H₀"
            else:  # kiri
                z_tabel = norm.ppf(alpha)
                keputusan = "Tolak H₀" if z_hitung < z_tabel else "Gagal tolak H₀"

            # ==============================
            # Hasil Analisis
            # ==============================
            st.markdown("---")
            st.subheader("📈 Hasil Analisis Uji Z")
            st.metric(label="Z Hitung", value=f"{z_hitung:.3f}")
            st.metric(label="Z Tabel", value=f"{z_tabel:.3f}")
            st.success(f"**Keputusan:** {keputusan}")

            # ==============================
            # Interpretasi
            # ==============================
            if keputusan == "Tolak H₀":
                st.markdown(f"✅ Karena kriteria uji terpenuhi, maka **H₀ ditolak**. Artinya terdapat cukup bukti bahwa rata-rata populasi **berbeda atau lebih besar/kecil dari μ₀** tergantung jenis uji.")
            else:
                st.markdown(f"ℹ️ Karena kriteria uji tidak terpenuhi, maka **tidak ada bukti cukup untuk menolak H₀**. Rata-rata populasi dianggap sama dengan μ₀.")

        # ==============================
        # Catatan Tambahan
        # ==============================
        with st.expander("🧠 Contoh Kasus"):
            st.markdown("""
            **Contoh Soal:**  
            Sebuah perusahaan ingin mengetahui apakah rata-rata berat produk berbeda dari 45 gram.  
            Diketahui σ = 10, n = 30, dan hasil pengamatan sampel menunjukkan rata-rata = 50 gram.  
            Uji dengan α = 0.05 (dua sisi).  

            **Hasil:**  
            - Z hitung = (50 - 45) / (10 / √30) = 2.738  
            - Z tabel = 1.96  
            Karena |2.738| > 1.96 → **Tolak H₀**, terdapat bukti bahwa rata-rata berat produk ≠ 45 gram.
            """)
        
        st.markdown("---")
        st.caption("Dibuat Oleh Martin Bernard")
    with halaman1[2]:
        with st.expander("📘 Penjelasan Singkat"):
            st.markdown("""
                ### 🔹 Apa itu Uji Z?
                Uji Z digunakan untuk menguji hipotesis tentang rata-rata populasi saat standar deviasi populasi (σ) diketahui.

                Rumus:
                $$
                Z = \\frac{\\bar{X} - \\mu_0}{\\sigma / \\sqrt{n}}
                $$
                """)

        # ==============================
        # Input Data
        # ==============================
        st.subheader("🔢 Input Data")
        col1, col2 = st.columns(2)
        with col1:
            x_bar = st.number_input("Rata-rata1 sampel (x̄)", value=50.0)
            mu0 = st.number_input("Rata-rata1 populasi (μ₀)", value=45.0)
            sigma = st.number_input("Standar1 deviasi populasi (σ)", value=10.0)
        with col2:
            n = st.number_input("Jumlah sampel1 (n)", min_value=1, value=30)
            alpha = st.selectbox("Taraf signifikansi1 (α)", [0.10, 0.05, 0.01])
            jenis_uji = st.radio("Jenis Uji1", ["Dua sisi", "Satu sisi kanan", "Satu sisi kiri"])

        # ==============================
        # Hitung Nilai Z
        # ==============================
        if st.button("📈 Tampilkan Grafik Uji Z"):
            # Hitung nilai Z hitung
            z_hitung = (x_bar - mu0) / (sigma / math.sqrt(n))

            # Rentang Z
            z_values = np.linspace(-4, 4, 1000)
            y_values = norm.pdf(z_values, 0, 1)

            # ==============================
            # Menentukan Z Tabel dan Area
            # ==============================
            if jenis_uji == "Dua sisi":
                z_tabel = norm.ppf(1 - alpha / 2)
                left_critical = -z_tabel
                right_critical = z_tabel
                keputusan = "Tolak H₀" if abs(z_hitung) > z_tabel else "Gagal tolak H₀"
            elif jenis_uji == "Satu sisi kanan":
                z_tabel = norm.ppf(1 - alpha)
                left_critical = None
                right_critical = z_tabel
                keputusan = "Tolak H₀" if z_hitung > z_tabel else "Gagal tolak H₀"
            else:  # kiri
                z_tabel = norm.ppf(alpha)
                left_critical = z_tabel
                right_critical = None
                keputusan = "Tolak H₀" if z_hitung < z_tabel else "Gagal tolak H₀"

            # ==============================
            # Plot Kurva Distribusi Z
            # ==============================
            fig, ax = plt.subplots(figsize=(8, 4))
            ax.plot(z_values, y_values, color="blue", linewidth=2)

            # Arsiran area kritis
            if jenis_uji == "Dua sisi":
                ax.fill_between(z_values, 0, y_values, where=(z_values <= left_critical), color='red', alpha=0.3)
                ax.fill_between(z_values, 0, y_values, where=(z_values >= right_critical), color='red', alpha=0.3)
            elif jenis_uji == "Satu sisi kanan":
                ax.fill_between(z_values, 0, y_values, where=(z_values >= right_critical), color='red', alpha=0.3)
            else:
                ax.fill_between(z_values, 0, y_values, where=(z_values <= left_critical), color='red', alpha=0.3)

            # Garis vertikal untuk Z hitung
            ax.axvline(z_hitung, color='green', linestyle='--', linewidth=2, label=f"Z Hitung = {z_hitung:.2f}")

            # Garis vertikal untuk batas kritis
            if left_critical is not None:
                ax.axvline(left_critical, color='red', linestyle=':', label=f"Z Kritis (kiri) = {left_critical:.2f}")
            if right_critical is not None:
                ax.axvline(right_critical, color='red', linestyle=':', label=f"Z Kritis (kanan) = {right_critical:.2f}")

            # Dekorasi grafik
            ax.set_title("Distribusi Normal Standar (Z)", fontsize=14)
            ax.set_xlabel("Nilai Z")
            ax.set_ylabel("Probabilitas")
            ax.legend()
            ax.grid(alpha=0.2)

            # Tampilkan grafik di Streamlit
            st.pyplot(fig)

            # ==============================
            # Tampilkan Hasil Perhitungan
            # ==============================
            st.markdown("---")
            st.subheader("📊 Hasil Uji Z")
            st.metric(label="Z Hitung", value=f"{z_hitung:.3f}")
            st.metric(label="Z Tabel", value=f"{z_tabel:.3f}")
            st.success(f"**Keputusan:** {keputusan}")

            if keputusan == "Tolak H₀":
                st.markdown("✅ Hasil menunjukkan bahwa **hipotesis nol ditolak**. Ada cukup bukti bahwa rata-rata populasi berbeda atau lebih besar/kecil dari μ₀.")
            else:
                st.markdown("ℹ️ Hasil menunjukkan bahwa **tidak ada bukti cukup untuk menolak H₀**. Rata-rata populasi dianggap sama dengan μ₀.")

        # ==============================
        # Catatan Tambahan
        # ==============================
        with st.expander("🧠 Contoh Interpretasi"):
            st.markdown("""
            **Contoh:**  
            Diketahui μ₀ = 45, σ = 10, n = 30, x̄ = 50, α = 0.05 (dua sisi).  
            Hasil menunjukkan Z hitung = 2.738 dan Z tabel = 1.96 → **|2.738| > 1.96 → Tolak H₀**.  
            Artinya, terdapat perbedaan signifikan antara rata-rata sampel dan populasi.
            """)
    with halaman1[3]:
        st.markdown('''
        <iframe src="https://martin123-oke.github.io/LatianUjiZ/LatihanUjiZ.html" style="width:100%; height:3000px;"></iframe>
        ''',unsafe_allow_html=True)

def tampilkan_materi7():
    pilihan = st.tabs(['Teori Pegantar','Teori','Simulasi'])
    with pilihan[0]:
        st.markdown('''
        <iframe src="https://martin-bernard26.github.io/statistika/TeoriNormal.html" style="width:100%; height:1800px"></iframe>
        ''',unsafe_allow_html=True)
    with pilihan[1]:
        koding='''
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Uji Normalitas Data Nilai</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            overflow: hidden;
        }

        .header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 40px;
            text-align: center;
        }

        .header h1 {
            font-size: 2.5em;
            margin-bottom: 10px;
        }

        .header p {
            font-size: 1.2em;
            opacity: 0.9;
        }

        .content {
            padding: 40px;
        }

        .section {
            margin-bottom: 40px;
        }

        .section h2 {
            color: #667eea;
            font-size: 1.8em;
            margin-bottom: 20px;
            border-bottom: 3px solid #667eea;
            padding-bottom: 10px;
        }

        .section h3 {
            color: #764ba2;
            font-size: 1.4em;
            margin: 20px 0 10px 0;
        }

        .section p, .section li {
            line-height: 1.8;
            color: #333;
            font-size: 1.1em;
        }

        .section ul, .section ol {
            margin-left: 30px;
            margin-top: 10px;
        }

        .info-box {
            background: #f0f4ff;
            border-left: 5px solid #667eea;
            padding: 20px;
            margin: 20px 0;
            border-radius: 5px;
            color:blue;
        }

        .info-box.warning {
            background: #fff4e6;
            border-left-color: #ff9800;
        }

        .info-box.success {
            background: #e8f5e9;
            border-left-color: #4caf50;
        }

        .formula {
            background: #f5f5f5;
            padding: 20px;
            margin: 20px 0;
            border-radius: 10px;
            text-align: center;
            font-family: 'Courier New', monospace;
            font-size: 1.2em;
            overflow-x: auto;
        }

        .tabs {
            display: flex;
            border-bottom: 2px solid #ddd;
            margin-bottom: 20px;
        }

        .tab {
            padding: 15px 30px;
            cursor: pointer;
            background: #f5f5f5;
            border: none;
            font-size: 1.1em;
            transition: all 0.3s;
            border-radius: 10px 10px 0 0;
            margin-right: 5px;
        }

        .tab.active {
            background: #667eea;
            color: white;
        }

        .tab:hover {
            background: #764ba2;
            color: white;
        }

        .tab-content {
            display: none;
            animation: fadeIn 0.5s;
        }

        .tab-content.active {
            display: block;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .calculator {
            background: #f9f9f9;
            padding: 30px;
            border-radius: 15px;
            margin-top: 20px;
        }

        .input-group {
            margin-bottom: 20px;
        }

        .input-group label {
            display: block;
            margin-bottom: 8px;
            font-weight: bold;
            color: #667eea;
        }

        .input-group input, .input-group textarea {
            width: 100%;
            padding: 12px;
            border: 2px solid #ddd;
            border-radius: 8px;
            font-size: 1em;
            transition: border 0.3s;
        }

        .input-group input:focus, .input-group textarea:focus {
            outline: none;
            border-color: #667eea;
        }

        .btn {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 15px 40px;
            border: none;
            border-radius: 30px;
            font-size: 1.1em;
            cursor: pointer;
            transition: transform 0.3s, box-shadow 0.3s;
        }

        .btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 20px rgba(102, 126, 234, 0.4);
        }

        .result {
            margin-top: 30px;
            padding: 20px;
            background: white;
            border-radius: 10px;
            border: 2px solid #667eea;
        }

        .result h3 {
            color: #667eea;
            margin-bottom: 15px;
        }

        .result-item {
            padding: 10px;
            margin: 10px 0;
            background: #f0f4ff;
            border-radius: 5px;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
        }

        table th, table td {
            border: 1px solid #ddd;
            padding: 12px;
            text-align: left;
        }

        table th {
            background: #667eea;
            color: white;
        }

        table tr:nth-child(even) {
            background: #f9f9f9;
        }

        .highlight {
            background: #fff9c4;
            padding: 2px 5px;
            border-radius: 3px;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📊 Uji Normalitas Data Nilai</h1>
            <p>Panduan Lengkap dan Kalkulator Interaktif</p>
        </div>

        <div class="content">
            <div class="tabs">
                <button class="tab active" onclick="openTab(event, 'pengertian')">Pengertian</button>
                <button class="tab" onclick="openTab(event, 'metode')">Metode Uji</button>
                <button class="tab" onclick="openTab(event, 'langkah')">Langkah-langkah</button>
                <button class="tab" onclick="openTab(event, 'kalkulator')">Kalkulator</button>
            </div>

            <!-- Tab Pengertian -->
            <div id="pengertian" class="tab-content active">
                <div class="section">
                    <h2>Pengertian Uji Normalitas</h2>
                    <p>Uji normalitas adalah prosedur statistik yang digunakan untuk menentukan apakah data yang dikumpulkan berasal dari populasi yang berdistribusi normal atau tidak. Dalam konteks data nilai siswa, uji ini sangat penting untuk menentukan apakah:</p>
                    
                    <ul>
                        <li>Nilai-nilai siswa tersebar secara merata di sekitar rata-rata</li>
                        <li>Data memenuhi asumsi untuk analisis statistik parametrik</li>
                        <li>Hasil evaluasi pembelajaran mencerminkan distribusi yang wajar</li>
                    </ul>

                    <div class="info-box">
                        <h3>Mengapa Uji Normalitas Penting?</h3>
                        <p><strong>1. Prasyarat Analisis Statistik:</strong> Banyak uji statistik parametrik (seperti uji t, ANOVA) mengasumsikan data berdistribusi normal.</p>
                        <p><strong>2. Validitas Hasil:</strong> Jika data tidak normal, hasil analisis statistik mungkin tidak akurat.</p>
                        <p><strong>3. Pemilihan Metode:</strong> Membantu menentukan apakah menggunakan statistik parametrik atau non-parametrik.</p>
                    </div>

                    <h3>Karakteristik Distribusi Normal</h3>
                    <ul>
                        <li><strong>Simetris:</strong> Kurva berbentuk lonceng dengan nilai tengah sebagai puncak</li>
                        <li><strong>Mean = Median = Modus:</strong> Ketiga ukuran pemusatan data berada pada titik yang sama</li>
                        <li><strong>Aturan 68-95-99.7:</strong> 68% data dalam 1 SD, 95% dalam 2 SD, 99.7% dalam 3 SD</li>
                    </ul>
                </div>
            </div>

            <!-- Tab Metode -->
            <div id="metode" class="tab-content">
                <div class="section">
                    <h2>Metode-Metode Uji Normalitas</h2>

                    <h3>1. Uji Kolmogorov-Smirnov</h3>
                    <p>Metode yang membandingkan distribusi frekuensi kumulatif data dengan distribusi normal teoretis.</p>
                    
                    <div class="formula">
                        D = max |F₀(x) - Sₙ(x)|
                    </div>

                    <div class="info-box">
                        <strong>Keterangan:</strong>
                        <ul>
                            <li>D = Nilai statistik Kolmogorov-Smirnov</li>
                            <li>F₀(x) = Fungsi distribusi frekuensi kumulatif teoritis</li>
                            <li>Sₙ(x) = Fungsi distribusi frekuensi kumulatif observasi</li>
                        </ul>
                    </div>

                    <h3>2. Uji Shapiro-Wilk</h3>
                    <p>Metode yang sangat sensitif untuk sampel kecil (n < 50), menghitung korelasi antara data dan skor normal.</p>
                    
                    <div class="formula">
                        W = (Σaᵢxᵢ)² / Σ(xᵢ - x̄)²
                    </div>

                    <h3>3. Uji Lilliefors</h3>
                    <p>Modifikasi dari uji Kolmogorov-Smirnov yang tidak memerlukan mean dan standar deviasi populasi.</p>

                    <h3>4. Uji Chi-Square (Kai Kuadrat)</h3>
                    <p>Membandingkan frekuensi observasi dengan frekuensi ekspektasi pada distribusi normal.</p>
                    
                    <div class="formula">
                        χ² = Σ [(Oᵢ - Eᵢ)² / Eᵢ]
                    </div>

                    <div class="info-box warning">
                        <strong>Kriteria Keputusan:</strong>
                        <ul>
                            <li>Jika nilai signifikansi (p-value) > 0.05 → Data <span class="highlight">berdistribusi normal</span></li>
                            <li>Jika nilai signifikansi (p-value) ≤ 0.05 → Data <span class="highlight">tidak berdistribusi normal</span></li>
                        </ul>
                    </div>
                </div>
            </div>

            <!-- Tab Langkah-langkah -->
            <div id="langkah" class="tab-content">
                <div class="section">
                    <h2>Langkah-langkah Uji Normalitas Manual</h2>

                    <h3>Metode: Uji Chi-Square (Kai Kuadrat)</h3>

                    <div class="info-box success">
                        <strong>Contoh Data Nilai Siswa:</strong><br>
                        65, 70, 75, 80, 85, 75, 80, 70, 85, 90, 75, 80, 85, 70, 75, 80, 85, 90, 75, 80
                    </div>

                    <h3>Langkah 1: Hitung Statistik Deskriptif</h3>
                    <ol>
                        <li>Hitung Mean (rata-rata): x̄ = Σx / n</li>
                        <li>Hitung Standar Deviasi: SD = √[Σ(x - x̄)² / n]</li>
                        <li>Tentukan nilai minimum dan maksimum</li>
                    </ol>

                    <h3>Langkah 2: Buat Tabel Distribusi Frekuensi</h3>
                    <ol>
                        <li>Tentukan jumlah kelas (K) = 1 + 3.3 log n</li>
                        <li>Hitung rentang (R) = nilai max - nilai min</li>
                        <li>Hitung panjang kelas (P) = R / K</li>
                        <li>Buat interval kelas</li>
                    </ol>

                    <table>
                        <tr>
                            <th>Kelas</th>
                            <th>Frekuensi Observasi (Oᵢ)</th>
                            <th>Frekuensi Harapan (Eᵢ)</th>
                            <th>(Oᵢ - Eᵢ)²/Eᵢ</th>
                        </tr>
                        <tr>
                            <td>65-69</td>
                            <td>1</td>
                            <td>1.5</td>
                            <td>0.17</td>
                        </tr>
                        <tr>
                            <td>70-74</td>
                            <td>3</td>
                            <td>3.2</td>
                            <td>0.01</td>
                        </tr>
                        <tr>
                            <td>75-79</td>
                            <td>5</td>
                            <td>5.0</td>
                            <td>0.00</td>
                        </tr>
                        <tr>
                            <td>80-84</td>
                            <td>5</td>
                            <td>5.0</td>
                            <td>0.00</td>
                        </tr>
                        <tr>
                            <td>85-89</td>
                            <td>4</td>
                            <td>3.8</td>
                            <td>0.01</td>
                        </tr>
                        <tr>
                            <td>90-94</td>
                            <td>2</td>
                            <td>1.5</td>
                            <td>0.17</td>
                        </tr>
                    </table>

                    <h3>Langkah 3: Hitung Chi-Square</h3>
                    <div class="formula">
                        χ² = Σ [(Oᵢ - Eᵢ)² / Eᵢ] = 0.36
                    </div>

                    <h3>Langkah 4: Bandingkan dengan Tabel Chi-Square</h3>
                    <ul>
                        <li>df (derajat bebas) = k - 3 = 6 - 3 = 3</li>
                        <li>α = 0.05</li>
                        <li>χ²tabel = 7.815</li>
                    </ul>

                    <h3>Langkah 5: Kesimpulan</h3>
                    <div class="info-box success">
                        <p>Karena χ²hitung (0.36) < χ²tabel (7.815), maka <strong>H₀ diterima</strong>.</p>
                        <p><strong>Kesimpulan:</strong> Data nilai siswa <span class="highlight">berdistribusi normal</span> pada tingkat signifikansi 5%.</p>
                    </div>
                </div>
            </div>

            <!-- Tab Kalkulator -->
            <div id="kalkulator" class="tab-content">
                <div class="section">
                    <h2>Kalkulator Uji Normalitas</h2>
                    <p>Masukkan data nilai siswa untuk menghitung statistik deskriptif dan uji normalitas secara otomatis.</p>

                    <div class="calculator">
                        <div class="input-group">
                            <label for="dataInput">Masukkan Data Nilai (pisahkan dengan koma atau spasi):</label>
                            <textarea id="dataInput" rows="4" placeholder="Contoh: 65, 70, 75, 80, 85, 75, 80, 70, 85, 90"></textarea>
                        </div>

                        <button class="btn" onclick="hitungNormalitas()">Hitung Uji Normalitas</button>

                        <div id="hasil" class="result" style="display: none;">
                            <h3>Hasil Analisis</h3>
                            <div id="hasilContent"></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script>
        function openTab(evt, tabName) {
            const tabContents = document.getElementsByClassName('tab-content');
            for (let i = 0; i < tabContents.length; i++) {
                tabContents[i].classList.remove('active');
            }

            const tabs = document.getElementsByClassName('tab');
            for (let i = 0; i < tabs.length; i++) {
                tabs[i].classList.remove('active');
            }

            document.getElementById(tabName).classList.add('active');
            evt.currentTarget.classList.add('active');
        }

        function hitungNormalitas() {
            const input = document.getElementById('dataInput').value;
            const data = input.split(/[\s,]+/).map(Number).filter(n => !isNaN(n));

            if (data.length < 3) {
                alert('Masukkan minimal 3 data nilai!');
                return;
            }

            // Statistik Deskriptif
            const n = data.length;
            const sum = data.reduce((a, b) => a + b, 0);
            const mean = sum / n;
            
            const sortedData = [...data].sort((a, b) => a - b);
            const min = sortedData[0];
            const max = sortedData[n - 1];
            
            // Median
            let median;
            if (n % 2 === 0) {
                median = (sortedData[n/2 - 1] + sortedData[n/2]) / 2;
            } else {
                median = sortedData[Math.floor(n/2)];
            }

            // Standar Deviasi
            const variance = data.reduce((acc, val) => acc + Math.pow(val - mean, 2), 0) / n;
            const sd = Math.sqrt(variance);

            // Skewness (Kemencengan)
            const skewness = (data.reduce((acc, val) => acc + Math.pow(val - mean, 3), 0) / n) / Math.pow(sd, 3);

            // Kurtosis
            const kurtosis = (data.reduce((acc, val) => acc + Math.pow(val - mean, 4), 0) / n) / Math.pow(sd, 4) - 3;

            // Interpretasi
            let interpretasiSkew = '';
            if (Math.abs(skewness) < 0.5) {
                interpretasiSkew = '✅ Data cenderung simetris (mendekati normal)';
            } else if (skewness > 0) {
                interpretasiSkew = '⚠️ Data menceng ke kanan (positif)';
            } else {
                interpretasiSkew = '⚠️ Data menceng ke kiri (negatif)';
            }

            let interpretasiKurt = '';
            if (Math.abs(kurtosis) < 1) {
                interpretasiKurt = '✅ Kurva mendekati normal (mesokurtik)';
            } else if (kurtosis > 0) {
                interpretasiKurt = '⚠️ Kurva lebih lancip (leptokurtik)';
            } else {
                interpretasiKurt = '⚠️ Kurva lebih datar (platikurtik)';
            }

            // Uji Normalitas Sederhana (berdasarkan skewness dan kurtosis)
            let kesimpulan = '';
            if (Math.abs(skewness) < 0.5 && Math.abs(kurtosis) < 1) {
                kesimpulan = '<strong style="color: green;">✅ Data BERDISTRIBUSI NORMAL</strong>';
            } else if (Math.abs(skewness) < 1 && Math.abs(kurtosis) < 2) {
                kesimpulan = '<strong style="color: orange;">⚠️ Data MENDEKATI NORMAL (perlu uji lebih lanjut)</strong>';
            } else {
                kesimpulan = '<strong style="color: red;">❌ Data TIDAK BERDISTRIBUSI NORMAL</strong>';
            }

            // Tampilkan Hasil
            const hasilHTML = `
                <div class="result-item">
                    <strong>Jumlah Data (n):</strong> ${n}
                </div>
                <div class="result-item">
                    <strong>Nilai Minimum:</strong> ${min.toFixed(2)}
                </div>
                <div class="result-item">
                    <strong>Nilai Maksimum:</strong> ${max.toFixed(2)}
                </div>
                <div class="result-item">
                    <strong>Mean (Rata-rata):</strong> ${mean.toFixed(2)}
                </div>
                <div class="result-item">
                    <strong>Median:</strong> ${median.toFixed(2)}
                </div>
                <div class="result-item">
                    <strong>Standar Deviasi:</strong> ${sd.toFixed(2)}
                </div>
                <div class="result-item">
                    <strong>Varians:</strong> ${variance.toFixed(2)}
                </div>
                <div class="result-item">
                    <strong>Skewness (Kemencengan):</strong> ${skewness.toFixed(4)}<br>
                    <em>${interpretasiSkew}</em>
                </div>
                <div class="result-item">
                    <strong>Kurtosis:</strong> ${kurtosis.toFixed(4)}<br>
                    <em>${interpretasiKurt}</em>
                </div>
                <div class="result-item" style="background: #f0f4ff; border: 2px solid #667eea; margin-top: 20px;">
                    <h4 style="color: #667eea; margin-bottom: 10px;">Kesimpulan Uji Normalitas:</h4>
                    ${kesimpulan}
                    <p style="margin-top: 10px; font-size: 0.9em; color: #666;">
                        <em>Catatan: Hasil ini berdasarkan metode skewness dan kurtosis. Untuk hasil yang lebih akurat, gunakan uji Kolmogorov-Smirnov atau Shapiro-Wilk dengan software statistik.</em>
                    </p>
                </div>
            `;

            document.getElementById('hasilContent').innerHTML = hasilHTML;
            document.getElementById('hasil').style.display = 'block';
            document.getElementById('hasil').scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        }
    </script>
</body>
</html>
        '''
        st.components.v1.html(koding, height=2000)
    with pilihan[2]:
        st.write('oke')
        # Fungsi-fungsi statistik
        def hitung_statistik(data):
            """Menghitung statistik deskriptif"""
            return {
                'n': len(data),
                'mean': np.mean(data),
                'median': np.median(data),
                'std': np.std(data, ddof=1),
                'min': np.min(data),
                'max': np.max(data),
                'q1': np.percentile(data, 25),
                'q3': np.percentile(data, 75),
                'skewness': stats.skew(data),
                'kurtosis': stats.kurtosis(data)
            }

        def uji_normalitas_lengkap(data):
            """Melakukan berbagai uji normalitas"""
            hasil = {}
    
            # Shapiro-Wilk Test
            if len(data) >= 3:
                stat_shapiro, p_shapiro = shapiro(data)
                hasil['shapiro'] = {
                    'statistic': stat_shapiro,
                    'p_value': p_shapiro,
                    'normal': p_shapiro > 0.05
                }
    
            # Kolmogorov-Smirnov Test
            stat_ks, p_ks = kstest(data, 'norm', args=(np.mean(data), np.std(data, ddof=1)))
            hasil['ks'] = {
                'statistic': stat_ks,
                'p_value': p_ks,
                'normal': p_ks > 0.05
            }
    
            # D'Agostino-Pearson Test
            if len(data) >= 8:
                stat_dp, p_dp = normaltest(data)
                hasil['dagostino'] = {
                    'statistic': stat_dp,
                    'p_value': p_dp,
                    'normal': p_dp > 0.05
                }
    
            return hasil

        def buat_histogram(data):
            """Membuat histogram dengan kurva normal"""
            fig, ax = plt.subplots(figsize=(10, 6))
    
            # Histogram
            n, bins, patches = ax.hist(data, bins='auto', density=True, 
                                        alpha=0.7, color='steelblue', 
                                        edgecolor='black', label='Data Aktual')
    
            # Kurva normal teoritis
            mu, std = np.mean(data), np.std(data, ddof=1)
            x = np.linspace(mu - 4*std, mu + 4*std, 100)
            ax.plot(x, stats.norm.pdf(x, mu, std), 'r-', 
                    linewidth=2, label='Distribusi Normal')
    
            ax.set_xlabel('Nilai', fontsize=12)
            ax.set_ylabel('Densitas', fontsize=12)
            ax.set_title('Histogram dengan Kurva Normal', fontsize=14, fontweight='bold')
            ax.legend()
            ax.grid(True, alpha=0.3)
    
            return fig

        def buat_qq_plot(data):
            """Membuat Q-Q Plot"""
            fig, ax = plt.subplots(figsize=(8, 8))
            stats.probplot(data, dist="norm", plot=ax)
            ax.set_title('Q-Q Plot', fontsize=14, fontweight='bold')
            ax.grid(True, alpha=0.3)
            return fig

        def buat_boxplot(data):
            """Membuat boxplot"""
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.boxplot(data, vert=False, patch_artist=True,
                       boxprops=dict(facecolor='lightblue', color='blue'),
                       whiskerprops=dict(color='blue'),
                       capprops=dict(color='blue'),
                       medianprops=dict(color='red', linewidth=2))
            ax.set_xlabel('Nilai', fontsize=12)
            ax.set_title('Boxplot Data Nilai', fontsize=14, fontweight='bold')
            ax.grid(True, alpha=0.3)
            return fig

        # Inisialisasi session state
        if 'data_nilai' not in st.session_state:
            st.session_state.data_nilai = [65, 70, 75, 80, 85, 70, 75, 80, 85, 90, 
                                            75, 80, 85, 90, 95, 72, 78, 82, 88, 92]

        if 'quiz_submitted' not in st.session_state:
            st.session_state.quiz_submitted = False

        if 'quiz_answers' not in st.session_state:
            st.session_state.quiz_answers = {}

        # Header
        st.title("📊 Uji Normalitas Data Nilai Kelas")
        st.markdown("### Aplikasi Pembelajaran Statistik Interaktif")
        st.markdown("---")

        # Tabs
        tab1, tab2, tab3, tab4 = st.tabs(["📚 Materi", "🎮 Praktik Interaktif", "✏️ Latihan Soal", "🧮 Kalkulator"])

        # ==================== TAB MATERI ====================
        with tab1:
            st.header("📖 Materi Uji Normalitas")
    
            # Pengertian
            st.subheader("🎯 Apa itu Uji Normalitas?")
            st.info("""
            **Uji normalitas** adalah prosedur statistik untuk menguji apakah data yang dikumpulkan 
            berdistribusi normal atau tidak. Hal ini penting karena banyak uji statistik parametrik 
            mengasumsikan data berdistribusi normal.
    
            Dalam konteks nilai kelas, uji normalitas membantu kita memahami apakah sebaran nilai 
            siswa mengikuti pola distribusi normal (kurva lonceng), di mana sebagian besar siswa 
            mendapat nilai rata-rata, sementara nilai sangat tinggi dan sangat rendah lebih sedikit.
            """)
    
            # Metode Pengujian
            st.subheader("🔬 Metode Pengujian Normalitas")
    
            col1, col2 = st.columns(2)
    
            with col1:
                st.markdown("#### 1️⃣ Metode Grafis")
                st.success("""
                **a. Histogram**
                - Visualisasi distribusi frekuensi data
                - Data normal membentuk kurva lonceng simetris
        
                **b. Q-Q Plot (Quantile-Quantile Plot)**
                - Membandingkan kuantil data dengan distribusi normal teoritis
                - Jika titik-titik mendekati garis diagonal → data normal
        
                **c. Boxplot**
                - Melihat simetri dan outlier
                - Data normal: median di tengah, whisker seimbang
                """)
    
            with col2:
                st.markdown("#### 2️⃣ Metode Numerik")
                st.warning("""
                **a. Shapiro-Wilk Test**
                - Paling powerful untuk sampel kecil (n < 50)
                - H₀: Data berdistribusi normal
                - Keputusan: p-value > 0.05 → normal
        
                **b. Kolmogorov-Smirnov Test**
                - Untuk sampel besar (n > 50)
                - Membandingkan distribusi empiris dengan teoritis
        
                **c. Skewness & Kurtosis**
                - Skewness ≈ 0: simetris
                - Kurtosis ≈ 0: ketebalan normal
                """)
    
            # Interpretasi
            st.subheader("📊 Interpretasi Hasil")
    
            tab_skew, tab_kurt, tab_uji = st.tabs(["Skewness", "Kurtosis", "Uji Statistik"])
    
            with tab_skew:
                st.markdown("""
                **Skewness (Kemencengan)**
        
                | Nilai | Interpretasi | Bentuk Distribusi |
                |-------|--------------|-------------------|
                | Skewness ≈ 0 | Simetris (Normal) | Kurva lonceng sempurna |
                | Skewness > 0 | Menceng ke kanan (Positif) | Ekor memanjang ke kanan |
                | Skewness < 0 | Menceng ke kiri (Negatif) | Ekor memanjang ke kiri |
        
                **Kriteria:** Data normal jika **|Skewness| < 2**
                """)
    
            with tab_kurt:
                st.markdown("""
                **Kurtosis (Keruncingan)**
        
                | Nilai | Interpretasi | Karakteristik |
                |-------|--------------|---------------|
                | Kurtosis ≈ 0 | Mesokurtik (Normal) | Ketebalan ekor normal |
                | Kurtosis > 0 | Leptokurtik | Runcing, ekor tebal |
                | Kurtosis < 0 | Platikurtik | Datar, ekor tipis |
        
                **Kriteria:** Data normal jika **|Kurtosis| < 7**
                """)
    
            with tab_uji:
                st.markdown("""
                **Pengujian Hipotesis**
        
                - **H₀ (Hipotesis Nol):** Data berdistribusi normal
                - **H₁ (Hipotesis Alternatif):** Data tidak berdistribusi normal
                - **α (Tingkat Signifikansi):** 0.05 (5%)
        
                **Keputusan:**
                - Jika **p-value > 0.05** → Terima H₀ (Data Normal)
                - Jika **p-value ≤ 0.05** → Tolak H₀ (Data Tidak Normal)
                """)
    
            # Pentingnya
            st.subheader("⭐ Pentingnya Uji Normalitas")
            st.error("""
            1. **Menentukan metode statistik yang tepat** untuk analisis lanjutan
            2. **Memvalidasi asumsi** untuk uji parametrik (t-test, ANOVA, regresi)
            3. **Memahami karakteristik** distribusi data nilai siswa
            4. **Mendeteksi outlier** atau nilai ekstrem dalam data
            5. **Meningkatkan validitas** kesimpulan penelitian
            """)

        # ==================== TAB PRAKTIK INTERAKTIF ====================
        with tab2:
            st.header("🎮 Praktik Interaktif: Analisis Data Nilai")
    
            # Input Data
            st.subheader("📝 Input Data Nilai")
    
            col_input1, col_input2 = st.columns([2, 1])
    
            with col_input1:
                metode_input = st.radio(
                    "Pilih metode input data:",
                    ["Manual (ketik)", "Generate Random", "Upload File CSV"],
                    horizontal=True
                )
        
                if metode_input == "Manual (ketik)":
                    input_text = st.text_area(
                        "Masukkan data nilai (pisahkan dengan koma atau spasi):",
                        value=", ".join(map(str, st.session_state.data_nilai)),
                        height=100
                    )
                    if st.button("🔄 Proses Data"):
                        try:
                            # Parse input
                            data_baru = [float(x.strip()) for x in input_text.replace(',', ' ').split() if x.strip()]
                            if len(data_baru) < 3:
                                st.error("Minimal 3 data diperlukan!")
                            else:
                                st.session_state.data_nilai = data_baru
                                st.success(f"✅ Berhasil memproses {len(data_baru)} data!")
                                st.rerun()
                        except:
                            st.error("Format data tidak valid! Gunakan angka yang dipisahkan koma atau spasi.")
        
                elif metode_input == "Generate Random":
                    col_gen1, col_gen2, col_gen3 = st.columns(3)
                    with col_gen1:
                        n_data = st.number_input("Jumlah data:", 10, 100, 30)
                    with col_gen2:
                        mean_val = st.number_input("Rata-rata:", 0, 100, 75)
                    with col_gen3:
                        std_val = st.number_input("Std Dev:", 1, 30, 10)
            
                    if st.button("🎲 Generate Data Random"):
                        st.session_state.data_nilai = np.random.normal(mean_val, std_val, n_data).tolist()
                        st.session_state.data_nilai = [round(max(0, min(100, x)), 1) for x in st.session_state.data_nilai]
                        st.success(f"✅ Generated {n_data} data nilai!")
                        st.rerun()
        
                else:  # Upload CSV
                    uploaded_file = st.file_uploader("Upload file CSV", type=['csv'])
                    if uploaded_file is not None:
                        try:
                            df = pd.read_csv(uploaded_file)
                            kolom = st.selectbox("Pilih kolom yang berisi nilai:", df.columns)
                            if st.button("📥 Load Data dari CSV"):
                                st.session_state.data_nilai = df[kolom].dropna().tolist()
                                st.success(f"✅ Berhasil load {len(st.session_state.data_nilai)} data!")
                                st.rerun()
                        except Exception as e:
                            st.error(f"Error membaca file: {e}")
    
            with col_input2:
                st.info(f"""
                **Data Saat Ini:**
                - Jumlah: {len(st.session_state.data_nilai)}
                - Range: {min(st.session_state.data_nilai):.1f} - {max(st.session_state.data_nilai):.1f}
                """)
    
            st.markdown("---")
    
            # Analisis Data
            if len(st.session_state.data_nilai) >= 3:
                data = np.array(st.session_state.data_nilai)
                stats_data = hitung_statistik(data)
                hasil_uji = uji_normalitas_lengkap(data)
        
                # Statistik Deskriptif
                st.subheader("📊 Statistik Deskriptif")
        
                col1, col2, col3, col4, col5 = st.columns(5)
                col1.metric("Jumlah Data", f"{stats_data['n']}")
                col2.metric("Rata-rata", f"{stats_data['mean']:.2f}")
                col3.metric("Median", f"{stats_data['median']:.2f}")
                col4.metric("Std Dev", f"{stats_data['std']:.2f}")
                col5.metric("Range", f"{stats_data['max'] - stats_data['min']:.1f}")
        
                st.markdown("---")
        
                # Hasil Uji Normalitas
                st.subheader("🔬 Hasil Uji Normalitas")
        
                col_uji1, col_uji2 = st.columns(2)
        
                with col_uji1:
                    st.markdown("#### 📈 Ukuran Bentuk Distribusi")
            
                    skew_val = stats_data['skewness']
                    kurt_val = stats_data['kurtosis']
            
                    # Skewness
                    skew_color = "green" if abs(skew_val) < 2 else "red"
                    st.markdown(f"**Skewness:** :{skew_color}[{skew_val:.3f}]")
                    if abs(skew_val) < 0.5:
                        st.success("✅ Data sangat simetris (mendekati normal)")
                    elif abs(skew_val) < 2:
                        st.warning("⚠️ Data agak menceng (masih dapat diterima)")
                    else:
                        st.error("❌ Data sangat menceng (tidak normal)")
            
                    # Kurtosis
                    kurt_color = "green" if abs(kurt_val) < 7 else "red"
                    st.markdown(f"**Kurtosis:** :{kurt_color}[{kurt_val:.3f}]")
                    if abs(kurt_val) < 3:
                        st.success("✅ Ketebalan ekor normal")
                    elif abs(kurt_val) < 7:
                        st.warning("⚠️ Ketebalan ekor agak ekstrem")
                    else:
                        st.error("❌ Ketebalan ekor sangat ekstrem (tidak normal)")
        
                with col_uji2:
                    st.markdown("#### 🧪 Uji Statistik")
            
                    # Shapiro-Wilk
                    if 'shapiro' in hasil_uji:
                        sw = hasil_uji['shapiro']
                        st.markdown(f"**Shapiro-Wilk Test**")
                        st.write(f"- Statistik: {sw['statistic']:.4f}")
                        st.write(f"- p-value: {sw['p_value']:.4f}")
                        if sw['normal']:
                            st.success("✅ Data berdistribusi normal (p > 0.05)")
                        else:
                            st.error("❌ Data tidak berdistribusi normal (p ≤ 0.05)")
            
                    # Kolmogorov-Smirnov
                    if 'ks' in hasil_uji:
                        ks = hasil_uji['ks']
                        st.markdown(f"**Kolmogorov-Smirnov Test**")
                        st.write(f"- Statistik: {ks['statistic']:.4f}")
                        st.write(f"- p-value: {ks['p_value']:.4f}")
                        if ks['normal']:
                            st.success("✅ Data berdistribusi normal (p > 0.05)")
                        else:
                            st.error("❌ Data tidak berdistribusi normal (p ≤ 0.05)")
        
                # Kesimpulan
                st.markdown("---")
                st.subheader("📋 Kesimpulan")
        
                # Hitung berapa banyak kriteria yang terpenuhi
                kriteria_terpenuhi = 0
                total_kriteria = 0
        
                # Skewness & Kurtosis
                if abs(stats_data['skewness']) < 2:
                    kriteria_terpenuhi += 1
                total_kriteria += 1
        
                if abs(stats_data['kurtosis']) < 7:
                    kriteria_terpenuhi += 1
                total_kriteria += 1
        
                # Uji statistik
                for key in ['shapiro', 'ks']:
                    if key in hasil_uji:
                        if hasil_uji[key]['normal']:
                            kriteria_terpenuhi += 1
                        total_kriteria += 1
        
                persentase = (kriteria_terpenuhi / total_kriteria) * 100
        
                if persentase >= 75:
                    st.success(f"""
                    ### ✅ Data BERDISTRIBUSI NORMAL
            
                    **Kriteria terpenuhi:** {kriteria_terpenuhi}/{total_kriteria} ({persentase:.0f}%)
            
                    **Interpretasi:** Data nilai kelas ini mengikuti distribusi normal. 
                    Anda dapat menggunakan uji statistik parametrik (t-test, ANOVA, dll.) 
                        untuk analisis lebih lanjut.
                        """)
                else:
                    st.error(f"""
                    ### ❌ Data TIDAK BERDISTRIBUSI NORMAL
            
                    **Kriteria terpenuhi:** {kriteria_terpenuhi}/{total_kriteria} ({persentase:.0f}%)
            
                    **Interpretasi:** Data nilai kelas ini tidak mengikuti distribusi normal. 
                    Pertimbangkan menggunakan uji statistik non-parametrik (Mann-Whitney, 
                    Kruskal-Wallis, dll.) atau transformasi data.
                    """)
        
                st.markdown("---")
        
                # Visualisasi
                st.subheader("📊 Visualisasi Data")
        
                tab_hist, tab_qq, tab_box = st.tabs(["Histogram", "Q-Q Plot", "Boxplot"])
        
                with tab_hist:
                    st.pyplot(buat_histogram(data))
                    st.info("""
                    **Cara Membaca:**
                    - Batang biru: distribusi data aktual
                    - Garis merah: kurva normal teoritis
                    - Jika batang mengikuti garis merah → data normal
                    """)
        
                with tab_qq:
                    st.pyplot(buat_qq_plot(data))
                    st.info("""
                    **Cara Membaca:**
                    - Titik biru: data observasi
                    - Garis merah: garis referensi normal
                    - Jika titik mendekati garis → data normal
                    - Titik menyimpang dari garis → data tidak normal
                    """)
        
                with tab_box:
                    st.pyplot(buat_boxplot(data))
                    st.info("""
                    **Cara Membaca:**
                    - Kotak: Q1, Median (garis merah), Q3
                    - Whisker: nilai min dan max (tanpa outlier)
                    - Titik: outlier
                    - Jika median di tengah kotak dan whisker seimbang → data normal
                    """)
        
                # Tabel Data
                st.markdown("---")
                with st.expander("📋 Lihat Tabel Data Lengkap"):
                    df_data = pd.DataFrame({
                        'No': range(1, len(data) + 1),
                        'Nilai': data
                    })
                    st.dataframe(df_data, use_container_width=True)
            
                    # Download
                    csv = df_data.to_csv(index=False)
                    st.download_button(
                        label="📥 Download Data CSV",
                        data=csv,
                        file_name="data_nilai.csv",
                        mime="text/csv"
                    )

        # ==================== TAB LATIHAN SOAL ====================
        with tab3:
            st.header("✏️ Latihan Soal Pilihan Ganda")
    
            # Definisi soal
            soal_quiz = [
                {
                    "no": 1,
                    "pertanyaan": "Apa tujuan utama dari uji normalitas data?",
                    "pilihan": [
                        "Menghitung rata-rata data",
                        "Menguji apakah data berdistribusi normal",
                        "Mencari nilai tertinggi dalam data",
                        "Menghitung median data"
                    ],
                    "jawaban": 1,
                    "pembahasan": "Uji normalitas bertujuan untuk menguji apakah data berdistribusi normal atau tidak, yang penting untuk menentukan jenis uji statistik yang akan digunakan."
                },
                {
                    "no": 2,
                    "pertanyaan": "Jika nilai skewness mendekati 0, maka distribusi data adalah?",
                    "pilihan": [
                        "Menceng ke kiri (negatif)",
                        "Menceng ke kanan (positif)",
                        "Simetris (mendekati normal)",
                        "Tidak dapat ditentukan"
                    ],
                    "jawaban": 2,
                    "pembahasan": "Skewness mengukur tingkat kemencengan distribusi. Nilai skewness ≈ 0 menunjukkan distribusi yang simetris atau mendekati normal."
                },
                {
                    "no": 3,
                    "pertanyaan": "Metode grafis yang paling tepat untuk melihat normalitas data adalah?",
                   "pilihan": [
                        "Diagram lingkaran (pie chart)",
                        "Histogram dan Q-Q Plot",
                        "Diagram batang biasa",
                        "Line chart"
                    ],
                    "jawaban": 1,
                    "pembahasan": "Histogram menunjukkan bentuk distribusi data, sedangkan Q-Q Plot membandingkan kuantil data dengan distribusi normal teoritis."
                },
                {
                    "no": 4,
                    "pertanyaan": "Pada uji Shapiro-Wilk, jika p-value = 0.08, maka kesimpulannya adalah?",
                    "pilihan": [
                        "Data tidak berdistribusi normal",
                        "Data berdistribusi normal",
                        "Perlu uji ulang",
                        "Data memiliki outlier"
                    ],
                    "jawaban": 1,
                    "pembahasan": "Dengan α = 0.05, jika p-value (0.08) > 0.05, maka kita terima H₀ yang berarti data berdistribusi normal."
                },
                {
                    "no": 5,
                    "pertanyaan": "Kurtosis mengukur apa dalam distribusi data?",
                    "pilihan": [
                        "Tingkat kemencengan distribusi",
                        "Ketebalan ekor distribusi",
                        "Nilai tengah distribusi",
                        "Penyebaran data"
                    ],
                    "jawaban": 1,
                    "pembahasan": "Kurtosis mengukur ketebalan ekor dan keruncingan distribusi. Nilai kurtosis ≈ 0 menunjukkan distribusi normal (mesokurtik)."
                },
                {
                    "no": 6,
                    "pertanyaan": "Jika data tidak berdistribusi normal, uji statistik apa yang sebaiknya digunakan?",
                    "pilihan": [
                        "Uji t (t-test)",
                        "ANOVA",
                        "Uji non-parametrik (Mann-Whitney, Kruskal-Wallis)",
                        "Regresi linear"
                    ],
                    "jawaban": 2,
                    "pembahasan": "Untuk data yang tidak berdistribusi normal, gunakan uji non-parametrik yang tidak mengasumsikan distribusi normal."
                },
                {
                    "no": 7,
                    "pertanyaan": "Pada Q-Q Plot, jika titik-titik data menyebar jauh dari garis diagonal, artinya?",
                    "pilihan": [
                        "Data berdistribusi normal",
                        "Data tidak berdistribusi normal",
                        "Data memiliki rata-rata tinggi",
                        "Data tidak memiliki outlier"
                    ],
                    "jawaban": 1,
                    "pembahasan": "Jika titik-titik pada Q-Q Plot menyimpang jauh dari garis diagonal, ini mengindikasikan bahwa data tidak mengikuti distribusi normal."
                },
                {
                    "no": 8,
                    "pertanyaan": "Kriteria skewness untuk data berdistribusi normal adalah?",
                    "pilihan": [
                        "|Skewness| > 5",
                        "|Skewness| < 2",
                        "|Skewness| = 10",
                        "Skewness > 0"
                    ],
                    "jawaban": 1,
                    "pembahasan": "Data dianggap berdistribusi normal jika nilai absolut skewness kurang dari 2 (|Skewness| < 2)."
                }
            ]
    
            # Tampilkan soal
            for soal in soal_quiz:
                st.markdown(f"### Soal {soal['no']}")
                st.write(soal['pertanyaan'])
        
                jawaban_user = st.radio(
                    f"Pilih jawaban untuk soal {soal['no']}:",
                    soal['pilihan'],
                    key=f"soal_{soal['no']}",
                    index=None
                )
        
                if jawaban_user:
                    st.session_state.quiz_answers[soal['no']] = soal['pilihan'].index(jawaban_user)
        
                st.markdown("---")
    
            # Tombol submit
            col_submit1, col_submit2 = st.columns([1, 3])
    
            with col_submit1:
                if st.button("✅ Submit Jawaban", use_container_width=True):
                    st.session_state.quiz_submitted = True
    
            with col_submit2:
                if st.button("🔄 Reset Quiz", use_container_width=True):
                    st.session_state.quiz_submitted = False
                    st.session_state.quiz_answers = {}
                    st.rerun()
    
            # Tampilkan hasil
            if st.session_state.quiz_submitted:
                st.markdown("---")
                st.subheader("📊 Hasil Quiz")
        
                benar = 0
                total = len(soal_quiz)
        
                for soal in soal_quiz:
                    jawaban_user = st.session_state.quiz_answers.get(soal['no'])
                    jawaban_benar = soal['jawaban']
            
                    if jawaban_user == jawaban_benar:
                        benar += 1
                        st.success(f"**Soal {soal['no']}:** ✅ Benar!")
                    else:
                        st.error(f"**Soal {soal['no']}:** ❌ Salah!")
                        if jawaban_user is not None:
                            st.write(f"Jawaban Anda: {soal['pilihan'][jawaban_user]}")
                        st.write(f"Jawaban Benar: {soal['pilihan'][jawaban_benar]}")
            
                    with st.expander(f"💡 Pembahasan Soal {soal['no']}"):
                        st.info(soal['pembahasan'])
        
                # Nilai akhir
                nilai = (benar / total) * 100
        
                st.markdown("---")
                col_nilai1, col_nilai2, col_nilai3 = st.columns(3)
        
                with col_nilai1:
                    st.metric("Jawaban Benar", f"{benar}/{total}")
                with col_nilai2:
                    st.metric("Nilai Akhir", f"{nilai:.1f}")
                with col_nilai3:
                    if nilai >= 80:
                        st.success("🌟 Excellent!")
                    elif nilai >= 60:
                        st.info("👍 Good Job!")
                    else:
                        st.warning("💪 Keep Learning!")
    
            # Latihan Praktik Tambahan
            st.markdown("---")
            st.subheader("💡 Latihan Praktik Mandiri")
    
            with st.expander("📝 Soal Latihan 1: Analisis Data Manual"):
                st.write("""
        **Soal:**
        Diberikan data nilai ujian matematika dari 15 siswa:
        
        **60, 65, 70, 70, 75, 75, 75, 80, 80, 85, 85, 90, 90, 95, 100**
        
        **Tugas:**
        1. Hitung rata-rata dan standar deviasi
        2. Hitung skewness dan kurtosis
        3. Buat histogram distribusi frekuensi (kelompokkan dalam interval)
        4. Tentukan apakah data berdistribusi normal
        5. Berikan interpretasi hasil analisis
        
        **Tips:** Gunakan tab "Praktik Interaktif" untuk memverifikasi jawaban Anda!
        """)
    
            with st.expander("📝 Soal Latihan 2: Interpretasi Hasil"):
                st.write("""
        **Soal:**
        Hasil uji normalitas suatu data nilai menunjukkan:
        - Skewness = 0.15
        - Kurtosis = -0.45
        - Shapiro-Wilk p-value = 0.23
        - Kolmogorov-Smirnov p-value = 0.18
        
        **Pertanyaan:**
        1. Apakah data berdistribusi normal? Jelaskan!
        2. Bagaimana bentuk distribusi data tersebut?
        3. Uji statistik apa yang tepat digunakan untuk data ini?
        
        **Jawaban:**
        1. Ya, data berdistribusi normal karena:
           - |Skewness| = 0.15 < 2 ✅
           - |Kurtosis| = 0.45 < 7 ✅
           - p-value Shapiro-Wilk = 0.23 > 0.05 ✅
           - p-value K-S = 0.18 > 0.05 ✅
        
        2. Distribusi hampir simetris (skewness ≈ 0) dengan ketebalan ekor normal (kurtosis ≈ 0)
        
        3. Dapat menggunakan uji parametrik seperti t-test, ANOVA, atau regresi linear
        """)
    
            with st.expander("📝 Soal Latihan 3: Kasus Nyata"):
                st.write("""
        **Kasus:**
        Seorang guru ingin menganalisis nilai ujian akhir semester dari 2 kelas:
        - **Kelas A:** 85, 87, 89, 90, 91, 88, 86, 92, 93, 88
        - **Kelas B:** 60, 70, 85, 90, 95, 75, 80, 85, 65, 100
        
        **Tugas:**
        1. Uji normalitas kedua kelas
        2. Bandingkan distribusi kedua kelas
        3. Metode statistik apa yang tepat untuk membandingkan kedua kelas?
        4. Kelas mana yang memiliki performa lebih konsisten?
        
        **Petunjuk Analisis:**
        - Masukkan data Kelas A dan Kelas B ke tab "Praktik Interaktif"
        - Perhatikan mean, std dev, dan hasil uji normalitas
        - Std dev lebih kecil = lebih konsisten
        """)

        # ==================== TAB KALKULATOR ====================
        with tab4:
            st.header("🧮 Kalkulator Uji Normalitas")
            st.write("Masukkan data dan dapatkan hasil analisis lengkap dengan cepat!")
    
            col_kalk1, col_kalk2 = st.columns([3, 2])
    
            with col_kalk1:
                st.subheader("Input Data")
        
                input_kalkulator = st.text_area(
                    "Masukkan data (pisahkan dengan koma, spasi, atau baris baru):",
                    height=150,
                    placeholder="Contoh:\n75, 80, 85, 90\natau\n75\n80\n85\n90"
                )
        
                alpha_level = st.select_slider(
                    "Pilih tingkat signifikansi (α):",
                    options=[0.01, 0.05, 0.10],
                    value=0.05,
                    format_func=lambda x: f"{x*100:.0f}% ({x})"
                )

def tampilkan_materi8():
    st.markdown('''<iframe src="https://martin-bernard26.github.io/Angket_kepuasan/angket_kepuasan.html" style="width:100%; height:4500px"></iframe>''', unsafe_allow_html=True)
    
def tampilkan_materi9():
    kolom = st.columns(3)
    with kolom[0]:
        if st.button("Teori Homogen"):
            st.session_state.tampilan1=False
            st.session_state.tampilan2=False
            st.session_state.tampilan3 = False
            st.session_state.tampilan4 = False
            st.session_state.tampilan5 = False
            st.session_state.tampilan6 = False
            st.session_state.tampilan7 = False
            st.session_state.tampilan8 = False
            st.session_state.tampilan9 = False
            st.session_state.tampilan10 = False
            st.session_state.tampilan11 = False
            st.session_state.tampilan12 = False
            st.session_state.tampilan13 = False
            st.session_state.tampilan14 = True
            st.session_state.tampilan15 = False
            st.session_state.tampilan16 = False
            st.session_state.tampilan17 = False
            st.session_state.tampilan18 = False
            st.session_state.tampilan19 = False
            st.session_state.tampilan20 = False
            st.session_state.tampilan21 = False
            st.session_state.tampilan22 = False
            st.session_state.tampilan23 = False
            st.session_state.tampilan24 = False
            st.session_state.tampilan25 = False
            st.session_state.tampilan26 = False
            st.session_state.tampilan27 = False
            st.session_state.tampilan28 = False
            st.session_state.tampilan29 = False
            st.session_state.tampilan30 = False
            st.rerun()
    with kolom[1]:
        if st.button("Uji F"):
            st.session_state.tampilan1=False
            st.session_state.tampilan2=False
            st.session_state.tampilan3 = False
            st.session_state.tampilan4 = False
            st.session_state.tampilan5 = False
            st.session_state.tampilan6 = False
            st.session_state.tampilan7 = False
            st.session_state.tampilan8 = False
            st.session_state.tampilan9 = False
            st.session_state.tampilan10 = False
            st.session_state.tampilan11 = False
            st.session_state.tampilan12 = False
            st.session_state.tampilan13 = False
            st.session_state.tampilan14 = False
            st.session_state.tampilan15 = True
            st.session_state.tampilan16 = False
            st.session_state.tampilan17 = False
            st.session_state.tampilan18 = False
            st.session_state.tampilan19 = False
            st.session_state.tampilan20 = False
            st.session_state.tampilan21 = False
            st.session_state.tampilan22 = False
            st.session_state.tampilan23 = False
            st.session_state.tampilan24 = False
            st.session_state.tampilan25 = False
            st.session_state.tampilan26 = False
            st.session_state.tampilan27 = False
            st.session_state.tampilan28 = False
            st.session_state.tampilan29 = False
            st.session_state.tampilan30 = False
            st.rerun()
    with kolom[2]:
        if st.button("Contoh Uji Homogen Lainnya"):
            st.session_state.tampilan1=False
            st.session_state.tampilan2=False
            st.session_state.tampilan3 = False
            st.session_state.tampilan4 = False
            st.session_state.tampilan5 = False
            st.session_state.tampilan6 = False
            st.session_state.tampilan7 = False
            st.session_state.tampilan8 = False
            st.session_state.tampilan9 = False
            st.session_state.tampilan10 = False
            st.session_state.tampilan11 = False
            st.session_state.tampilan12 = False
            st.session_state.tampilan13 = True
            st.session_state.tampilan14 = False
            st.session_state.tampilan15 = False
            st.session_state.tampilan16 = False
            st.session_state.tampilan17 = False
            st.session_state.tampilan18 = False
            st.session_state.tampilan19 = False
            st.session_state.tampilan20 = False
            st.session_state.tampilan21 = False
            st.session_state.tampilan22 = False
            st.session_state.tampilan23 = False
            st.session_state.tampilan24 = False
            st.session_state.tampilan25 = False
            st.session_state.tampilan26 = False
            st.session_state.tampilan27 = False
            st.session_state.tampilan28 = False
            st.session_state.tampilan29 = False
            st.session_state.tampilan30 = False
            st.rerun()
    # Custom CSS
    st.markdown("""
    <style>
    .main {
        padding: 0rem 1rem;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
    }
    .stTabs [data-baseweb="tab"] {
        padding: 10px 20px;
        background-color: #f0f2f6;
        border-radius: 10px;
    }
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
    }
    .info-box {
        background-color: #d1ecf1;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #17a2b8;
        margin: 10px 0;
    }
    .warning-box {
        background-color: #f8d7da;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #dc3545;
        margin: 10px 0;
    }
    .success-box {
        background-color: #d4edda;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #28a745;
        margin: 10px 0;
    }
    .formula-box {
        background-color: #fff3cd;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #ffc107;
        margin: 10px 0;
        font-family: monospace;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

    # Header
    st.markdown("""
    <h1 style='text-align: center; color: #667eea;'>
        📊 Uji Homogenitas Varians
    </h1>
    <p style='text-align: center; font-size: 1.2em; color: #666;'>
        Memahami dan Mempraktikkan Uji Homogenitas dalam Analisis Statistik
    </p>
    <hr>
    """, unsafe_allow_html=True)

    # Tabs
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "📚 Teori", "🎯 Metode Uji", "🧪 Simulasi Data", 
    "📂 Upload Data", "📈 Analisis Lanjutan", "💡 Studi Kasus"
    ])

    # TAB 1: TEORI
    with tab1:
        st.header("📚 Pengertian Uji Homogenitas")
    
        col1, col2 = st.columns([2, 1])
    
        with col1:
            st.markdown("""
        <div class="info-box" style="color:black">
        <h3>Apa itu Uji Homogenitas?</h3>
        <p>
        Uji homogenitas adalah uji statistik yang digunakan untuk mengetahui apakah 
        beberapa kelompok data memiliki varians (ragam) yang sama atau tidak. 
        Uji ini merupakan <strong>syarat penting</strong> dalam analisis parametrik seperti 
        ANOVA, uji-t, dan regresi.
        </p>
        </div>
        """, unsafe_allow_html=True)
        
            st.markdown("""
        ### 🎯 Tujuan Uji Homogenitas
        
        1. **Memenuhi Asumsi ANOVA**: Memastikan varians antar kelompok sama
        2. **Validitas Uji Statistik**: Meningkatkan keakuratan hasil analisis
        3. **Pemilihan Metode**: Menentukan uji statistik yang tepat
        4. **Interpretasi Data**: Memahami karakteristik variabilitas data
        """)
        
            st.markdown("""
        ### ✅ Kapan Uji Homogenitas Diperlukan?
        
        - Sebelum melakukan **ANOVA** (Analysis of Variance)
        - Sebelum melakukan **uji-t untuk dua sampel independen**
        - Dalam **analisis regresi** dengan variabel dummy
        - Ketika membandingkan **3 kelompok atau lebih**
        - Dalam **desain eksperimen** dengan beberapa perlakuan
        """)
    
        with col2:
            st.markdown("""
        <div class="warning-box" style="color:black">
        <h4>⚠️ Hipotesis</h4>
        <p><strong>H₀:</strong> Varians semua kelompok sama (homogen)</p>
        <p><strong>H₁:</strong> Minimal ada satu varians kelompok yang berbeda</p>
        </div>
        """, unsafe_allow_html=True)
        
            st.markdown("""
        <div class="success-box" style="color:black">
        <h4>📊 Interpretasi</h4>
        <p><strong>p-value > 0.05:</strong><br>Gagal tolak H₀<br>→ Data homogen ✅</p>
        <p><strong>p-value ≤ 0.05:</strong><br>Tolak H₀<br>→ Data tidak homogen ❌</p>
        </div>
        """, unsafe_allow_html=True)
    
        st.markdown("---")
    
        # Karakteristik
        st.subheader("📋 Karakteristik Data Homogen vs Tidak Homogen")
    
        col1, col2 = st.columns(2)
    
        with col1:
            st.markdown("""
        **Data Homogen (Varians Sama):**
        - Sebaran data antar kelompok relatif sama
        - Box plot menunjukkan lebar yang mirip
        - Cocok untuk uji parametrik
        - Hasil analisis lebih reliabel
        """)
    
        with col2:
            st.markdown("""
        **Data Tidak Homogen (Varians Berbeda):**
        - Sebaran data antar kelompok berbeda signifikan
        - Box plot menunjukkan lebar yang berbeda
        - Perlu uji non-parametrik atau transformasi data
        - Gunakan Welch's ANOVA atau Kruskal-Wallis
        """)

    # TAB 2: METODE UJI
    with tab2:
        st.header("🎯 Metode-Metode Uji Homogenitas")
    
        method_tab1, method_tab2, method_tab3, method_tab4 = st.tabs([
        "Levene Test", "Bartlett Test", "Fligner-Killeen", "Perbandingan"
        ])
    
        with method_tab1:
            st.subheader("1️⃣ Uji Levene")
        
            col1, col2 = st.columns([3, 2])
        
            with col1:
                st.markdown("""
            ### 📖 Deskripsi
            Uji Levene adalah uji yang paling umum digunakan untuk menguji homogenitas varians. 
            Uji ini **robust terhadap pelanggaran asumsi normalitas** dan dapat digunakan 
            untuk berbagai jenis distribusi data.
            
            ### 🔢 Formula
            """)
            
                st.markdown("""
            <div class="formula-box" style='color:black'>
            W = [(N - k) / (k - 1)] × [Σnᵢ(Zᵢ. - Z..)² / Σ(Zᵢⱼ - Zᵢ.)²]
            </div>
            """, unsafe_allow_html=True)
            
                st.markdown("""
            Dimana:
            - **N** = total sampel
            - **k** = jumlah kelompok
            - **Zᵢⱼ** = |Xᵢⱼ - median kelompok i|
            - **nᵢ** = ukuran sampel kelompok ke-i
            """)
        
            with col2:
                st.markdown("""
            ### ✅ Kelebihan
            - Robust terhadap non-normalitas
            - Cocok untuk data skewed
            - Paling sering digunakan
            - Tidak sensitif terhadap outlier
            
            ### ⚠️ Kekurangan
            - Memerlukan sampel minimal 20
            - Power test sedang untuk sampel kecil
            
            ### 📊 Penggunaan
            - **Sangat direkomendasikan** untuk data yang tidak normal
            - Pilihan utama dalam SPSS dan software statistik
            """)
    
        with method_tab2:
            st.subheader("2️⃣ Uji Bartlett")
        
            col1, col2 = st.columns([3, 2])
        
            with col1:
                st.markdown("""
            ### 📖 Deskripsi
            Uji Bartlett digunakan untuk menguji homogenitas varians dari k kelompok. 
            Uji ini **sangat sensitif terhadap asumsi normalitas**, sehingga hanya 
            direkomendasikan jika data benar-benar berdistribusi normal.
            
            ### 🔢 Formula
            """)
            
                st.markdown("""
            <div class="formula-box" style="color:black">
            χ² = [(N - k) × ln(S²pooled) - Σ(nᵢ - 1) × ln(S²ᵢ)] / C
            </div>
            """, unsafe_allow_html=True)
            
                st.markdown("""
            Dimana:
            - **S²pooled** = varians gabungan
            - **S²ᵢ** = varians kelompok ke-i
            - **C** = faktor koreksi
            - Distribusi mengikuti Chi-square
            """)
        
            with col2:
                st.markdown("""
            ### ✅ Kelebihan
            - Power test tinggi untuk data normal
            - Akurat untuk distribusi normal
            - Mudah dihitung
            
            ### ⚠️ Kekurangan
            - **Sangat sensitif** terhadap non-normalitas
            - Tidak robust terhadap outlier
            - Memberikan hasil false positive jika data tidak normal
            
            ### 📊 Penggunaan
            - Hanya untuk data yang **benar-benar normal**
            - Uji normalitas terlebih dahulu
            """)
    
        with method_tab3:
            st.subheader("3️⃣ Uji Fligner-Killeen")
        
            col1, col2 = st.columns([3, 2])
        
            with col1:
                st.markdown("""
            ### 📖 Deskripsi
            Uji Fligner-Killeen adalah uji non-parametrik yang menggunakan ranking 
            dan median. Uji ini sangat robust dan cocok untuk data yang tidak normal 
            atau memiliki outlier.
            
            ### 🔢 Karakteristik
            - Menggunakan **rank (peringkat)** data
            - Berbasis **median absolut deviasi**
            - Distribusi Chi-square
            - Lebih robust dari Levene dan Bartlett
            """)
        
            with col2:
                st.markdown("""
            ### ✅ Kelebihan
            - **Paling robust** terhadap non-normalitas
            - Tahan terhadap outlier
            - Cocok untuk data ordinal
            - Power test baik
            
            ### ⚠️ Kekurangan
            - Kurang populer
            - Komputasi lebih kompleks
            
            ### 📊 Penggunaan
            - Data dengan **distribusi tidak diketahui**
            - Banyak outlier
            - Alternatif Levene
            """)
    
        with method_tab4:
            st.subheader("📊 Perbandingan Metode Uji Homogenitas")
        
            comparison_data = pd.DataFrame({
            'Metode': ['Levene Test', 'Bartlett Test', 'Fligner-Killeen'],
            'Asumsi Normalitas': ['Tidak perlu', 'Harus normal', 'Tidak perlu'],
            'Robustness': ['Tinggi', 'Rendah', 'Sangat Tinggi'],
            'Power Test': ['Sedang-Tinggi', 'Tinggi (jika normal)', 'Sedang-Tinggi'],
            'Sensitivitas Outlier': ['Rendah', 'Tinggi', 'Sangat Rendah'],
            'Rekomendasi': ['Pilihan utama', 'Hanya jika data normal', 'Alternatif robust']
        })
        
            st.dataframe(comparison_data, use_container_width=True)
        
            st.markdown("---")
        
            st.markdown("""
        ### 🎯 Rekomendasi Pemilihan Metode:
        
        **Gunakan Levene Test jika:**
        - Data tidak berdistribusi normal atau tidak diketahui distribusinya
        - Analisis umum (paling sering digunakan)
        - Ingin metode yang robust dan reliable
        
        **Gunakan Bartlett Test jika:**
        - Data sudah dipastikan berdistribusi normal
        - Tidak ada outlier
        - Ingin power test maksimal untuk data normal
        
        **Gunakan Fligner-Killeen jika:**
        - Data memiliki banyak outlier
        - Distribusi sangat tidak normal
        - Ingin metode paling robust
        """)

    # TAB 3: SIMULASI DATA
    with tab3:
        st.header("🧪 Simulasi dan Visualisasi Data")
    
        st.markdown("""
    Bagian ini memungkinkan Anda untuk membuat data simulasi dengan karakteristik 
    yang berbeda dan melakukan uji homogenitas secara langsung.
    """)
    
        col1, col2 = st.columns([1, 2])
    
        with col1:
            st.subheader("⚙️ Pengaturan Simulasi")
        
            num_groups = st.slider("Jumlah Kelompok", 2, 5, 3)
            sample_size = st.slider("Ukuran Sampel per Kelompok", 20, 100, 30)
        
            st.markdown("---")
            st.markdown("### 📊 Parameter Kelompok")
        
            group_params = []
            for i in range(num_groups):
                with st.expander(f"Kelompok {i+1}"):
                    mean = st.number_input(f"Mean Kelompok {i+1}", 0.0, 100.0, 50.0 + i*5, key=f"mean_{i}")
                    std = st.number_input(f"Std Dev Kelompok {i+1}", 1.0, 20.0, 5.0 + i*2, key=f"std_{i}")
                    group_params.append((mean, std))
        
            st.markdown("---")
            generate_button = st.button("🎲 Generate Data", type="primary", use_container_width=True)
    
        with col2:
            if generate_button:
                # Generate data
                groups_data = []
                all_data = []
                group_labels = []
            
                for i, (mean, std) in enumerate(group_params):
                    data = np.random.normal(mean, std, sample_size)
                    groups_data.append(data)
                    all_data.extend(data)
                    group_labels.extend([f'Kelompok {i+1}'] * sample_size)
            
                df_sim = pd.DataFrame({
                'Nilai': all_data,
                'Kelompok': group_labels
                })
            
                # Visualisasi
                st.subheader("📈 Visualisasi Data")
            
                viz_col1, viz_col2 = st.columns(2)
            
                with viz_col1:
                    # Box Plot
                    fig1 = px.box(df_sim, x='Kelompok', y='Nilai', 
                             title='Box Plot - Perbandingan Distribusi',
                             color='Kelompok')
                    fig1.update_layout(showlegend=False, height=400)
                    st.plotly_chart(fig1, use_container_width=True)
            
                with viz_col2:
                    # Violin Plot
                    fig2 = px.violin(df_sim, x='Kelompok', y='Nilai',
                                title='Violin Plot - Distribusi Detail',
                                color='Kelompok', box=True)
                    fig2.update_layout(showlegend=False, height=400)
                    st.plotly_chart(fig2, use_container_width=True)
            
                # Histogram
                fig3 = px.histogram(df_sim, x='Nilai', color='Kelompok',
                               title='Histogram - Distribusi Frekuensi',
                               barmode='overlay', opacity=0.7)
                fig3.update_layout(height=300)
                st.plotly_chart(fig3, use_container_width=True)
            
                st.markdown("---")
            
                # Statistik Deskriptif
                st.subheader("📊 Statistik Deskriptif")
            
                stats_df = df_sim.groupby('Kelompok')['Nilai'].agg([
                ('Jumlah Data', 'count'),
                ('Mean', 'mean'),
                ('Median', 'median'),
                ('Std Dev', 'std'),
                ('Varians', 'var'),
                ('Min', 'min'),
                ('Max', 'max')
                ]).round(3)
            
                st.dataframe(stats_df, use_container_width=True)
            
                st.markdown("---")
            
                # Uji Homogenitas
                st.subheader("🔬 Hasil Uji Homogenitas")
            
                # Levene Test
                stat_levene, p_levene = stats.levene(*groups_data)
            
                # Bartlett Test
                stat_bartlett, p_bartlett = stats.bartlett(*groups_data)
            
                # Fligner-Killeen Test (custom implementation)
                from scipy.stats import fligner
                stat_fligner, p_fligner = fligner(*groups_data)
            
                results_df = pd.DataFrame({
                'Metode Uji': ['Levene Test', 'Bartlett Test', 'Fligner-Killeen Test'],
                'Statistik': [f'{stat_levene:.4f}', f'{stat_bartlett:.4f}', f'{stat_fligner:.4f}'],
                'P-value': [f'{p_levene:.4f}', f'{p_bartlett:.4f}', f'{p_fligner:.4f}'],
                'Keputusan (α=0.05)': [
                    'Homogen ✅' if p_levene > 0.05 else 'Tidak Homogen ❌',
                    'Homogen ✅' if p_bartlett > 0.05 else 'Tidak Homogen ❌',
                    'Homogen ✅' if p_fligner > 0.05 else 'Tidak Homogen ❌'
                    ]
                })
            
                st.dataframe(results_df, use_container_width=True)
            
                # Interpretasi
                st.markdown("---")
                st.subheader("💡 Interpretasi Hasil")
            
                if p_levene > 0.05:
                    st.markdown("""
                <div class="success-box" style="color:black">
                <h4>✅ Kesimpulan (Levene Test - Rekomendasi)</h4>
                <p>Dengan p-value = {:.4f} > α (0.05), maka <strong>gagal tolak H₀</strong>.</p>
                <p><strong>Kesimpulan:</strong> Varians antar kelompok adalah <strong>homogen</strong>.</p>
                <p><strong>Rekomendasi:</strong> Anda dapat melanjutkan dengan uji ANOVA atau uji-t parametrik.</p>
                </div>
                """.format(p_levene), unsafe_allow_html=True)
                else:
                    st.markdown("""
                <div class="warning-box" style="color:black">
                <h4>❌ Kesimpulan (Levene Test - Rekomendasi)</h4>
                <p>Dengan p-value = {:.4f} ≤ α (0.05), maka <strong>tolak H₀</strong>.</p>
                <p><strong>Kesimpulan:</strong> Varians antar kelompok <strong>tidak homogen</strong>.</p>
                <p><strong>Rekomendasi:</strong> Gunakan Welch's ANOVA, Kruskal-Wallis Test, atau transformasi data.</p>
                </div>
                """.format(p_levene), unsafe_allow_html=True)
            
                # Download data
                st.markdown("---")
                csv = df_sim.to_csv(index=False)
                st.download_button(
                    label="📥 Download Data Simulasi (CSV)",
                    data=csv,
                    file_name="data_simulasi_homogenitas.csv",
                    mime="text/csv"
                )

    # TAB 4: UPLOAD DATA
    with tab4:
        st.header("📂 Upload dan Analisis Data Sendiri")
    
        st.markdown("""
    Upload file CSV Anda untuk melakukan uji homogenitas. File harus memiliki minimal 
    dua kolom: satu untuk nilai data dan satu untuk kategori/kelompok.
    """)
    
        # Contoh format
        with st.expander("📋 Lihat Format Data yang Diharapkan"):
            example_df = pd.DataFrame({
            'Kelompok': ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C'],
            'Nilai': [85, 90, 88, 75, 80, 78, 92, 95, 93]
            })
            st.dataframe(example_df)
            st.markdown("**Catatan:** Kolom dapat memiliki nama apa saja, Anda akan memilih kolom mana yang digunakan.")
    
        uploaded_file = st.file_uploader("Upload file CSV", type=['csv'])
    
        if uploaded_file is not None:
            try:
                df_upload = pd.read_csv(uploaded_file)
            
                st.success("✅ File berhasil diupload!")
            
                col1, col2 = st.columns([1, 2])
            
                with col1:
                    st.subheader("⚙️ Pengaturan Kolom")
                
                    # Pilih kolom
                    value_col = st.selectbox("Pilih kolom nilai (numerik)", df_upload.columns)
                    group_col = st.selectbox("Pilih kolom kelompok (kategori)", 
                                        [col for col in df_upload.columns if col != value_col])
                
                    # Pilih metode
                    test_method = st.radio("Pilih Metode Uji", 
                                      ["Levene Test (Rekomendasi)", "Bartlett Test", 
                                       "Fligner-Killeen Test", "Semua Metode"])
                
                    analyze_button = st.button("🔍 Analisis Data", type="primary", use_container_width=True)
            
                with col2:
                    st.subheader("👀 Preview Data")
                    st.dataframe(df_upload.head(10), use_container_width=True)
                    st.caption(f"Total: {len(df_upload)} baris, {len(df_upload.columns)} kolom")
            
                if analyze_button:
                    # Bersihkan data
                    df_clean = df_upload[[group_col, value_col]].dropna()
                
                    # Group data
                    groups = df_clean[group_col].unique()
                    groups_list = [df_clean[df_clean[group_col] == g][value_col].values for g in groups]
                
                    st.markdown("---")
                
                    # Visualisasi
                    st.subheader("📊 Visualisasi Data")
                
                    viz_col1, viz_col2 = st.columns(2)
                
                    with viz_col1:
                        fig1 = px.box(df_clean, x=group_col, y=value_col,
                                 title='Box Plot', color=group_col)
                        fig1.update_layout(showlegend=False, height=400)
                        st.plotly_chart(fig1, use_container_width=True)
                
                    with viz_col2:
                        fig2 = px.violin(df_clean, x=group_col, y=value_col,
                                    title='Violin Plot', color=group_col, box=True)
                        fig2.update_layout(showlegend=False, height=400)
                        st.plotly_chart(fig2, use_container_width=True)
                
                    # Statistik
                    st.markdown("---")
                    st.subheader("📈 Statistik Deskriptif")
                
                    stats_df = df_clean.groupby(group_col)[value_col].agg([
                    ('Count', 'count'),
                    ('Mean', 'mean'),
                    ('Median', 'median'),
                    ('Std Dev', 'std'),
                    ('Variance', 'var'),
                    ('Min', 'min'),
                    ('Max', 'max')
                    ]).round(3)
                
                    st.dataframe(stats_df, use_container_width=True)
                
                    # Uji Homogenitas
                    st.markdown("---")
                    st.subheader("🔬 Hasil Uji Homogenitas")
                
                    if test_method == "Semua Metode":
                        stat_levene, p_levene = stats.levene(*groups_list)
                        stat_bartlett, p_bartlett = stats.bartlett(*groups_list)
                        stat_fligner, p_fligner = stats.fligner(*groups_list)
                    
                        results = pd.DataFrame({
                        'Metode': ['Levene Test', 'Bartlett Test', 'Fligner-Killeen'],
                        'Statistik': [stat_levene, stat_bartlett, stat_fligner],
                        'P-value': [p_levene, p_bartlett, p_fligner],
                        'Kesimpulan': [
                            'Homogen ✅' if p_levene > 0.05 else 'Tidak Homogen ❌',
                            'Homogen ✅' if p_bartlett > 0.05 else 'Tidak Homogen ❌',
                            'Homogen ✅' if p_fligner > 0.05 else 'Tidak Homogen ❌'
                            ]
                        })
                    
                        st.dataframe(results, use_container_width=True)
                    
                        # Interpretasi Levene (rekomendasi)
                        st.markdown("---")
                        st.subheader("💡 Interpretasi (Berdasarkan Levene Test)")
                        if p_levene > 0.05:
                            st.markdown(f"""
                        <div class="success-box">
                        <p><strong>P-value = {p_levene:.4f} > 0.05</strong></p>
                        <p>✅ Data memiliki varians yang <strong>homogen</strong></p>
                        <p>Anda dapat melanjutkan dengan uji parametrik (ANOVA, t-test)</p>
                        </div>
                        """, unsafe_allow_html=True)
                        else:
                            st.markdown(f"""
                        <div class="warning-box">
                        <p><strong>P-value = {p_levene:.4f} ≤ 0.05</strong></p>
                        <p>❌ Data memiliki varians yang <strong>tidak homogen</strong></p>
                        <p>Gunakan Welch's ANOVA atau Kruskal-Wallis Test</p>
                        </div>
                        """, unsafe_allow_html=True)
                
                    else:
                        # Single test
                        if "Levene" in test_method:
                            stat, p_value = stats.levene(*groups_list)
                            method_name = "Levene Test"
                        elif "Bartlett" in test_method:
                            stat, p_value = stats.bartlett(*groups_list)
                            method_name = "Bartlett Test"
                        else:
                            stat, p_value = stats.fligner(*groups_list)
                            method_name = "Fligner-Killeen Test"
                    
                        st.markdown(f"""
                    **Metode:** {method_name}  
                    **Statistik Uji:** {stat:.4f}  
                    **P-value:** {p_value:.4f}  
                    **Tingkat Signifikansi:** α = 0.05
                    """)
                    
                        if p_value > 0.05:
                            st.markdown(f"""
                        <div class="success-box">
                        <h4>✅ Kesimpulan</h4>
                        <p>Dengan p-value = {p_value:.4f} > 0.05, gagal tolak H₀</p>
                        <p>Data memiliki varians yang <strong>homogen</strong></p>
                        </div>
                        """, unsafe_allow_html=True)
                        else:
                            st.markdown(f"""
                        <div class="warning-box">
                        <h4>❌ Kesimpulan</h4>
                        <p>Dengan p-value = {p_value:.4f} ≤ 0.05, tolak H₀</p>
                        <p>Data memiliki varians yang <strong>tidak homogen</strong></p>
                        </div>
                        """, unsafe_allow_html=True)
        
            except Exception as e:
                st.error(f"❌ Error membaca file: {str(e)}")
                st.info("Pastikan file CSV Anda memiliki format yang benar dengan kolom numerik dan kategori.")

    # TAB 5: ANALISIS LANJUTAN
    with tab5:
        st.header("📈 Analisis Lanjutan")
    
        st.markdown("""
        Bagian ini menampilkan analisis mendalam dan visualisasi tambahan untuk 
        memahami homogenitas data secara komprehensif.
        """)
    
        # Mini simulasi untuk tab ini
        st.subheader("🎲 Generate Data untuk Analisis")
    
        col1, col2, col3 = st.columns(3)
    
        with col1:
            scenario = st.selectbox(
            "Pilih Skenario",
            ["Data Homogen", "Data Tidak Homogen (Varians Berbeda)", 
             "Data Campuran", "Custom"]
            )
    
        with col2:
            n_groups_adv = st.number_input("Jumlah Kelompok", 2, 5, 3, key="adv_groups")
    
        with col3:
            n_samples_adv = st.number_input("Sampel per Kelompok", 20, 100, 50, key="adv_samples")
    
        if st.button("🚀 Generate & Analisis", type="primary"):
            # Generate berdasarkan skenario
            groups_adv = []
        
            if scenario == "Data Homogen":
                # Semua kelompok dengan varians sama
                for i in range(n_groups_adv):
                    data = np.random.normal(50 + i*5, 5, n_samples_adv)
                    groups_adv.append(data)
        
            elif scenario == "Data Tidak Homogen (Varians Berbeda)":
                # Varians berbeda antar kelompok
                for i in range(n_groups_adv):
                    data = np.random.normal(50, 5 + i*5, n_samples_adv)
                    groups_adv.append(data)
        
            elif scenario == "Data Campuran":
                # Kombinasi varians sama dan berbeda
                for i in range(n_groups_adv):
                    if i % 2 == 0:
                        data = np.random.normal(50, 5, n_samples_adv)
                    else:
                        data = np.random.normal(50, 15, n_samples_adv)
                    groups_adv.append(data)
        
            else:  # Custom
                for i in range(n_groups_adv):
                    mean = 50 + np.random.randint(-10, 10)
                    std = np.random.uniform(3, 15)
                    data = np.random.normal(mean, std, n_samples_adv)
                    groups_adv.append(data)
        
            # Buat DataFrame
            all_data_adv = []
            group_labels_adv = []
            for i, data in enumerate(groups_adv):
                all_data_adv.extend(data)
                group_labels_adv.extend([f'Grup {i+1}'] * len(data))
        
            df_adv = pd.DataFrame({
            'Nilai': all_data_adv,
            'Kelompok': group_labels_adv
            })
        
            st.markdown("---")
        
            # 1. Visualisasi Komprehensif
            st.subheader("📊 Visualisasi Komprehensif")
        
            fig = go.Figure()
        
            # Subplot layout
            from plotly.subplots import make_subplots
        
            fig_subplots = make_subplots(
                rows=2, cols=2,
                subplot_titles=('Box Plot', 'Violin Plot', 'Histogram', 'Scatter Plot'),
                specs=[[{'type': 'box'}, {'type': 'violin'}],
                   [{'type': 'bar'}, {'type': 'scatter'}]]
            )
        
            colors = px.colors.qualitative.Set2[:n_groups_adv]
        
            for i, group in enumerate(groups_adv):
                group_name = f'Grup {i+1}'
            
                # Box plot
                fig_subplots.add_trace(
                    go.Box(y=group, name=group_name, marker_color=colors[i],
                       showlegend=False),
                    row=1, col=1
                )
            
                # Violin plot
                fig_subplots.add_trace(
                    go.Violin(y=group, name=group_name, marker_color=colors[i],
                         showlegend=False),
                    row=1, col=2
                )
            
                # Histogram
                fig_subplots.add_trace(
                    go.Histogram(x=group, name=group_name, marker_color=colors[i],
                            opacity=0.7),
                    row=2, col=1
                )
            
                # Scatter
                fig_subplots.add_trace(
                    go.Scatter(x=np.arange(len(group)), y=group, mode='markers',
                              name=group_name, marker=dict(color=colors[i], size=8)),
                    row=2, col=2
                )   
        
            fig_subplots.update_layout(height=700, showlegend=True)
            st.plotly_chart(fig_subplots, use_container_width=True)
        
            st.markdown("---")
        
            # 2. Statistik Detail
            st.subheader("📈 Statistik Detail per Kelompok")
        
            stats_detail = []
            for i, group in enumerate(groups_adv):
                stats_detail.append({
                    'Kelompok': f'Grup {i+1}',
                    'N': len(group),
                    'Mean': np.mean(group),
                    'Median': np.median(group),
                    'Std Dev': np.std(group, ddof=1),
                    'Variance': np.var(group, ddof=1),
                    'CV (%)': (np.std(group, ddof=1) / np.mean(group)) * 100,
                    'Range': np.max(group) - np.min(group),
                    'IQR': np.percentile(group, 75) - np.percentile(group, 25)
                })
        
            stats_detail_df = pd.DataFrame(stats_detail)
            st.dataframe(stats_detail_df.round(3), use_container_width=True)
        
            st.markdown("---")
        
            # 3. Perbandingan Varians Visual
            st.subheader("🔍 Perbandingan Varians Antar Kelompok")
        
            variances = [np.var(g, ddof=1) for g in groups_adv]
        
            fig_var = go.Figure(data=[
                go.Bar(x=[f'Grup {i+1}' for i in range(n_groups_adv)],
                       y=variances,
                       marker_color=colors,
                       text=[f'{v:.2f}' for v in variances],
                       textposition='auto')
            ])
        
            fig_var.update_layout(
                title='Perbandingan Varians (Semakin sama, semakin homogen)',
                xaxis_title='Kelompok',
                yaxis_title='Varians',
                height=400
            )
        
            st.plotly_chart(fig_var, use_container_width=True)
        
            # Rasio varians
            max_var = max(variances)
            min_var = min(variances)
            ratio = max_var / min_var if min_var > 0 else float('inf')
        
            st.markdown(f"""
        **Rasio Varians (Max/Min):** {ratio:.2f}
        
        - **Rasio < 2:** Data kemungkinan homogen ✅
        - **Rasio 2-4:** Data borderline, perlu uji statistik 🟡
        - **Rasio > 4:** Data kemungkinan tidak homogen ❌
        """)
        
            st.markdown("---")
        
            # 4. Uji Homogenitas Lengkap
            st.subheader("🔬 Hasil Uji Homogenitas (Semua Metode)")
        
            stat_l, p_l = stats.levene(*groups_adv)
            stat_b, p_b = stats.bartlett(*groups_adv)
            stat_f, p_f = stats.fligner(*groups_adv)
        
            results_complete = pd.DataFrame({
            'Metode': ['Levene Test', 'Bartlett Test', 'Fligner-Killeen Test'],
            'Statistik Uji': [f'{stat_l:.4f}', f'{stat_b:.4f}', f'{stat_f:.4f}'],
            'P-value': [f'{p_l:.6f}', f'{p_b:.6f}', f'{p_f:.6f}'],
            'α = 0.05': [
                'Homogen ✅' if p_l > 0.05 else 'Tidak Homogen ❌',
                'Homogen ✅' if p_b > 0.05 else 'Tidak Homogen ❌',
                'Homogen ✅' if p_f > 0.05 else 'Tidak Homogen ❌'
            ],
            'α = 0.01': [
                'Homogen ✅' if p_l > 0.01 else 'Tidak Homogen ❌',
                'Homogen ✅' if p_b > 0.01 else 'Tidak Homogen ❌',
                'Homogen ✅' if p_f > 0.01 else 'Tidak Homogen ❌'
            ]
            })
        
            st.dataframe(results_complete, use_container_width=True)
        
            # Visualisasi p-values
            fig_pval = go.Figure()
        
            methods = ['Levene', 'Bartlett', 'Fligner-K']
            p_values = [p_l, p_b, p_f]
        
            fig_pval.add_trace(go.Bar(
                x=methods,
                y=p_values,
                marker_color=['#667eea', '#764ba2', '#f093fb'],
                text=[f'{p:.4f}' for p in p_values],
                textposition='auto'
            ))
        
            fig_pval.add_hline(y=0.05, line_dash="dash", line_color="red",
                              annotation_text="α = 0.05")
            fig_pval.add_hline(y=0.01, line_dash="dash", line_color="orange",
                              annotation_text="α = 0.01")
        
            fig_pval.update_layout(
                title='Perbandingan P-values (Semakin tinggi, semakin homogen)',
                xaxis_title='Metode Uji',
                yaxis_title='P-value',
                height=400
            )
        
            st.plotly_chart(fig_pval, use_container_width=True)
        
            st.markdown("---")
        
            # 5. Kesimpulan dan Rekomendasi
            st.subheader("💡 Kesimpulan dan Rekomendasi")
        
            # Majority voting
            homogen_count = sum([p_l > 0.05, p_b > 0.05, p_f > 0.05])
        
            if homogen_count >= 2:
                st.markdown("""
            <div class="success-box" style="color:black">
            <h4>✅ KESIMPULAN: Data HOMOGEN</h4>
            <p>Mayoritas uji ({}/3) menunjukkan varians kelompok adalah homogen.</p>
            
            <h4>📋 Rekomendasi Analisis Lanjutan:</h4>
            <ul>
                <li>✅ <strong>One-Way ANOVA</strong> - untuk membandingkan mean antar kelompok</li>
                <li>✅ <strong>Independent t-test</strong> - jika hanya 2 kelompok</li>
                <li>✅ <strong>Post-hoc tests</strong> (Tukey HSD, Bonferroni) - jika ANOVA signifikan</li>
                <li>✅ <strong>Regresi Linear</strong> - jika ada variabel prediktor</li>
            </ul>
            </div>
            """.format(homogen_count), unsafe_allow_html=True)
            else:
                st.markdown("""
            <div class="warning-box">
            <h4>❌ KESIMPULAN: Data TIDAK HOMOGEN</h4>
            <p>Mayoritas uji ({}/3) menunjukkan varians kelompok tidak homogen.</p>
            
            <h4>📋 Rekomendasi Analisis Alternatif:</h4>
            <ul>
                <li>🔄 <strong>Transformasi Data</strong> - log, sqrt, atau Box-Cox transformation</li>
                <li>📊 <strong>Welch's ANOVA</strong> - ANOVA yang tidak mengasumsikan varians sama</li>
                <li>📉 <strong>Kruskal-Wallis Test</strong> - alternatif non-parametrik</li>
                <li>🎯 <strong>Welch's t-test</strong> - jika hanya 2 kelompok</li>
                <li>📈 <strong>Robust Regression</strong> - regresi yang tahan terhadap heteroskedastisitas</li>
            </ul>
            
            <h4>🔧 Opsi Transformasi Data:</h4>
            <ul>
                <li><strong>Log transformation:</strong> y' = log(y) - untuk data skewed kanan</li>
                <li><strong>Square root:</strong> y' = √y - untuk data count</li>
                <li><strong>Reciprocal:</strong> y' = 1/y - untuk rasio atau rate</li>
            </ul>
            </div>
            """.format(3 - homogen_count), unsafe_allow_html=True)
        
            # Download hasil
            st.markdown("---")
        
            # Prepare download data
            download_df = df_adv.copy()
            csv_download = download_df.to_csv(index=False)
        
            col_dl1, col_dl2 = st.columns(2)
        
            with col_dl1:
                st.download_button(
                    label="📥 Download Data (CSV)",
                    data=csv_download,
                    file_name="data_analisis_homogenitas.csv",
                    mime="text/csv",
                    use_container_width=True
                )
        
            with col_dl2:
                # Create report
                report = f"""
LAPORAN UJI HOMOGENITAS
========================

Skenario: {scenario}
Jumlah Kelompok: {n_groups_adv}
Sampel per Kelompok: {n_samples_adv}
Total Sampel: {n_groups_adv * n_samples_adv}

HASIL UJI HOMOGENITAS
----------------------
1. Levene Test
   Statistik: {stat_l:.4f}
   P-value: {p_l:.6f}
   Kesimpulan: {'Homogen' if p_l > 0.05 else 'Tidak Homogen'}

2. Bartlett Test
   Statistik: {stat_b:.4f}
   P-value: {p_b:.6f}
   Kesimpulan: {'Homogen' if p_b > 0.05 else 'Tidak Homogen'}

3. Fligner-Killeen Test
   Statistik: {stat_f:.4f}
   P-value: {p_f:.6f}
   Kesimpulan: {'Homogen' if p_f > 0.05 else 'Tidak Homogen'}

STATISTIK DESKRIPTIF
---------------------
{stats_detail_df.to_string()}

KESIMPULAN AKHIR
----------------
{'Data memiliki varians yang homogen.' if homogen_count >= 2 else 'Data memiliki varians yang tidak homogen.'}
Rekomendasi: {'Gunakan uji parametrik (ANOVA, t-test)' if homogen_count >= 2 else 'Gunakan uji non-parametrik atau Welch ANOVA'}
"""
            
                st.download_button(
                    label="📄 Download Laporan (TXT)",
                    data=report,
                    file_name="laporan_homogenitas.txt",
                    mime="text/plain",
                    use_container_width=True
                )

    # TAB 6: STUDI KASUS
    with tab6:
        st.header("💡 Studi Kasus Praktis")
    
        st.markdown("""
    Berikut adalah beberapa contoh kasus nyata penggunaan uji homogenitas 
    dalam berbagai bidang penelitian.
    """)
    
        case_study = st.selectbox(
        "Pilih Studi Kasus",
        ["Kasus 1: Perbandingan Nilai Ujian", 
         "Kasus 2: Efektivitas Obat",
         "Kasus 3: Produktivitas Karyawan",
         "Kasus 4: Kualitas Produk"]
        )
    
        if case_study == "Kasus 1: Perbandingan Nilai Ujian":
            st.subheader("📚 Studi Kasus: Perbandingan Nilai Ujian Tiga Kelas")
        
            st.markdown("""
        **Latar Belakang:**  
        Seorang guru ingin membandingkan nilai ujian matematika dari 3 kelas yang berbeda 
        untuk mengetahui apakah ada perbedaan rata-rata nilai. Sebelum melakukan ANOVA, 
        guru perlu memastikan varians nilai ketiga kelas homogen.
        """)
        
            # Data
            np.random.seed(42)
            kelas_a = np.random.normal(75, 8, 30)
            kelas_b = np.random.normal(78, 9, 30)
            kelas_c = np.random.normal(73, 7, 30)
        
            df_case1 = pd.DataFrame({
            'Kelas': ['Kelas A']*30 + ['Kelas B']*30 + ['Kelas C']*30,
            'Nilai': np.concatenate([kelas_a, kelas_b, kelas_c])
            })
        
            col1, col2 = st.columns([2, 1])
        
            with col1:
                # Visualisasi
                fig = px.box(df_case1, x='Kelas', y='Nilai', color='Kelas',
                            title='Distribusi Nilai per Kelas')
                st.plotly_chart(fig, use_container_width=True)
        
            with col2:
                # Statistik
                st.markdown("**Statistik Deskriptif:**")
                stats_case1 = df_case1.groupby('Kelas')['Nilai'].agg([
                ('Mean', 'mean'),
                ('Std', 'std'),
                ('Var', 'var')
                ]).round(2)
                st.dataframe(stats_case1)
        
            # Uji Homogenitas
            stat_lev, p_lev = stats.levene(kelas_a, kelas_b, kelas_c)
        
            st.markdown(f"""
        **Hasil Uji Levene:**
        - Statistik: {stat_lev:.4f}
        - P-value: {p_lev:.4f}
        
        **Interpretasi:**  
        Dengan p-value = {p_lev:.4f} {'>' if p_lev > 0.05 else '<'} 0.05, 
        maka varians ketiga kelas {'homogen' if p_lev > 0.05 else 'tidak homogen'}.
        
        **Kesimpulan:**  
        Guru {'dapat' if p_lev > 0.05 else 'tidak dapat'} melanjutkan dengan One-Way ANOVA 
        {'untuk membandingkan rata-rata nilai ketiga kelas' if p_lev > 0.05 else 'dan sebaiknya menggunakan Welch ANOVA atau Kruskal-Wallis Test'}.
        """)
    
        elif case_study == "Kasus 2: Efektivitas Obat":
            st.subheader("💊 Studi Kasus: Uji Klinis Efektivitas Obat")
        
            st.markdown("""
        **Latar Belakang:**  
        Peneliti ingin menguji efektivitas 3 jenis obat penurun tekanan darah. 
        Data penurunan tekanan darah (mmHg) dikumpulkan dari masing-masing kelompok pasien.
        """)
        
            # Data dengan varians tidak sama (realistis untuk data medis)
            np.random.seed(123)
            obat_a = np.random.normal(15, 3, 25)  # Penurunan rata-rata 15 mmHg
            obat_b = np.random.normal(18, 5, 25)  # Penurunan rata-rata 18 mmHg
            obat_c = np.random.normal(12, 8, 25)  # Penurunan rata-rata 12 mmHg
        
            df_case2 = pd.DataFrame({
            'Obat': ['Obat A']*25 + ['Obat B']*25 + ['Obat C']*25,
            'Penurunan_TD': np.concatenate([obat_a, obat_b, obat_c])
            })
        
            col1, col2 = st.columns(2)
        
            with col1:
                fig1 = px.violin(df_case2, x='Obat', y='Penurunan_TD', color='Obat',
                                box=True, title='Distribusi Penurunan Tekanan Darah')
                st.plotly_chart(fig1, use_container_width=True)
        
            with col2:
                fig2 = px.box(df_case2, x='Obat', y='Penurunan_TD', color='Obat',
                             title='Box Plot Penurunan TD')
                st.plotly_chart(fig2, use_container_width=True)
        
            # Stats
            stats_case2 = df_case2.groupby('Obat')['Penurunan_TD'].agg([
            ('N', 'count'),
            ('Mean', 'mean'),
            ('Std Dev', 'std'),
            ('Variance', 'var')
            ]).round(2)
            st.dataframe(stats_case2, use_container_width=True)
        
            # Uji
            stat_lev2, p_lev2 = stats.levene(obat_a, obat_b, obat_c)
        
            if p_lev2 > 0.05:
                st.markdown(f"""
            <div class="success-box">
            <h4>✅ Hasil Uji Levene</h4>
            <p><strong>Statistik:</strong> {stat_lev2:.4f}</p>
            <p><strong>P-value:</strong> {p_lev2:.4f}</p>
            <p><strong>Kesimpulan:</strong> Varians homogen, lanjutkan dengan ANOVA</p>
            </div>
            """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
            <div class="warning-box">
            <h4>⚠️ Hasil Uji Levene</h4>
            <p><strong>Statistik:</strong> {stat_lev2:.4f}</p>
            <p><strong>P-value:</strong> {p_lev2:.4f}</p>
            <p><strong>Kesimpulan:</strong> Varians tidak homogen</p>
            <p><strong>Rekomendasi:</strong> Gunakan Welch's ANOVA atau transformasi data</p>
            </div>
            """, unsafe_allow_html=True)
        
            st.markdown("""
        **Implikasi Klinis:**  
        Perbedaan varians menunjukkan bahwa respon pasien terhadap obat berbeda-beda. 
        Obat dengan varians tinggi menunjukkan efek yang tidak konsisten antar pasien.
        """)
    
        elif case_study == "Kasus 3: Produktivitas Karyawan":
            st.subheader("👔 Studi Kasus: Produktivitas Karyawan per Divisi")
        
            st.markdown("""
        **Latar Belakang:**  
        Manajer HR ingin membandingkan produktivitas (unit produksi per hari) 
        karyawan di 4 divisi berbeda.
        """)
        
            np.random.seed(456)
            divisi_1 = np.random.normal(45, 6, 20)
            divisi_2 = np.random.normal(48, 6.5, 20)
            divisi_3 = np.random.normal(42, 5.8, 20)
            divisi_4 = np.random.normal(50, 6.2, 20)
        
            df_case3 = pd.DataFrame({
            'Divisi': ['Divisi 1']*20 + ['Divisi 2']*20 + ['Divisi 3']*20 + ['Divisi 4']*20,
            'Produktivitas': np.concatenate([divisi_1, divisi_2, divisi_3, divisi_4])
            })
        
            # Visualisasi modern
            fig3 = px.strip(df_case3, x='Divisi', y='Produktivitas', color='Divisi',
                           title='Produktivitas Karyawan per Divisi')
            fig3.update_traces(marker=dict(size=10, opacity=0.6))
            st.plotly_chart(fig3, use_container_width=True)
        
            # Test
            stat_lev3, p_lev3 = stats.levene(divisi_1, divisi_2, divisi_3, divisi_4)
        
            col1, col2 = st.columns(2)
        
            with col1:
                st.metric("Statistik Uji Levene", f"{stat_lev3:.4f}")
                st.metric("P-value", f"{p_lev3:.4f}")
        
            with col2:
                if p_lev3 > 0.05:
                    st.success("✅ Varians Homogen")
                    st.info("Dapat menggunakan ANOVA untuk analisis lanjutan")
                else:
                    st.error("❌ Varians Tidak Homogen")
                    st.warning("Gunakan Welch's ANOVA")
    
        else:  # Kasus 4
            st.subheader("🏭 Studi Kasus: Kontrol Kualitas Produk")
        
            st.markdown("""
        **Latar Belakang:**  
        Quality Control Engineer ingin memastikan konsistensi dimensi produk 
        dari 3 mesin produksi yang berbeda.
            """)
        
            np.random.seed(789)
            # Mesin 3 sengaja dibuat dengan variasi tinggi (masalah kualitas)
            mesin_1 = np.random.normal(10.0, 0.1, 40)  # Presisi tinggi
            mesin_2 = np.random.normal(10.0, 0.12, 40)  # Presisi sedang
            mesin_3 = np.random.normal(10.0, 0.5, 40)  # Presisi rendah (bermasalah)
        
            df_case4 = pd.DataFrame({
            'Mesin': ['Mesin 1']*40 + ['Mesin 2']*40 + ['Mesin 3']*40,
            'Dimensi_mm': np.concatenate([mesin_1, mesin_2, mesin_3])
            })
        
            # Visualisasi detail
            fig4 = make_subplots(
                rows=1, cols=2,
                subplot_titles=('Box Plot', 'Histogram Overlay')
            )
        
            colors_case4 = ['#667eea', '#764ba2', '#f093fb']
        
            for i, mesin in enumerate(['Mesin 1', 'Mesin 2', 'Mesin 3']):
                data_mesin = df_case4[df_case4['Mesin'] == mesin]['Dimensi_mm']
            
                fig4.add_trace(
                    go.Box(y=data_mesin, name=mesin, marker_color=colors_case4[i]),
                    row=1, col=1
                )
            
                fig4.add_trace(
                    go.Histogram(x=data_mesin, name=mesin, marker_color=colors_case4[i],
                            opacity=0.6, nbinsx=20),
                    row=1, col=2
                )
        
            fig4.update_layout(height=400, barmode='overlay')
            st.plotly_chart(fig4, use_container_width=True)
        
            # Stats detail
            stats_case4 = df_case4.groupby('Mesin')['Dimensi_mm'].agg([
            ('N', 'count'),
            ('Mean', 'mean'),
            ('Std Dev', 'std'),
            ('CV (%)', lambda x: (x.std() / x.mean()) * 100),
            ('Range', lambda x: x.max() - x.min())
            ]).round(4)
        
            st.dataframe(stats_case4, use_container_width=True)
        
            # Uji homogenitas
            stat_lev4, p_lev4 = stats.levene(mesin_1, mesin_2, mesin_3)
            stat_bart4, p_bart4 = stats.bartlett(mesin_1, mesin_2, mesin_3)
        
            st.markdown("---")
            st.subheader("🔬 Hasil Uji Homogenitas")
        
            results_case4 = pd.DataFrame({
            'Metode': ['Levene Test', 'Bartlett Test'],
            'Statistik': [f'{stat_lev4:.4f}', f'{stat_bart4:.4f}'],
            'P-value': [f'{p_lev4:.6f}', f'{p_bart4:.6f}'],
            'Kesimpulan': [
                'Homogen ✅' if p_lev4 > 0.05 else 'Tidak Homogen ❌',
                'Homogen ✅' if p_bart4 > 0.05 else 'Tidak Homogen ❌'
                ]
            })
        
            st.dataframe(results_case4, use_container_width=True)
        
            if p_lev4 <= 0.05:
                st.markdown("""
            <div class="warning-box">
            <h4>⚠️ Interpretasi Kualitas Produksi</h4>
            <p><strong>Temuan:</strong> Varians dimensi produk dari ketiga mesin TIDAK homogen.</p>
            
            <p><strong>Implikasi:</strong></p>
            <ul>
                <li>🔧 <strong>Mesin 3</strong> memiliki varians sangat tinggi → Perlu kalibrasi atau maintenance</li>
                <li>📊 Konsistensi produksi tidak terjaga</li>
                <li>⚠️ Risiko produk reject/defect tinggi</li>
                <li>🎯 Standar deviasi Mesin 3 5x lebih besar dari Mesin 1</li>
            </ul>
            
            <p><strong>Rekomendasi:</strong></p>
            <ul>
                <li>✅ Lakukan maintenance mendalam pada Mesin 3</li>
                <li>✅ Implementasi Statistical Process Control (SPC)</li>
                <li>✅ Training operator untuk Mesin 3</li>
                <li>✅ Pertimbangkan penggantian komponen Mesin 3</li>
            </ul>
            </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown("""
            <div class="success-box">
            <h4>✅ Interpretasi Kualitas Produksi</h4>
            <p><strong>Temuan:</strong> Varians dimensi produk dari ketiga mesin homogen.</p>
            <p><strong>Kesimpulan:</strong> Semua mesin menghasilkan produk dengan konsistensi yang sebanding.</p>
            <p><strong>Status:</strong> Proses produksi terkendali dengan baik.</p>
            </div>
                """, unsafe_allow_html=True)
        
            # Coefficient of Variation comparison
            st.markdown("---")
            st.subheader("📊 Perbandingan Koefisien Variasi (CV)")
        
            cv_data = stats_case4['CV (%)'].values
            mesin_names = stats_case4.index.tolist()
        
            fig_cv = go.Figure(data=[
                go.Bar(x=mesin_names, y=cv_data,
                       marker_color=colors_case4,
                       text=[f'{cv:.2f}%' for cv in cv_data],
                      textposition='auto')
            ])
        
            fig_cv.update_layout(
                title='Koefisien Variasi per Mesin (Semakin rendah, semakin baik)',
                xaxis_title='Mesin',
                yaxis_title='CV (%)',
                height=400
            )
        
            st.plotly_chart(fig_cv, use_container_width=True)
        
            st.markdown("""
        **Interpretasi CV:**
        - **CV < 10%:** Variasi rendah, presisi sangat baik ✅
        - **CV 10-20%:** Variasi sedang, presisi cukup baik 🟡
        - **CV > 20%:** Variasi tinggi, presisi buruk ❌
            """)

    # SIDEBAR
    with st.sidebar:
        st.image("https://via.placeholder.com/300x150/667eea/ffffff?text=Uji+Homogenitas", use_container_width=True)
    
        st.markdown("---")
    
        st.subheader("📚 Tentang Aplikasi")
        st.markdown("""
        Aplikasi ini dibuat untuk membantu memahami dan melakukan uji homogenitas varians 
        dalam analisis statistik.
    
        **Fitur:**
        - 📖 Materi teori lengkap
        - 🧪 Simulasi data interaktif
        - 📂 Upload data sendiri
        - 📊 Visualisasi komprehensif
        - 💡 Studi kasus nyata
        """)
    
        st.markdown("---")
    
        st.subheader("🎯 Quick Guide")
        st.markdown("""
        **Langkah-langkah:**
    
    1. **Pelajari Teori** di Tab "📚 Teori"
    2. **Pahami Metode** di Tab "🎯 Metode Uji"
    3. **Coba Simulasi** di Tab "🧪 Simulasi Data"
    4. **Upload Data** Anda di Tab "📂 Upload Data"
    5. **Analisis Mendalam** di Tab "📈 Analisis Lanjutan"
    6. **Lihat Contoh** di Tab "💡 Studi Kasus"
    """)
    
        st.markdown("---")
    
        st.subheader("🔑 Aturan Keputusan")
        st.markdown("""
    **p-value > 0.05:**
    - ✅ Gagal tolak H₀
    - Data HOMOGEN
    - Gunakan uji parametrik
    
    **p-value ≤ 0.05:**
    - ❌ Tolak H₀
    - Data TIDAK HOMOGEN
    - Gunakan uji non-parametrik
    """)
    
        st.markdown("---")
    
        st.subheader("📖 Referensi")
        st.markdown("""
    - Levene, H. (1960). Robust tests for equality of variances
    - Bartlett, M. S. (1937). Properties of sufficiency and statistical tests
    - Fligner, M. A., & Killeen, T. J. (1976). Distribution-free two-sample tests
    """)
    
        st.markdown("---")
    
        st.info("""
    💡 **Tips:**
    
    Selalu lakukan uji normalitas sebelum memilih metode uji homogenitas!
    """)
    
        st.markdown("---")
    
        # Footer
        st.markdown("""
    <div style='text-align: center; padding: 20px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
    border-radius: 10px; color: white;'>
        <p><strong>Uji Homogenitas Data</strong></p>
        <p style='font-size: 0.8em;'>Dibuat dengan ❤️ menggunakan Streamlit</p>
        <p style='font-size: 0.7em;'>© 2025 - Statistical Analysis Tools</p>
    </div>
    """, unsafe_allow_html=True)

    # Footer di bagian bawah halaman utama
    st.markdown("---")
    st.markdown("""
<div style='text-align: center; padding: 20px;'>
    <h4>🎓 Tips Penggunaan Uji Homogenitas</h4>
    <p>
    1. Pastikan data Anda sudah bersih dari outlier ekstrem<br>
    2. Cek normalitas data sebelum memilih metode uji<br>
    3. Gunakan Levene Test sebagai pilihan utama untuk data non-normal<br>
    4. Bartlett Test hanya untuk data yang benar-benar normal<br>
    5. Interpretasikan hasil dengan konteks penelitian Anda
    </p>
</div>
""", unsafe_allow_html=True)

    st.markdown("---")

    # Informasi tambahan
    col_info1, col_info2, col_info3 = st.columns(3)

    with col_info1:
        st.markdown("""
    <div style='background: #d1ecf1; padding: 20px; border-radius: 10px; text-align: center;color:black'>
        <h3 style='color: #0c5460;'>📊</h3>
        <h4>Data Homogen</h4>
        <p>Varians sama antar kelompok → Gunakan ANOVA</p>
    </div>
    """, unsafe_allow_html=True)

    with col_info2:
        st.markdown("""
    <div style='background: #fff3cd; padding: 20px; border-radius: 10px; text-align: center;color:black'>
        <h3 style='color: #856404;'>⚠️</h3>
        <h4>Data Tidak Homogen</h4>
        <p>Varians berbeda → Gunakan Welch's ANOVA</p>
    </div>
    """, unsafe_allow_html=True)

    with col_info3:
        st.markdown("""
    <div style='background: #d4edda; padding: 20px; border-radius: 10px; text-align: center; color:black'>
        <h3 style='color: #155724;'>✅</h3>
        <h4>Alternative</h4>
        <p>Transformasi data atau uji non-parametrik</p>
    </div>
        """, unsafe_allow_html=True)

def tampilkan_materi10():
    st.title("📊 Aplikasi Uji Homogenitas Sampel")
    st.write("Bandingkan kesamaan variansi beberapa kelompok data dengan berbagai metode: Bartlett, Levene, Hartley (F-max), dan Cochran C.")

    # --- Input Data ---
    st.sidebar.header("🔧 Pengaturan Data")

    n = st.sidebar.number_input("Jumlah sampel per kelompok", 5, 200, 30)
    mean1 = st.sidebar.slider("Rata-rata Kelompok 1", 30, 80, 55)
    mean2 = st.sidebar.slider("Rata-rata Kelompok 2", 30, 80, 57)
    mean3 = st.sidebar.slider("Rata-rata Kelompok 3", 30, 80, 60)
    std = st.sidebar.slider("Standar Deviasi", 1, 20, 8)

    # --- Generate Data ---
    np.random.seed(42)
    group1 = np.random.normal(mean1, std, n)
    group2 = np.random.normal(mean2, std, n)
    group3 = np.random.normal(mean3, std, n)

    data = pd.DataFrame({
    "Kelompok 1": group1,
    "Kelompok 2": group2,
    "Kelompok 3": group3
    })

    st.subheader("📋 Data Sampel")
    st.dataframe(data)

    # --- Uji Bartlett ---
    bartlett_stat, bartlett_p = stats.bartlett(group1, group2, group3)

    # --- Uji Levene (mean) ---
    levene_stat, levene_p = stats.levene(group1, group2, group3, center='mean')

    # --- Uji Levene (median) ---
    levene_median_stat, levene_median_p = stats.levene(group1, group2, group3, center='median')

    # --- Uji Hartley (F-max) ---
    variances = [np.var(g, ddof=1) for g in [group1, group2, group3]]
    hartley_fmax = max(variances) / min(variances)

    # --- Uji Cochran C ---
    cochran_c = max(variances) / sum(variances)

    # --- Hasil ---
    st.subheader("📈 Hasil Uji Homogenitas")
    st.write("Semua hasil dibandingkan dengan α = 0.05")

    hasil_df = pd.DataFrame({
    "Uji": ["Bartlett", "Levene (mean)", "Levene (median)", "Hartley (F-max)", "Cochran C"],
    "Statistik": [bartlett_stat, levene_stat, levene_median_stat, hartley_fmax, cochran_c],
    "p-value": [bartlett_p, levene_p, levene_median_p, "-", "-"],
    "Kesimpulan": [
        "Homogen" if bartlett_p > 0.05 else "Tidak Homogen",
        "Homogen" if levene_p > 0.05 else "Tidak Homogen",
        "Homogen" if levene_median_p > 0.05 else "Tidak Homogen",
        "—", "—"
        ]
    })

    st.dataframe(hasil_df, use_container_width=True)

    # --- Visualisasi ---
    st.subheader("📊 Visualisasi Distribusi")
    st.bar_chart(data)

    # --- Kesimpulan umum ---
    if levene_p > 0.05 and bartlett_p > 0.05:
        st.success("✅ Variansi antar kelompok **homogen** (tidak berbeda signifikan).")
    else:
        st.warning("⚠️ Variansi antar kelompok **tidak homogen** (berbeda signifikan).")

    st.caption("Metode Bartlett sensitif terhadap data tidak normal, sedangkan Levene lebih robust untuk data non-normal.")
    st.sidebar.markdown("---")

def tampilkan_materi11():
    st.markdown('''
    <iframe src="https://martin-bernard26.github.io/statistika/dataHomogen.html" style="width:100%; height:2000px"></iframe>
    ''',unsafe_allow_html=True)
def tampilkan_materi12():
    st.title("📊 Uji Homogenitas Varians (Uji F)")
    st.write("""
Aplikasi ini digunakan untuk menguji apakah dua kelompok data memiliki varians yang **homogen** atau tidak.  
Metode: **Uji F** dengan hipotesis:
- H₀ : σ₁² = σ₂² (varians sama / homogen) (p-value > 0.05)
- H₁ : σ₁² ≠ σ₂² (varians berbeda / tidak homogen) (p-value <= 0.05)
    """)

    st.divider()

    # Input data
    st.subheader("Masukkan Data")
    data1 = st.text_area("Data Kelompok 1 (pisahkan dengan koma)", "12, 15, 14, 10, 13, 12, 11")
    data2 = st.text_area("Data Kelompok 2 (pisahkan dengan koma)", "9, 10, 11, 8, 12, 9, 10")

    if st.button("🔍 Lakukan Uji F"):
        try:
            # Ubah ke array numpy
            x1 = np.array([float(i) for i in data1.split(",")])
            x2 = np.array([float(i) for i in data2.split(",")])

            # Hitung varians
            var1 = np.var(x1, ddof=1)
            var2 = np.var(x2, ddof=1)

            # Tentukan F hitung
            if var1 > var2:
                F_hitung = var1 / var2
                df1, df2 = len(x1) - 1, len(x2) - 1
            else:
                F_hitung = var2 / var1
                df1, df2 = len(x2) - 1, len(x1) - 1

            # Nilai kritis F
            alpha = 0.05
            F_tabel_atas = f.ppf(1 - alpha/2, df1, df2)
            F_tabel_bawah = f.ppf(alpha/2, df1, df2)
            p_value = 2 * min(f.cdf(F_hitung, df1, df2), 1 - f.cdf(F_hitung, df1, df2))
            p_kanan = 1 - f.cdf(F_hitung, df1, df2)
            p_kiri = f.cdf(F_hitung, df1, df2)

            # Keputusan
            if F_hitung < F_tabel_atas and F_hitung > F_tabel_bawah:
                keputusan = "✅ Terima H₀ (Varians homogen)"
            else:
                keputusan = "❌ Tolak H₀ (Varians tidak homogen)"

            # Hasil
            st.subheader("📈 Hasil Uji F")
            hasil_df = pd.DataFrame({
                "Statistik": ["Varians 1", "Varians 2", "F hitung", "F kritis bawah", "F kritis atas","p-value dua sisi", "p-value sisi kanan","p-value sisi kiri"],
                "Nilai": [var1, var2, F_hitung, F_tabel_bawah, F_tabel_atas,p_value,p_kanan,p_kiri]
            })
            st.dataframe(hasil_df, use_container_width=True)

            st.success(keputusan)

            # Interpretasi
            st.info(f"""
        **Interpretasi:**
        - Nilai F hitung = {F_hitung:.4f}
        - Nilai F tabel bawah = {F_tabel_bawah:.4f}
        - Nilai F tabel atas = {F_tabel_atas:.4f}
        - Derajat kebebasan (df1, df2) = ({df1}, {df2})
        - Keputusan: {keputusan}
            """)

        except Exception as e:
            st.error(f"Terjadi kesalahan dalam input data: {e}")

def tampilkan_materi13():
    # --- Judul ---
    st.title("📊 Uji t 1 Sampel (Parametrik)")
    st.write("""
    Uji ini digunakan untuk menentukan apakah rata-rata satu kelompok data
    **berbeda secara signifikan** dari nilai pembanding tertentu (μ₀).

    **Hipotesis:**
    - H₀ : μ = μ₀  
    - H₁ : μ ≠ μ₀
    """)

    st.divider()

    # --- Input Data ---
    st.subheader("📥 Masukkan Data")

    option = st.radio("Pilih cara input data:", ["Ketik manual", "Upload CSV"])

    if option == "Ketik manual":
        data_text = st.text_area("Masukkan data (pisahkan dengan koma)", "12, 15, 14, 10, 13, 12, 11")
        data = np.array([float(i) for i in data_text.split(",")])
    else:
        uploaded = st.file_uploader("Upload file CSV dengan satu kolom data", type=["csv"])
        if uploaded is not None:
            df = pd.read_csv(uploaded)
            st.dataframe(df)
            col = st.selectbox("Pilih kolom data", df.columns)
            data = df[col].dropna().values
        else:
            st.warning("Silakan upload file CSV terlebih dahulu.")
            st.stop()

    # --- Input Parameter Uji ---
    mu0 = st.number_input("Masukkan nilai pembanding (μ₀)", value=10.0, step=0.1)
    alpha = st.slider("Tingkat signifikansi (α)", 0.01, 0.10, 0.05, step=0.01)
    arah = st.radio("Pilih arah uji:", ["Dua sisi", "Satu sisi (kanan)", "Satu sisi (kiri)"])

    # --- Tombol Eksekusi ---
    if st.button("🔍 Jalankan Uji t 1 Sampel"):
        try:
            n = len(data)
            mean_x = np.mean(data)
            std_x = np.std(data, ddof=1)
            se = std_x / np.sqrt(n)
            t_hitung = (mean_x - mu0) / se
            df = n - 1

            # --- P-value berdasarkan arah uji ---
            if arah == "Dua sisi":
                p_value = 2 * (1 - t.cdf(abs(t_hitung), df))
            elif arah == "Satu sisi (kanan)":
                p_value = 1 - t.cdf(t_hitung, df)
            else:
                p_value = t.cdf(t_hitung, df)

            # --- Nilai t kritis ---
            if arah == "Dua sisi":
                t_kritis = t.ppf(1 - alpha/2, df)
            else:
                t_kritis = t.ppf(1 - alpha, df)

            # --- Keputusan ---
            if p_value > alpha:
                keputusan = "✅ Terima H₀ (tidak ada perbedaan signifikan)"
            else:
                keputusan = "❌ Tolak H₀ (ada perbedaan signifikan)"

            # --- Hasil Tabel ---
            st.subheader("📈 Hasil Uji t")
            hasil_df = pd.DataFrame({
                "Statistik": ["Jumlah Sampel", "Rata-rata (x̄)", "Simpangan Baku (s)", "t hitung", "Derajat bebas (df)", "p-value"],
                "Nilai": [n, mean_x, std_x, t_hitung, df, p_value]
            })
            st.dataframe(hasil_df, use_container_width=True)

            # --- Hasil dan Interpretasi ---
            st.success(keputusan)
            st.info(f"""
        **Interpretasi:**
        - Nilai t hitung = {t_hitung:.4f}
        - Derajat bebas = {df}
        - p-value = {p_value:.4f}
        - α = {alpha}
        - Keputusan: {keputusan}
            """)

            # --- Visualisasi Distribusi t ---
            st.subheader("📊 Distribusi t dan Posisi t hitung")
            x = np.linspace(-4, 4, 400)
            y = t.pdf(x, df)
            fig, ax = plt.subplots()
            ax.plot(x, y, label='Distribusi t')
            ax.axvline(t_hitung, color='r', linestyle='--', label=f't hitung = {t_hitung:.2f}')
            if arah == "Dua sisi":
                ax.axvline(t_kritis, color='g', linestyle='--', label=f'±t kritis = {t_kritis:.2f}')
                ax.axvline(-t_kritis, color='g', linestyle='--')
            else:
                ax.axvline(t_kritis, color='g', linestyle='--', label=f't kritis = {t_kritis:.2f}')
            ax.legend()
            st.pyplot(fig)

        except Exception as e:
            st.error(f"Terjadi kesalahan: {e}")

def tampilkan_materi14():
    pass
    # --- Judul dan deskripsi ---
    st.title("📊 Uji Wilcoxon Signed-Rank 1 Sampel (Non-Parametrik)")
    st.write("""
Uji ini digunakan untuk menguji apakah **median sampel berbeda secara signifikan**
dari nilai pembanding tertentu (M₀).

**Catatan:**
- Uji ini digunakan **jika data tidak berdistribusi normal.**
- Padanan non-parametrik dari **Uji t 1 Sampel.**

**Hipotesis:**
- H₀ : median = M₀  
- H₁ : median ≠ M₀
    """)

    st.divider()

    # --- Input Data ---
    st.subheader("📥 Masukkan Data")

    option = st.radio("Pilih cara input data:", ["Ketik manual", "Upload CSV"])

    if option == "Ketik manual":
        data_text = st.text_area("Masukkan data (pisahkan dengan koma)", "12, 15, 14, 10, 13, 12, 11")
        data = np.array([float(i) for i in data_text.split(",")])
    else:
        uploaded = st.file_uploader("Upload file CSV dengan satu kolom data", type=["csv"])
        if uploaded is not None:
            df = pd.read_csv(uploaded)
            st.dataframe(df)
            col = st.selectbox("Pilih kolom data", df.columns)
            data = df[col].dropna().values
        else:
            st.warning("Silakan upload file CSV terlebih dahulu.")
            st.stop()

    # --- Input Parameter Uji ---
    M0 = st.number_input("Masukkan nilai median pembanding (M₀)", value=10.0, step=0.1)
    alpha = st.slider("Tingkat signifikansi (α)", 0.01, 0.10, 0.05, step=0.01)
    arah = st.radio("Pilih arah uji:", ["Dua sisi", "Satu sisi (kanan)", "Satu sisi (kiri)"])

    # --- Tombol Eksekusi ---
    if st.button("🔍 Jalankan Uji Wilcoxon 1 Sampel"):
        try:
            # Hitung selisih
            diff = data - M0

            # Jalankan uji Wilcoxon
            if arah == "Dua sisi":
                stat, p_value = wilcoxon(diff, alternative='two-sided')
            elif arah == "Satu sisi (kanan)":
                stat, p_value = wilcoxon(diff, alternative='greater')
            else:
                stat, p_value = wilcoxon(diff, alternative='less')

            # --- Hasil dan Keputusan ---
            if p_value > alpha:
                keputusan = "✅ Terima H₀ (tidak ada perbedaan signifikan)"
            else:
                keputusan = "❌ Tolak H₀ (ada perbedaan signifikan)"

            # --- Hasil Tabel ---
            st.subheader("📈 Hasil Uji Wilcoxon 1 Sampel")
            hasil_df = pd.DataFrame({
                "Statistik": ["Jumlah Sampel (n)", "Statistik Wilcoxon (W)", "p-value"],
                "Nilai": [len(data), stat, p_value]
            })
            st.dataframe(hasil_df, use_container_width=True)

            # --- Interpretasi ---
            st.success(keputusan)
            st.info(f"""
        **Interpretasi:**
        - Nilai W = {stat:.4f}
        - p-value = {p_value:.4f}
        - α = {alpha}
        - Keputusan: {keputusan}
        """)

            # --- Visualisasi ---
            st.subheader("📊 Visualisasi Selisih terhadap Median Pembanding (M₀)")
            fig, ax = plt.subplots()
            ax.axhline(0, color='gray', linestyle='--')
            ax.bar(range(1, len(diff)+1), diff, color=['red' if d < 0 else 'blue' for d in diff])
            ax.set_xlabel("Data ke-")
            ax.set_ylabel("Selisih (X - M₀)")
            ax.set_title("Visualisasi Selisih Data terhadap Median Pembanding")
            st.pyplot(fig)

        except Exception as e:
            st.error(f"Terjadi kesalahan: {e}")

def tampilkan_materi15():
    st.title("🧩 Evaluasi Instrumen Tes Esai")
    st.write("""
Aplikasi ini menghitung:

1️⃣ **Validitas butir soal**  
2️⃣ **Reliabilitas (Cronbach's Alpha)**  
3️⃣ **Daya pembeda**  
4️⃣ **Indeks kesukaran**

### 📘 Petunjuk:
- Upload file **CSV** berisi skor siswa untuk tiap butir soal (kolom soal_1, soal_2, dst).  
- Baris = responden, kolom = skor tiap soal.  
- Skor tiap butir dapat **bervariasi (misal 0–5 atau 0–10)**.
""")

    # --- Upload data ---
    uploaded_file = st.file_uploader("📥 Upload data skor siswa (CSV)", type=["csv"])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.subheader("📄 Data Skor Siswa")
        st.dataframe(df.head(), use_container_width=True)
    
        # --- Hitung total skor ---
        df["Total"] = df.sum(axis=1)
    
        # --- Validitas butir ---
        st.subheader("✅ Validitas Butir Soal (Korelasi Pearson)")
        validitas = []
        for col in df.columns[:-1]:  # semua kolom kecuali total
            r, p = pearsonr(df[col], df["Total"])
            validitas.append({"Soal": col, "r_hitung": r, "p_value": p})
        validitas_df = pd.DataFrame(validitas)
        validitas_df["Kategori"] = pd.cut(validitas_df["r_hitung"],
                                      bins=[-1, 0.2, 0.4, 0.6, 0.8, 1],
                                      labels=["Sangat Rendah", "Rendah", "Cukup", "Tinggi", "Sangat Tinggi"])
        st.dataframe(validitas_df, use_container_width=True)
    
        # --- Reliabilitas (Cronbach's Alpha) ---
        st.subheader("🔁 Reliabilitas (Cronbach's Alpha)")
        items = df.drop(columns=["Total"])
        var_items = items.var(axis=0, ddof=1)
        var_total = df["Total"].var(ddof=1)
        k = items.shape[1]
        cronbach_alpha = (k / (k - 1)) * (1 - (var_items.sum() / var_total))
        st.metric("Cronbach’s Alpha", f"{cronbach_alpha:.4f}")
        st.info("""
    Interpretasi Umum:
    - α ≥ 0.9 : Sangat tinggi  
    - 0.8–0.9 : Tinggi  
    - 0.7–0.8 : Cukup  
    - 0.6–0.7 : Rendah  
    - < 0.6 : Tidak reliabel
    """)
    
        # --- Daya Pembeda ---
        st.subheader("⚖️ Daya Pembeda")
        n = len(df)
        df_sorted = df.sort_values("Total", ascending=False)
        group_size = n // 2
        upper = df_sorted.head(group_size)
        lower = df_sorted.tail(group_size)
    
        daya_pembeda = []
        for col in df.columns[:-1]:
            mean_upper = upper[col].mean()
            mean_lower = lower[col].mean()
            D = (mean_upper - mean_lower) / df[col].max()  # dinormalisasi ke skor maksimum
            daya_pembeda.append({"Soal": col, "Daya Pembeda": D})
        daya_df = pd.DataFrame(daya_pembeda)
        daya_df["Kategori"] = pd.cut(daya_df["Daya Pembeda"],
                                 bins=[-1, 0.2, 0.4, 0.6, 0.8, 1],
                                 labels=["Buruk", "Cukup", "Baik", "Baik Sekali", "Sangat Baik"])
        st.dataframe(daya_df, use_container_width=True)
    
        # --- Indeks Kesukaran ---
        st.subheader("🎯 Indeks Kesukaran")
        indeks = []
        skor_maks = df.drop(columns=["Total"]).max().max()
        for col in df.columns[:-1]:
            P = df[col].mean() / skor_maks
            indeks.append({"Soal": col, "Indeks Kesukaran": P})
        indeks_df = pd.DataFrame(indeks)
        indeks_df["Kategori"] = pd.cut(indeks_df["Indeks Kesukaran"],
                                   bins=[0, 0.3, 0.7, 1],
                                   labels=["Sukar", "Sedang", "Mudah"])
        st.dataframe(indeks_df, use_container_width=True)
    
        # --- Rekapitulasi Akhir ---
        st.subheader("📊 Rekapitulasi Evaluasi Soal")
        rekap = validitas_df.merge(daya_df, on="Soal").merge(indeks_df, on="Soal")
        st.dataframe(rekap, use_container_width=True)
    
        st.success("✅ Analisis selesai! Gunakan hasil ini untuk revisi dan penyempurnaan butir soal.")

    else:
        st.info("Silakan upload file CSV terlebih dahulu.")

def tampilkan_materi16():
    halaman = st.tabs(['Alur Uji 1 Sampel','Alur Uji 2 Sampel Berpasangan','Alur Uji 2 Sampel Independen', 'Alur Uji > 2 Sampel Independen'])
    with halaman[0]:
        st.markdown('''
        <iframe src="https://martin-bernard26.github.io/statistika/alur1.html" style="width:100%; height:3700px"></iframe>
        ''',unsafe_allow_html=True)
    with halaman[1]:
        st.markdown('''
        <iframe src="https://martin-bernard26.github.io/statistika/uji2pasang.html" style="width:100%; height:3700px"></iframe>
        ''',unsafe_allow_html=True)
    with halaman[2]:
        st.markdown('''
        <iframe src="https://martin-bernard26.github.io/statistika/alur2.html" style="width:100%; height:1000px"></iframe>
        ''',unsafe_allow_html=True)
    with halaman[3]:
        st.markdown('''
        <iframe src="https://martin-bernard26.github.io/statistika/alur3.html" style="width:100%; height:1000px"></iframe>
        ''',unsafe_allow_html=True)
        
def tampilkan_materi17():
    st.markdown('''
    <iframe src="https://martin-bernard26.github.io/statistika/testdiag1.html" style="width:100%; height:3700px"></iframe>
    ''',unsafe_allow_html=True)
def tampilkan_materi18():
    st.markdown("Contoh Data normal")
    banyak = st.text_input("Masukan Banyak Sampel")
    rata_rata = st.text_input("Rata-rata")
    std = st.text_input("Standar Deviasi")
    st.write("Ketika sudah terisi semua tinggal di Enter")
    if banyak and rata_rata and std:
        data1 = np.random.normal(float(rata_rata),float(std),int(banyak))
        data1 = list(int(i) for i in list(np.array(data1)))
        st.write(str(data1))
        # Visualisasi
        fig, axes = plt.subplots(1, 2, figsize=(12, 4))
        sns.histplot(data1, kde=True, ax=axes[0])
        axes[0].set_title("Distribusi  Normal")
        sns.scatterplot(data1,c='black', ax=axes[1])
        sns.lineplot(data=np.array(list(mean(data1) for _ in range(len(data1)))),c='red', ax=axes[1])
        axes[1].set_title("Data Normal")
        # Tata letak rapi
        plt.tight_layout()
        st.pyplot(fig)
    st.markdown('---')
    st.markdown("Contoh Data tidak normal")
    banyak1 = st.text_input("Masukan Banyak Sampel2")
    std1 = st.text_input("Standar Deviasi2")
    st.write("Ketika sudah terisi semua tinggal di Enter")
    if banyak1 and std1:
        data2 = np.random.exponential(float(std1),int(banyak1))
        data2 = list(int(i) for i in list(np.array(data2)))
        st.write(str(data2))
        # Visualisasi
        fig, axes = plt.subplots(1, 2, figsize=(12, 4))
        sns.histplot(data2, kde=True, ax=axes[0])
        axes[0].set_title("Distribusi tidak Normal")
        sns.scatterplot(data2,c='black', ax=axes[1])
        sns.lineplot(data=np.array(list(mean(data2) for _ in range(len(data2)))),c='red', ax=axes[1])
        axes[1].set_title("Data tidak Normal")
        # Tata letak rapi
        plt.tight_layout()
        st.pyplot(fig)
def tampilkan_materi19():
    st.title("🎯 Simulasi Uji t 2 Sampel Berpasangan")
    st.markdown("""
    Aplikasi ini mensimulasikan **Uji t Berpasangan (Paired Sample t-test)**  
    untuk melihat apakah terdapat perbedaan signifikan antara dua kondisi, misalnya:
    - Sebelum dan sesudah pelatihan
    - Nilai pre-test dan post-test
    """)

    # =========================
    # Sidebar: Pengaturan Simulasi
    # =========================
    st.sidebar.header("⚙️ Pengaturan Simulasi")
    n = st.sidebar.slider("Jumlah Sampel (n)", 5, 100, 30)
    mean1 = st.sidebar.slider("Rata-rata Kondisi 1", 0.0, 100.0, 70.0)
    mean2 = st.sidebar.slider("Rata-rata Kondisi 2", 0.0, 100.0, 75.0)
    std1 = st.sidebar.slider("Standar Deviasi Kondisi 1", 1.0, 20.0, 10.0)
    std2 = st.sidebar.slider("Standar Deviasi Kondisi 2", 1.0, 20.0, 10.0)
    seed = st.sidebar.number_input("Seed (untuk reproduksi)", 0, 9999, 42)

    np.random.seed(seed)

    # =========================
    # Generate Data
    # =========================
    data1 = np.random.normal(mean1, std1, n)
    data2 = data1 + np.random.normal(mean2 - mean1, std2, n)

    df = pd.DataFrame({
        "Sebelum": data1,
        "Sesudah": data2
    })
    df["Selisih"] = df["Sesudah"] - df["Sebelum"]

    # =========================
    # Visualisasi Data
    # =========================
    st.subheader("📊 Visualisasi Data")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**Distribusi Data Sebelum vs Sesudah**")
        fig1 = px.box(df.melt(var_name="Kondisi", value_name="Nilai"),
                  x="Kondisi", y="Nilai", color="Kondisi",
                  title="Perbandingan Boxplot Dua Kondisi")
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        st.markdown("**Distribusi Selisih (Sesudah - Sebelum)**")
        fig2 = px.histogram(df, x="Selisih", nbins=15, title="Distribusi Selisih Nilai")
        st.plotly_chart(fig2, use_container_width=True)

    # =========================
    # Analisis Statistik
    # =========================
    st.subheader("🧮 Hasil Uji t Berpasangan")
    t_stat, p_val = ttest_rel(df["Sebelum"], df["Sesudah"])

    col3, col4 = st.columns(2)
    with col3:
        st.metric("Statistik t", f"{t_stat:.4f}")
    with col4:
        st.metric("p-value", f"{p_val:.4f}")

    # =========================
    # Interpretasi
    # =========================
    alpha = 0.05
    st.subheader("🧠 Interpretasi")
    if p_val < alpha:
        st.success(f"Hasil uji signifikan (p < {alpha}). Terdapat perbedaan yang bermakna antara kedua kondisi.")
    else:
        st.info(f"Tidak signifikan (p ≥ {alpha}). Tidak ada bukti kuat bahwa kedua kondisi berbeda.")

    # =========================
    # Tabel Data
    # =========================
    with st.expander("📋 Lihat Data Simulasi"):
        st.dataframe(df.style.format("{:.2f}"))
    with st.expander("Melihat hasil selisih data"):
        st.write(str([float(i) for i in df['Selisih']]))
    # =========================
    # Penjelasan Teori
    # =========================
    st.markdown("""
    ---
    ### 🧩 Penjelasan Singkat
    **Uji t berpasangan** digunakan ketika dua set data **berasal dari subjek yang sama** namun dalam dua kondisi berbeda.  
    Contoh: skor siswa sebelum dan sesudah mengikuti pelatihan.

    **Rumus:**
    $$
    t = \\frac{\\bar{d}}{s_d / \\sqrt{n}}
    $$
    dengan:
    - $ \\bar{d} $: rata-rata selisih
    - $ s_d $: standar deviasi selisih
    - $ n $: jumlah pasangan data

    **Hipotesis:**
    - H₀: Tidak ada perbedaan (μd = 0)
    - H₁: Ada perbedaan (μd ≠ 0)
    """)

    st.markdown("---")
    st.caption("Dibuat dengan ❤️ menggunakan Streamlit + SciPy + Plotly")

def tampilkan_materi20():
    st.title("🧠 Simulasi Uji Wilcoxon 2 Sampel Berpasangan (Non-Parametrik)")
    st.markdown("""
    Uji Wilcoxon digunakan ketika **data berpasangan** namun **tidak berdistribusi normal**.  
    Cocok untuk membandingkan dua kondisi dari subjek yang sama, misalnya:
    - Sebelum dan sesudah terapi  
    - Nilai pre-test dan post-test siswa  
    - Efek dari intervensi tertentu
    """)

    # =========================
    # Sidebar: Pengaturan Data
    # =========================
    st.sidebar.header("⚙️ Pengaturan Simulasi")
    n = st.sidebar.slider("Jumlah Sampel (n)", 5, 100, 20)
    median1 = st.sidebar.slider("Median Kondisi 1", 0.0, 100.0, 60.0)
    median2 = st.sidebar.slider("Median Kondisi 2", 0.0, 100.0, 65.0)
    spread1 = st.sidebar.slider("Sebaran Kondisi 1 (variabilitas)", 1.0, 20.0, 8.0)
    spread2 = st.sidebar.slider("Sebaran Kondisi 2 (variabilitas)", 1.0, 20.0, 8.0)
    noise = st.sidebar.slider("Tingkat Ketidakteraturan (noise)", 0.0, 10.0, 2.0)
    seed = st.sidebar.number_input("Seed (untuk reproduksi)", 0, 9999, 42)

    np.random.seed(seed)

    # =========================
    # Generate Data Non-Normal (menggunakan distribusi eksponensial/lognormal)
    # =========================
    # Data dibuat dengan distribusi lognormal agar tidak normal
    data1 = np.random.lognormal(mean=median1, sigma=spread1, size=n) * 10
    #data2 = data1 + np.random.normal(median2 - median1, spread2, n) + np.random.normal(0, noise, n)
    data2 = np.random.lognormal(mean=median2, sigma=spread2, size=n) * 10
    df = pd.DataFrame({
        "Kondisi 1 (Sebelum)": data1,
        "Kondisi 2 (Sesudah)": data2
    })
    df["Selisih"] = df["Kondisi 2 (Sesudah)"] - df["Kondisi 1 (Sebelum)"]

    # =========================
    # Visualisasi Data
    # =========================
    st.subheader("📊 Visualisasi Data")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**Boxplot Dua Kondisi**")
        fig1 = px.box(df.melt(var_name="Kondisi", value_name="Nilai"),
                  x="Kondisi", y="Nilai", color="Kondisi",
                  title="Perbandingan Nilai Sebelum vs Sesudah")
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        st.markdown("**Distribusi Selisih (Sesudah - Sebelum)**")
        fig2 = px.histogram(df, x="Selisih", nbins=15, title="Distribusi Selisih Nilai",
                        color_discrete_sequence=['#00CC96'])
        st.plotly_chart(fig2, use_container_width=True)

    # =========================
    # Uji Wilcoxon
    # =========================
    st.subheader("🧮 Hasil Uji Wilcoxon Berpasangan")

    try:
        stat, p_val = wilcoxon(df["Kondisi 1 (Sebelum)"], df["Kondisi 2 (Sesudah)"])
        col3, col4 = st.columns(2)
        with col3:
            st.metric("Statistik U", f"{stat:.4f}")
        with col4:
            st.metric("p-value", f"{p_val:.4f}")
    except ValueError as e:
        st.error("❌ Terjadi kesalahan: pastikan tidak semua nilai selisih = 0")
        st.stop()

    # =========================
    # Interpretasi
    # =========================
    alpha = 0.05
    st.subheader("🧠 Interpretasi")
    if p_val < alpha:
        st.success(f"Hasil uji **signifikan** (p < {alpha}). Ada perbedaan bermakna antara dua kondisi.")
    else:
        st.info(f"Hasil uji **tidak signifikan** (p ≥ {alpha}). Tidak ada bukti cukup bahwa kedua kondisi berbeda.")

    # =========================
    # Lihat Data Simulasi
    # =========================
    with st.expander("📋 Lihat Data Simulasi"):
        st.dataframe(df.style.format("{:.2f}"))
    with st.expander("Melihat hasil selisih data"):
        st.write(str([float(i) for i in df['Selisih']]))
    # =========================
    # Penjelasan Teori
    # =========================
    st.markdown("""
    ---
    ### 📘 Penjelasan Teori Singkat
    **Uji Wilcoxon Signed-Rank Test** digunakan untuk:
    - Data berpasangan (misalnya pengukuran sebelum–sesudah)
    - Data **tidak normal** (alternatif dari *Paired t-test*)

    **Hipotesis:**
    - H₀ : Tidak ada perbedaan median antara dua kondisi  
    - H₁ : Ada perbedaan median antara dua kondisi  

    **Langkah umum:**
    1. Hitung selisih antara dua kondisi.  
    2. Abaikan nilai 0, beri tanda + atau – sesuai arah selisih.  
    3. Rangking selisih berdasarkan nilai absolutnya.  
    4. Jumlahkan rank untuk nilai positif dan negatif.  
    5. Statistik U adalah nilai terkecil dari dua jumlah tersebut.  

    Jika p-value < 0.05 → Tolak H₀ → Ada perbedaan yang signifikan.
    """)

    st.markdown("---")
    st.caption("Dibuat dengan ❤️ menggunakan Streamlit + SciPy + Plotly")

def tampilkan_materi21():
    # CSS Styling
    st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        text-align: center;
        color: #2E86AB;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1.2rem;
        text-align: center;
        color: #666;
        margin-bottom: 2rem;
    }
    .result-box {
        background-color: #E8F4F8;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #2E86AB;
        margin: 1rem 0;
        color:black;
    }
    .hypothesis-box {
        background-color: #FFF4E6;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #FF9800;
        margin: 1rem 0;
        color:black;
    }
    .success-box {
        background-color: #E8F5E9;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #4CAF50;
        margin: 1rem 0;
        color: black;
    }
    .warning-box {
        background-color: #FFEBEE;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #F44336;
        margin: 1rem 0;
        color: black;
    }
    .metric-card {
        background-color: #F5F5F5;
        padding: 1rem;
        border-radius: 8px;
        text-align: center;
        margin: 0.5rem 0;
        color:black;
    }
    </style>
    """, unsafe_allow_html=True)

    # Header
    st.markdown('<div class="main-header">📊 Simulasi Uji T 2 Sampel Independen</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Independent Sample T-Test Simulator</div>', unsafe_allow_html=True)

    # Sidebar
    st.sidebar.title("⚙️ Pengaturan")
    mode = st.sidebar.radio(
    "Pilih Mode:",
    ["📝 Input Data Manual", "🎲 Generate Data Simulasi", "📁 Upload Data CSV"]
    )

    st.sidebar.markdown("---")
    st.sidebar.markdown("### 📖 Tentang Uji T")
    st.sidebar.info("""
    **Uji T 2 Sampel Independen** digunakan untuk membandingkan rata-rata dua kelompok yang tidak berhubungan.

    **Asumsi:**
    - Data berdistribusi normal
    - Varians kedua kelompok homogen
    - Sampel independen
    """)

    # Fungsi untuk menghitung uji t
    def perform_t_test(data1, data2, alpha, alternative):
        """Melakukan uji t dan mengembalikan hasil"""
        n1, n2 = len(data1), len(data2)
        mean1, mean2 = np.mean(data1), np.mean(data2)
        std1, std2 = np.std(data1, ddof=1), np.std(data2, ddof=1)
        var1, var2 = np.var(data1, ddof=1), np.var(data2, ddof=1)
    
        # Uji Levene untuk homogenitas varians
        levene_stat, levene_p = stats.levene(data1, data2)
    
        # Uji normalitas
        shapiro1_stat, shapiro1_p = stats.shapiro(data1)
        shapiro2_stat, shapiro2_p = stats.shapiro(data2)
    
        # Uji t
        if levene_p > 0.05:  # Varians homogen
            t_stat, p_value = stats.ttest_ind(data1, data2, alternative=alternative)
            equal_var = True
        else:  # Varians tidak homogen (Welch's t-test)
            t_stat, p_value = stats.ttest_ind(data1, data2, equal_var=False, alternative=alternative)
            equal_var = False
    
        # Derajat kebebasan
        if equal_var:
            df = n1 + n2 - 2
        else:
            df = ((var1/n1 + var2/n2)**2) / ((var1/n1)**2/(n1-1) + (var2/n2)**2/(n2-1))
    
        # Cohen's d (effect size)
        if equal_var:
            pooled_std = np.sqrt(((n1-1)*var1 + (n2-1)*var2) / (n1+n2-2))
        else:
            pooled_std = np.sqrt((var1 + var2) / 2)
    
        cohens_d = (mean1 - mean2) / pooled_std
    
        # Confidence interval
        se = pooled_std * np.sqrt(1/n1 + 1/n2)
        t_critical = stats.t.ppf(1-alpha/2, df)
        ci_lower = (mean1 - mean2) - t_critical * se
        ci_upper = (mean1 - mean2) + t_critical * se
    
        return {
        'n1': n1, 'n2': n2,
        'mean1': mean1, 'mean2': mean2,
        'std1': std1, 'std2': std2,
        'var1': var1, 'var2': var2,
        't_stat': t_stat,
        'p_value': p_value,
        'df': df,
        'cohens_d': cohens_d,
        'ci_lower': ci_lower,
        'ci_upper': ci_upper,
        'equal_var': equal_var,
        'levene_stat': levene_stat,
        'levene_p': levene_p,
        'shapiro1_stat': shapiro1_stat,
        'shapiro1_p': shapiro1_p,
        'shapiro2_stat': shapiro2_stat,
        'shapiro2_p': shapiro2_p
        }

    # Main content
    if mode == "📝 Input Data Manual":
        st.header("📝 Input Data Manual")
    
        col1, col2 = st.columns(2)
    
        with col1:
            st.subheader("Kelompok 1")
            data1_input = st.text_area(
            "Masukkan data kelompok 1 (pisahkan dengan koma):",
            "23, 25, 27, 29, 31, 33, 35, 37, 39, 41",
            height=100
            )
        
        with col2:
            st.subheader("Kelompok 2")
            data2_input = st.text_area(
            "Masukkan data kelompok 2 (pisahkan dengan koma):",
            "18, 20, 22, 24, 26, 28, 30, 32, 34, 36",
                height=100
            )
    
        try:
            data1 = np.array([float(x.strip()) for x in data1_input.split(',')])
            data2 = np.array([float(x.strip()) for x in data2_input.split(',')])
            data_ready = True
        except:
            st.error("❌ Format data tidak valid. Gunakan angka yang dipisahkan dengan koma.")
            data_ready = False

    elif mode == "🎲 Generate Data Simulasi":
        st.header("🎲 Generate Data Simulasi")
    
        col1, col2, col3 = st.columns(3)
    
        with col1:
            n1 = st.number_input("Ukuran sampel kelompok 1:", min_value=3, max_value=1000, value=30)
            mean1 = st.number_input("Mean kelompok 1:", value=50.0)
            std1 = st.number_input("Std Dev kelompok 1:", min_value=0.1, value=10.0)
        
        with col2:
            n2 = st.number_input("Ukuran sampel kelompok 2:", min_value=3, max_value=1000, value=30)
            mean2 = st.number_input("Mean kelompok 2:", value=55.0)
            std2 = st.number_input("Std Dev kelompok 2:", min_value=0.1, value=10.0)
    
        with col3:
            seed = st.number_input("Random Seed:", min_value=0, value=42)
            st.markdown("###")
            if st.button("🎲 Generate Data", use_container_width=True):
                np.random.seed(seed)
                st.session_state.data1 = np.random.normal(mean1, std1, n1)
                st.session_state.data2 = np.random.normal(mean2, std2, n2)
                st.success("✅ Data berhasil di-generate!")
    
        if 'data1' in st.session_state and 'data2' in st.session_state:
            data1 = st.session_state.data1
            data2 = st.session_state.data2
            data_ready = True
        else:
            st.info("👆 Klik tombol 'Generate Data' untuk membuat data simulasi")
            data_ready = False

    else:  # Upload CSV
        st.header("📁 Upload Data CSV")
    
        st.markdown("""
        **Format CSV yang diharapkan:**
        - Kolom 1: Nilai data
        - Kolom 2: Label kelompok (misalnya: 'Kelompok1' dan 'Kelompok2')
        """)
    
        uploaded_file = st.file_uploader("Upload file CSV", type=['csv'])
    
        if uploaded_file is not None:
            try:
                df = pd.read_csv(uploaded_file)
                st.write("Preview Data:")
                st.dataframe(df.head())
            
                col1, col2 = st.columns(2)
                with col1:
                    value_col = st.selectbox("Pilih kolom nilai:", df.columns)
                with col2:
                    group_col = st.selectbox("Pilih kolom kelompok:", df.columns)
            
                groups = df[group_col].unique()
                if len(groups) != 2:
                    st.error("❌ Data harus memiliki tepat 2 kelompok!")
                    data_ready = False
                else:
                    group1_name = st.selectbox("Pilih kelompok 1:", groups)
                    group2_name = st.selectbox("Pilih kelompok 2:", [g for g in groups if g != group1_name])
                
                    data1 = df[df[group_col] == group1_name][value_col].values
                    data2 = df[df[group_col] == group2_name][value_col].values
                    data_ready = True
            except Exception as e:
                st.error(f"❌ Error membaca file: {str(e)}")
                data_ready = False
        else:
            data_ready = False

    # Jika data siap, lakukan analisis
    if data_ready:
        st.markdown("---")
        st.header("🔧 Pengaturan Uji Hipotesis")
    
        col1, col2, col3 = st.columns(3)
    
        with col1:
            alpha = st.select_slider(
                "Tingkat signifikansi (α):",
                options=[0.01, 0.05, 0.10],
                value=0.05
            )
    
        with col2:
            alternative = st.selectbox(
                "Hipotesis alternatif:",
                ["two-sided", "less", "greater"],
                format_func=lambda x: {
                    "two-sided": "Dua sisi (≠)",
                    "less": "Sisi kiri (<)",
                    "greater": "Sisi kanan (>)"
                }[x]
            )
    
        with col3:
            group1_name = st.text_input("Nama Kelompok 1:", "Kelompok 1")
            group2_name = st.text_input("Nama Kelompok 2:", "Kelompok 2")
    
        # Hipotesis
        st.markdown("### 📋 Hipotesis")
        if alternative == "two-sided":
            h0 = f"H₀: μ₁ = μ₂ (Tidak ada perbedaan rata-rata)"
            h1 = f"H₁: μ₁ ≠ μ₂ (Ada perbedaan rata-rata)"
        elif alternative == "less":
            h0 = f"H₀: μ₁ ≥ μ₂"
            h1 = f"H₁: μ₁ < μ₂ (Rata-rata kelompok 1 lebih kecil)"
        else:
            h0 = f"H₀: μ₁ ≤ μ₂"
            h1 = f"H₁: μ₁ > μ₂ (Rata-rata kelompok 1 lebih besar)"
    
        st.markdown(f'<div class="hypothesis-box"><strong>{h0}</strong><br><strong>{h1}</strong></div>', 
                unsafe_allow_html=True)
    
        # Perform t-test
        if st.button("🚀 Jalankan Uji T", use_container_width=True, type="primary"):
            results = perform_t_test(data1, data2, alpha, alternative)
        
            st.markdown("---")
            st.header("📊 Hasil Analisis")
        
            # Statistik Deskriptif
            st.subheader("1️⃣ Statistik Deskriptif")
        
            col1, col2, col3, col4 = st.columns(4)
        
            with col1:
                st.markdown(f"""
                <div class="metric-card">
                <h4>{group1_name}</h4>
                <p><strong>n:</strong> {results['n1']}</p>
                <p><strong>Mean:</strong> {results['mean1']:.4f}</p>
                <p><strong>Std:</strong> {results['std1']:.4f}</p>
                </div>
                """, unsafe_allow_html=True)
        
            with col2:
                st.markdown(f"""
            <div class="metric-card">
                <h4>{group2_name}</h4>
                <p><strong>n:</strong> {results['n2']}</p>
                <p><strong>Mean:</strong> {results['mean2']:.4f}</p>
                <p><strong>Std:</strong> {results['std2']:.4f}</p>
            </div>
                """, unsafe_allow_html=True)
        
            with col3:
                st.markdown(f"""
            <div class="metric-card">
                <h4>Perbedaan</h4>
                <p><strong>Δ Mean:</strong> {results['mean1']-results['mean2']:.4f}</p>
                <p><strong>Cohen's d:</strong> {results['cohens_d']:.4f}</p>
            </div>
            """, unsafe_allow_html=True)
        
            with col4:
                effect_size = abs(results['cohens_d'])
                if effect_size < 0.2:
                    effect_label = "Sangat Kecil"
                elif effect_size < 0.5:
                    effect_label = "Kecil"
                elif effect_size < 0.8:
                    effect_label = "Sedang"
                else:
                    effect_label = "Besar"
            
                st.markdown(f"""
            <div class="metric-card">
                <h4>Effect Size</h4>
                <p><strong>{effect_label}</strong></p>
                <p>|d| = {effect_size:.4f}</p>
            </div>
            """, unsafe_allow_html=True)
        
            # Uji Asumsi
            st.subheader("2️⃣ Uji Asumsi")
        
            col1, col2 = st.columns(2)
        
            with col1:
                st.markdown("**Uji Normalitas (Shapiro-Wilk)**")
                if results['shapiro1_p'] > 0.05 and results['shapiro2_p'] > 0.05:
                    st.markdown(f"""
                <div class="success-box">
                ✅ Data berdistribusi normal<br>
                {group1_name}: p = {results['shapiro1_p']:.4f}<br>
                {group2_name}: p = {results['shapiro2_p']:.4f}
                </div>
                """, unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                <div class="warning-box">
                ⚠️ Data tidak berdistribusi normal<br>
                {group1_name}: p = {results['shapiro1_p']:.4f}<br>
                {group2_name}: p = {results['shapiro2_p']:.4f}<br>
                Pertimbangkan uji non-parametrik
                </div>
                """, unsafe_allow_html=True)
        
            with col2:
                st.markdown("**Uji Homogenitas Varians (Levene)**")
                if results['levene_p'] > 0.05:
                    st.markdown(f"""
                <div class="success-box">
                ✅ Varians homogen<br>
                Levene statistic = {results['levene_stat']:.4f}<br>
                p-value = {results['levene_p']:.4f}
                </div>
                """, unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                <div class="warning-box">
                ⚠️ Varians tidak homogen<br>
                Menggunakan Welch's t-test<br>
                Levene statistic = {results['levene_stat']:.4f}<br>
                p-value = {results['levene_p']:.4f}
                </div>
                """, unsafe_allow_html=True)
        
            # Hasil Uji T
            st.subheader("3️⃣ Hasil Uji T")
        
            col1, col2 = st.columns(2)
        
            with col1:
                st.markdown(f"""
            <div class="result-box">
            <h4>Statistik Uji</h4>
            <p><strong>t-statistic:</strong> {results['t_stat']:.4f}</p>
            <p><strong>Degrees of freedom:</strong> {results['df']:.2f}</p>
            <p><strong>p-value:</strong> {results['p_value']:.4f}</p>
            <p><strong>α:</strong> {alpha}</p>
            </div>
            """, unsafe_allow_html=True)
        
            with col2:
                ci_level = int((1-alpha)*100)
                st.markdown(f"""
            <div class="result-box">
            <h4>Confidence Interval ({ci_level}%)</h4>
            <p><strong>Lower bound:</strong> {results['ci_lower']:.4f}</p>
            <p><strong>Upper bound:</strong> {results['ci_upper']:.4f}</p>
            <p><strong>Selisih mean:</strong> {results['mean1']-results['mean2']:.4f}</p>
            </div>
            """, unsafe_allow_html=True)
        
            # Kesimpulan
            st.subheader("4️⃣ Kesimpulan")
        
            if results['p_value'] < alpha:
                conclusion = f"""
            <div class="warning-box">
            <h4>🔴 Tolak H₀</h4>
            <p>Dengan tingkat signifikansi α = {alpha}, terdapat cukup bukti untuk menolak hipotesis nol.</p>
            <p><strong>Kesimpulan:</strong> Terdapat perbedaan yang signifikan antara rata-rata {group1_name} dan {group2_name}.</p>
            <p>p-value ({results['p_value']:.4f}) < α ({alpha})</p>
            </div>
            """
            else:
                conclusion = f"""
            <div class="success-box">
            <h4>🟢 Gagal Tolak H₀</h4>
            <p>Dengan tingkat signifikansi α = {alpha}, tidak terdapat cukup bukti untuk menolak hipotesis nol.</p>
            <p><strong>Kesimpulan:</strong> Tidak terdapat perbedaan yang signifikan antara rata-rata {group1_name} dan {group2_name}.</p>
            <p>p-value ({results['p_value']:.4f}) ≥ α ({alpha})</p>
            </div>
            """
        
            st.markdown(conclusion, unsafe_allow_html=True)
        
            # Visualisasi
            st.markdown("---")
            st.header("📈 Visualisasi Data")
        
            # Create subplots
            fig = make_subplots(
            rows=2, cols=2,
            subplot_titles=('Distribusi Data', 'Box Plot', 'Histogram', 'Q-Q Plot'),
            specs=[[{'type': 'box'}, {'type': 'box'}],
                   [{'type': 'histogram'}, {'type': 'scatter'}]]
            )
        
            # Box plot
            fig.add_trace(
                go.Box(y=data1, name=group1_name, marker_color='lightblue'),
                row=1, col=1
            )
            fig.add_trace(
            go.Box(y=data2, name=group2_name, marker_color='lightcoral'),
            row=1, col=2
            )
        
            # Histogram
            fig.add_trace(
            go.Histogram(x=data1, name=group1_name, opacity=0.7, marker_color='lightblue'),
            row=2, col=1
            )
            fig.add_trace(
            go.Histogram(x=data2, name=group2_name, opacity=0.7, marker_color='lightcoral'),
            row=2, col=1
            )
        
            # Q-Q Plot
            qq1 = stats.probplot(data1, dist="norm")
            qq2 = stats.probplot(data2, dist="norm")
        
            fig.add_trace(
                go.Scatter(x=qq1[0][0], y=qq1[0][1], mode='markers', 
                      name=f'{group1_name} Q-Q', marker_color='lightblue'),
                row=2, col=2
            )
            fig.add_trace(
            go.Scatter(x=qq2[0][0], y=qq2[0][1], mode='markers', 
                      name=f'{group2_name} Q-Q', marker_color='lightcoral'),
            row=2, col=2
            )
        
            # Add reference line for Q-Q plot
            fig.add_trace(
            go.Scatter(x=qq1[0][0], y=qq1[1][1] + qq1[1][0]*qq1[0][0], 
                      mode='lines', name='Reference Line', 
                      line=dict(color='red', dash='dash')),
            row=2, col=2
            )
        
            fig.update_layout(height=800, showlegend=True, title_text="Visualisasi Lengkap")
            st.plotly_chart(fig, use_container_width=True)
        
            # Violin plot dengan matplotlib
            st.subheader("Violin Plot Perbandingan")
            fig_violin, ax = plt.subplots(figsize=(10, 6))
        
            data_combined = pd.DataFrame({
            'Nilai': np.concatenate([data1, data2]),
            'Kelompok': [group1_name]*len(data1) + [group2_name]*len(data2)
            })
        
            sns.violinplot(data=data_combined, x='Kelompok', y='Nilai', ax=ax, palette=['lightblue', 'lightcoral'])
            sns.swarmplot(data=data_combined, x='Kelompok', y='Nilai', ax=ax, color='black', alpha=0.5, size=3)
        
            ax.set_title('Violin Plot Perbandingan Data', fontsize=14, fontweight='bold')
            ax.set_ylabel('Nilai', fontsize=12)
            ax.set_xlabel('Kelompok', fontsize=12)
            ax.grid(True, alpha=0.3)
        
            st.pyplot(fig_violin)
        
            # Tabel data
            st.markdown("---")
            st.subheader("📋 Tabel Data")
        
            col1, col2 = st.columns(2)
        
            with col1:
                st.markdown(f"**{group1_name}**")
                df1 = pd.DataFrame({
                'Index': range(1, len(data1)+1),
                'Nilai': data1
                })
                st.dataframe(df1, height=300)
        
            with col2:
                st.markdown(f"**{group2_name}**")
                df2 = pd.DataFrame({
                'Index': range(1, len(data2)+1),
                'Nilai': data2
                })
                st.dataframe(df2, height=300)

    # Footer
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 📚 Interpretasi Effect Size (Cohen's d)")
    st.sidebar.markdown("""
    - |d| < 0.2: Sangat kecil
    - 0.2 ≤ |d| < 0.5: Kecil
    - 0.5 ≤ |d| < 0.8: Sedang
    - |d| ≥ 0.8: Besar
    """)

    st.sidebar.markdown("### ℹ️ Informasi")
    st.sidebar.info("Aplikasi ini menggunakan scipy.stats untuk perhitungan statistik dan visualisasi interaktif dengan plotly.")

def tampilkan_materi22():
    # CSS Styling
    st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        text-align: center;
        color: #6A1B9A;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1.2rem;
        text-align: center;
        color: #666;
        margin-bottom: 2rem;
    }
    .result-box {
        background-color: #F3E5F5;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #6A1B9A;
        margin: 1rem 0;
        color:black;
    }
    .hypothesis-box {
        background-color: #FFF9C4;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #FBC02D;
        margin: 1rem 0;
        color: black;
    }
    .success-box {
        background-color: #E8F5E9;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #4CAF50;
        margin: 1rem 0;
        color: black;
    }
    .warning-box {
        background-color: #FFEBEE;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #F44336;
        margin: 1rem 0;
    }
    .info-box {
        background-color: #E3F2FD;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #2196F3;
        margin: 1rem 0;
        color: black;
    }
    .metric-card {
        background-color: #FAFAFA;
        padding: 1rem;
        border-radius: 8px;
        text-align: center;
        margin: 0.5rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        color: black;
    }
    .rank-table {
        font-size: 0.9rem;
    }
    </style>
""", unsafe_allow_html=True)

    # Header
    st.markdown('<div class="main-header">📊 Simulasi Uji U Mann-Whitney</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Mann-Whitney U Test for Two Independent Samples (Non-Parametric)</div>', unsafe_allow_html=True)

    # Sidebar
    st.sidebar.title("⚙️ Pengaturan")
    mode = st.sidebar.radio(
    "Pilih Mode:",
    ["📝 Input Data Manual", "🎲 Generate Data Simulasi", "📁 Upload Data CSV"]
    )

    st.sidebar.markdown("---")
    st.sidebar.markdown("### 📖 Tentang Uji Mann-Whitney")
    st.sidebar.info("""
**Uji U Mann-Whitney** (atau Wilcoxon Rank-Sum Test) adalah uji non-parametrik untuk membandingkan dua kelompok independen.

**Kapan digunakan:**
- Data tidak berdistribusi normal
- Data ordinal atau interval
- Sampel kecil
- Alternatif dari uji t independen

**Asumsi:**
- Sampel independen
- Data minimal skala ordinal
- Distribusi bentuk serupa (untuk inferensi median)
""")

    # Fungsi untuk menghitung rank dan statistik
    def calculate_ranks(data1, data2):
        """Menghitung ranking untuk Mann-Whitney U test"""
        # Gabungkan data dan beri label
        combined = np.concatenate([data1, data2])
        labels = np.array([1]*len(data1) + [2]*len(data2))
    
        # Urutkan dan hitung rank
        sorted_indices = np.argsort(combined)
        sorted_data = combined[sorted_indices]
        sorted_labels = labels[sorted_indices]
    
        # Hitung rank dengan menangani ties
        ranks = stats.rankdata(combined, method='average')
    
        # Pisahkan rank berdasarkan kelompok
        ranks_sorted = ranks[sorted_indices]
    
        # Buat dataframe untuk ditampilkan
        rank_df = pd.DataFrame({
        'Nilai': sorted_data,
        'Kelompok': ['Kelompok 1' if l == 1 else 'Kelompok 2' for l in sorted_labels],
        'Rank': ranks_sorted
        })
    
        # Rank untuk masing-masing kelompok
        ranks_group1 = ranks[:len(data1)]
        ranks_group2 = ranks[len(data1):]
    
        return ranks, ranks_group1, ranks_group2, rank_df

    # Fungsi untuk melakukan uji Mann-Whitney
    def perform_mann_whitney(data1, data2, alpha, alternative):
        """Melakukan uji Mann-Whitney dan mengembalikan hasil"""
        n1, n2 = len(data1), len(data2)
    
        # Statistik deskriptif
        mean1, mean2 = np.mean(data1), np.mean(data2)
        median1, median2 = np.median(data1), np.median(data2)
        std1, std2 = np.std(data1, ddof=1), np.std(data2, ddof=1)
        q1_1, q3_1 = np.percentile(data1, [25, 75])
        q1_2, q3_2 = np.percentile(data2, [25, 75])
        iqr1, iqr2 = q3_1 - q1_1, q3_2 - q1_2
        min1, max1 = np.min(data1), np.max(data1)
        min2, max2 = np.min(data2), np.max(data2)
    
        # Hitung ranks
        ranks, ranks_group1, ranks_group2, rank_df = calculate_ranks(data1, data2)
    
        # Sum of ranks
        sum_ranks1 = np.sum(ranks_group1)
        sum_ranks2 = np.sum(ranks_group2)
        mean_rank1 = np.mean(ranks_group1)
        mean_rank2 = np.mean(ranks_group2)
    
        # Mann-Whitney U test
        u_stat, p_value = stats.mannwhitneyu(data1, data2, alternative=alternative)
    
        # Hitung U untuk kelompok lainnya
        u_stat2 = n1 * n2 - u_stat
    
        # Hitung z-score untuk sampel besar
        mean_u = n1 * n2 / 2
    
        # Koreksi untuk ties
        ties = {}
        for val in np.concatenate([data1, data2]):
            ties[val] = ties.get(val, 0) + 1
    
        tie_correction = 0
        n_total = n1 + n2
        for count in ties.values():
            if count > 1:
                tie_correction += (count**3 - count)
    
        std_u = np.sqrt((n1 * n2 * (n_total + 1) / 12) - (n1 * n2 * tie_correction / (12 * n_total * (n_total - 1))))
    
        if std_u > 0:
            z_score = (u_stat - mean_u) / std_u
        else:
            z_score = 0
    
        # Effect size (r = Z / sqrt(N))
        r_effect = abs(z_score) / np.sqrt(n1 + n2)
    
        # Common Language Effect Size (probability)
        cles = u_stat / (n1 * n2)
    
        # Rank-biserial correlation
        rank_biserial = 1 - (2*u_stat) / (n1 * n2)
    
        return {
        'n1': n1, 'n2': n2,
        'mean1': mean1, 'mean2': mean2,
        'median1': median1, 'median2': median2,
        'std1': std1, 'std2': std2,
        'q1_1': q1_1, 'q3_1': q3_1,
        'q1_2': q1_2, 'q3_2': q3_2,
        'iqr1': iqr1, 'iqr2': iqr2,
        'min1': min1, 'max1': max1,
        'min2': min2, 'max2': max2,
        'u_stat': u_stat,
        'u_stat2': u_stat2,
        'p_value': p_value,
        'z_score': z_score,
        'r_effect': r_effect,
        'cles': cles,
        'rank_biserial': rank_biserial,
        'sum_ranks1': sum_ranks1,
        'sum_ranks2': sum_ranks2,
        'mean_rank1': mean_rank1,
        'mean_rank2': mean_rank2,
        'rank_df': rank_df,
        'ranks_group1': ranks_group1,
        'ranks_group2': ranks_group2
        }

    # Main content
    if mode == "📝 Input Data Manual":
        st.header("📝 Input Data Manual")
    
        col1, col2 = st.columns(2)
    
        with col1:
            st.subheader("Kelompok 1")
            data1_input = st.text_area(
            "Masukkan data kelompok 1 (pisahkan dengan koma):",
            "12, 15, 18, 20, 22, 25, 28, 30, 32, 35",
            height=100
            )
        
        with col2:
            st.subheader("Kelompok 2")
            data2_input = st.text_area(
            "Masukkan data kelompok 2 (pisahkan dengan koma):",
            "10, 13, 16, 19, 21, 24, 27, 29, 31, 33",
            height=100
            )
    
        try:
            data1 = np.array([float(x.strip()) for x in data1_input.split(',')])
            data2 = np.array([float(x.strip()) for x in data2_input.split(',')])
            data_ready = True
        except:
            st.error("❌ Format data tidak valid. Gunakan angka yang dipisahkan dengan koma.")
            data_ready = False

    elif mode == "🎲 Generate Data Simulasi":
        st.header("🎲 Generate Data Simulasi")
    
        st.markdown("""
    <div class="info-box">
    💡 <strong>Tips:</strong> Untuk data non-normal, gunakan distribusi seperti exponential, uniform, atau poisson.
    </div>
    """, unsafe_allow_html=True)
    
        col1, col2, col3 = st.columns(3)
    
        with col1:
            n1 = st.number_input("Ukuran sampel kelompok 1:", min_value=3, max_value=1000, value=20)
            dist1 = st.selectbox("Distribusi kelompok 1:", 
                            ["Normal", "Exponential", "Uniform", "Poisson", "Skewed Normal"])
        
            if dist1 == "Normal":
                mean1 = st.number_input("Mean K1:", value=50.0, key="mean1")
                std1 = st.number_input("Std Dev K1:", min_value=0.1, value=10.0, key="std1")
            elif dist1 == "Exponential":
                scale1 = st.number_input("Scale K1:", min_value=0.1, value=5.0, key="scale1")
            elif dist1 == "Uniform":
                low1 = st.number_input("Min K1:", value=0.0, key="low1")
                high1 = st.number_input("Max K1:", value=100.0, key="high1")
            elif dist1 == "Poisson":
                lam1 = st.number_input("Lambda K1:", min_value=0.1, value=10.0, key="lam1")
            else:  # Skewed Normal
                loc1 = st.number_input("Location K1:", value=50.0, key="loc1")
                scale1_skew = st.number_input("Scale K1:", min_value=0.1, value=10.0, key="scale1_skew")
                skew1 = st.number_input("Skewness K1:", value=5.0, key="skew1")
        
        with col2:
            n2 = st.number_input("Ukuran sampel kelompok 2:", min_value=3, max_value=1000, value=20)
            dist2 = st.selectbox("Distribusi kelompok 2:", 
                            ["Normal", "Exponential", "Uniform", "Poisson", "Skewed Normal"])
        
            if dist2 == "Normal":
                mean2 = st.number_input("Mean K2:", value=55.0, key="mean2")
                std2 = st.number_input("Std Dev K2:", min_value=0.1, value=10.0, key="std2")
            elif dist2 == "Exponential":
                scale2 = st.number_input("Scale K2:", min_value=0.1, value=7.0, key="scale2")
            elif dist2 == "Uniform":
                low2 = st.number_input("Min K2:", value=10.0, key="low2")
                high2 = st.number_input("Max K2:", value=110.0, key="high2")
            elif dist2 == "Poisson":
                lam2 = st.number_input("Lambda K2:", min_value=0.1, value=15.0, key="lam2")
            else:  # Skewed Normal
                loc2 = st.number_input("Location K2:", value=55.0, key="loc2")
                scale2_skew = st.number_input("Scale K2:", min_value=0.1, value=10.0, key="scale2_skew")
                skew2 = st.number_input("Skewness K2:", value=5.0, key="skew2")
    
        with col3:
            seed = st.number_input("Random Seed:", min_value=0, value=42)
            st.markdown("###")
            if st.button("🎲 Generate Data", use_container_width=True):
                np.random.seed(seed)
            
                # Generate data1
                if dist1 == "Normal":
                    st.session_state.data1 = np.random.normal(mean1, std1, n1)
                elif dist1 == "Exponential":
                    st.session_state.data1 = np.random.exponential(scale1, n1)
                elif dist1 == "Uniform":
                    st.session_state.data1 = np.random.uniform(low1, high1, n1)
                elif dist1 == "Poisson":
                    st.session_state.data1 = np.random.poisson(lam1, n1).astype(float)
                else:  # Skewed Normal
                    st.session_state.data1 = stats.skewnorm.rvs(skew1, loc=loc1, scale=scale1_skew, size=n1)
            
                # Generate data2
                if dist2 == "Normal":
                    st.session_state.data2 = np.random.normal(mean2, std2, n2)
                elif dist2 == "Exponential":
                    st.session_state.data2 = np.random.exponential(scale2, n2)
                elif dist2 == "Uniform":
                    st.session_state.data2 = np.random.uniform(low2, high2, n2)
                elif dist2 == "Poisson":
                    st.session_state.data2 = np.random.poisson(lam2, n2).astype(float)
                else:  # Skewed Normal
                    st.session_state.data2 = stats.skewnorm.rvs(skew2, loc=loc2, scale=scale2_skew, size=n2)
            
                st.success("✅ Data berhasil di-generate!")
    
        if 'data1' in st.session_state and 'data2' in st.session_state:
            data1 = st.session_state.data1
            data2 = st.session_state.data2
            data_ready = True
        else:
            st.info("👆 Klik tombol 'Generate Data' untuk membuat data simulasi")
            data_ready = False

    else:  # Upload CSV
        st.header("📁 Upload Data CSV")
    
        st.markdown("""
    **Format CSV yang diharapkan:**
    - Kolom 1: Nilai data
    - Kolom 2: Label kelompok (misalnya: 'Kelompok1' dan 'Kelompok2')
    """)
    
        uploaded_file = st.file_uploader("Upload file CSV", type=['csv'])
    
        if uploaded_file is not None:
            try:
                df = pd.read_csv(uploaded_file)
                st.write("Preview Data:")
                st.dataframe(df.head())
            
                col1, col2 = st.columns(2)
                with col1:
                    value_col = st.selectbox("Pilih kolom nilai:", df.columns)
                with col2:
                    group_col = st.selectbox("Pilih kolom kelompok:", df.columns)
            
                groups = df[group_col].unique()
                if len(groups) != 2:
                    st.error("❌ Data harus memiliki tepat 2 kelompok!")
                    data_ready = False
                else:
                    group1_name = st.selectbox("Pilih kelompok 1:", groups)
                    group2_name = st.selectbox("Pilih kelompok 2:", [g for g in groups if g != group1_name])
                
                    data1 = df[df[group_col] == group1_name][value_col].values
                    data2 = df[df[group_col] == group2_name][value_col].values
                    data_ready = True
            except Exception as e:
                st.error(f"❌ Error membaca file: {str(e)}")
                data_ready = False
        else:
            data_ready = False

    # Jika data siap, lakukan analisis
    if data_ready:
        st.markdown("---")
        st.header("🔧 Pengaturan Uji Hipotesis")
    
        col1, col2, col3 = st.columns(3)
    
        with col1:
            alpha = st.select_slider(
                "Tingkat signifikansi (α):",
                options=[0.01, 0.05, 0.10],
                value=0.05
            )
    
        with col2:
            alternative = st.selectbox(
                "Hipotesis alternatif:",
                ["two-sided", "less", "greater"],
                format_func=lambda x: {
                    "two-sided": "Dua sisi (≠)",
                    "less": "Sisi kiri (<)",
                    "greater": "Sisi kanan (>)"
                }[x]
            )
    
    with col3:
        group1_name = st.text_input("Nama Kelompok 1:", "Kelompok 1")
        group2_name = st.text_input("Nama Kelompok 2:", "Kelompok 2")
    
    # Hipotesis
    st.markdown("### 📋 Hipotesis")
    if alternative == "two-sided":
        h0 = f"H₀: Distribusi {group1_name} = Distribusi {group2_name}"
        h1 = f"H₁: Distribusi {group1_name} ≠ Distribusi {group2_name}"
    elif alternative == "less":
        h0 = f"H₀: Distribusi {group1_name} ≥ Distribusi {group2_name}"
        h1 = f"H₁: Distribusi {group1_name} < Distribusi {group2_name}"
    else:
        h0 = f"H₀: Distribusi {group1_name} ≤ Distribusi {group2_name}"
        h1 = f"H₁: Distribusi {group1_name} > Distribusi {group2_name}"
    
    st.markdown(f'<div class="hypothesis-box"><strong>{h0}</strong><br><strong>{h1}</strong></div>', 
                unsafe_allow_html=True)
    
    # Perform Mann-Whitney test
    if st.button("🚀 Jalankan Uji Mann-Whitney", use_container_width=True, type="primary"):
        results = perform_mann_whitney(data1, data2, alpha, alternative)
        
        st.markdown("---")
        st.header("📊 Hasil Analisis")
        
        # Statistik Deskriptif
        st.subheader("1️⃣ Statistik Deskriptif")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown(f"""
                <div class="metric-card">
                <h4>{group1_name}</h4>
                <p><strong>n:</strong> {results['n1']}</p>
                <p><strong>Median:</strong> {results['median1']:.2f}</p>
                <p><strong>Mean:</strong> {results['mean1']:.2f}</p>
                <p><strong>IQR:</strong> {results['iqr1']:.2f}</p>
            </div>
               """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div class="metric-card">
                <h4>{group2_name}</h4>
                <p><strong>n:</strong> {results['n2']}</p>
                <p><strong>Median:</strong> {results['median2']:.2f}</p>
                <p><strong>Mean:</strong> {results['mean2']:.2f}</p>
                <p><strong>IQR:</strong> {results['iqr2']:.2f}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown(f"""
            <div class="metric-card">
                <h4>Ranking</h4>
                <p><strong>Mean Rank K1:</strong> {results['mean_rank1']:.2f}</p>
                <p><strong>Mean Rank K2:</strong> {results['mean_rank2']:.2f}</p>
                <p><strong>Sum Ranks K1:</strong> {results['sum_ranks1']:.0f}</p>
                <p><strong>Sum Ranks K2:</strong> {results['sum_ranks2']:.0f}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col4:
            r_effect = abs(results['r_effect'])
            if r_effect < 0.1:
                effect_label = "Sangat Kecil"
            elif r_effect < 0.3:
                effect_label = "Kecil"
            elif r_effect < 0.5:
                effect_label = "Sedang"
            else:
                effect_label = "Besar"
            
            st.markdown(f"""
            <div class="metric-card">
                <h4>Effect Size</h4>
                <p><strong>{effect_label}</strong></p>
                <p>r = {r_effect:.4f}</p>
                <p><strong>CLES:</strong> {results['cles']:.4f}</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Hasil Uji Mann-Whitney
        st.subheader("2️⃣ Hasil Uji Mann-Whitney")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f"""
            <div class="result-box">
            <h4>Statistik Uji</h4>
            <p><strong>U-statistic (K1):</strong> {results['u_stat']:.4f}</p>
            <p><strong>U-statistic (K2):</strong> {results['u_stat2']:.4f}</p>
            <p><strong>Z-score:</strong> {results['z_score']:.4f}</p>
            <p><strong>p-value:</strong> {results['p_value']:.6f}</p>
            <p><strong>α:</strong> {alpha}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div class="result-box">
            <h4>Effect Size Metrics</h4>
            <p><strong>r (effect size):</strong> {results['r_effect']:.4f}</p>
            <p><strong>Rank-biserial correlation:</strong> {results['rank_biserial']:.4f}</p>
            <p><strong>CLES (probability):</strong> {results['cles']:.4f}</p>
            <p><em>CLES: Probabilitas nilai dari K1 > K2</em></p>
            </div>
            """, unsafe_allow_html=True)
        
        # Kesimpulan
        st.subheader("3️⃣ Kesimpulan")
        
        if results['p_value'] < alpha:
            conclusion = f"""
            <div class="warning-box">
            <h4>🔴 Tolak H₀</h4>
            <p>Dengan tingkat signifikansi α = {alpha}, terdapat cukup bukti untuk menolak hipotesis nol.</p>
            <p><strong>Kesimpulan:</strong> Terdapat perbedaan yang signifikan antara distribusi {group1_name} dan {group2_name}.</p>
            <p>p-value ({results['p_value']:.6f}) < α ({alpha})</p>
            <p><strong>Interpretasi:</strong> Median kelompok berbeda secara signifikan (Median K1 = {results['median1']:.2f}, Median K2 = {results['median2']:.2f})</p>
            </div>
            """
        else:
            conclusion = f"""
            <div class="success-box">
            <h4>🟢 Gagal Tolak H₀</h4>
            <p>Dengan tingkat signifikansi α = {alpha}, tidak terdapat cukup bukti untuk menolak hipotesis nol.</p>
            <p><strong>Kesimpulan:</strong> Tidak terdapat perbedaan yang signifikan antara distribusi {group1_name} dan {group2_name}.</p>
            <p>p-value ({results['p_value']:.6f}) ≥ α ({alpha})</p>
            <p><strong>Interpretasi:</strong> Median kelompok tidak berbeda secara signifikan (Median K1 = {results['median1']:.2f}, Median K2 = {results['median2']:.2f})</p>
            </div>
            """
        
        st.markdown(conclusion, unsafe_allow_html=True)
        
        # Tabel Ranking
        st.subheader("4️⃣ Tabel Ranking Data")
        
        st.markdown("""
        <div class="info-box">
        💡 Tabel ini menunjukkan ranking gabungan dari kedua kelompok. Ranking digunakan untuk menghitung statistik U Mann-Whitney.
        </div>
        """, unsafe_allow_html=True)
        
        # Tampilkan tabel dengan styling
        st.dataframe(
        results['rank_df'].style.background_gradient(subset=['Rank'], cmap='YlOrRd'),
        height=400
        )
        
        # Statistik ranking per kelompok
        col1, col2 = st.columns(2)
        with col1:
            st.metric(f"Total Rank {group1_name}", f"{results['sum_ranks1']:.0f}")
            st.metric(f"Mean Rank {group1_name}", f"{results['mean_rank1']:.2f}")
        with col2:
            st.metric(f"Total Rank {group2_name}", f"{results['sum_ranks2']:.0f}")
            st.metric(f"Mean Rank {group2_name}", f"{results['mean_rank2']:.2f}")
        
        # Visualisasi
        st.markdown("---")
        st.header("📈 Visualisasi Data")
        
        # Create comprehensive plots
        fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=('Box Plot Perbandingan', 'Distribusi Ranking', 
                          'Histogram Distribusi', 'Cumulative Distribution'),
        specs=[[{'type': 'box'}, {'type': 'box'}],
                [{'type': 'histogram'}, {'type': 'scatter'}]]
        )
        
        # Box plot
        fig.add_trace(
        go.Box(y=data1, name=group1_name, marker_color='mediumpurple', boxmean='sd'),
        row=1, col=1
        )
        fig.add_trace(
        go.Box(y=data2, name=group2_name, marker_color='lightcoral', boxmean='sd'),
        row=1, col=1
        )
        
        # Box plot ranking
        fig.add_trace(
        go.Box(y=results['ranks_group1'], name=f'Rank {group1_name}', 
                marker_color='mediumpurple', boxmean='sd'),
        row=1, col=2
        )
        fig.add_trace(
        go.Box(y=results['ranks_group2'], name=f'Rank {group2_name}', 
                marker_color='lightcoral', boxmean='sd'),
        row=1, col=2
        )
        
        # Histogram
        fig.add_trace(
        go.Histogram(x=data1, name=group1_name, opacity=0.7, 
                    marker_color='mediumpurple', nbinsx=20),
        row=2, col=1
        )
        fig.add_trace(
        go.Histogram(x=data2, name=group2_name, opacity=0.7, 
                    marker_color='lightcoral', nbinsx=20),
        row=2, col=1
        )
        
        # Cumulative distribution
        data1_sorted = np.sort(data1)
        data2_sorted = np.sort(data2)
        cum1 = np.arange(1, len(data1_sorted) + 1) / len(data1_sorted)
        cum2 = np.arange(1, len(data2_sorted) + 1) / len(data2_sorted)
        
        fig.add_trace(
            go.Scatter(x=data1_sorted, y=cum1, mode='lines', 
                  name=f'CDF {group1_name}', line=dict(color='mediumpurple', width=3)),
            row=2, col=2
        )
        fig.add_trace(
        go.Scatter(x=data2_sorted, y=cum2, mode='lines', 
                name=f'CDF {group2_name}', line=dict(color='lightcoral', width=3)),
        row=2, col=2
        )
        
        fig.update_layout(height=800, showlegend=True, 
                         title_text="Visualisasi Lengkap Mann-Whitney U Test")
        fig.update_xaxes(title_text="Nilai", row=2, col=1)
        fig.update_xaxes(title_text="Nilai", row=2, col=2)
        fig.update_yaxes(title_text="Cumulative Probability", row=2, col=2)
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Violin plot dengan matplotlib
        st.subheader("Violin Plot Perbandingan")
        fig_violin, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
        
        # Violin plot untuk data asli
        data_combined = pd.DataFrame({
        'Nilai': np.concatenate([data1, data2]),
        'Kelompok': [group1_name]*len(data1) + [group2_name]*len(data2)
        })
        
        sns.violinplot(data=data_combined, x='Kelompok', y='Nilai', ax=ax1, 
                    palette=['mediumpurple', 'lightcoral'])
        sns.swarmplot(data=data_combined, x='Kelompok', y='Nilai', ax=ax1, 
                    color='black', alpha=0.4, size=3)
        ax1.set_title('Violin Plot - Data Asli', fontsize=14, fontweight='bold')
        ax1.set_ylabel('Nilai', fontsize=12)
        ax1.set_xlabel('Kelompok', fontsize=12)
        ax1.grid(True, alpha=0.3, axis='y')
        
        # Add median lines
        ax1.hlines(results['median1'], -0.4, 0.4, colors='red', linestyles='--', 
                  linewidth=2, label=f'Median: {results["median1"]:.2f}')
        ax1.hlines(results['median2'], 0.6, 1.4, colors='red', linestyles='--', 
                  linewidth=2, label=f'Median: {results["median2"]:.2f}')
        ax1.legend()
        
        # Violin plot untuk ranking
        rank_combined = pd.DataFrame({
            'Rank': np.concatenate([results['ranks_group1'], results['ranks_group2']]),
            'Kelompok': [group1_name]*len(results['ranks_group1']) + [group2_name]*len(results['ranks_group2'])
        })
        
        sns.violinplot(data=rank_combined, x='Kelompok', y='Rank', ax=ax2, 
                      palette=['mediumpurple', 'lightcoral'])
        sns.swarmplot(data=rank_combined, x='Kelompok', y='Rank', ax=ax2, 
                     color='black', alpha=0.4, size=3)
        ax2.set_title('Violin Plot - Ranking', fontsize=14, fontweight='bold')
        ax2.set_ylabel('Rank', fontsize=12)
        ax2.set_xlabel('Kelompok', fontsize=12)
        ax2.grid(True, alpha=0.3, axis='y')
        
        # Add mean rank lines
        ax2.hlines(results['mean_rank1'], -0.4, 0.4, colors='red', linestyles='--', 
                  linewidth=2, label=f'Mean Rank: {results["mean_rank1"]:.2f}')
        ax2.hlines(results['mean_rank2'], 0.6, 1.4, colors='red', linestyles='--', 
                  linewidth=2, label=f'Mean Rank: {results["mean_rank2"]:.2f}')
        ax2.legend()
        
        plt.tight_layout()
        st.pyplot(fig_violin)
        
        # Distribusi ranking dengan histogram
        st.subheader("Distribusi Ranking")
        fig_rank, ax_rank = plt.subplots(figsize=(12, 6))
        
        ax_rank.hist(results['ranks_group1'], bins=15, alpha=0.6, 
                    label=group1_name, color='mediumpurple', edgecolor='black')
        ax_rank.hist(results['ranks_group2'], bins=15, alpha=0.6, 
                    label=group2_name, color='lightcoral', edgecolor='black')
        
        ax_rank.axvline(results['mean_rank1'], color='purple', linestyle='--', 
                       linewidth=2, label=f'Mean Rank {group1_name}: {results["mean_rank1"]:.2f}')
        ax_rank.axvline(results['mean_rank2'], color='red', linestyle='--', 
                       linewidth=2, label=f'Mean Rank {group2_name}: {results["mean_rank2"]:.2f}')
        
        ax_rank.set_xlabel('Rank', fontsize=12)
        ax_rank.set_ylabel('Frekuensi', fontsize=12)
        ax_rank.set_title('Distribusi Ranking Kedua Kelompok', fontsize=14, fontweight='bold')
        ax_rank.legend()
        ax_rank.grid(True, alpha=0.3)
        
        st.pyplot(fig_rank)
        
        # Tabel data
        st.markdown("---")
        st.subheader("📋 Tabel Data Lengkap")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f"**{group1_name}**")
            df1 = pd.DataFrame({
                'Index': range(1, len(data1)+1),
                'Nilai': data1,
                'Rank': results['ranks_group1']
                })
            st.dataframe(df1, height=300)
            
            # Download button
            csv1 = df1.to_csv(index=False)
            st.download_button(
            label=f"📥 Download Data {group1_name}",
            data=csv1,
            file_name=f"{group1_name.replace(' ', '_')}.csv",
            mime="text/csv"
            )
        
        with col2:
            st.markdown(f"**{group2_name}**")
            df2 = pd.DataFrame({
            'Inex': range(1, len(data2)+1),
            'Nilai': data2,
            'Rank': results['ranks_group2']
            })
            st.dataframe(df2, height=300)
            
            # Download button
            csv2 = df2.to_csv(index=False)
            st.download_button(
            label=f"📥 Download Data {group2_name}",
            data=csv2,
            file_name=f"{group2_name.replace(' ', '_')}.csv",
            mime="text/csv"
            )
            
        # Ringkasan statistik detail
        st.markdown("---")
        st.subheader("📊 Ringkasan Statistik Detail")
        
        summary_df = pd.DataFrame({
                'Statistik': ['N', 'Mean', 'Median', 'Std Dev', 'Min', 'Q1', 'Q3', 'Max', 'IQR', 'Mean Rank', 'Sum Rank'],
                group1_name: [
                results['n1'],
                f"{results['mean1']:.4f}",
                f"{results['median1']:.4f}",
                f"{results['std1']:.4f}",
                f"{results['min1']:.4f}",
                f"{results['q1_1']:.4f}",
                f"{results['q3_1']:.4f}",
                f"{results['max1']:.4f}",
                f"{results['iqr1']:.4f}",
                f"{results['mean_rank1']:.4f}",
                f"{results['sum_ranks1']:.0f}"
            ],
                group2_name: [
                results['n2'],
                f"{results['mean2']:.4f}",
                f"{results['median2']:.4f}",
                f"{results['std2']:.4f}",
                f"{results['min2']:.4f}",
                f"{results['q1_2']:.4f}",
                f"{results['q3_2']:.4f}",
                f"{results['max2']:.4f}",
                f"{results['iqr2']:.4f}",
                f"{results['mean_rank2']:.4f}",
                f"{results['sum_ranks2']:.0f}"
                ]
        })
        
        st.dataframe(summary_df, use_container_width=True)
        
        # Interpretasi Effect Size
        st.markdown("---")
        st.subheader("🎯 Interpretasi Effect Size")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class="info-box">
            <h4>📏 Koefisien Korelasi (r)</h4>
            <p><strong>Nilai:</strong> {:.4f}</p>
            <p><strong>Interpretasi:</strong></p>
            <ul>
                <li>r < 0.1: Sangat kecil (negligible)</li>
                <li>0.1 ≤ r < 0.3: Kecil (small)</li>
                <li>0.3 ≤ r < 0.5: Sedang (medium)</li>
                <li>r ≥ 0.5: Besar (large)</li>
            </ul>
            <p><em>Effect size Anda: <strong>{}</strong></em></p>
            </div>
            """.format(abs(results['r_effect']), 
                      "Sangat Kecil" if abs(results['r_effect']) < 0.1 else
                      "Kecil" if abs(results['r_effect']) < 0.3 else
                      "Sedang" if abs(results['r_effect']) < 0.5 else "Besar"),
            unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="info-box">
            <h4>🎲 Common Language Effect Size (CLES)</h4>
            <p><strong>Nilai:</strong> {:.4f} ({:.1f}%)</p>
            <p><strong>Interpretasi:</strong></p>
            <p>Probabilitas bahwa nilai yang dipilih secara acak dari {} akan lebih besar dari nilai yang dipilih secara acak dari {}.</p>
            <p><em>Dengan kata lain, jika Anda memilih satu nilai dari {}, ada peluang {:.1f}% bahwa nilai tersebut akan lebih tinggi dari nilai acak dari {}.</em></p>
            </div>
            """.format(results['cles'], results['cles']*100, 
                      group1_name, group2_name,
                      group1_name, results['cles']*100, group2_name),
            unsafe_allow_html=True)
        
        # Laporan Lengkap
        st.markdown("---")
        st.subheader("📝 Laporan Hasil Analisis")
        
        report = f"""
        ### Laporan Uji U Mann-Whitney
        
        **Tanggal Analisis:** {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}
        
        #### 1. Deskripsi Data
        - **{group1_name}**: n = {results['n1']}, Median = {results['median1']:.4f}, IQR = {results['iqr1']:.4f}
        - **{group2_name}**: n = {results['n2']}, Median = {results['median2']:.4f}, IQR = {results['iqr2']:.4f}
        
        #### 2. Hipotesis
        - **H₀**: {h0}
        - **H₁**: {h1}
        
        #### 3. Hasil Uji Statistik
        - **Statistik U ({group1_name})**: {results['u_stat']:.4f}
        - **Statistik U ({group2_name})**: {results['u_stat2']:.4f}
        - **Z-score**: {results['z_score']:.4f}
        - **p-value**: {results['p_value']:.6f}
        - **Tingkat signifikansi (α)**: {alpha}
        
        #### 4. Effect Size
        - **Koefisien korelasi (r)**: {abs(results['r_effect']):.4f} ({
            "Sangat Kecil" if abs(results['r_effect']) < 0.1 else
            "Kecil" if abs(results['r_effect']) < 0.3 else
            "Sedang" if abs(results['r_effect']) < 0.5 else "Besar"
        })
        - **Rank-biserial correlation**: {results['rank_biserial']:.4f}
        - **CLES**: {results['cles']:.4f} ({results['cles']*100:.1f}%)
        
        #### 5. Kesimpulan
        {"**Tolak H₀**" if results['p_value'] < alpha else "**Gagal Tolak H₀**"}
        
        Dengan tingkat signifikansi α = {alpha}, {"terdapat" if results['p_value'] < alpha else "tidak terdapat"} 
        perbedaan yang signifikan antara distribusi {group1_name} dan {group2_name} 
        (U = {results['u_stat']:.4f}, p = {results['p_value']:.6f}).
        
        #### 6. Interpretasi
        {"Median kelompok " + group1_name + f" ({results['median1']:.2f}) " + 
         ("lebih besar" if results['median1'] > results['median2'] else "lebih kecil") + 
         " dibandingkan median kelompok " + group2_name + f" ({results['median2']:.2f}), " +
         ("dan perbedaan ini signifikan secara statistik." if results['p_value'] < alpha else 
          "namun perbedaan ini tidak signifikan secara statistik.")}
        
        Mean rank {group1_name} = {results['mean_rank1']:.2f}, sedangkan mean rank {group2_name} = {results['mean_rank2']:.2f}.
        
        ---
        *Catatan: Uji Mann-Whitney adalah uji non-parametrik yang cocok digunakan ketika asumsi normalitas tidak terpenuhi 
        atau untuk data ordinal.*
        """
        
        st.markdown(report)
        
        # Download report
        st.download_button(
        label="📥 Download Laporan (Markdown)",
        data=report,
        file_name="mann_whitney_report.md",
        mime="text/markdown"
        )
    # Footer
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 📚 Interpretasi Effect Size")
    st.sidebar.markdown("""
**Koefisien r:**
- r < 0.1: Sangat kecil
- 0.1 ≤ r < 0.3: Kecil
- 0.3 ≤ r < 0.5: Sedang
- r ≥ 0.5: Besar

**CLES:**
- 0.50: Tidak ada perbedaan
- 0.56: Kecil
- 0.64: Sedang
- 0.71: Besar
""")

    st.sidebar.markdown("### ⚡ Kelebihan Mann-Whitney")
    st.sidebar.success("""
✅ Tidak perlu asumsi normalitas
✅ Robust terhadap outlier
✅ Cocok untuk data ordinal
✅ Cocok untuk sampel kecil
""")

    st.sidebar.markdown("### ℹ️ Informasi")
    st.sidebar.info("Aplikasi ini menggunakan scipy.stats untuk perhitungan Mann-Whitney U test yang akurat dan terpercaya.")

def tampilkan_materi23():
    # CSS Styling
    st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        text-align: center;
        color: #D32F2F;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1.2rem;
        text-align: center;
        color: #666;
        margin-bottom: 2rem;
    }
    .result-box {
        background-color: #FFEBEE;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #D32F2F;
        margin: 1rem 0;
        color: black;
    }
    .hypothesis-box {
        background-color: #FFF3E0;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #FF9800;
        margin: 1rem 0;
        color: black;
    }
    .success-box {
        background-color: #E8F5E9;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #4CAF50;
        margin: 1rem 0;
        color: black;
    }
    .warning-box {
        background-color: #FFF9C4;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #FBC02D;
        margin: 1rem 0;
        color: black;
    }
    .info-box {
        background-color: #E3F2FD;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #2196F3;
        margin: 1rem 0;
        color: black;
    }
    .metric-card {
        background-color: #FAFAFA;
        padding: 1rem;
        border-radius: 8px;
        text-align: center;
        margin: 0.5rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        color: black;
    }
    .comparison-card {
        background-color: #F5F5F5;
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
        color: black;
    }
    </style>
    """, unsafe_allow_html=True)

    # Header
    st.markdown('<div class="main-header">📊 Simulasi Uji Welch\'s T-Test</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Welch\'s T-Test for Two Independent Samples with Unequal Variances</div>', unsafe_allow_html=True)

    # Sidebar
    st.sidebar.title("⚙️ Pengaturan")
    mode = st.sidebar.radio(
    "Pilih Mode:",
    ["📝 Input Data Manual", "🎲 Generate Data Simulasi", "📁 Upload Data CSV"]
    )

    st.sidebar.markdown("---")
    st.sidebar.markdown("### 📖 Tentang Welch's T-Test")
    st.sidebar.info("""
**Welch's T-Test** adalah modifikasi dari Student's t-test yang lebih robust ketika dua sampel memiliki varians yang tidak sama (heterogeneous variances).

**Kapan digunakan:**
- Varians kedua kelompok tidak sama
- Ukuran sampel berbeda
- Data berdistribusi normal atau mendekati normal
- Alternatif yang lebih aman dari t-test klasik

**Keunggulan:**
- Tidak perlu asumsi varians homogen
- Lebih akurat untuk varians berbeda
- Menggunakan Welch-Satterthwaite equation untuk df
""")

    # Fungsi untuk menghitung Welch's t-test
    def perform_welch_test(data1, data2, alpha, alternative):
        """Melakukan Welch's t-test dan mengembalikan hasil"""
        n1, n2 = len(data1), len(data2)
        mean1, mean2 = np.mean(data1), np.mean(data2)
        std1, std2 = np.std(data1, ddof=1), np.std(data2, ddof=1)
        var1, var2 = np.var(data1, ddof=1), np.var(data2, ddof=1)
        se1, se2 = std1/np.sqrt(n1), std2/np.sqrt(n2)
    
        # Statistik deskriptif tambahan
        median1, median2 = np.median(data1), np.median(data2)
        q1_1, q3_1 = np.percentile(data1, [25, 75])
        q1_2, q3_2 = np.percentile(data2, [25, 75])
        min1, max1 = np.min(data1), np.max(data1)
        min2, max2 = np.min(data2), np.max(data2)
    
        # Uji normalitas (Shapiro-Wilk)
        shapiro1_stat, shapiro1_p = stats.shapiro(data1)
        shapiro2_stat, shapiro2_p = stats.shapiro(data2)
    
        # Uji Levene untuk homogenitas varians
        levene_stat, levene_p = stats.levene(data1, data2)
    
        # Welch's t-test
        t_stat, p_value = stats.ttest_ind(data1, data2, equal_var=False, alternative=alternative)
    
        # Welch-Satterthwaite degrees of freedom
        df = ((var1/n1 + var2/n2)**2) / ((var1/n1)**2/(n1-1) + (var2/n2)**2/(n2-1))
    
        # Standard error of difference
        se_diff = np.sqrt(var1/n1 + var2/n2)
    
        # Confidence interval
        if alternative == 'two-sided':
            t_critical = stats.t.ppf(1-alpha/2, df)
            ci_lower = (mean1 - mean2) - t_critical * se_diff
            ci_upper = (mean1 - mean2) + t_critical * se_diff
        elif alternative == 'less':
            t_critical = stats.t.ppf(1-alpha, df)
            ci_lower = -np.inf
            ci_upper = (mean1 - mean2) + t_critical * se_diff
        else:  # greater
            t_critical = stats.t.ppf(1-alpha, df)
            ci_lower = (mean1 - mean2) - t_critical * se_diff
            ci_upper = np.inf
    
        # Effect size (Cohen's d dengan pooled std untuk varians berbeda)
        cohens_d = (mean1 - mean2) / np.sqrt((var1 + var2) / 2)
    
        # Glass's delta (menggunakan std kelompok kontrol)
        glass_delta1 = (mean1 - mean2) / std2
        glass_delta2 = (mean1 - mean2) / std1
    
        # Hedge's g (koreksi untuk sampel kecil)
        hedge_correction = 1 - (3 / (4 * (n1 + n2) - 9))
        hedges_g = cohens_d * hedge_correction
    
        # Perbandingan dengan Student's t-test (equal variance)
        t_stat_student, p_value_student = stats.ttest_ind(data1, data2, equal_var=True, alternative=alternative)
        df_student = n1 + n2 - 2
    
        return {
        'n1': n1, 'n2': n2,
        'mean1': mean1, 'mean2': mean2,
        'median1': median1, 'median2': median2,
        'std1': std1, 'std2': std2,
        'var1': var1, 'var2': var2,
        'se1': se1, 'se2': se2,
        'q1_1': q1_1, 'q3_1': q3_1,
        'q1_2': q1_2, 'q3_2': q3_2,
        'min1': min1, 'max1': max1,
        'min2': min2, 'max2': max2,
        't_stat': t_stat,
        'p_value': p_value,
        'df': df,
        'se_diff': se_diff,
        'cohens_d': cohens_d,
        'hedges_g': hedges_g,
        'glass_delta1': glass_delta1,
        'glass_delta2': glass_delta2,
        'ci_lower': ci_lower,
        'ci_upper': ci_upper,
        't_critical': t_critical,
        'levene_stat': levene_stat,
        'levene_p': levene_p,
        'shapiro1_stat': shapiro1_stat,
        'shapiro1_p': shapiro1_p,
        'shapiro2_stat': shapiro2_stat,
        'shapiro2_p': shapiro2_p,
        't_stat_student': t_stat_student,
        'p_value_student': p_value_student,
        'df_student': df_student
        }

    # Main content
    if mode == "📝 Input Data Manual":
        st.header("📝 Input Data Manual")
    
        col1, col2 = st.columns(2)
    
        with col1:
            st.subheader("Kelompok 1")
            data1_input = st.text_area(
            "Masukkan data kelompok 1 (pisahkan dengan koma):",
            "45, 52, 48, 55, 53, 50, 49, 51, 54, 47",
            height=100
            )
        
        with col2:
            st.subheader("Kelompok 2")
            data2_input = st.text_area(
            "Masukkan data kelompok 2 (pisahkan dengan koma):",
            "62, 68, 71, 65, 70, 64, 69, 67, 72, 66, 63, 74, 75, 68, 70",
            height=100
            )
    
        try:
            data1 = np.array([float(x.strip()) for x in data1_input.split(',')])
            data2 = np.array([float(x.strip()) for x in data2_input.split(',')])
            data_ready = True
        except:
            st.error("❌ Format data tidak valid. Gunakan angka yang dipisahkan dengan koma.")
            data_ready = False

    elif mode == "🎲 Generate Data Simulasi":
        st.header("🎲 Generate Data Simulasi")
    
        st.markdown("""
    <div class="info-box">
    💡 <strong>Tips:</strong> Coba buat dua kelompok dengan varians yang sangat berbeda untuk melihat keunggulan Welch's t-test!
    </div>
    """, unsafe_allow_html=True)
    
        col1, col2, col3 = st.columns(3)
    
        with col1:
            st.markdown("#### Kelompok 1")
            n1 = st.number_input("Ukuran sampel K1:", min_value=3, max_value=1000, value=30, key="n1")
            mean1 = st.number_input("Mean K1:", value=50.0, key="mean1")
            std1 = st.number_input("Std Dev K1:", min_value=0.1, value=5.0, key="std1")
        
        with col2:
            st.markdown("#### Kelompok 2")
            n2 = st.number_input("Ukuran sampel K2:", min_value=3, max_value=1000, value=40, key="n2")
            mean2 = st.number_input("Mean K2:", value=55.0, key="mean2")
            std2 = st.number_input("Std Dev K2:", min_value=0.1, value=15.0, key="std2")
    
        with col3:
            st.markdown("#### Pengaturan")
            seed = st.number_input("Random Seed:", min_value=0, value=42)
        
            # Visualisasi rasio varians
            variance_ratio = std1**2 / std2**2
            st.metric("Rasio Varians", f"{variance_ratio:.3f}")
        
            if variance_ratio < 0.5 or variance_ratio > 2:
                st.warning("⚠️ Varians sangat berbeda - Welch's t-test direkomendasikan!")
            else:
                st.info("ℹ️ Varians relatif mirip")
        
            st.markdown("###")
            if st.button("🎲 Generate Data", use_container_width=True):
                np.random.seed(seed)
                st.session_state.data1 = np.random.normal(mean1, std1, n1)
                st.session_state.data2 = np.random.normal(mean2, std2, n2)
                st.success("✅ Data berhasil di-generate!")
    
        if 'data1' in st.session_state and 'data2' in st.session_state:
            data1 = st.session_state.data1
            data2 = st.session_state.data2
            data_ready = True
        else:
            st.info("👆 Klik tombol 'Generate Data' untuk membuat data simulasi")
            data_ready = False

    else:  # Upload CSV
        st.header("📁 Upload Data CSV")
    
        st.markdown("""
    **Format CSV yang diharapkan:**
    - Kolom 1: Nilai data
    - Kolom 2: Label kelompok (misalnya: 'Kelompok1' dan 'Kelompok2')
    """)
    
        uploaded_file = st.file_uploader("Upload file CSV", type=['csv'])
    
        if uploaded_file is not None:
            try:
                df = pd.read_csv(uploaded_file)
                st.write("Preview Data:")
                st.dataframe(df.head())
            
                col1, col2 = st.columns(2)
                with col1:
                    value_col = st.selectbox("Pilih kolom nilai:", df.columns)
                with col2:
                    group_col = st.selectbox("Pilih kolom kelompok:", df.columns)
            
                groups = df[group_col].unique()
                if len(groups) != 2:
                    st.error("❌ Data harus memiliki tepat 2 kelompok!")
                    data_ready = False
                else:
                    group1_name = st.selectbox("Pilih kelompok 1:", groups)
                    group2_name = st.selectbox("Pilih kelompok 2:", [g for g in groups if g != group1_name])
                
                    data1 = df[df[group_col] == group1_name][value_col].values
                    data2 = df[df[group_col] == group2_name][value_col].values
                    data_ready = True
            except Exception as e:
                st.error(f"❌ Error membaca file: {str(e)}")
                data_ready = False
        else:
            data_ready = False

    # Jika data siap, lakukan analisis
    if data_ready:
        st.markdown("---")
        st.header("🔧 Pengaturan Uji Hipotesis")
    
        col1, col2, col3 = st.columns(3)
    
        with col1:
            alpha = st.select_slider(
            "Tingkat signifikansi (α):",
            options=[0.01, 0.05, 0.10],
            value=0.05
            )
    
        with col2:
            alternative = st.selectbox(
            "Hipotesis alternatif:",
            ["two-sided", "less", "greater"],
            format_func=lambda x: {
                "two-sided": "Dua sisi (≠)",
                "less": "Sisi kiri (<)",
                "greater": "Sisi kanan (>)"
            }[x]
            )
    
        with col3:
            group1_name = st.text_input("Nama Kelompok 1:", "Kelompok 1")
            group2_name = st.text_input("Nama Kelompok 2:", "Kelompok 2")
    
        # Hipotesis
        st.markdown("### 📋 Hipotesis")
        if alternative == "two-sided":
            h0 = f"H₀: μ₁ = μ₂ (Tidak ada perbedaan rata-rata)"
            h1 = f"H₁: μ₁ ≠ μ₂ (Ada perbedaan rata-rata)"
        elif alternative == "less":
            h0 = f"H₀: μ₁ ≥ μ₂"
            h1 = f"H₁: μ₁ < μ₂ (Rata-rata kelompok 1 lebih kecil)"
        else:
            h0 = f"H₀: μ₁ ≤ μ₂"
            h1 = f"H₁: μ₁ > μ₂ (Rata-rata kelompok 1 lebih besar)"
    
        st.markdown(f'<div class="hypothesis-box"><strong>{h0}</strong><br><strong>{h1}</strong></div>', 
                unsafe_allow_html=True)
    
        # Perform Welch's t-test
        if st.button("🚀 Jalankan Uji Welch's T-Test", use_container_width=True, type="primary"):
            results = perform_welch_test(data1, data2, alpha, alternative)
        
            st.markdown("---")
            st.header("📊 Hasil Analisis")
        
            # Statistik Deskriptif
            st.subheader("1️⃣ Statistik Deskriptif")
        
            col1, col2, col3, col4 = st.columns(4)
        
            with col1:
                st.markdown(f"""
            <div class="metric-card">
                <h4>{group1_name}</h4>
                <p><strong>n:</strong> {results['n1']}</p>
                <p><strong>Mean:</strong> {results['mean1']:.4f}</p>
                <p><strong>Std:</strong> {results['std1']:.4f}</p>
                <p><strong>Var:</strong> {results['var1']:.4f}</p>
                <p><strong>SE:</strong> {results['se1']:.4f}</p>
            </div>
            """, unsafe_allow_html=True)
        
            with col2:
                st.markdown(f"""
            <div class="metric-card">
                <h4>{group2_name}</h4>
                <p><strong>n:</strong> {results['n2']}</p>
                <p><strong>Mean:</strong> {results['mean2']:.4f}</p>
                <p><strong>Std:</strong> {results['std2']:.4f}</p>
                <p><strong>Var:</strong> {results['var2']:.4f}</p>
                <p><strong>SE:</strong> {results['se2']:.4f}</p>
            </div>
            """, unsafe_allow_html=True)
        
            with col3:
                variance_ratio = results['var1'] / results['var2']
                st.markdown(f"""
            <div class="metric-card">
                <h4>Perbandingan</h4>
                <p><strong>Δ Mean:</strong> {results['mean1']-results['mean2']:.4f}</p>
                <p><strong>SE Diff:</strong> {results['se_diff']:.4f}</p>
                <p><strong>Var Ratio:</strong> {variance_ratio:.4f}</p>
            </div>
            """, unsafe_allow_html=True)
        
            with col4:
                effect_size = abs(results['cohens_d'])
                if effect_size < 0.2:
                    effect_label = "Sangat Kecil"
                elif effect_size < 0.5:
                    effect_label = "Kecil"
                elif effect_size < 0.8:
                    effect_label = "Sedang"
                else:
                    effect_label = "Besar"
            
                st.markdown(f"""
            <div class="metric-card">
                <h4>Effect Size</h4>
                <p><strong>{effect_label}</strong></p>
                <p>Cohen's d = {effect_size:.4f}</p>
                <p>Hedge's g = {abs(results['hedges_g']):.4f}</p>
            </div>
            """, unsafe_allow_html=True)
        
            # Uji Asumsi
            st.subheader("2️⃣ Uji Asumsi")
        
            col1, col2 = st.columns(2)
        
            with col1:
                st.markdown("**Uji Normalitas (Shapiro-Wilk)**")
                if results['shapiro1_p'] > 0.05 and results['shapiro2_p'] > 0.05:
                    st.markdown(f"""
                <div class="success-box">
                ✅ Data berdistribusi normal<br>
                {group1_name}: W = {results['shapiro1_stat']:.4f}, p = {results['shapiro1_p']:.4f}<br>
                {group2_name}: W = {results['shapiro2_stat']:.4f}, p = {results['shapiro2_p']:.4f}
                </div>
                """, unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                <div class="warning-box">
                ⚠️ Data tidak berdistribusi normal<br>
                {group1_name}: W = {results['shapiro1_stat']:.4f}, p = {results['shapiro1_p']:.4f}<br>
                {group2_name}: W = {results['shapiro2_stat']:.4f}, p = {results['shapiro2_p']:.4f}<br>
                Pertimbangkan transformasi atau uji non-parametrik
                </div>
                """, unsafe_allow_html=True)
        
            with col2:
                st.markdown("**Uji Homogenitas Varians (Levene)**")
                variance_ratio = results['var1'] / results['var2']
                if results['levene_p'] > 0.05:
                    st.markdown(f"""
                <div class="success-box">
                ✅ Varians homogen<br>
                Levene statistic = {results['levene_stat']:.4f}<br>
                p-value = {results['levene_p']:.4f}<br>
                Variance ratio = {variance_ratio:.4f}
                </div>
                """, unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                <div class="info-box">
                ℹ️ Varians tidak homogen<br>
                Welch's t-test adalah pilihan yang TEPAT!<br>
                Levene statistic = {results['levene_stat']:.4f}<br>
                p-value = {results['levene_p']:.4f}<br>
                Variance ratio = {variance_ratio:.4f}
                </div>
                """, unsafe_allow_html=True)
        
            # Hasil Uji Welch's T-Test
            st.subheader("3️⃣ Hasil Uji Welch's T-Test")
        
            col1, col2 = st.columns(2)
        
            with col1:
                st.markdown(f"""
            <div class="result-box">
            <h4>Welch's T-Test Statistics</h4>
            <p><strong>t-statistic:</strong> {results['t_stat']:.4f}</p>
            <p><strong>Welch-Satterthwaite df:</strong> {results['df']:.2f}</p>
            <p><strong>p-value:</strong> {results['p_value']:.6f}</p>
            <p><strong>α:</strong> {alpha}</p>
            <p><strong>t-critical:</strong> ±{results['t_critical']:.4f}</p>
            </div>
            """, unsafe_allow_html=True)
        
            with col2:
                ci_level = int((1-alpha)*100)
                ci_text = f"{results['ci_lower']:.4f} to {results['ci_upper']:.4f}"
                if results['ci_lower'] == -np.inf:
                    ci_text = f"(-∞, {results['ci_upper']:.4f}]"
                elif results['ci_upper'] == np.inf:
                    ci_text = f"[{results['ci_lower']:.4f}, +∞)"
            
                st.markdown(f"""
            <div class="result-box">
            <h4>Confidence Interval ({ci_level}%)</h4>
            <p><strong>CI for (μ₁ - μ₂):</strong></p>
            <p>{ci_text}</p>
            <p><strong>Point estimate:</strong> {results['mean1']-results['mean2']:.4f}</p>
            <p><strong>Standard error:</strong> {results['se_diff']:.4f}</p>
            </div>
            """, unsafe_allow_html=True)
        
            # Perbandingan dengan Student's t-test
            st.subheader("4️⃣ Perbandingan: Welch's vs Student's T-Test")
        
            comparison_df = pd.DataFrame({
            'Metode': ["Welch's T-Test", "Student's T-Test"],
            'T-Statistic': [f"{results['t_stat']:.4f}", f"{results['t_stat_student']:.4f}"],
            'Degrees of Freedom': [f"{results['df']:.2f}", f"{results['df_student']:.0f}"],
            'P-Value': [f"{results['p_value']:.6f}", f"{results['p_value_student']:.6f}"],
            'Keputusan (α=0.05)': [
                "Tolak H₀" if results['p_value'] < 0.05 else "Gagal Tolak H₀",
                "Tolak H₀" if results['p_value_student'] < 0.05 else "Gagal Tolak H₀"
            ]
            })
        
            st.dataframe(comparison_df, use_container_width=True)
        
            # Analisis perbedaan
            diff_p = abs(results['p_value'] - results['p_value_student'])
            if diff_p > 0.01:
                st.markdown(f"""
            <div class="warning-box">
            ⚠️ <strong>Perbedaan Signifikan!</strong><br>
            Terdapat perbedaan p-value sebesar {diff_p:.6f} antara kedua metode.<br>
            Welch's t-test lebih tepat karena varians tidak homogen.
            </div>
            """, unsafe_allow_html=True)
            else:
                st.markdown("""
            <div class="info-box">
            ℹ️ Hasil kedua metode relatif sama, namun Welch's t-test tetap lebih robust.
            </div>
            """, unsafe_allow_html=True)
        
            # Kesimpulan
            st.subheader("5️⃣ Kesimpulan")
        
            if results['p_value'] < alpha:
                conclusion = f"""
            <div class="warning-box">
            <h4>🔴 Tolak H₀</h4>
            <p>Dengan tingkat signifikansi α = {alpha}, terdapat cukup bukti untuk menolak hipotesis nol.</p>
            <p><strong>Kesimpulan:</strong> Terdapat perbedaan yang signifikan antara rata-rata {group1_name} dan {group2_name}.</p>
            <p>p-value ({results['p_value']:.6f}) < α ({alpha})</p>
            <p><strong>Interpretasi:</strong> Mean {group1_name} ({results['mean1']:.2f}) {"lebih besar" if results['mean1'] > results['mean2'] else "lebih kecil"} dari mean {group2_name} ({results['mean2']:.2f}) secara signifikan.</p>
            <p><strong>Effect size:</strong> {effect_label} (Cohen's d = {abs(results['cohens_d']):.4f})</p>
            </div>
            """
            else:
                conclusion = f"""
            <div class="success-box">
            <h4>🟢 Gagal Tolak H₀</h4>
            <p>Dengan tingkat signifikansi α = {alpha}, tidak terdapat cukup bukti untuk menolak hipotesis nol.</p>
            <p><strong>Kesimpulan:</strong> Tidak terdapat perbedaan yang signifikan antara rata-rata {group1_name} dan {group2_name}.</p>
            <p>p-value ({results['p_value']:.6f}) ≥ α ({alpha})</p>
            <p><strong>Interpretasi:</strong> Mean {group1_name} ({results['mean1']:.2f}) tidak berbeda secara signifikan dari mean {group2_name} ({results['mean2']:.2f}).</p>
            </div>
            """
        
            st.markdown(conclusion, unsafe_allow_html=True)
        
            # Visualisasi
            st.markdown("---")
            st.header("📈 Visualisasi Data")
        
            # Create comprehensive plots
            fig = make_subplots(
            rows=2, cols=2,
            subplot_titles=('Box Plot Perbandingan', 'Distribusi Data', 
                          'Q-Q Plot Normalitas', 'Confidence Interval'),
            specs=[[{'type': 'box'}, {'type': 'histogram'}],
                   [{'type': 'scatter'}, {'type': 'scatter'}]]
            )
        
            # Box plot
            fig.add_trace(
            go.Box(y=data1, name=group1_name, marker_color='#EF5350', boxmean='sd'),
            row=1, col=1
            )
            fig.add_trace(
            go.Box(y=data2, name=group2_name, marker_color='#42A5F5', boxmean='sd'),
            row=1, col=1
            )
        
            # Histogram
            fig.add_trace(
            go.Histogram(x=data1, name=group1_name, opacity=0.7, 
                        marker_color='#EF5350', nbinsx=20),
            row=1, col=2
            )
            fig.add_trace(
            go.Histogram(x=data2, name=group2_name, opacity=0.7, 
                        marker_color='#42A5F5', nbinsx=20),
            row=1, col=2
            )
        
            # Q-Q Plot
            qq1 = stats.probplot(data1, dist="norm")
            qq2 = stats.probplot(data2, dist="norm")
        
            fig.add_trace(
            go.Scatter(x=qq1[0][0], y=qq1[0][1], mode='markers', 
                      name=f'{group1_name} Q-Q', marker=dict(color='#EF5350', size=6)),
            row=2, col=1
            )
            fig.add_trace(
            go.Scatter(x=qq2[0][0], y=qq2[0][1], mode='markers', 
                      name=f'{group2_name} Q-Q', marker=dict(color='#42A5F5', size=6)),
            row=2, col=1
            )
        
            # Reference line for Q-Q plot
            fig.add_trace(
            go.Scatter(x=qq1[0][0], y=qq1[1][1] + qq1[1][0]*qq1[0][0], 
                      mode='lines', name='Reference Line', 
                      line=dict(color='black', dash='dash')),
            row=2, col=1
            )
        
            # Confidence Interval visualization
            means = [results['mean1'], results['mean2']]
            errors = [results['se1'] * results['t_critical'], 
                 results['se2'] * results['t_critical']]
        
            fig.add_trace(
                go.Scatter(
                x=[group1_name, group2_name],
                y=means,
                error_y=dict(type='data', array=errors, visible=True),
                mode='markers',
                marker=dict(size=12, color=['#EF5350', '#42A5F5']),
                name='Mean ± CI'
                ),
                row=2, col=2
            )
        
            fig.update_layout(height=800, showlegend=True, 
                         title_text="Visualisasi Lengkap Welch's T-Test")
            fig.update_xaxes(title_text="Theoretical Quantiles", row=2, col=1)
            fig.update_yaxes(title_text="Sample Quantiles", row=2, col=1)
        
            st.plotly_chart(fig, use_container_width=True)
        
            # Violin plot dengan matplotlib
            st.subheader("Violin Plot & Distribution Comparison")
            fig_violin, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 10))
        
            # Violin plot untuk data asli
            data_combined = pd.DataFrame({
            'Nilai': np.concatenate([data1, data2]),
            'Kelompok': [group1_name]*len(data1) + [group2_name]*len(data2)
            })
        
            sns.violinplot(data=data_combined, x='Kelompok', y='Nilai', ax=ax1, 
                      palette=['#EF5350', '#42A5F5'])
            sns.swarmplot(data=data_combined, x='Kelompok', y='Nilai', ax=ax1, 
                     color='black', alpha=0.4, size=3)
            ax1.set_title('Violin Plot - Data Distribution', fontsize=13, fontweight='bold')
            ax1.set_ylabel('Nilai', fontsize=11)
            ax1.set_xlabel('Kelompok', fontsize=11)
            ax1.grid(True, alpha=0.3, axis='y')
        
            # Add mean and median lines
            ax1.hlines(results['mean1'], -0.4, 0.4, colors='red', linestyles='--', 
                  linewidth=2, label=f'Mean: {results["mean1"]:.2f}')
            ax1.hlines(results['median1'], -0.4, 0.4, colors='green', linestyles=':', 
                  linewidth=2, label=f'Median: {results["median1"]:.2f}')
            ax1.hlines(results['mean2'], 0.6, 1.4, colors='red', linestyles='--', 
                  linewidth=2)
            ax1.hlines(results['median2'], 0.6, 1.4, colors='green', linestyles=':', 
                  linewidth=2)
            ax1.legend(loc='best')
        
            # Density plot
            data1_kde = stats.gaussian_kde(data1)
            data2_kde = stats.gaussian_kde(data2)
            x_range = np.linspace(min(data1.min(), data2.min()), 
                             max(data1.max(), data2.max()), 200)
        
            ax2.fill_between(x_range, data1_kde(x_range), alpha=0.5, color='#EF5350', label=group1_name)
            ax2.fill_between(x_range, data2_kde(x_range), alpha=0.5, color='#42A5F5', label=group2_name)
            ax2.axvline(results['mean1'], color='#EF5350', linestyle='--', linewidth=2)
            ax2.axvline(results['mean2'], color='#42A5F5', linestyle='--', linewidth=2)
            ax2.set_title('Kernel Density Estimation', fontsize=13, fontweight='bold')
            ax2.set_xlabel('Nilai', fontsize=11)
            ax2.set_ylabel('Density', fontsize=11)
            ax2.legend()
            ax2.grid(True, alpha=0.3)
        
            # Strip plot dengan error bars
            ax3.errorbar([1], [results['mean1']], yerr=results['se1']*results['t_critical'],
                    fmt='o', markersize=10, color='#EF5350', capsize=10, capthick=2,
                    label=f'{group1_name} (Mean ± CI)')
            ax3.errorbar([2], [results['mean2']], yerr=results['se2']*results['t_critical'],
                    fmt='o', markersize=10, color='#42A5F5', capsize=10, capthick=2,
                    label=f'{group2_name} (Mean ± CI)')
        
            # Add data points
            ax3.scatter([1]*len(data1), data1, alpha=0.3, color='#EF5350', s=20)
            ax3.scatter([2]*len(data2), data2, alpha=0.3, color='#42A5F5', s=20)
        
            ax3.set_xlim(0.5, 2.5)
            ax3.set_xticks([1, 2])
            ax3.set_xticklabels([group1_name, group2_name])
            ax3.set_ylabel('Nilai', fontsize=11)
            ax3.set_title('Mean Comparison with Confidence Intervals', fontsize=13, fontweight='bold')
            ax3.legend()
            ax3.grid(True, alpha=0.3, axis='y')
        
            # Variance comparison
            variance_data = pd.DataFrame({
            'Kelompok': [group1_name, group2_name],
            'Variance': [results['var1'], results['var2']],
            'Std Dev': [results['std1'], results['std2']]
            })
        
            x_pos = np.arange(len(variance_data))
            ax4.bar(x_pos - 0.2, variance_data['Variance'], 0.4, 
               label='Variance', color='#FF7043', alpha=0.7)
            ax4.bar(x_pos + 0.2, variance_data['Std Dev'], 0.4, 
               label='Std Dev', color='#66BB6A', alpha=0.7)
        
            ax4.set_xticks(x_pos)
            ax4.set_xticklabels(variance_data['Kelompok'])
            ax4.set_ylabel('Value', fontsize=11)
            ax4.set_title('Variance & Standard Deviation Comparison', fontsize=13, fontweight='bold')
            ax4.legend()
            ax4.grid(True, alpha=0.3, axis='y')
        
            # Add variance ratio annotation
            var_ratio = results['var1'] / results['var2']
            ax4.text(0.5, max(results['var1'], results['var2']) * 0.9,
                f'Variance Ratio: {var_ratio:.3f}',
                ha='center', fontsize=10, 
                bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
        
            plt.tight_layout()
            st.pyplot(fig_violin)
        
            # T-distribution visualization
            st.subheader("T-Distribution & Critical Values")
        
            fig_t, ax_t = plt.subplots(figsize=(12, 6))
        
            # Generate t-distribution
            x = np.linspace(-5, 5, 1000)
            y = stats.t.pdf(x, results['df'])
        
            ax_t.plot(x, y, 'b-', linewidth=2, label=f't-distribution (df={results["df"]:.2f})')
            ax_t.fill_between(x, y, where=(x <= -results['t_critical']), 
                          alpha=0.3, color='red', label=f'Rejection region (α/2)')
            ax_t.fill_between(x, y, where=(x >= results['t_critical']), 
                          alpha=0.3, color='red')
        
            # Mark critical values
            ax_t.axvline(-results['t_critical'], color='red', linestyle='--', 
                    linewidth=2, label=f't-critical = ±{results["t_critical"]:.4f}')
            ax_t.axvline(results['t_critical'], color='red', linestyle='--', linewidth=2)
        
            # Mark observed t-statistic
            ax_t.axvline(results['t_stat'], color='green', linestyle='-', 
                    linewidth=3, label=f't-observed = {results["t_stat"]:.4f}')
        
            ax_t.set_xlabel('t-value', fontsize=12)
            ax_t.set_ylabel('Probability Density', fontsize=12)
            ax_t.set_title(f"T-Distribution with Welch-Satterthwaite df={results['df']:.2f}", 
                      fontsize=14, fontweight='bold')
            ax_t.legend(fontsize=10)
            ax_t.grid(True, alpha=0.3)
            
            # Add p-value annotation
            if abs(results['t_stat']) > results['t_critical']:
                color_box = 'lightcoral'
                decision = 'TOLAK H₀'
            else:
                color_box = 'lightgreen'
                decision = 'GAGAL TOLAK H₀'
        
            ax_t.text(0, max(y)*0.8, 
                 f'p-value = {results["p_value"]:.6f}\n{decision}',
                 ha='center', fontsize=12, fontweight='bold',
                 bbox=dict(boxstyle='round', facecolor=color_box, alpha=0.8))
        
            st.pyplot(fig_t)
        
            # Effect size visualization
            st.subheader("Effect Size Comparison")
        
            fig_effect, ax_effect = plt.subplots(figsize=(10, 6))
        
            effect_sizes = {
            "Cohen's d": abs(results['cohens_d']),
            "Hedge's g": abs(results['hedges_g']),
            "Glass's Δ₁": abs(results['glass_delta1']),
            "Glass's Δ₂": abs(results['glass_delta2'])
            }
        
            colors_map = {
            "Cohen's d": '#EF5350',
            "Hedge's g": '#AB47BC',
            "Glass's Δ₁": '#42A5F5',
            "Glass's Δ₂": '#66BB6A'
            }
        
            bars = ax_effect.barh(list(effect_sizes.keys()), list(effect_sizes.values()),
                             color=[colors_map[k] for k in effect_sizes.keys()], alpha=0.7)
        
            # Add effect size interpretation lines
            ax_effect.axvline(0.2, color='gray', linestyle='--', alpha=0.5, label='Small (0.2)')
            ax_effect.axvline(0.5, color='gray', linestyle='--', alpha=0.5, label='Medium (0.5)')
            ax_effect.axvline(0.8, color='gray', linestyle='--', alpha=0.5, label='Large (0.8)')
        
            # Add value labels
            for i, (key, value) in enumerate(effect_sizes.items()):
                ax_effect.text(value + 0.02, i, f'{value:.4f}', 
                          va='center', fontsize=10, fontweight='bold')
        
            ax_effect.set_xlabel('Effect Size Value', fontsize=12)
            ax_effect.set_title('Effect Size Metrics Comparison', fontsize=14, fontweight='bold')
            ax_effect.legend(loc='lower right')
            ax_effect.grid(True, alpha=0.3, axis='x')
        
            st.pyplot(fig_effect)
        
            # Tabel data
            st.markdown("---")
            st.subheader("📋 Tabel Data Lengkap")
        
            col1, col2 = st.columns(2)
        
            with col1:
                st.markdown(f"**{group1_name}**")
                df1 = pd.DataFrame({
                'Index': range(1, len(data1)+1),
                'Nilai': data1
                })
                df1['Z-Score'] = (df1['Nilai'] - results['mean1']) / results['std1']
                st.dataframe(df1, height=300)
            
                # Summary statistics
                st.markdown(f"""
            **Statistik:**
            - Mean: {results['mean1']:.4f}
            - Median: {results['median1']:.4f}
            - Std Dev: {results['std1']:.4f}
            - Variance: {results['var1']:.4f}
            - Min: {results['min1']:.4f}
            - Max: {results['max1']:.4f}
            """)
            
                # Download button
                csv1 = df1.to_csv(index=False)
                st.download_button(
                label=f"📥 Download Data {group1_name}",
                data=csv1,
                file_name=f"{group1_name.replace(' ', '_')}.csv",
                mime="text/csv"
                )
        
            with col2:
                st.markdown(f"**{group2_name}**")
                df2 = pd.DataFrame({
                'Index': range(1, len(data2)+1),
                'Nilai': data2
            })
                df2['Z-Score'] = (df2['Nilai'] - results['mean2']) / results['std2']
                st.dataframe(df2, height=300)
            
                # Summary statistics
                st.markdown(f"""
            **Statistik:**
            - Mean: {results['mean2']:.4f}
            - Median: {results['median2']:.4f}
            - Std Dev: {results['std2']:.4f}
            - Variance: {results['var2']:.4f}
            - Min: {results['min2']:.4f}
            - Max: {results['max2']:.4f}
            """)
            
                # Download button
                csv2 = df2.to_csv(index=False)
                st.download_button(
                label=f"📥 Download Data {group2_name}",
                data=csv2,
                file_name=f"{group2_name.replace(' ', '_')}.csv",
                mime="text/csv"
                )
        
            # Ringkasan statistik detail
            st.markdown("---")
            st.subheader("📊 Ringkasan Statistik Detail")
        
            summary_df = pd.DataFrame({
            'Statistik': ['N', 'Mean', 'Median', 'Std Dev', 'Variance', 'SE', 
                         'Min', 'Q1', 'Q3', 'Max', 'Range', 'IQR'],
                group1_name: [
                results['n1'],
                f"{results['mean1']:.4f}",
                f"{results['median1']:.4f}",
                f"{results['std1']:.4f}",
                f"{results['var1']:.4f}",
                f"{results['se1']:.4f}",
                f"{results['min1']:.4f}",
                f"{results['q1_1']:.4f}",
                f"{results['q3_1']:.4f}",
                f"{results['max1']:.4f}",
                f"{results['max1'] - results['min1']:.4f}",
                f"{results['q3_1'] - results['q1_1']:.4f}"
                ],
                group2_name: [
                results['n2'],
                f"{results['mean2']:.4f}",
                f"{results['median2']:.4f}",
                f"{results['std2']:.4f}",
                f"{results['var2']:.4f}",
                f"{results['se2']:.4f}",
                f"{results['min2']:.4f}",
                f"{results['q1_2']:.4f}",
                f"{results['q3_2']:.4f}",
                f"{results['max2']:.4f}",
                f"{results['max2'] - results['min2']:.4f}",
                f"{results['q3_2'] - results['q1_2']:.4f}"
                ]
            })
        
            st.dataframe(summary_df, use_container_width=True)
        
            # Interpretasi Effect Size
            st.markdown("---")
            st.subheader("🎯 Interpretasi Effect Size")
        
            col1, col2 = st.columns(2)
        
            with col1:
                st.markdown(f"""
            <div class="info-box">
            <h4>📏 Cohen's d</h4>
            <p><strong>Nilai:</strong> {abs(results['cohens_d']):.4f}</p>
            <p><strong>Interpretasi:</strong></p>
            <ul>
                <li>|d| < 0.2: Sangat kecil (negligible)</li>
                <li>0.2 ≤ |d| < 0.5: Kecil (small)</li>
                <li>0.5 ≤ |d| < 0.8: Sedang (medium)</li>
                <li>|d| ≥ 0.8: Besar (large)</li>
            </ul>
            <p><em>Effect size Anda: <strong>{effect_label}</strong></em></p>
            <p>Menggunakan pooled standard deviation untuk varians berbeda.</p>
            </div>
            """, unsafe_allow_html=True)
        
            with col2:
                st.markdown(f"""
            <div class="info-box">
            <h4>📐 Hedge's g</h4>
            <p><strong>Nilai:</strong> {abs(results['hedges_g']):.4f}</p>
            <p><strong>Interpretasi:</strong></p>
            <p>Hedge's g adalah koreksi bias dari Cohen's d untuk sampel kecil (n < 20).</p>
            <p>Nilai ini lebih akurat untuk sampel kecil dan menggunakan correction factor:</p>
            <p><em>g = d × (1 - 3/(4N - 9))</em></p>
            <p>Interpretasi sama dengan Cohen's d.</p>
            </div>
            """, unsafe_allow_html=True)
        
            # Laporan Lengkap
            st.markdown("---")
            st.subheader("📝 Laporan Hasil Analisis")
        
            ci_text = f"[{results['ci_lower']:.4f}, {results['ci_upper']:.4f}]"
            if results['ci_lower'] == -np.inf:
                ci_text = f"(-∞, {results['ci_upper']:.4f}]"
            elif results['ci_upper'] == np.inf:
                ci_text = f"[{results['ci_lower']:.4f}, +∞)"
        
            report = f"""
        ### Laporan Uji Welch's T-Test
        
        **Tanggal Analisis:** {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}
        
        #### 1. Deskripsi Data
        - **{group1_name}**: n = {results['n1']}, Mean = {results['mean1']:.4f}, SD = {results['std1']:.4f}, Var = {results['var1']:.4f}
        - **{group2_name}**: n = {results['n2']}, Mean = {results['mean2']:.4f}, SD = {results['std2']:.4f}, Var = {results['var2']:.4f}
        - **Variance Ratio**: {results['var1'] / results['var2']:.4f}
        
        #### 2. Hipotesis
        - **H₀**: {h0}
        - **H₁**: {h1}
        
        #### 3. Uji Asumsi
        
        **Normalitas (Shapiro-Wilk Test):**
        - {group1_name}: W = {results['shapiro1_stat']:.4f}, p = {results['shapiro1_p']:.4f} {"(Normal ✓)" if results['shapiro1_p'] > 0.05 else "(Tidak Normal ✗)"}
        - {group2_name}: W = {results['shapiro2_stat']:.4f}, p = {results['shapiro2_p']:.4f} {"(Normal ✓)" if results['shapiro2_p'] > 0.05 else "(Tidak Normal ✗)"}
        
        **Homogenitas Varians (Levene Test):**
        - Levene Statistic = {results['levene_stat']:.4f}, p = {results['levene_p']:.4f}
        - Kesimpulan: Varians {"homogen" if results['levene_p'] > 0.05 else "TIDAK homogen - Welch's t-test TEPAT digunakan!"}
        
        #### 4. Hasil Uji Welch's T-Test
        - **T-statistic (Welch)**: {results['t_stat']:.4f}
        - **Degrees of Freedom (Welch-Satterthwaite)**: {results['df']:.2f}
        - **p-value**: {results['p_value']:.6f}
        - **Tingkat signifikansi (α)**: {alpha}
        - **T-critical**: ±{results['t_critical']:.4f}
        - **Confidence Interval ({int((1-alpha)*100)}%)**: {ci_text}
        
        #### 5. Perbandingan dengan Student's T-Test
        - **Student's t-statistic**: {results['t_stat_student']:.4f}
        - **Student's df**: {results['df_student']:.0f}
        - **Student's p-value**: {results['p_value_student']:.6f}
        - **Perbedaan p-value**: {abs(results['p_value'] - results['p_value_student']):.6f}
        
        #### 6. Effect Size
        - **Cohen's d**: {abs(results['cohens_d']):.4f} ({effect_label})
        - **Hedge's g**: {abs(results['hedges_g']):.4f}
        - **Glass's Delta (menggunakan SD K1)**: {abs(results['glass_delta2']):.4f}
        - **Glass's Delta (menggunakan SD K2)**: {abs(results['glass_delta1']):.4f}
        
        #### 7. Kesimpulan
        {"**TOLAK H₀**" if results['p_value'] < alpha else "**GAGAL TOLAK H₀**"}
        
        Dengan tingkat signifikansi α = {alpha}, {"terdapat" if results['p_value'] < alpha else "tidak terdapat"} 
        perbedaan yang signifikan antara rata-rata {group1_name} dan {group2_name} 
        (Welch's t({results['df']:.2f}) = {results['t_stat']:.4f}, p = {results['p_value']:.6f}).
        
        #### 8. Interpretasi Praktis
        Mean {group1_name} ({results['mean1']:.2f}) {"lebih besar" if results['mean1'] > results['mean2'] else "lebih kecil"} 
        dari mean {group2_name} ({results['mean2']:.2f}) dengan selisih {abs(results['mean1'] - results['mean2']):.2f} unit.
        
        {"Perbedaan ini signifikan secara statistik" if results['p_value'] < alpha else "Perbedaan ini tidak signifikan secara statistik"} 
        dengan effect size {effect_label.lower()} (Cohen's d = {abs(results['cohens_d']):.4f}).
        
        {f"Confidence interval {int((1-alpha)*100)}% untuk perbedaan mean adalah {ci_text}, " +
         ("yang tidak mencakup 0, mengonfirmasi perbedaan signifikan." if (results['ci_lower'] > 0 or results['ci_upper'] < 0) and results['p_value'] < alpha 
          else "yang mencakup 0, mengindikasikan perbedaan tidak signifikan.")}
        
        #### 9. Rekomendasi
        {"Karena varians kedua kelompok tidak homogen" if results['levene_p'] < 0.05 else "Meskipun varians homogen"}, 
        Welch's t-test memberikan hasil yang lebih robust dan direkomendasikan untuk analisis ini.
        
        ---
        *Catatan: Welch's t-test menggunakan Welch-Satterthwaite equation untuk menghitung degrees of freedom yang 
        disesuaikan dengan perbedaan varians, sehingga lebih akurat ketika asumsi homogenitas varians tidak terpenuhi.*
        """
        
            st.markdown(report)
        
            # Download report
            st.download_button(
            label="📥 Download Laporan (Markdown)",
            data=report,
            file_name="welch_t_test_report.md",
            mime="text/markdown"
            )

    # Footer
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 📚 Interpretasi Effect Size")
    st.sidebar.markdown("""
**Cohen's d / Hedge's g:**
- |d| < 0.2: Sangat kecil
- 0.2 ≤ |d| < 0.5: Kecil
- 0.5 ≤ |d| < 0.8: Sedang
- |d| ≥ 0.8: Besar

**Variance Ratio:**
- 0.5 < ratio < 2: Relatif sama
- ratio < 0.5 atau > 2: Sangat berbeda
  → Gunakan Welch's t-test!
""")

    st.sidebar.markdown("### ⚡ Keunggulan Welch's T-Test")
    st.sidebar.success("""
✅ Tidak perlu varians homogen
✅ Robust untuk varians berbeda
✅ Akurat untuk n berbeda
✅ Lebih aman dari Student's t-test
✅ Menggunakan adjusted df
""")

    st.sidebar.markdown("### 🆚 Welch vs Student")
    st.sidebar.info("""
**Gunakan Welch's t-test jika:**
- Varians tidak sama (Levene p < 0.05)
- Ukuran sampel berbeda
- Tidak yakin tentang homogenitas
- Ingin hasil lebih robust

**Student's t-test hanya jika:**
- Varians benar-benar homogen
- Sampel seimbang
- Asumsi terpenuhi sempurna
""")

    st.sidebar.markdown("### ℹ️ Informasi")
    st.sidebar.info("Aplikasi ini menggunakan scipy.stats untuk Welch's t-test yang akurat dengan Welch-Satterthwaite degrees of freedom.")

def tampilkan_materi24():
    # Judul aplikasi
    st.title("📊 ANOVA 1 Jalur (One-Way ANOVA)")
    st.markdown("### Pembelajaran dan Simulasi Interaktif")

    # Sidebar untuk navigasi
    menu = st.sidebar.radio(
        "Pilih Menu:",
        ["📚 Materi", "🧮 Simulasi Manual", "📈 Simulasi Data"]
    )

    # ============ MENU MATERI ============
    if menu == "📚 Materi":
        st.header("📚 Materi ANOVA 1 Jalur")
    
        tab1, tab2, tab3, tab4 = st.tabs(["Pengertian", "Asumsi", "Hipotesis", "Rumus"])
    
        with tab1:
            st.subheader("Apa itu ANOVA 1 Jalur?")
            st.markdown("""
        **ANOVA (Analysis of Variance) 1 Jalur** adalah uji statistik parametrik yang digunakan untuk 
        membandingkan rata-rata dari **tiga kelompok atau lebih** untuk mengetahui apakah terdapat 
        perbedaan yang signifikan di antara kelompok-kelompok tersebut.
        
        **Contoh Kasus:**
        - Membandingkan efektivitas 3 metode pembelajaran yang berbeda
        - Membandingkan produktivitas karyawan dari 4 divisi berbeda
        - Membandingkan hasil panen dari 5 jenis pupuk berbeda
        
        **Mengapa disebut "1 Jalur"?**
        Karena hanya ada **satu variabel independen (faktor)** yang memiliki beberapa level/kategori.
        """)
    
        with tab2:
            st.subheader("Asumsi ANOVA 1 Jalur")
            st.markdown("""
        Sebelum melakukan ANOVA, data harus memenuhi asumsi berikut:
        
        1. **Independensi**: Observasi dalam setiap kelompok harus independen
        2. **Normalitas**: Data dalam setiap kelompok berdistribusi normal
        3. **Homogenitas Varians**: Varians antar kelompok harus homogen (sama)
        
        **Uji Asumsi:**
        - **Normalitas**: Uji Shapiro-Wilk atau Kolmogorov-Smirnov
        - **Homogenitas**: Uji Levene atau Bartlett
        """)
    
        with tab3:
            st.subheader("Hipotesis ANOVA")
            st.markdown("""
        **H₀ (Hipotesis Nol):**
        
        Tidak ada perbedaan rata-rata yang signifikan antar semua kelompok
        
        μ₁ = μ₂ = μ₃ = ... = μₖ
        
        **H₁ (Hipotesis Alternatif):**
        
        Minimal ada satu kelompok yang rata-ratanya berbeda signifikan
        
        **Keputusan:**
        - Jika **p-value < α** (biasanya 0.05), maka **Tolak H₀**
        - Jika **p-value ≥ α**, maka **Gagal Tolak H₀**
        """)
    
        with tab4:
            st.subheader("Rumus ANOVA 1 Jalur")
            st.markdown("""
        **1. Total Sum of Squares (SST)**
        
        SST = Σ(Xᵢⱼ - X̄)²
        
        **2. Between-Group Sum of Squares (SSB)**
        
        SSB = Σnⱼ(X̄ⱼ - X̄)²
        
        **3. Within-Group Sum of Squares (SSW)**
        
        SSW = SST - SSB
        
        **4. F-Statistik**
        
        F = (SSB / dfB) / (SSW / dfW)
        
        Dimana:
        - dfB = k - 1 (derajat bebas between)
        - dfW = N - k (derajat bebas within)
        - k = jumlah kelompok
        - N = total observasi
        """)
        
            st.info("💡 **Tips**: F-statistik yang besar menunjukkan variasi antar kelompok lebih besar dibanding variasi dalam kelompok")

    # ============ MENU SIMULASI MANUAL ============
    elif menu == "🧮 Simulasi Manual":
        st.header("🧮 Simulasi Manual - Input Data Sendiri")
    
        st.markdown("Masukkan data untuk setiap kelompok (pisahkan dengan koma)")
    
        col1, col2 = st.columns(2)
    
        with col1:
            num_groups = st.number_input("Jumlah Kelompok", min_value=2, max_value=10, value=3)
            alpha = st.number_input("Tingkat Signifikansi (α)", min_value=0.01, max_value=0.10, value=0.05, step=0.01)
    
        # Input data untuk setiap kelompok
        groups_data = {}
        group_names = []
    
        st.markdown("---")
        st.subheader("Input Data Kelompok")
    
        cols = st.columns(min(3, num_groups))
    
        for i in range(num_groups):
            with cols[i % 3]:
                group_name = st.text_input(f"Nama Kelompok {i+1}", value=f"Kelompok {i+1}", key=f"name_{i}")
                group_names.append(group_name)
            
                data_input = st.text_area(
                    f"Data {group_name}",
                    value="10, 12, 11, 13, 12" if i == 0 else f"{15+i*5}, {16+i*5}, {14+i*5}, {17+i*5}, {15+i*5}",
                    key=f"data_{i}",
                    height=100
                )
            
                try:
                    data = [float(x.strip()) for x in data_input.split(",") if x.strip()]
                    groups_data[group_name] = data
                except:
                    st.error(f"Format data tidak valid untuk {group_name}")
    
        if st.button("🔍 Analisis ANOVA", type="primary"):
            if len(groups_data) >= 2 and all(len(v) >= 2 for v in groups_data.values()):
                # Persiapan data
                all_data = []
                group_labels = []
                for name, data in groups_data.items():
                    all_data.extend(data)
                    group_labels.extend([name] * len(data))
            
                df = pd.DataFrame({'Nilai': all_data, 'Kelompok': group_labels})
            
                # ANOVA
                groups = [groups_data[name] for name in group_names]
                f_stat, p_value = stats.f_oneway(*groups)
            
                # Hasil
                st.markdown("---")
                st.subheader("📊 Hasil Analisis")
            
                col1, col2, col3 = st.columns(3)
                col1.metric("F-Statistik", f"{f_stat:.4f}")
                col2.metric("P-Value", f"{p_value:.4f}")
                col3.metric("Keputusan", "Tolak H₀" if p_value < alpha else "Gagal Tolak H₀")
            
                # Interpretasi
                st.markdown("### 📝 Interpretasi")
                if p_value < alpha:
                    st.success(f"""
                    ✅ **Kesimpulan**: Dengan tingkat signifikansi {alpha}, terdapat perbedaan rata-rata 
                    yang signifikan antar kelompok (p-value = {p_value:.4f} < {alpha}).
                    """)
                else:
                    st.info(f"""
                ℹ️ **Kesimpulan**: Dengan tingkat signifikansi {alpha}, tidak terdapat perbedaan rata-rata 
                yang signifikan antar kelompok (p-value = {p_value:.4f} ≥ {alpha}).
                    """)
            
                # Statistik Deskriptif
                st.markdown("### 📈 Statistik Deskriptif")
                desc_stats = df.groupby('Kelompok')['Nilai'].agg(['count', 'mean', 'std', 'min', 'max']).round(3)
                desc_stats.columns = ['N', 'Mean', 'Std Dev', 'Min', 'Max']
                st.dataframe(desc_stats, use_container_width=True)
            
                # Visualisasi
                col1, col2 = st.columns(2)
            
                with col1:
                    # Box plot
                    fig_box = px.box(df, x='Kelompok', y='Nilai', title='Box Plot per Kelompok',
                                color='Kelompok', points='all')
                    fig_box.update_layout(showlegend=False)
                    st.plotly_chart(fig_box, use_container_width=True)
            
                with col2:
                    # Bar plot mean
                    mean_data = df.groupby('Kelompok')['Nilai'].mean().reset_index()
                    fig_bar = px.bar(mean_data, x='Kelompok', y='Nilai', title='Rata-rata per Kelompok',
                                color='Kelompok')
                    fig_bar.update_layout(showlegend=False)
                    st.plotly_chart(fig_bar, use_container_width=True)
            
                # Tabel ANOVA
                st.markdown("### 📋 Tabel ANOVA")
                k = len(groups)
                N = sum(len(g) for g in groups)
                grand_mean = np.mean(all_data)
            
                # SSB
                ssb = sum(len(g) * (np.mean(g) - grand_mean)**2 for g in groups)
                # SSW
                ssw = sum(sum((x - np.mean(g))**2 for x in g) for g in groups)
                # SST
                sst = ssb + ssw
            
                dfb = k - 1
                dfw = N - k
                dft = N - 1
            
                msb = ssb / dfb
                msw = ssw / dfw
            
                anova_table = pd.DataFrame({
                'Sumber Variasi': ['Between Groups', 'Within Groups', 'Total'],
                'SS': [f"{ssb:.4f}", f"{ssw:.4f}", f"{sst:.4f}"],
                'df': [dfb, dfw, dft],
                'MS': [f"{msb:.4f}", f"{msw:.4f}", "-"],
                'F': [f"{f_stat:.4f}", "-", "-"],
                'P-value': [f"{p_value:.4f}", "-", "-"]
                })
                st.dataframe(anova_table, use_container_width=True, hide_index=True)
            
            else:
                st.error("⚠️ Setiap kelompok harus memiliki minimal 2 data!")

    # ============ MENU SIMULASI DATA ============
    else:
        st.header("📈 Simulasi Data - Generate Data Random")
    
        st.markdown("Generate data random untuk simulasi ANOVA")
    
        col1, col2, col3 = st.columns(3)
    
        with col1:
            num_groups_sim = st.slider("Jumlah Kelompok", 2, 6, 3)
            samples_per_group = st.slider("Sampel per Kelompok", 10, 100, 30)
    
        with col2:
            mean_start = st.number_input("Mean Awal", value=50.0, step=1.0)
            mean_diff = st.number_input("Perbedaan Mean antar Kelompok", value=5.0, step=1.0)
    
        with col3:
            std_dev = st.number_input("Standar Deviasi", value=10.0, step=1.0)
            alpha_sim = st.selectbox("Tingkat Signifikansi (α)", [0.01, 0.05, 0.10], index=1)
    
        if st.button("🎲 Generate & Analisis", type="primary"):
            # Generate data
            np.random.seed(42)
            groups_sim = []
            group_names_sim = []
        
            all_data_sim = []
            all_labels_sim = []
        
            for i in range(num_groups_sim):
                mean = mean_start + (i * mean_diff)
                data = np.random.normal(mean, std_dev, samples_per_group)
                groups_sim.append(data)
                group_name = f"Kelompok {i+1}"
                group_names_sim.append(group_name)
                all_data_sim.extend(data)
                all_labels_sim.extend([group_name] * samples_per_group)
        
            df_sim = pd.DataFrame({'Nilai': all_data_sim, 'Kelompok': all_labels_sim})
        
            # ANOVA
            f_stat_sim, p_value_sim = stats.f_oneway(*groups_sim)
        
            # Hasil
            st.markdown("---")
            st.subheader("📊 Hasil Simulasi")
        
            col1, col2, col3 = st.columns(3)
            col1.metric("F-Statistik", f"{f_stat_sim:.4f}")
            col2.metric("P-Value", f"{p_value_sim:.6f}")
            col3.metric("Keputusan", "Tolak H₀" if p_value_sim < alpha_sim else "Gagal Tolak H₀")
        
            # Interpretasi
            st.markdown("### 📝 Interpretasi")
            if p_value_sim < alpha_sim:
                st.success(f"""
            ✅ **Kesimpulan**: Dengan tingkat signifikansi {alpha_sim}, terdapat perbedaan rata-rata 
            yang signifikan antar kelompok (p-value = {p_value_sim:.6f} < {alpha_sim}).
            
            Artinya, minimal ada satu kelompok yang memiliki rata-rata berbeda secara signifikan.
            """)
            else:
                st.info(f"""
            ℹ️ **Kesimpulan**: Dengan tingkat signifikansi {alpha_sim}, tidak terdapat perbedaan rata-rata 
            yang signifikan antar kelompok (p-value = {p_value_sim:.6f} ≥ {alpha_sim}).
            
            Artinya, semua kelompok memiliki rata-rata yang tidak berbeda secara statistik.
            """)
        
            # Statistik Deskriptif
            st.markdown("### 📈 Statistik Deskriptif")
            desc_stats_sim = df_sim.groupby('Kelompok')['Nilai'].agg(['count', 'mean', 'std', 'min', 'max']).round(3)
            desc_stats_sim.columns = ['N', 'Mean', 'Std Dev', 'Min', 'Max']
            st.dataframe(desc_stats_sim, use_container_width=True)
        
            # Visualisasi
            tab1, tab2, tab3 = st.tabs(["📦 Box Plot", "📊 Bar Chart", "📈 Violin Plot"])
        
            with tab1:
                fig_box_sim = px.box(df_sim, x='Kelompok', y='Nilai', 
                                title='Distribusi Data per Kelompok',
                                color='Kelompok', points='all')
                fig_box_sim.update_layout(showlegend=False, height=500)
                st.plotly_chart(fig_box_sim, use_container_width=True)
        
            with tab2:
                mean_data_sim = df_sim.groupby('Kelompok')['Nilai'].mean().reset_index()
                std_data_sim = df_sim.groupby('Kelompok')['Nilai'].std().reset_index()
                mean_data_sim['std'] = std_data_sim['Nilai']
            
                fig_bar_sim = go.Figure()
                fig_bar_sim.add_trace(go.Bar(
                    x=mean_data_sim['Kelompok'],
                    y=mean_data_sim['Nilai'],
                    error_y=dict(type='data', array=mean_data_sim['std']),
                    marker_color='lightblue'
                ))
                fig_bar_sim.update_layout(title='Rata-rata ± Std Dev per Kelompok',
                                     xaxis_title='Kelompok',
                                     yaxis_title='Nilai',
                                     height=500)
                st.plotly_chart(fig_bar_sim, use_container_width=True)
        
            with tab3:
                fig_violin = px.violin(df_sim, x='Kelompok', y='Nilai', 
                                  title='Violin Plot per Kelompok',
                                  color='Kelompok', box=True, points='all')
                fig_violin.update_layout(showlegend=False, height=500)
                st.plotly_chart(fig_violin, use_container_width=True)
        
            # Download data
            st.markdown("### 💾 Download Data")
            csv = df_sim.to_csv(index=False)
            st.download_button(
                label="📥 Download Data CSV",
                data=csv,
                file_name="data_anova_simulasi.csv",
                mime="text/csv"
            )

    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: gray;'>
        <p>📚 Aplikasi Pembelajaran ANOVA 1 Jalur | Dibuat dengan Streamlit</p>
    </div>
    """, unsafe_allow_html=True)

def tampilkan_materi25():
    # Judul aplikasi
    st.title("📊 Uji Kruskal-Wallis")
    st.markdown("### Uji Non-Parametrik untuk Lebih dari 2 Sampel Independen")

    # Sidebar untuk navigasi
    menu = st.sidebar.radio(
    "Pilih Menu:",
    ["📚 Materi", "🧮 Simulasi Manual", "📈 Simulasi Data", "🔬 Uji Asumsi"]
    )

    # ============ MENU MATERI ============
    if menu == "📚 Materi":
        st.header("📚 Materi Uji Kruskal-Wallis")
    
        tab1, tab2, tab3, tab4, tab5 = st.tabs(["Pengertian", "Kapan Digunakan", "Asumsi", "Hipotesis", "Rumus"])
    
        with tab1:
            st.subheader("Apa itu Uji Kruskal-Wallis?")
            st.markdown("""
        **Uji Kruskal-Wallis** adalah uji statistik **non-parametrik** yang digunakan untuk 
        membandingkan **tiga kelompok atau lebih** yang independen ketika data **tidak memenuhi 
        asumsi normalitas**.
        
        **Karakteristik:**
        - 🔹 Alternatif non-parametrik untuk ANOVA 1 jalur
        - 🔹 Tidak memerlukan asumsi normalitas data
        - 🔹 Menggunakan **ranking/peringkat** data, bukan nilai asli
        - 🔹 Lebih robust terhadap outliers
        
        **Contoh Kasus:**
        - Membandingkan kepuasan pelanggan dari 3 cabang toko (data ordinal/tidak normal)
        - Membandingkan skor nyeri pasien dengan 4 jenis obat yang berbeda
        - Membandingkan produktivitas dari 5 shift kerja dengan data yang skewed
        """)
        
            st.info("💡 **Catatan**: Jika data berdistribusi normal, lebih baik gunakan ANOVA karena lebih powerful")
    
        with tab2:
            st.subheader("Kapan Menggunakan Uji Kruskal-Wallis?")
        
            col1, col2 = st.columns(2)
        
            with col1:
                st.markdown("""
            ### ✅ Gunakan Kruskal-Wallis Jika:
            
            1. **Data tidak berdistribusi normal**
               - Hasil uji normalitas menunjukkan p < 0.05
               
            2. **Data ordinal (skala likert)**
               - Sangat tidak setuju - Sangat setuju
               - Rendah - Sedang - Tinggi
               
            3. **Ada outliers ekstrem**
               - Data memiliki nilai ekstrem yang berpengaruh
               
            4. **Sampel kecil (n < 30 per kelompok)**
               - Dan tidak dapat diasumsikan normal
               
            5. **Varians tidak homogen**
               - Meskipun Kruskal-Wallis tidak terlalu sensitif
            """)
        
            with col2:
                st.markdown("""
            ### ❌ Gunakan ANOVA Jika:
            
            1. **Data berdistribusi normal**
               - Uji Shapiro-Wilk p > 0.05
               
            2. **Data numerik kontinu**
               - Pengukuran yang presisi
               
            3. **Varians homogen**
               - Uji Levene p > 0.05
               
            4. **Sampel besar (n ≥ 30)**
               - Central Limit Theorem berlaku
               
            5. **Ingin lebih powerful**
               - ANOVA lebih sensitif jika asumsi terpenuhi
            """)
        
            st.warning("⚠️ **Penting**: Selalu lakukan uji normalitas terlebih dahulu sebelum memilih uji statistik!")
    
        with tab3:
            st.subheader("Asumsi Uji Kruskal-Wallis")
            st.markdown("""
        Uji Kruskal-Wallis memiliki asumsi yang lebih longgar dibanding ANOVA:
        
        ### 1️⃣ Independensi Observasi
        - Setiap observasi harus independen satu sama lain
        - Tidak ada subjek yang muncul di lebih dari satu kelompok
        
        ### 2️⃣ Variabel Dependen
        - Minimal skala ordinal atau interval/rasio
        - Dapat berupa:
          - Data ordinal (ranking, likert scale)
          - Data numerik yang tidak normal
        
        ### 3️⃣ Bentuk Distribusi
        - **TIDAK memerlukan normalitas** ✅
        - Idealnya bentuk distribusi antar kelompok serupa (tetapi tidak wajib)
        - Jika bentuk distribusi berbeda, interpretasi berubah dari median ke distribusi umum
        
        ### 4️⃣ Jumlah Kelompok
        - Minimal 3 kelompok independen
        - Dapat digunakan untuk 2 kelompok (sama dengan Mann-Whitney U)
        """)
        
            st.success("✨ **Keunggulan**: Tidak perlu asumsi normalitas dan homogenitas varians!")
    
        with tab4:
            st.subheader("Hipotesis Uji Kruskal-Wallis")
        
            st.markdown("""
        ### Hipotesis
        
        **H₀ (Hipotesis Nol):**
        
        Tidak ada perbedaan distribusi/median yang signifikan antar semua kelompok
        
        *Distribusi₁ = Distribusi₂ = Distribusi₃ = ... = Distribuiₖ*
        
        atau dalam konteks median:
        
        *Median₁ = Median₂ = Median₃ = ... = Medianₖ*
        
        **H₁ (Hipotesis Alternatif):**
        
        Minimal ada satu kelompok yang distribusi/mediannya berbeda signifikan
        
        ### Kriteria Pengambilan Keputusan
        
        - **Jika p-value < α** (biasanya 0.05) → **Tolak H₀**
          - Ada perbedaan signifikan antar kelompok
          
        - **Jika p-value ≥ α** → **Gagal Tolak H₀**
          - Tidak ada perbedaan signifikan antar kelompok
        
        ### Post-hoc Test
        
        Jika hasil signifikan (Tolak H₀), lakukan **post-hoc test** untuk mengetahui 
        kelompok mana yang berbeda:
        - Dunn's Test
        - Mann-Whitney U dengan koreksi Bonferroni
        """)
    
        with tab5:
            st.subheader("Rumus Uji Kruskal-Wallis")
        
            st.markdown("""
        ### Statistik H (Kruskal-Wallis)
        
        $$H = \\frac{12}{N(N+1)} \\sum_{i=1}^{k} \\frac{R_i^2}{n_i} - 3(N+1)$$
        
        **Keterangan:**
        - **H** = Statistik Kruskal-Wallis
        - **N** = Total jumlah observasi (semua kelompok)
        - **k** = Jumlah kelompok
        - **Rᵢ** = Jumlah ranking untuk kelompok ke-i
        - **nᵢ** = Jumlah observasi dalam kelompok ke-i
        
        ### Langkah Perhitungan:
        
        **1. Gabungkan semua data** dari semua kelompok
        
        **2. Beri ranking** pada seluruh data (dari terkecil ke terbesar)
           - Jika ada data yang sama (ties), gunakan rata-rata ranking
        
        **3. Jumlahkan ranking** untuk setiap kelompok (Rᵢ)
        
        **4. Hitung statistik H** menggunakan rumus di atas
        
        **5. Bandingkan dengan distribusi Chi-Square**
           - df = k - 1
           - Atau gunakan p-value langsung
        
        ### Contoh Sederhana:
        
        | Kelompok A | Kelompok B | Kelompok C |
        |------------|------------|------------|
        | 5 (rank 2) | 8 (rank 5) | 12 (rank 8)|
        | 4 (rank 1) | 10 (rank 7)| 15 (rank 9)|
        | 6 (rank 3) | 9 (rank 6) | 16 (rank 10)|
        | 7 (rank 4) | - | - |
        
        R₁ = 2+1+3+4 = 10, R₂ = 5+7+6 = 18, R₃ = 8+9+10 = 27
        """)
        
            st.info("💡 **Tips**: Semakin besar nilai H, semakin besar perbedaan antar kelompok")

    # ============ MENU SIMULASI MANUAL ============
    elif menu == "🧮 Simulasi Manual":
        st.header("🧮 Simulasi Manual - Input Data Sendiri")
    
        st.markdown("Masukkan data untuk setiap kelompok (pisahkan dengan koma)")
    
        col1, col2 = st.columns(2)
    
        with col1:
            num_groups = st.number_input("Jumlah Kelompok", min_value=2, max_value=10, value=3)
            alpha = st.number_input("Tingkat Signifikansi (α)", min_value=0.01, max_value=0.10, value=0.05, step=0.01)
    
        with col2:
            show_ranking = st.checkbox("Tampilkan Tabel Ranking", value=True)
            show_posthoc = st.checkbox("Tampilkan Post-hoc Test (jika signifikan)", value=True)
    
        # Input data untuk setiap kelompok
        groups_data = {}
        group_names = []
    
        st.markdown("---")
        st.subheader("Input Data Kelompok")
    
        cols = st.columns(min(3, num_groups))
    
        example_data = [
        "23, 28, 25, 30, 27",
        "35, 40, 38, 42, 36",
        "45, 50, 48, 52, 46"
        ]
    
        for i in range(num_groups):
            with cols[i % 3]:
                group_name = st.text_input(f"Nama Kelompok {i+1}", value=f"Kelompok {i+1}", key=f"name_{i}")
                group_names.append(group_name)
            
                data_input = st.text_area(
                f"Data {group_name}",
                value=example_data[i] if i < len(example_data) else "10, 15, 12, 18, 14",
                key=f"data_{i}",
                height=100,
                help="Masukkan angka dipisah koma. Contoh: 10, 12, 15, 18"
                )
            
                try:
                    data = [float(x.strip()) for x in data_input.split(",") if x.strip()]
                    groups_data[group_name] = data
                    st.caption(f"✅ {len(data)} data valid")
                except:
                    st.error(f"❌ Format data tidak valid")
                    groups_data[group_name] = []
    
        if st.button("🔍 Analisis Kruskal-Wallis", type="primary"):
            if len(groups_data) >= 2 and all(len(v) >= 2 for v in groups_data.values()):
                # Persiapan data
                all_data = []
                group_labels = []
                for name, data in groups_data.items():
                    all_data.extend(data)
                    group_labels.extend([name] * len(data))
            
                df = pd.DataFrame({'Nilai': all_data, 'Kelompok': group_labels})
            
                # Uji Kruskal-Wallis
                groups = [groups_data[name] for name in group_names]
                h_stat, p_value = stats.kruskal(*groups)
            
                # Uji Normalitas per kelompok
                normality_results = {}
                for name, data in groups_data.items():
                    if len(data) >= 3:
                        _, p_norm = stats.shapiro(data)
                        normality_results[name] = p_norm
            
                # Hasil Utama
                st.markdown("---")
                st.subheader("📊 Hasil Uji Kruskal-Wallis")
            
                col1, col2, col3, col4 = st.columns(4)
                col1.metric("H-Statistik", f"{h_stat:.4f}")
                col2.metric("P-Value", f"{p_value:.6f}")
                col3.metric("df", f"{len(groups) - 1}")
                col4.metric("Keputusan", "Tolak H₀" if p_value < alpha else "Gagal Tolak H₀")
            
                # Interpretasi
                st.markdown("### 📝 Interpretasi")
                if p_value < alpha:
                    st.success(f"""
                ✅ **Kesimpulan**: Dengan tingkat signifikansi {alpha}, terdapat perbedaan distribusi/median 
                yang **signifikan** antar kelompok.
                
                - H-statistik = {h_stat:.4f}
                - P-value = {p_value:.6f} < {alpha}
                - **Tolak H₀**
                
                Artinya: Minimal ada satu kelompok yang memiliki distribusi/median berbeda secara signifikan.
                """)
                
                    if show_posthoc:
                        st.info("💡 **Rekomendasi**: Lakukan post-hoc test (Dunn's test) untuk mengetahui kelompok mana yang berbeda.")
                else:
                    st.info(f"""
                ℹ️ **Kesimpulan**: Dengan tingkat signifikansi {alpha}, **tidak** terdapat perbedaan 
                distribusi/median yang signifikan antar kelompok.
                
                - H-statistik = {h_stat:.4f}
                - P-value = {p_value:.6f} ≥ {alpha}
                - **Gagal Tolak H₀**
                
                Artinya: Semua kelompok memiliki distribusi/median yang tidak berbeda secara statistik.
                """)
            
                # Uji Normalitas
                st.markdown("### 🔬 Uji Normalitas (Shapiro-Wilk)")
                st.caption("Untuk memvalidasi pemilihan uji non-parametrik")
            
                norm_df = pd.DataFrame({
                'Kelompok': list(normality_results.keys()),
                'P-Value': [f"{p:.4f}" for p in normality_results.values()],
                'Status': ['❌ Tidak Normal (p < 0.05)' if p < 0.05 else '✅ Normal (p ≥ 0.05)' 
                          for p in normality_results.values()]
                })
                st.dataframe(norm_df, use_container_width=True, hide_index=True)
            
                not_normal_count = sum(1 for p in normality_results.values() if p < 0.05)
                if not_normal_count > 0:
                    st.success(f"✅ Pilihan Kruskal-Wallis sudah tepat! {not_normal_count} dari {len(normality_results)} kelompok tidak berdistribusi normal.")
                else:
                    st.warning("⚠️ Semua kelompok berdistribusi normal. Pertimbangkan menggunakan ANOVA untuk analisis yang lebih powerful.")
            
                # Statistik Deskriptif
                st.markdown("### 📈 Statistik Deskriptif")
                desc_stats = df.groupby('Kelompok')['Nilai'].agg([
                ('N', 'count'),
                ('Mean', 'mean'),
                ('Median', 'median'),
                ('Std Dev', 'std'),
                ('Min', 'min'),
                ('Max', 'max')
                ]).round(3)
                st.dataframe(desc_stats, use_container_width=True)
            
                # Tabel Ranking
                if show_ranking:
                    st.markdown("### 🔢 Tabel Ranking")
                    df_rank = df.copy()
                    df_rank['Rank'] = stats.rankdata(df_rank['Nilai'])
                    df_rank = df_rank.sort_values('Rank')
                
                    st.dataframe(df_rank, use_container_width=True, hide_index=True)
                
                    # Jumlah ranking per kelompok
                    rank_sum = df_rank.groupby('Kelompok')['Rank'].agg(['sum', 'mean']).round(2)
                    rank_sum.columns = ['Jumlah Rank', 'Rata-rata Rank']
                    st.markdown("#### Ringkasan Ranking per Kelompok")
                    st.dataframe(rank_sum, use_container_width=True)
            
                # Visualisasi
                st.markdown("### 📊 Visualisasi Data")
            
                tab1, tab2, tab3 = st.tabs(["📦 Box Plot", "📊 Violin Plot", "📈 Histogram"])
            
                with tab1:
                    fig_box = px.box(df, x='Kelompok', y='Nilai', 
                                title='Box Plot - Distribusi Data per Kelompok',
                                color='Kelompok', points='all')
                    fig_box.add_hline(y=df['Nilai'].median(), line_dash="dash", 
                                 line_color="red", annotation_text="Median Keseluruhan")
                    fig_box.update_layout(showlegend=False, height=500)
                    st.plotly_chart(fig_box, use_container_width=True)
            
                with tab2:
                    fig_violin = px.violin(df, x='Kelompok', y='Nilai', 
                                      title='Violin Plot - Distribusi Data per Kelompok',
                                      color='Kelompok', box=True, points='all')
                    fig_violin.update_layout(showlegend=False, height=500)
                    st.plotly_chart(fig_violin, use_container_width=True)
            
                with tab3:
                    fig_hist = px.histogram(df, x='Nilai', color='Kelompok', 
                                       title='Histogram - Distribusi Frekuensi',
                                       marginal='box', barmode='overlay', opacity=0.7)
                    fig_hist.update_layout(height=500)
                    st.plotly_chart(fig_hist, use_container_width=True)
            
                # Perbandingan Median
                st.markdown("### 📊 Perbandingan Median Kelompok")
                median_data = df.groupby('Kelompok')['Nilai'].median().reset_index()
                median_data.columns = ['Kelompok', 'Median']
            
                fig_median = px.bar(median_data, x='Kelompok', y='Median', 
                               title='Perbandingan Median antar Kelompok',
                               color='Kelompok', text='Median')
                fig_median.update_traces(texttemplate='%{text:.2f}', textposition='outside')
                fig_median.update_layout(showlegend=False, height=400)
                st.plotly_chart(fig_median, use_container_width=True)
            
            else:
                st.error("⚠️ Setiap kelompok harus memiliki minimal 2 data!")

    # ============ MENU SIMULASI DATA ============
    elif menu == "📈 Simulasi Data":
        st.header("📈 Simulasi Data - Generate Data Non-Normal")
    
        st.markdown("Generate data dengan distribusi non-normal untuk simulasi Uji Kruskal-Wallis")
    
        col1, col2, col3 = st.columns(3)
    
        with col1:
            num_groups_sim = st.slider("Jumlah Kelompok", 2, 6, 3)
            samples_per_group = st.slider("Sampel per Kelompok", 10, 100, 30)
            distribution_type = st.selectbox(
            "Tipe Distribusi",
            ["Exponential (Skewed)", "Uniform", "Poisson", "Chi-Square"]
            )
    
        with col2:
            scale_start = st.number_input("Skala Awal", value=10.0, step=1.0)
            scale_diff = st.number_input("Perbedaan Skala antar Kelompok", value=5.0, step=1.0)
            alpha_sim = st.selectbox("Tingkat Signifikansi (α)", [0.01, 0.05, 0.10], index=1)
    
        with col3:
            add_outliers = st.checkbox("Tambahkan Outliers", value=False)
            if add_outliers:
                outlier_count = st.slider("Jumlah Outliers per Kelompok", 1, 5, 2)
            seed_value = st.number_input("Random Seed", value=42, step=1)
    
        if st.button("🎲 Generate & Analisis", type="primary"):
            np.random.seed(seed_value)
        
            # Generate data
            groups_sim = []
            group_names_sim = []
            all_data_sim = []
            all_labels_sim = []
        
            for i in range(num_groups_sim):
                scale = scale_start + (i * scale_diff)
            
                # Generate berdasarkan distribusi
                if distribution_type == "Exponential (Skewed)":
                    data = np.random.exponential(scale, samples_per_group)
                elif distribution_type == "Uniform":
                    data = np.random.uniform(scale, scale + 20, samples_per_group)
                elif distribution_type == "Poisson":
                    data = np.random.poisson(scale, samples_per_group).astype(float)
                else:  # Chi-Square
                    data = np.random.chisquare(5, samples_per_group) * scale / 5
            
                # Tambahkan outliers jika diminta
                if add_outliers:
                    outliers = np.random.uniform(scale * 3, scale * 4, outlier_count)
                    data = np.concatenate([data, outliers])
            
                groups_sim.append(data)
                group_name = f"Kelompok {i+1}"
                group_names_sim.append(group_name)
                all_data_sim.extend(data)
                all_labels_sim.extend([group_name] * len(data))
        
            df_sim = pd.DataFrame({'Nilai': all_data_sim, 'Kelompok': all_labels_sim})
        
            # Uji Kruskal-Wallis
            h_stat_sim, p_value_sim = stats.kruskal(*groups_sim)
        
            # Uji Normalitas
            normality_sim = {}
            for i, data in enumerate(groups_sim):
                if len(data) >= 3:
                    _, p_norm = stats.shapiro(data)
                    normality_sim[group_names_sim[i]] = p_norm
        
            # Hasil
            st.markdown("---")
            st.subheader("📊 Hasil Simulasi Kruskal-Wallis")
        
            col1, col2, col3, col4 = st.columns(4)
            col1.metric("H-Statistik", f"{h_stat_sim:.4f}")
            col2.metric("P-Value", f"{p_value_sim:.6f}")
            col3.metric("df", f"{num_groups_sim - 1}")
            col4.metric("Keputusan", "Tolak H₀" if p_value_sim < alpha_sim else "Gagal Tolak H₀")
        
            # Interpretasi
            st.markdown("### 📝 Interpretasi")
            if p_value_sim < alpha_sim:
                st.success(f"""
            ✅ **Kesimpulan**: Dengan tingkat signifikansi {alpha_sim}, terdapat perbedaan distribusi/median 
            yang **signifikan** antar kelompok (p-value = {p_value_sim:.6f} < {alpha_sim}).
            
            Artinya: Minimal ada satu kelompok yang memiliki distribusi/median berbeda secara signifikan.
            """)
            else:
                st.info(f"""
            ℹ️ **Kesimpulan**: Dengan tingkat signifikansi {alpha_sim}, **tidak** terdapat perbedaan 
            distribusi/median yang signifikan antar kelompok (p-value = {p_value_sim:.6f} ≥ {alpha_sim}).
            """)
        
            # Hasil Uji Normalitas
            st.markdown("### 🔬 Hasil Uji Normalitas (Shapiro-Wilk)")
            norm_df_sim = pd.DataFrame({
            'Kelompok': list(normality_sim.keys()),
            'P-Value': [f"{p:.4f}" for p in normality_sim.values()],
            'Status': ['❌ Tidak Normal' if p < 0.05 else '✅ Normal' 
                      for p in normality_sim.values()],
            'Keterangan': ['Data tidak berdistribusi normal' if p < 0.05 else 'Data berdistribusi normal' 
                          for p in normality_sim.values()]
            })
            st.dataframe(norm_df_sim, use_container_width=True, hide_index=True)
        
            not_normal = sum(1 for p in normality_sim.values() if p < 0.05)
            st.info(f"📊 **Ringkasan**: {not_normal} dari {len(normality_sim)} kelompok tidak berdistribusi normal → Kruskal-Wallis adalah pilihan yang tepat!")
        
            # Statistik Deskriptif
            st.markdown("### 📈 Statistik Deskriptif")
            desc_stats_sim = df_sim.groupby('Kelompok')['Nilai'].agg([
            ('N', 'count'),
            ('Mean', 'mean'),
            ('Median', 'median'),
            ('Std Dev', 'std'),
            ('Min', 'min'),
            ('Max', 'max'),
            ('Skewness', lambda x: stats.skew(x))
            ]).round(3)
            st.dataframe(desc_stats_sim, use_container_width=True)
        
            # Visualisasi
            st.markdown("### 📊 Visualisasi Data")
        
            tab1, tab2, tab3, tab4 = st.tabs(["📦 Box Plot", "📊 Violin Plot", "📈 Distribusi", "🔢 Q-Q Plot"])
        
            with tab1:
                fig_box = px.box(df_sim, x='Kelompok', y='Nilai', 
                            title=f'Box Plot - Distribusi {distribution_type}',
                            color='Kelompok', points='all')
                fig_box.update_layout(showlegend=False, height=500)
                st.plotly_chart(fig_box, use_container_width=True)
        
            with tab2:
                fig_violin = px.violin(df_sim, x='Kelompok', y='Nilai', 
                                  title='Violin Plot - Menunjukkan Skewness',
                                  color='Kelompok', box=True, points='all')
                fig_violin.update_layout(showlegend=False, height=500)
                st.plotly_chart(fig_violin, use_container_width=True)
        
            with tab3:
                fig_hist = px.histogram(df_sim, x='Nilai', color='Kelompok', 
                                   title='Histogram - Distribusi Non-Normal',
                                   marginal='box', barmode='overlay', opacity=0.6)
                fig_hist.update_layout(height=500)
                st.plotly_chart(fig_hist, use_container_width=True)
        
            with tab4:
                # Q-Q Plot untuk setiap kelompok
                fig_qq = make_subplots(
                rows=1, cols=min(3, num_groups_sim),
                subplot_titles=[f"Q-Q Plot {name}" for name in group_names_sim[:3]]
                )
            
                for i, (name, data) in enumerate(list(zip(group_names_sim, groups_sim))[:3]):
                    qq = stats.probplot(data, dist="norm")
                    fig_qq.add_trace(
                    go.Scatter(x=qq[0][0], y=qq[0][1], mode='markers', 
                              name=name, showlegend=True),
                    row=1, col=i+1
                    )
                    # Garis referensi
                    fig_qq.add_trace(
                        go.Scatter(x=qq[0][0], y=qq[1][1] + qq[1][0] * qq[0][0], 
                              mode='lines', name='Normal', 
                              line=dict(color='red', dash='dash'), showlegend=False),
                        row=1, col=i+1
                    )
            
                fig_qq.update_xaxes(title_text="Theoretical Quantiles")
                fig_qq.update_yaxes(title_text="Sample Quantiles")
                fig_qq.update_layout(height=400, title_text="Q-Q Plot - Menunjukkan Deviasi dari Normalitas")
                st.plotly_chart(fig_qq, use_container_width=True)
            
                st.caption("💡 Jika titik-titik menyimpang dari garis merah, data tidak berdistribusi normal")
        
            # Perbandingan Median
            st.markdown("### 📊 Perbandingan Median Kelompok")
            median_data_sim = df_sim.groupby('Kelompok')['Nilai'].median().reset_index()
            median_data_sim.columns = ['Kelompok', 'Median']
        
            fig_median = px.bar(median_data_sim, x='Kelompok', y='Median', 
                           title='Perbandingan Median antar Kelompok',
                           color='Kelompok', text='Median')
            fig_median.update_traces(texttemplate='%{text:.2f}', textposition='outside')
            fig_median.update_layout(showlegend=False, height=400)
            st.plotly_chart(fig_median, use_container_width=True)
        
            # Download data
            st.markdown("### 💾 Download Data")
            csv = df_sim.to_csv(index=False)
            st.download_button(
            label="📥 Download Data CSV",
            data=csv,
            file_name=f"data_kruskal_wallis_{distribution_type.lower().replace(' ', '_')}.csv",
            mime="text/csv"
            )

    # ============ MENU UJI ASUMSI ============
    else:
        st.header("🔬 Uji Asumsi - Normalitas dan Homogenitas")
    
        st.markdown("""
    Lakukan uji asumsi untuk menentukan apakah harus menggunakan **ANOVA** atau **Kruskal-Wallis**
    """)
    
        # Input data
        st.subheader("Input Data untuk Uji Asumsi")
    
        num_groups_test = st.number_input("Jumlah Kelompok", min_value=2, max_value=10, value=3, key="test_groups")
    
        groups_test_data = {}
        group_test_names = []
    
        cols = st.columns(min(3, num_groups_test))
    
        for i in range(num_groups_test):
            with cols[i % 3]:
                group_name = st.text_input(f"Nama Kelompok {i+1}", value=f"Kelompok {i+1}", key=f"test_name_{i}")
                group_test_names.append(group_name)
            
                data_input = st.text_area(
                f"Data {group_name}",
                value="20, 22, 21, 23, 24, 22, 25, 23, 21, 24" if i == 0 else f"{30+i*5}, {32+i*5}, {31+i*5}, {33+i*5}, {34+i*5}, {32+i*5}, {35+i*5}, {33+i*5}, {31+i*5}, {34+i*5}",
                key=f"test_data_{i}",
                height=100
                )
            
                try:
                    data = [float(x.strip()) for x in data_input.split(",") if x.strip()]
                    groups_test_data[group_name] = data
                except:
                    st.error(f"Format tidak valid")
                    groups_test_data[group_name] = []
    
        if st.button("🔬 Uji Asumsi", type="primary", key="test_button"):
            if all(len(v) >= 3 for v in groups_test_data.values()):
            
                st.markdown("---")
                st.subheader("📊 Hasil Uji Asumsi")
            
                # 1. UJI NORMALITAS (Shapiro-Wilk)
                st.markdown("### 1️⃣ Uji Normalitas (Shapiro-Wilk)")
                st.caption("H₀: Data berdistribusi normal")
            
                normality_results = []
                all_normal = True
            
                for name, data in groups_test_data.items():
                    stat, p_val = stats.shapiro(data)
                    is_normal = p_val >= 0.05
                    if not is_normal:
                        all_normal = False
                
                    normality_results.append({
                    'Kelompok': name,
                    'Statistik': f"{stat:.4f}",
                    'P-Value': f"{p_val:.4f}",
                    'Status': '✅ Normal' if is_normal else '❌ Tidak Normal',
                    'Keputusan': 'Gagal Tolak H₀' if is_normal else 'Tolak H₀'
                    })
            
                norm_df = pd.DataFrame(normality_results)
                st.dataframe(norm_df, use_container_width=True, hide_index=True)
            
                # 2. UJI HOMOGENITAS (Levene)
                st.markdown("### 2️⃣ Uji Homogenitas Varians (Levene)")
                st.caption("H₀: Varians semua kelompok homogen (sama)")
            
                groups_list = [groups_test_data[name] for name in group_test_names]
                levene_stat, levene_p = stats.levene(*groups_list)
            
                homogen = levene_p >= 0.05
            
                levene_df = pd.DataFrame({
                'Uji': ['Levene'],
                'Statistik': [f"{levene_stat:.4f}"],
                'P-Value': [f"{levene_p:.4f}"],
                'Status': ['✅ Homogen' if homogen else '❌ Tidak Homogen'],
                'Keputusan': ['Gagal Tolak H₀' if homogen else 'Tolak H₀']
                })
                st.dataframe(levene_df, use_container_width=True, hide_index=True)
            
                # REKOMENDASI
                st.markdown("### 🎯 Rekomendasi Uji Statistik")
            
                if all_normal and homogen:
                    st.success("""
                ✅ **GUNAKAN ANOVA 1 JALUR**
                
                **Alasan:**
                - ✅ Semua kelompok berdistribusi normal
                - ✅ Varians homogen
                
                ANOVA akan memberikan hasil yang lebih powerful dan akurat untuk data Anda.
                """)
                elif all_normal and not homogen:
                    st.warning("""
                ⚠️ **GUNAKAN WELCH ANOVA atau KRUSKAL-WALLIS**
                
                **Alasan:**
                - ✅ Semua kelompok berdistribusi normal
                - ❌ Varians tidak homogen
                
                Welch ANOVA atau Kruskal-Wallis lebih robust terhadap heterogenitas varians.
                """)
                else:
                    st.info("""
                📊 **GUNAKAN UJI KRUSKAL-WALLIS**
                
                **Alasan:**
                - ❌ Minimal satu kelompok tidak berdistribusi normal
                
                Kruskal-Wallis adalah alternatif non-parametrik yang tepat karena tidak memerlukan asumsi normalitas.
                """)
            
                # Visualisasi untuk Uji Asumsi
                st.markdown("### 📊 Visualisasi Data")
            
                all_data_test = []
                all_labels_test = []
                for name, data in groups_test_data.items():
                    all_data_test.extend(data)
                    all_labels_test.extend([name] * len(data))
            
                df_test = pd.DataFrame({'Nilai': all_data_test, 'Kelompok': all_labels_test})
            
                col1, col2 = st.columns(2)
            
                with col1:
                    fig_box_test = px.box(df_test, x='Kelompok', y='Nilai', 
                                     title='Box Plot - Cek Outliers dan Distribusi',
                                     color='Kelompok', points='all')
                    fig_box_test.update_layout(showlegend=False)
                    st.plotly_chart(fig_box_test, use_container_width=True)
            
                with col2:
                    fig_hist_test = px.histogram(df_test, x='Nilai', color='Kelompok', 
                                            title='Histogram - Cek Normalitas Visual',
                                            marginal='box', barmode='overlay', opacity=0.6)
                    st.plotly_chart(fig_hist_test, use_container_width=True)
            
                # Statistik Deskriptif
                st.markdown("### 📈 Statistik Deskriptif")
                desc_test = df_test.groupby('Kelompok')['Nilai'].agg([
                ('N', 'count'),
                ('Mean', 'mean'),
                ('Median', 'median'),
                ('Std Dev', 'std'),
                ('Varians', 'var'),
                ('Skewness', lambda x: stats.skew(x))
                ]).round(3)
                st.dataframe(desc_test, use_container_width=True)
            
                # Interpretasi Skewness
                st.info("""
            💡 **Interpretasi Skewness:**
            - Skewness ≈ 0: Distribusi simetris (mendekati normal)
            - Skewness > 0: Skewed ke kanan (ekor di kanan lebih panjang)
            - Skewness < 0: Skewed ke kiri (ekor di kiri lebih panjang)
            - |Skewness| > 1: Data sangat skewed (pertimbangkan Kruskal-Wallis)
            """)
            
            else:
                st.error("⚠️ Setiap kelompok harus memiliki minimal 3 data untuk uji normalitas!")

    # Footer
    st.markdown("---")
    st.markdown("""
<div style='text-align: center; color: gray;'>
    <p>📊 Aplikasi Pembelajaran Uji Kruskal-Wallis | Uji Non-Parametrik untuk > 2 Sampel</p>
    <p style='font-size: 0.8em;'>💡 Alternatif non-parametrik untuk ANOVA ketika data tidak berdistribusi normal</p>
</div>
""", unsafe_allow_html=True)

def tampilkan_materi26():
    # Fungsi untuk Welch's ANOVA
    def welch_anova(*args):
        """
        Menghitung Welch's ANOVA (ANOVA untuk varians tidak homogen)
        """
        k = len(args)  # jumlah kelompok
        n_i = np.array([len(arg) for arg in args])  # ukuran sampel per kelompok
        means = np.array([np.mean(arg) for arg in args])  # rata-rata per kelompok
        vars = np.array([np.var(arg, ddof=1) for arg in args])  # varians per kelompok
    
        # Weights
        w_i = n_i / vars
    
        # Grand mean (weighted)
        grand_mean = np.sum(w_i * means) / np.sum(w_i)
    
        # Welch F-statistic
        numerator = np.sum(w_i * (means - grand_mean)**2) / (k - 1)
    
        # Denominator correction
        tmp = (1 - w_i / np.sum(w_i))**2 / (n_i - 1)
        denominator = 1 + (2 * (k - 2) / (k**2 - 1)) * np.sum(tmp)
    
        F_welch = numerator / denominator
    
        # Degrees of freedom
        df1 = k - 1
        df2 = (k**2 - 1) / (3 * np.sum(tmp))
    
        # P-value
        p_value = 1 - stats.f.cdf(F_welch, df1, df2)
    
        return F_welch, p_value, df1, df2

    # Fungsi untuk Games-Howell post-hoc test
    def games_howell_test(groups_dict):
        """
        Games-Howell post-hoc test untuk Welch's ANOVA
        """
        group_names = list(groups_dict.keys())
        results = []
    
        for i in range(len(group_names)):
            for j in range(i+1, len(group_names)):
                g1_name = group_names[i]
                g2_name = group_names[j]
                g1 = groups_dict[g1_name]
                g2 = groups_dict[g2_name]
            
                n1, n2 = len(g1), len(g2)
                mean1, mean2 = np.mean(g1), np.mean(g2)
                var1, var2 = np.var(g1, ddof=1), np.var(g2, ddof=1)
            
                # Mean difference
                mean_diff = mean1 - mean2
            
                # Standard error
                se = np.sqrt(var1/n1 + var2/n2)
            
                # t-statistic
                t_stat = mean_diff / se
            
                # Degrees of freedom (Welch-Satterthwaite)
                df = (var1/n1 + var2/n2)**2 / ((var1/n1)**2/(n1-1) + (var2/n2)**2/(n2-1))
            
                # P-value (two-tailed)
                p_val = 2 * (1 - stats.t.cdf(abs(t_stat), df))
            
                results.append({
                'Perbandingan': f"{g1_name} vs {g2_name}",
                'Mean Diff': mean_diff,
                't-statistic': t_stat,
                'df': df,
                'p-value': p_val,
                'Signifikan': 'Ya ✓' if p_val < 0.05 else 'Tidak'
                })
    
        return pd.DataFrame(results)

    # Judul aplikasi
    st.title("📊 Welch's ANOVA (One-Way)")
    st.markdown("### ANOVA untuk Data dengan Varians Tidak Homogen")

    # Sidebar untuk navigasi
    menu = st.sidebar.radio(
    "Pilih Menu:",
    ["📚 Materi", "🧮 Simulasi Manual", "📈 Simulasi Data", "⚖️ Perbandingan Uji"]
    )

    # ============ MENU MATERI ============
    if menu == "📚 Materi":
        st.header("📚 Materi Welch's ANOVA")
    
        tab1, tab2, tab3, tab4, tab5 = st.tabs(["Pengertian", "Kapan Digunakan", "Asumsi", "Hipotesis", "Rumus"])
    
        with tab1:
            st.subheader("Apa itu Welch's ANOVA?")
            st.markdown("""
        **Welch's ANOVA** adalah variasi dari ANOVA klasik yang **tidak memerlukan asumsi homogenitas varians** 
        (homoscedasticity). Uji ini dikembangkan oleh Bernard Lewis Welch pada tahun 1951.
        
        **Karakteristik:**
        - 🔹 Modifikasi dari ANOVA 1 jalur klasik
        - 🔹 Robust terhadap **heterogenitas varians** (varians tidak sama)
        - 🔹 Menggunakan **weighted means** berdasarkan varians kelompok
        - 🔹 Degrees of freedom dihitung dengan metode Welch-Satterthwaite
        - 🔹 Tetap memerlukan asumsi **normalitas**
        
        **Perbedaan dengan ANOVA Klasik:**
        
        | Aspek | ANOVA Klasik | Welch's ANOVA |
        |-------|--------------|---------------|
        | Homogenitas Varians | **Diperlukan** ✓ | **Tidak diperlukan** ✗ |
        | Normalitas | Diperlukan | Diperlukan |
        | Ukuran Sampel | Bisa tidak sama | Bisa tidak sama |
        | Pooled Variance | Ya | Tidak (individual) |
        | Degrees of Freedom | Integer | Desimal (adjusted) |
        
        **Contoh Kasus:**
        - Membandingkan gaji karyawan dari 3 departemen (variabilitas gaji berbeda)
        - Membandingkan waktu respon dari 4 server (varians tidak sama)
        - Membandingkan nilai ujian dari 3 kelas dengan spread yang berbeda
        """)
        
            st.success("✨ **Keunggulan**: Memberikan hasil yang lebih akurat ketika varians antar kelompok sangat berbeda!")
    
        with tab2:
            st.subheader("Kapan Menggunakan Welch's ANOVA?")
        
            col1, col2 = st.columns(2)
        
            with col1:
                st.markdown("""
            ### ✅ Gunakan Welch's ANOVA Jika:
            
            1. **Data berdistribusi normal**
               - Uji Shapiro-Wilk: p > 0.05
               
            2. **Varians TIDAK homogen**
               - Uji Levene: p < 0.05
               - Rasio varians terbesar/terkecil > 3
               
            3. **Ukuran sampel tidak sama**
               - Dan varians berbeda antar kelompok
               
            4. **Ada 3 atau lebih kelompok independen**
               - Untuk 2 kelompok, gunakan Welch's t-test
               
            5. **ANOVA klasik tidak memenuhi asumsi**
               - Tetapi data masih normal
            """)
        
            with col2:
                st.markdown("""
            ### ❌ Gunakan Uji Lain Jika:
            
            **ANOVA Klasik:**
            - ✓ Data normal
            - ✓ Varians homogen (Levene p > 0.05)
            - → Lebih powerful jika asumsi terpenuhi
            
            **Kruskal-Wallis:**
            - ✗ Data tidak normal
            - ? Varians homogen atau tidak
            - → Alternatif non-parametrik
            
            **Brown-Forsythe:**
            - ✓ Data normal
            - ✗ Varians tidak homogen
            - → Alternatif lain untuk Welch's ANOVA
            """)
        
            st.info("""
        💡 **Proses Pemilihan Uji:**
        1. Uji Normalitas (Shapiro-Wilk) → Jika p < 0.05: Gunakan **Kruskal-Wallis**
        2. Jika Normal, Uji Homogenitas (Levene) → Jika p < 0.05: Gunakan **Welch's ANOVA**
        3. Jika Normal & Homogen → Gunakan **ANOVA Klasik**
        """)
    
        with tab3:
            st.subheader("Asumsi Welch's ANOVA")
            st.markdown("""
        Welch's ANOVA memiliki asumsi yang lebih longgar dibanding ANOVA klasik:
        
        ### 1️⃣ Independensi Observasi ✅ (WAJIB)
        - Setiap observasi harus independen
        - Tidak ada subjek yang muncul di lebih dari satu kelompok
        - Sampling harus random
        
        ### 2️⃣ Normalitas ✅ (WAJIB)
        - Data dalam setiap kelompok harus berdistribusi normal
        - **Cara Uji:**
          - Visual: Q-Q plot, histogram
          - Statistik: Shapiro-Wilk test (p > 0.05)
        - **Catatan**: Robust terhadap pelanggaran ringan jika n > 30
        
        ### 3️⃣ Variabel Dependen ✅
        - Harus berupa data numerik (interval atau rasio)
        - Contoh: skor, waktu, berat, tinggi
        
        ### 4️⃣ Homogenitas Varians ❌ (TIDAK DIPERLUKAN)
        - **INI YANG MEMBEDAKAN!**
        - Welch's ANOVA dirancang untuk data dengan varians tidak homogen
        - Tidak perlu memenuhi asumsi equal variance
        
        ### 📊 Perbandingan Asumsi
        
        | Asumsi | ANOVA Klasik | Welch's ANOVA | Kruskal-Wallis |
        |--------|--------------|---------------|----------------|
        | Normalitas | ✅ Wajib | ✅ Wajib | ❌ Tidak perlu |
        | Homogenitas | ✅ Wajib | ❌ Tidak perlu | ❌ Tidak perlu |
        | Independensi | ✅ Wajib | ✅ Wajib | ✅ Wajib |
        """)
        
            st.warning("⚠️ **Penting**: Meskipun Welch's ANOVA robust terhadap heterogenitas varians, data TETAP harus berdistribusi normal!")
    
        with tab4:
            st.subheader("Hipotesis Welch's ANOVA")
        
            st.markdown("""
        ### Perumusan Hipotesis
        
        **H₀ (Hipotesis Nol):**
        
        Tidak ada perbedaan rata-rata populasi yang signifikan antar semua kelompok
        
        $$\\mu_1 = \\mu_2 = \\mu_3 = ... = \\mu_k$$
        
        **H₁ (Hipotesis Alternatif):**
        
        Minimal ada satu kelompok yang rata-ratanya berbeda signifikan
        
        $$\\text{Minimal ada satu } \\mu_i \\neq \\mu_j$$
        
        ### Kriteria Pengambilan Keputusan
        
        **Berdasarkan P-value:**
        - Jika **p-value < α** (biasanya 0.05) → **Tolak H₀**
          - ✓ Ada perbedaan signifikan antar kelompok
          - Lanjutkan dengan **post-hoc test**
          
        - Jika **p-value ≥ α** → **Gagal Tolak H₀**
          - ✗ Tidak ada perbedaan signifikan
          - Post-hoc test tidak diperlukan
        
        **Berdasarkan F-statistik:**
        - Jika **F-hitung > F-tabel** → Tolak H₀
        - Jika **F-hitung ≤ F-tabel** → Gagal Tolak H₀
        
        ### Post-hoc Test untuk Welch's ANOVA
        
        Jika hasil signifikan, gunakan **Games-Howell test**:
        - Dirancang khusus untuk data dengan varians tidak homogen
        - Tidak mengasumsikan equal variance
        - Robust terhadap ukuran sampel yang tidak sama
        - Lebih konservatif dari Tukey HSD
        
        **Alternatif Post-hoc:**
        - Dunnett's T3 test
        - Tamhane's T2 test
        """)
        
            st.info("💡 **Catatan**: Jangan gunakan Tukey HSD untuk Welch's ANOVA karena Tukey mengasumsikan varians homogen!")
    
        with tab5:
            st.subheader("Rumus Welch's ANOVA")
        
            st.markdown("""
        ### Formula Welch's F-statistic
        
        $$F_w = \\frac{\\sum_{i=1}^{k} w_i(\\bar{X}_i - \\bar{X}_w)^2 / (k-1)}{1 + \\frac{2(k-2)}{k^2-1} \\sum_{i=1}^{k} \\frac{(1-w_i/\\sum w_i)^2}{n_i-1}}$$
        
        **Dimana:**
        
        $$w_i = \\frac{n_i}{s_i^2}$$
        
        $$\\bar{X}_w = \\frac{\\sum_{i=1}^{k} w_i \\bar{X}_i}{\\sum_{i=1}^{k} w_i}$$
        
        **Keterangan:**
        - **F_w** = Welch's F-statistic
        - **k** = Jumlah kelompok
        - **n_i** = Ukuran sampel kelompok ke-i
        - **X̄_i** = Rata-rata kelompok ke-i
        - **s_i²** = Varians kelompok ke-i
        - **w_i** = Weight (bobot) untuk kelompok ke-i
        - **X̄_w** = Weighted grand mean
        
        ### Degrees of Freedom
        
        **df₁ (numerator):**
        $$df_1 = k - 1$$
        
        **df₂ (denominator) - Welch-Satterthwaite:**
        $$df_2 = \\frac{(k^2-1)}{3\\sum_{i=1}^{k} \\frac{(1-w_i/\\sum w_i)^2}{n_i-1}}$$
        
        ### Langkah Perhitungan Manual:
        
        **Step 1:** Hitung rata-rata (X̄ᵢ) dan varians (sᵢ²) untuk setiap kelompok
        
        **Step 2:** Hitung weight untuk setiap kelompok:
        ```
        wᵢ = nᵢ / sᵢ²
        ```
        
        **Step 3:** Hitung weighted grand mean:
        ```
        X̄_w = Σ(wᵢ × X̄ᵢ) / Σwᵢ
        ```
        
        **Step 4:** Hitung numerator:
        ```
        Numerator = Σ[wᵢ(X̄ᵢ - X̄_w)²] / (k-1)
        ```
        
        **Step 5:** Hitung correction factor untuk denominator:
        ```
        λ = Σ[(1 - wᵢ/Σwᵢ)² / (nᵢ-1)]
        ```
        
        **Step 6:** Hitung denominator:
        ```
        Denominator = 1 + [2(k-2)/(k²-1)] × λ
        ```
        
        **Step 7:** Hitung F_welch:
        ```
        F_w = Numerator / Denominator
        ```
        
        **Step 8:** Hitung df dan p-value menggunakan distribusi F
        """)
        
            st.success("✨ **Insight**: Kelompok dengan varians lebih kecil mendapat weight lebih besar dalam perhitungan!")

    # ============ MENU SIMULASI MANUAL ============
    elif menu == "🧮 Simulasi Manual":
        st.header("🧮 Simulasi Manual - Input Data Sendiri")
    
        st.markdown("Masukkan data untuk setiap kelompok (pisahkan dengan koma)")
    
        col1, col2 = st.columns(2)
    
        with col1:
            num_groups = st.number_input("Jumlah Kelompok", min_value=2, max_value=10, value=3)
            alpha = st.number_input("Tingkat Signifikansi (α)", min_value=0.01, max_value=0.10, value=0.05, step=0.01)
    
        with col2:
            compare_tests = st.checkbox("Bandingkan dengan ANOVA Klasik", value=True)
            show_posthoc = st.checkbox("Tampilkan Games-Howell Post-hoc", value=True)
    
        # Input data
        groups_data = {}
        group_names = []
    
        st.markdown("---")
        st.subheader("Input Data Kelompok")
        st.caption("💡 Tip: Buat data dengan varians yang berbeda untuk melihat perbedaan Welch's ANOVA vs ANOVA klasik")
    
        cols = st.columns(min(3, num_groups))
    
        # Data contoh dengan varians berbeda
        example_data = [
        "50, 52, 51, 53, 49, 50, 52",  # Varians kecil
        "45, 55, 40, 60, 38, 62, 43",  # Varians sedang
        "30, 70, 35, 65, 25, 75, 40"   # Varians besar
        ]
    
        for i in range(num_groups):
            with cols[i % 3]:
                group_name = st.text_input(f"Nama Kelompok {i+1}", value=f"Kelompok {i+1}", key=f"name_{i}")
                group_names.append(group_name)
            
                data_input = st.text_area(
                f"Data {group_name}",
                value=example_data[i] if i < len(example_data) else "10, 12, 11, 13, 14",
                key=f"data_{i}",
                height=100
                )
            
                try:
                    data = [float(x.strip()) for x in data_input.split(",") if x.strip()]
                    groups_data[group_name] = data
                
                    if len(data) >= 2:
                        st.caption(f"✅ n={len(data)}, σ²={np.var(data, ddof=1):.2f}")
                except:
                    st.error(f"❌ Format tidak valid")
                    groups_data[group_name] = []
    
        if st.button("🔍 Analisis Welch's ANOVA", type="primary"):
            if len(groups_data) >= 2 and all(len(v) >= 2 for v in groups_data.values()):
            
                # Persiapan data
                all_data = []
                group_labels = []
                for name, data in groups_data.items():
                    all_data.extend(data)
                    group_labels.extend([name] * len(data))
            
                df = pd.DataFrame({'Nilai': all_data, 'Kelompok': group_labels})
            
                # Welch's ANOVA
                groups = [groups_data[name] for name in group_names]
                f_welch, p_welch, df1, df2 = welch_anova(*groups)
            
                # ANOVA Klasik untuk perbandingan
                f_classic, p_classic = stats.f_oneway(*groups)
            
                # Uji Asumsi
                # 1. Normalitas
                normality_results = {}
                for name, data in groups_data.items():
                    if len(data) >= 3:
                        _, p_norm = stats.shapiro(data)
                        normality_results[name] = p_norm
            
                # 2. Homogenitas Varians
                levene_stat, levene_p = stats.levene(*groups)
            
                # Hasil Utama
                st.markdown("---")
                st.subheader("📊 Hasil Welch's ANOVA")
            
                col1, col2, col3, col4 = st.columns(4)
                col1.metric("F-Welch", f"{f_welch:.4f}")
                col2.metric("P-Value", f"{p_welch:.6f}")
                col3.metric("df", f"({df1:.0f}, {df2:.2f})")
                col4.metric("Keputusan", "Tolak H₀" if p_welch < alpha else "Gagal Tolak H₀")
            
                # Interpretasi
                st.markdown("### 📝 Interpretasi")
                if p_welch < alpha:
                    st.success(f"""
                ✅ **Kesimpulan Welch's ANOVA**: Dengan α = {alpha}, terdapat perbedaan rata-rata 
                yang **signifikan** antar kelompok.
                
                - F-Welch = {f_welch:.4f}
                - P-value = {p_welch:.6f} < {alpha}
                - **Tolak H₀**: Minimal ada satu kelompok yang berbeda
                    """)
                else:
                    st.info(f"""
                ℹ️ **Kesimpulan Welch's ANOVA**: Dengan α = {alpha}, **tidak** terdapat perbedaan 
                rata-rata yang signifikan antar kelompok.
                
                - F-Welch = {f_welch:.4f}
                - P-value = {p_welch:.6f} ≥ {alpha}
                - **Gagal Tolak H₀**: Semua kelompok tidak berbeda secara signifikan
                """)
            
                # Perbandingan dengan ANOVA Klasik
                if compare_tests:
                    st.markdown("### ⚖️ Perbandingan: Welch's ANOVA vs ANOVA Klasik")
                
                    comparison_df = pd.DataFrame({
                    'Metode': ["Welch's ANOVA", 'ANOVA Klasik'],
                    'F-Statistik': [f"{f_welch:.4f}", f"{f_classic:.4f}"],
                    'P-Value': [f"{p_welch:.6f}", f"{p_classic:.6f}"],
                    'df': [f"({df1:.0f}, {df2:.2f})", f"({len(groups)-1}, {len(all_data)-len(groups)})"],
                    'Keputusan': [
                        "Tolak H₀" if p_welch < alpha else "Gagal Tolak H₀",
                        "Tolak H₀" if p_classic < alpha else "Gagal Tolak H₀"
                        ]
                    })
                    st.dataframe(comparison_df, use_container_width=True, hide_index=True)
                
                    # Analisis perbedaan
                    if abs(p_welch - p_classic) > 0.01:
                        st.warning(f"""
                    ⚠️ **Perbedaan signifikan** antara kedua metode!
                    
                    Selisih p-value: {abs(p_welch - p_classic):.6f}
                    
                    Ini menunjukkan bahwa heterogenitas varians mempengaruhi hasil analisis.
                    Welch's ANOVA lebih dapat dipercaya untuk data ini.
                    """)
                    else:
                        st.info("✓ Kedua metode memberikan hasil yang serupa. Varians relatif homogen.")
            
                # Uji Asumsi
                st.markdown("### 🔬 Uji Asumsi")
            
                col1, col2 = st.columns(2)
            
                with col1:
                    st.markdown("#### 1️⃣ Uji Normalitas (Shapiro-Wilk)")
                    norm_df = pd.DataFrame({
                    'Kelompok': list(normality_results.keys()),
                    'P-Value': [f"{p:.4f}" for p in normality_results.values()],
                    'Status': ['✅ Normal' if p >= 0.05 else '❌ Tidak Normal' 
                              for p in normality_results.values()]
                    })
                    st.dataframe(norm_df, use_container_width=True, hide_index=True)
                
                    all_normal = all(p >= 0.05 for p in normality_results.values())
                    if all_normal:
                        st.success("✅ Asumsi normalitas terpenuhi")
                    else:
                        st.error("❌ Beberapa kelompok tidak normal. Pertimbangkan Kruskal-Wallis.")
            
                with col2:
                    st.markdown("#### 2️⃣ Uji Homogenitas Varians (Levene)")
                    levene_df = pd.DataFrame({
                    'Statistik': [f"{levene_stat:.4f}"],
                    'P-Value': [f"{levene_p:.4f}"],
                    'Status': ['✅ Homogen' if levene_p >= 0.05 else '❌ Tidak Homogen']
                    })
                    st.dataframe(levene_df, use_container_width=True, hide_index=True)
                
                    if levene_p < 0.05:
                        st.success("✅ Varians tidak homogen → Welch's ANOVA adalah pilihan tepat!")
                    else:
                        st.info("ℹ️ Varians homogen → ANOVA klasik juga bisa digunakan")
            
                # Variance Ratio
                variances = [np.var(data, ddof=1) for data in groups]
                var_ratio = max(variances) / min(variances)
            
                st.markdown("#### 📊 Analisis Varians")
                st.metric("Rasio Varians (Max/Min)", f"{var_ratio:.2f}", 
                     help="Rasio > 3 menunjukkan heterogenitas varians yang signifikan")
            
                if var_ratio > 3:
                    st.warning(f"⚠️ Rasio varians = {var_ratio:.2f} > 3 → Heterogenitas tinggi! Welch's ANOVA sangat direkomendasikan.")
                elif var_ratio > 2:
                    st.info(f"ℹ️ Rasio varians = {var_ratio:.2f} → Heterogenitas sedang. Welch's ANOVA lebih aman.")
                else:
                    st.success(f"✅ Rasio varians = {var_ratio:.2f} → Varians relatif homogen.")
            
                # Statistik Deskriptif
                st.markdown("### 📈 Statistik Deskriptif")
                desc_stats = df.groupby('Kelompok')['Nilai'].agg([
                ('N', 'count'),
                ('Mean', 'mean'),
                ('Std Dev', 'std'),
                ('Varians', lambda x: np.var(x, ddof=1)),
                ('Min', 'min'),
                ('Max', 'max')
                ]).round(3)
                st.dataframe(desc_stats, use_container_width=True)
            
                # Games-Howell Post-hoc
                if show_posthoc and p_welch < alpha:
                    st.markdown("### 🎯 Games-Howell Post-hoc Test")
                    st.caption("Untuk mengetahui pasangan kelompok mana yang berbeda signifikan")
                
                    gh_results = games_howell_test(groups_data)
                    gh_results_display = gh_results.copy()
                    gh_results_display['Mean Diff'] = gh_results_display['Mean Diff'].round(3)
                    gh_results_display['t-statistic'] = gh_results_display['t-statistic'].round(4)
                    gh_results_display['df'] = gh_results_display['df'].round(2)
                    gh_results_display['p-value'] = gh_results_display['p-value'].round(4)
                
                    st.dataframe(gh_results_display, use_container_width=True, hide_index=True)
                
                    sig_pairs = gh_results[gh_results['p-value'] < 0.05]
                    if len(sig_pairs) > 0:
                        st.success(f"✅ Ditemukan {len(sig_pairs)} pasangan yang berbeda signifikan (p < 0.05)")
                    else:
                        st.info("ℹ️ Tidak ada pasangan yang berbeda signifikan pada level α = 0.05")
            
                # Visualisasi
                st.markdown("### 📊 Visualisasi Data")
            
                tab1, tab2, tab3 = st.tabs(["📦 Box Plot", "📊 Violin Plot", "📈 Variance Plot"])
            
                with tab1:
                    fig_box = px.box(df, x='Kelompok', y='Nilai', 
                                title='Box Plot - Distribusi Data per Kelompok',
                                color='Kelompok', points='all')
                    fig_box.add_hline(y=df['Nilai'].mean(), line_dash="dash", 
                                 line_color="red", annotation_text="Grand Mean")
                    fig_box.update_layout(showlegend=False, height=500)
                    st.plotly_chart(fig_box, use_container_width=True)
            
                with tab2:
                    fig_violin = px.violin(df, x='Kelompok', y='Nilai', 
                                      title='Violin Plot - Perhatikan Perbedaan Spread',
                                      color='Kelompok', box=True, points='all')
                    fig_violin.update_layout(showlegend=False, height=500)
                    st.plotly_chart(fig_violin, use_container_width=True)
            
                with tab3:
                    # Plot varians
                    var_df = pd.DataFrame({
                    'Kelompok': group_names,
                    'Varians': [np.var(groups_data[name], ddof=1) for name in group_names],
                    'Std Dev': [np.std(groups_data[name], ddof=1) for name in group_names]
                    })
                
                    fig_var = go.Figure()
                    fig_var.add_trace(go.Bar(
                    x=var_df['Kelompok'],
                    y=var_df['Varians'],
                    name='Varians',
                    marker_color='lightblue',
                    text=var_df['Varians'].round(2),
                    textposition='outside'
                    ))
                    fig_var.update_layout(
                    title='Perbandingan Varians antar Kelompok',
                    xaxis_title='Kelompok',
                    yaxis_title='Varians',
                    height=500,
                    showlegend=False
                    )
                    st.plotly_chart(fig_var, use_container_width=True)
                
                    st.caption("💡 Perbedaan tinggi varians menunjukkan heterogenitas varians (alasan pakai Welch's ANOVA)")
            
            else:
                st.error("⚠️ Setiap kelompok harus memiliki minimal 2 data!")

    # ============ MENU SIMULASI DATA ============
    elif menu == "📈 Simulasi Data":
        st.header("📈 Simulasi Data - Generate Data dengan Varians Berbeda")
    
        st.markdown("Generate data dengan varians yang berbeda untuk demonstrasi Welch's ANOVA")
    
        col1, col2, col3 = st.columns(3)
    
        with col1:
            num_groups_sim = st.slider("Jumlah Kelompok", 2, 6, 3)
            samples_per_group = st.slider("Sampel per Kelompok", 10, 100, 30)
    
        with col2:
            mean_start = st.number_input("Mean Kelompok Pertama", value=50.0, step=1.0)
            mean_increment = st.number_input("Kenaikan Mean antar Kelompok", value=5.0, step=1.0)
    
        with col3:
            std_start = st.number_input("Std Dev Kelompok Pertama", value=5.0, step=1.0)
            std_multiplier = st.slider("Multiplier Std Dev", 1.0, 5.0, 2.0, 0.5,
                                   help="Setiap kelompok std dev dikali faktor ini")
            alpha_sim = st.selectbox("Tingkat Signifikansi (α)", [0.01, 0.05, 0.10], index=1)
    
        seed_sim = st.number_input("Random Seed", value=42, step=1, key="seed_sim")
    
        if st.button("🎲 Generate & Analisis", type="primary"):
            np.random.seed(seed_sim)
        
            # Generate data
            groups_sim = []
            group_names_sim = []
            all_data_sim = []
            all_labels_sim = []
        
            for i in range(num_groups_sim):
                mean = mean_start + (i * mean_increment)
                std = std_start * (std_multiplier ** i)
            
                data = np.random.normal(mean, std, samples_per_group)
            
                groups_sim.append(data)
                group_name = f"Kelompok {i+1}"
                group_names_sim.append(group_name)
                all_data_sim.extend(data)
                all_labels_sim.extend([group_name] * samples_per_group)
        
            df_sim = pd.DataFrame({'Nilai': all_data_sim, 'Kelompok': all_labels_sim})
        
            # Analisis
            f_welch_sim, p_welch_sim, df1_sim, df2_sim = welch_anova(*groups_sim)
            f_classic_sim, p_classic_sim = stats.f_oneway(*groups_sim)
        
            # Uji Asumsi
            normality_sim = {}
            for i, data in enumerate(groups_sim):
                _, p_norm = stats.shapiro(data)
                normality_sim[group_names_sim[i]] = p_norm
        
            levene_stat_sim, levene_p_sim = stats.levene(*groups_sim)
        
            # Hasil
            st.markdown("---")
            st.subheader("📊 Hasil Simulasi Welch's ANOVA")
        
            col1, col2, col3, col4 = st.columns(4)
            col1.metric("F-Welch", f"{f_welch_sim:.4f}")
            col2.metric("P-Value", f"{p_welch_sim:.6f}")
            col3.metric("df", f"({df1_sim:.0f}, {df2_sim:.2f})")
            col4.metric("Keputusan", "Tolak H₀" if p_welch_sim < alpha_sim else "Gagal Tolak H₀")
        
            # Interpretasi
            st.markdown("### 📝 Interpretasi")
            if p_welch_sim < alpha_sim:
                st.success(f"""
            ✅ **Kesimpulan**: Dengan α = {alpha_sim}, terdapat perbedaan rata-rata yang **signifikan** 
            antar kelompok (p = {p_welch_sim:.6f} < {alpha_sim}).
            """)
            else:
                st.info(f"""
            ℹ️ **Kesimpulan**: Dengan α = {alpha_sim}, **tidak** terdapat perbedaan rata-rata 
            yang signifikan antar kelompok (p = {p_welch_sim:.6f} ≥ {alpha_sim}).
            """)
        
            # Perbandingan Metode
            st.markdown("### ⚖️ Perbandingan: Welch's ANOVA vs ANOVA Klasik")
        
            comparison_sim = pd.DataFrame({
            'Metode': ["Welch's ANOVA", 'ANOVA Klasik'],
            'F-Statistik': [f"{f_welch_sim:.4f}", f"{f_classic_sim:.4f}"],
            'P-Value': [f"{p_welch_sim:.6f}", f"{p_classic_sim:.6f}"],
            'Keputusan (α=0.05)': [
                "Tolak H₀" if p_welch_sim < 0.05 else "Gagal Tolak H₀",
                "Tolak H₀" if p_classic_sim < 0.05 else "Gagal Tolak H₀"
            ]
            })
            st.dataframe(comparison_sim, use_container_width=True, hide_index=True)
        
            # Analisis perbedaan
            p_diff = abs(p_welch_sim - p_classic_sim)
            if p_diff > 0.01:
                st.warning(f"""
            ⚠️ **Perbedaan Signifikan!**
            
            Selisih p-value: {p_diff:.6f}
            
            Ini disebabkan oleh heterogenitas varians yang tinggi. Welch's ANOVA memberikan 
            hasil yang lebih akurat dalam kondisi ini.
            """)
            else:
                st.info(f"ℹ️ Selisih p-value kecil ({p_diff:.6f}). Kedua metode memberikan hasil serupa.")
        
            # Uji Asumsi
            st.markdown("### 🔬 Hasil Uji Asumsi")
        
            col1, col2 = st.columns(2)
        
            with col1:
                st.markdown("#### Normalitas (Shapiro-Wilk)")
                norm_df_sim = pd.DataFrame({
                'Kelompok': list(normality_sim.keys()),
                'P-Value': [f"{p:.4f}" for p in normality_sim.values()],
                'Status': ['✅ Normal' if p >= 0.05 else '❌ Tidak Normal' 
                          for p in normality_sim.values()]
                })
                st.dataframe(norm_df_sim, use_container_width=True, hide_index=True)
        
            with col2:
                st.markdown("#### Homogenitas (Levene)")
                st.metric("Levene Statistik", f"{levene_stat_sim:.4f}")
                st.metric("P-Value", f"{levene_p_sim:.4f}")
                if levene_p_sim < 0.05:
                    st.error("❌ Varians TIDAK homogen")
                    st.success("✅ Welch's ANOVA adalah pilihan yang tepat!")
                else:
                    st.success("✅ Varians homogen")
                    st.info("ℹ️ ANOVA klasik juga bisa digunakan")
        
            # Variance Ratio
            variances_sim = [np.var(data, ddof=1) for data in groups_sim]
            var_ratio_sim = max(variances_sim) / min(variances_sim)
        
            st.markdown("#### 📊 Analisis Variabilitas")
            col1, col2, col3 = st.columns(3)
            col1.metric("Varians Terkecil", f"{min(variances_sim):.2f}")
            col2.metric("Varians Terbesar", f"{max(variances_sim):.2f}")
            col3.metric("Rasio (Max/Min)", f"{var_ratio_sim:.2f}")
        
            if var_ratio_sim > 3:
                st.error(f"❌ Rasio varians = {var_ratio_sim:.2f} > 3 → Heterogenitas TINGGI")
            elif var_ratio_sim > 2:
                st.warning(f"⚠️ Rasio varians = {var_ratio_sim:.2f} > 2 → Heterogenitas SEDANG")
            else:
                st.success(f"✅ Rasio varians = {var_ratio_sim:.2f} ≤ 2 → Relatif homogen")
        
            # Statistik Deskriptif
            st.markdown("### 📈 Statistik Deskriptif")
            desc_sim = df_sim.groupby('Kelompok')['Nilai'].agg([
            ('N', 'count'),
            ('Mean', 'mean'),
            ('Std Dev', 'std'),
            ('Varians', lambda x: np.var(x, ddof=1)),
            ('Min', 'min'),
            ('Max', 'max')
            ]).round(3)
            st.dataframe(desc_sim, use_container_width=True)
        
            # Visualisasi
            st.markdown("### 📊 Visualisasi Data")
        
            tab1, tab2, tab3, tab4 = st.tabs(["📦 Box Plot", "📊 Violin Plot", "📈 Variance Chart", "🔔 Distribution"])
        
            with tab1:
                fig_box = px.box(df_sim, x='Kelompok', y='Nilai', 
                            title='Box Plot - Perhatikan Perbedaan Spread',
                            color='Kelompok', points='all')
                fig_box.update_layout(showlegend=False, height=500)
                st.plotly_chart(fig_box, use_container_width=True)
        
            with tab2:
                fig_violin = px.violin(df_sim, x='Kelompok', y='Nilai', 
                                  title='Violin Plot - Variabilitas Berbeda',
                                  color='Kelompok', box=True, points='all')
                fig_violin.update_layout(showlegend=False, height=500)
                st.plotly_chart(fig_violin, use_container_width=True)
        
            with tab3:
                var_data = pd.DataFrame({
                'Kelompok': group_names_sim,
                'Varians': variances_sim,
                'Std Dev': [np.std(data, ddof=1) for data in groups_sim]
                })
            
                fig_var = make_subplots(specs=[[{"secondary_y": True}]])
            
                fig_var.add_trace(
                    go.Bar(x=var_data['Kelompok'], y=var_data['Varians'], 
                      name='Varians', marker_color='lightblue'),
                    secondary_y=False
                )
            
                fig_var.add_trace(
                go.Scatter(x=var_data['Kelompok'], y=var_data['Std Dev'], 
                          name='Std Dev', mode='lines+markers', 
                          line=dict(color='red', width=3)),
                secondary_y=True
                )
            
                fig_var.update_layout(title='Perbandingan Varians dan Std Dev', height=500)
                fig_var.update_xaxes(title_text="Kelompok")
                fig_var.update_yaxes(title_text="Varians", secondary_y=False)
                fig_var.update_yaxes(title_text="Std Dev", secondary_y=True)
            
                st.plotly_chart(fig_var, use_container_width=True)
        
            with tab4:
                fig_hist = px.histogram(df_sim, x='Nilai', color='Kelompok', 
                                   title='Distribusi Frekuensi - Perhatikan Spread',
                                   marginal='box', barmode='overlay', opacity=0.6,
                                   nbins=30)
                fig_hist.update_layout(height=500)
                st.plotly_chart(fig_hist, use_container_width=True)
        
            # Download
            st.markdown("### 💾 Download Data")
            csv_sim = df_sim.to_csv(index=False)
            st.download_button(
            label="📥 Download Data CSV",
            data=csv_sim,
            file_name="welch_anova_simulation.csv",
            mime="text/csv"
            )

    # ============ MENU PERBANDINGAN UJI ============
    else:
        st.header("⚖️ Perbandingan Uji: ANOVA vs Welch's vs Kruskal-Wallis")
    
        st.markdown("""
    Panduan memilih uji statistik yang tepat untuk membandingkan lebih dari 2 kelompok
    """)
    
        # Flowchart
        st.subheader("🌳 Decision Tree: Memilih Uji yang Tepat")
    
        st.markdown("""
    ```
    Apakah data berdistribusi NORMAL? (Uji Shapiro-Wilk)
    │
    ├─ YA ✓ → Apakah varians HOMOGEN? (Uji Levene)
    │         │
    │         ├─ YA ✓ → Gunakan ANOVA KLASIK
    │         │         (Paling powerful jika asumsi terpenuhi)
    │         │
    │         └─ TIDAK ✗ → Gunakan WELCH'S ANOVA
    │                      (Robust terhadap heterogenitas varians)
    │
    └─ TIDAK ✗ → Gunakan KRUSKAL-WALLIS
                  (Uji non-parametrik, tidak perlu normalitas)
    ```
    """)
    
        # Tabel Perbandingan Detail
        st.subheader("📊 Tabel Perbandingan Lengkap")
    
        comparison_table = pd.DataFrame({
        'Aspek': [
            'Asumsi Normalitas',
            'Asumsi Homogenitas Varians',
            'Jenis Uji',
            'Ukuran Sampel',
            'Sensitif terhadap Outlier',
            'Power (jika asumsi terpenuhi)',
            'Robust',
            'Post-hoc Test',
            'Interpretasi',
            'Kapan Digunakan'
        ],
        'ANOVA Klasik': [
            '✅ Diperlukan',
            '✅ Diperlukan',
            'Parametrik',
            'Bebas (ideal n≥30)',
            '⚠️ Sangat sensitif',
            '⭐⭐⭐⭐⭐ (Tertinggi)',
            '❌ Tidak robust',
            'Tukey HSD, Bonferroni',
            'Perbedaan rata-rata',
            'Data normal & varians homogen'
        ],
        "Welch's ANOVA": [
            '✅ Diperlukan',
            '❌ TIDAK diperlukan',
            'Parametrik',
            'Bebas (ideal n≥30)',
            '⚠️ Cukup sensitif',
            '⭐⭐⭐⭐ (Tinggi)',
            '✅ Robust thd heterogenitas',
            'Games-Howell, Dunnett T3',
            'Perbedaan rata-rata',
            'Data normal, varians TIDAK homogen'
        ],
        'Kruskal-Wallis': [
            '❌ TIDAK diperlukan',
            '❌ TIDAK diperlukan',
            'Non-parametrik',
            'Bebas (lebih baik n≥5)',
            '✅ Robust terhadap outlier',
            '⭐⭐⭐ (Sedang)',
            '✅ Sangat robust',
            "Dunn's test, Mann-Whitney",
            'Perbedaan median/distribusi',
            'Data TIDAK normal atau ordinal'
        ]
        })
    
        st.dataframe(comparison_table, use_container_width=True, hide_index=True)
    
        # Contoh Kasus
        st.subheader("📚 Contoh Kasus Penggunaan")
    
        col1, col2, col3 = st.columns(3)
    
        with col1:
            st.markdown("""
        ### ANOVA Klasik
        
        **Contoh:**
        Membandingkan tinggi tanaman dari 3 jenis pupuk
        
        **Kondisi:**
        - Data tinggi berdistribusi normal
        - Varians ketiga kelompok homogen
        - Tidak ada outlier ekstrem
        
        **Hasil:**
        Dapat mendeteksi perbedaan kecil dengan power tinggi
        """)
    
        with col2:
            st.markdown("""
        ### Welch's ANOVA
        
        **Contoh:**
        Membandingkan gaji karyawan dari 4 departemen
        
        **Kondisi:**
        - Data gaji berdistribusi normal
        - Varians sangat berbeda (accounting vs marketing)
        - Ukuran sampel berbeda per departemen
        
        **Hasil:**
        Hasil lebih akurat dibanding ANOVA klasik
        """)
    
        with col3:
            st.markdown("""
        ### Kruskal-Wallis
        
        **Contoh:**
        Membandingkan skor kepuasan pelanggan (skala 1-5)
        
        **Kondisi:**
        - Data ordinal (skala Likert)
        - Data skewed (tidak normal)
        - Ada outlier
        
        **Hasil:**
        Tidak terpengaruh oleh outlier atau bentuk distribusi
        """)
    
        # Simulasi Perbandingan
        st.subheader("🧪 Simulasi Perbandingan")
        st.markdown("Bandingkan ketiga metode dengan data yang sama")
    
        col1, col2 = st.columns(2)
    
        with col1:
            scenario = st.selectbox(
            "Pilih Skenario",
            [
                "Varians Homogen & Normal",
                "Varians Heterogen & Normal",
                "Varians Homogen & Tidak Normal",
                "Varians Heterogen & Tidak Normal"
            ]
            )
    
        with col2:
            n_per_group = st.slider("Sampel per Kelompok", 10, 100, 30, key="comp_n")
    
        if st.button("🔍 Jalankan Perbandingan", type="primary"):
            np.random.seed(42)
        
            if scenario == "Varians Homogen & Normal":
                g1 = np.random.normal(50, 10, n_per_group)
                g2 = np.random.normal(55, 10, n_per_group)
                g3 = np.random.normal(60, 10, n_per_group)
            elif scenario == "Varians Heterogen & Normal":
                g1 = np.random.normal(50, 5, n_per_group)
                g2 = np.random.normal(55, 15, n_per_group)
                g3 = np.random.normal(60, 25, n_per_group)
            elif scenario == "Varians Homogen & Tidak Normal":
                g1 = np.random.exponential(50, n_per_group)
                g2 = np.random.exponential(55, n_per_group)
                g3 = np.random.exponential(60, n_per_group)
            else:  # Heterogen & Tidak Normal
                g1 = np.random.exponential(30, n_per_group)
                g2 = np.random.exponential(50, n_per_group) * 1.5
                g3 = np.random.chisquare(5, n_per_group) * 10
        
            # Uji semua metode
            f_classic, p_classic = stats.f_oneway(g1, g2, g3)
            f_welch, p_welch, df1, df2 = welch_anova(g1, g2, g3)
            h_kw, p_kw = stats.kruskal(g1, g2, g3)
        
            # Uji asumsi
            _, p_norm1 = stats.shapiro(g1)
            _, p_norm2 = stats.shapiro(g2)
            _, p_norm3 = stats.shapiro(g3)
            _, p_levene = stats.levene(g1, g2, g3)
        
            st.markdown("---")
            st.markdown("### 📊 Hasil Perbandingan")
        
            results_comp = pd.DataFrame({
            'Metode': ['ANOVA Klasik', "Welch's ANOVA", 'Kruskal-Wallis'],
            'Statistik': [f"F = {f_classic:.4f}", f"F = {f_welch:.4f}", f"H = {h_kw:.4f}"],
            'P-Value': [f"{p_classic:.6f}", f"{p_welch:.6f}", f"{p_kw:.6f}"],
            'Keputusan': [
                "Tolak H₀" if p_classic < 0.05 else "Gagal Tolak H₀",
                "Tolak H₀" if p_welch < 0.05 else "Gagal Tolak H₀",
                "Tolak H₀" if p_kw < 0.05 else "Gagal Tolak H₀"
            ]
            })
            st.dataframe(results_comp, use_container_width=True, hide_index=True)
        
            # Cek asumsi
            st.markdown("### 🔬 Pemeriksaan Asumsi")
        
            col1, col2 = st.columns(2)
        
            with col1:
                st.markdown("#### Normalitas")
                st.metric("Kelompok 1 (p-value)", f"{p_norm1:.4f}", 
                     "✅ Normal" if p_norm1 >= 0.05 else "❌ Tidak Normal")
                st.metric("Kelompok 2 (p-value)", f"{p_norm2:.4f}",
                     "✅ Normal" if p_norm2 >= 0.05 else "❌ Tidak Normal")
                st.metric("Kelompok 3 (p-value)", f"{p_norm3:.4f}",
                     "✅ Normal" if p_norm3 >= 0.05 else "❌ Tidak Normal")
        
            with col2:
                st.markdown("#### Homogenitas Varians")
                st.metric("Levene Test (p-value)", f"{p_levene:.4f}",
                     "✅ Homogen" if p_levene >= 0.05 else "❌ Heterogen")
            
                var_ratio_comp = max(np.var(g1), np.var(g2), np.var(g3)) / min(np.var(g1), np.var(g2), np.var(g3))
                st.metric("Rasio Varians", f"{var_ratio_comp:.2f}",
                     "✅ Homogen" if var_ratio_comp < 3 else "❌ Heterogen")
        
            # Rekomendasi
            st.markdown("### 🎯 Rekomendasi")
        
            all_normal = p_norm1 >= 0.05 and p_norm2 >= 0.05 and p_norm3 >= 0.05
            homogen = p_levene >= 0.05
        
            if all_normal and homogen:
                st.success("""
            ✅ **GUNAKAN ANOVA KLASIK**
            
            - Data berdistribusi normal
            - Varians homogen
            - Akan memberikan power tertinggi
            """)
            elif all_normal and not homogen:
                st.warning("""
            ⚠️ **GUNAKAN WELCH'S ANOVA**
            
            - Data berdistribusi normal
            - Varians TIDAK homogen
            - Lebih akurat dari ANOVA klasik untuk kasus ini
            """)
            else:
                st.info("""
            📊 **GUNAKAN KRUSKAL-WALLIS**
            
            - Data TIDAK berdistribusi normal
            - Uji non-parametrik lebih tepat
            - Tidak terpengaruh bentuk distribusi
            """)

    # Footer
    st.markdown("---")
    st.markdown("""
<div style='text-align: center; color: gray;'>
    <p>📊 Aplikasi Pembelajaran Welch's ANOVA | ANOVA untuk Varians Tidak Homogen</p>
    <p style='font-size: 0.8em;'>💡 Alternatif robust untuk ANOVA klasik ketika asumsi homogenitas varians tidak terpenuhi</p>
</div>
""", unsafe_allow_html=True)

def tampilkan_materi27():
    # CSS untuk styling
    st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #2c3e50;
        margin-top: 2rem;
    }
    .info-box {
        background-color: #e3f2fd;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #1f77b4;
        margin: 1rem 0;
        color:black;
    }
    .warning-box {
        background-color: #fff3cd;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #ffc107;
        margin: 1rem 0;
        color: black;
    }
    .success-box {
        background-color: #d4edda;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #28a745;
        margin: 1rem 0;
        color: black;
    }
</style>
""", unsafe_allow_html=True)

    # Fungsi untuk Tukey HSD
    def tukey_hsd(data_groups, group_names, alpha=0.05):
        """Melakukan uji Tukey HSD"""
        results = []
        n_groups = len(data_groups)
        n_total = sum(len(g) for g in data_groups)
    
        # Hitung MSE (Mean Square Error) dari ANOVA
        all_data = np.concatenate(data_groups)
        group_labels = np.concatenate([[i]*len(g) for i, g in enumerate(data_groups)])
    
        # ANOVA untuk mendapatkan MSE
        f_stat, p_val = f_oneway(*data_groups)
    
        # Hitung SSW (Sum of Squares Within)
        grand_mean = np.mean(all_data)
        ssw = sum(np.sum((g - np.mean(g))**2) for g in data_groups)
        dfw = n_total - n_groups
        mse = ssw / dfw
    
        # Hitung q kritis (menggunakan aproksimasi)
        q_crit = stats.studentized_range.ppf(1-alpha, n_groups, dfw)
    
        # Bandingkan semua pasangan
        for i, j in combinations(range(n_groups), 2):
            mean_i = np.mean(data_groups[i])
            mean_j = np.mean(data_groups[j])
            n_i = len(data_groups[i])
            n_j = len(data_groups[j])
        
            # Hitung HSD
            diff = abs(mean_i - mean_j)
            se = np.sqrt(mse * (1/n_i + 1/n_j))
            hsd = q_crit * se
        
            is_significant = diff > hsd
        
            results.append({
            'Kelompok 1': group_names[i],
            'Kelompok 2': group_names[j],
            'Mean 1': mean_i,
            'Mean 2': mean_j,
            'Selisih': diff,
            'HSD': hsd,
            'Signifikan': 'Ya' if is_significant else 'Tidak',
            'p-value': '<0.05' if is_significant else '>0.05'
            })
    
        return pd.DataFrame(results)

    # Fungsi untuk Bonferroni
    def bonferroni_test(data_groups, group_names, alpha=0.05):
        """Melakukan uji Bonferroni"""
        results = []
        n_comparisons = len(list(combinations(range(len(data_groups)), 2)))
        adjusted_alpha = alpha / n_comparisons
    
        for i, j in combinations(range(len(data_groups)), 2):
            t_stat, p_val = stats.ttest_ind(data_groups[i], data_groups[j])
            is_significant = p_val < adjusted_alpha
        
            results.append({
            'Kelompok 1': group_names[i],
            'Kelompok 2': group_names[j],
            'Mean 1': np.mean(data_groups[i]),
            'Mean 2': np.mean(data_groups[j]),
            'Selisih': abs(np.mean(data_groups[i]) - np.mean(data_groups[j])),
            't-statistic': t_stat,
            'p-value': p_val,
            'α terkoreksi': adjusted_alpha,
            'Signifikan': 'Ya' if is_significant else 'Tidak'
            })
    
        return pd.DataFrame(results)

    # Fungsi untuk LSD (Least Significant Difference)
    def lsd_test(data_groups, group_names, alpha=0.05):
        """Melakukan uji LSD"""
        results = []
        n_groups = len(data_groups)
        n_total = sum(len(g) for g in data_groups)
    
        # Hitung MSE
        all_data = np.concatenate(data_groups)
        ssw = sum(np.sum((g - np.mean(g))**2) for g in data_groups)
        dfw = n_total - n_groups
        mse = ssw / dfw
    
        t_crit = stats.t.ppf(1-alpha/2, dfw)
    
        for i, j in combinations(range(n_groups), 2):
            mean_i = np.mean(data_groups[i])
            mean_j = np.mean(data_groups[j])
            n_i = len(data_groups[i])
            n_j = len(data_groups[j])
        
            diff = abs(mean_i - mean_j)
            se = np.sqrt(mse * (1/n_i + 1/n_j))
            lsd = t_crit * se
        
            is_significant = diff > lsd
        
            results.append({
            'Kelompok 1': group_names[i],
            'Kelompok 2': group_names[j],
            'Mean 1': mean_i,
            'Mean 2': mean_j,
            'Selisih': diff,
            'LSD': lsd,
            'Signifikan': 'Ya' if is_significant else 'Tidak'
            })
    
        return pd.DataFrame(results)

    # Sidebar untuk navigasi
    st.sidebar.title("📚 Navigasi")
    menu = st.sidebar.radio(
    "Pilih Menu:",
    ["🏠 Beranda", "📖 Materi", "🎯 Simulasi Interaktif", "📊 Upload Data", "ℹ️ Tentang"]
    )

    # BERANDA
    if menu == "🏠 Beranda":
        st.markdown("<h1 class='main-header'>📊 Uji Post-hoc untuk ANOVA 1 Jalur</h1>", unsafe_allow_html=True)
    
        col1, col2, col3 = st.columns(3)
    
        with col1:
            st.markdown("""
        <div class='info-box'>
            <h3>🎓 Belajar Teori</h3>
            <p>Pelajari konsep dasar ANOVA dan uji Post-hoc dengan penjelasan lengkap dan contoh.</p>
        </div>
        """, unsafe_allow_html=True)
    
        with col2:
            st.markdown("""
        <div class='info-box'>
            <h3>🔬 Simulasi</h3>
            <p>Lakukan simulasi interaktif dengan data yang dapat Anda atur sendiri.</p>
        </div>
        """, unsafe_allow_html=True)
    
        with col3:
            st.markdown("""
        <div class='info-box'>
            <h3>📁 Upload Data</h3>
            <p>Analisis data Anda sendiri dengan berbagai metode Post-hoc.</p>
        </div>
        """, unsafe_allow_html=True)
    
        st.markdown("---")
    
        st.markdown("""
    ## Apa itu Uji Post-hoc?
    
    Uji Post-hoc adalah uji lanjutan yang dilakukan **setelah** ANOVA menunjukkan hasil yang signifikan. 
    ANOVA hanya memberitahu kita bahwa ada perbedaan di antara kelompok, tetapi tidak menjelaskan 
    kelompok mana yang berbeda. Di sinilah uji Post-hoc berperan!
    
    ### Kapan Menggunakan Uji Post-hoc?
    - ✅ Setelah ANOVA 1 jalur menunjukkan p-value < 0.05
    - ✅ Ketika memiliki 3 atau lebih kelompok untuk dibandingkan
    - ✅ Untuk mengidentifikasi pasangan kelompok mana yang berbeda secara signifikan
        """)

    # MATERI
    elif menu == "📖 Materi":
        st.markdown("<h1 class='main-header'>📖 Materi Pembelajaran</h1>", unsafe_allow_html=True)
    
        tab1, tab2, tab3, tab4 = st.tabs(["🔍 ANOVA Dasar", "📐 Metode Post-hoc", "🧮 Contoh Perhitungan", "💡 Tips Pemilihan"])
    
        with tab1:
            st.markdown("## 🔍 ANOVA 1 Jalur (One-Way ANOVA)")
        
            st.markdown("""
        ### Definisi
        ANOVA (Analysis of Variance) adalah uji statistik untuk membandingkan rata-rata dari **tiga atau lebih kelompok** independen.
        
        ### Hipotesis
        - **H₀**: μ₁ = μ₂ = μ₃ = ... (Semua rata-rata kelompok sama)
        - **H₁**: Setidaknya ada satu rata-rata yang berbeda
        
        ### Asumsi ANOVA
        1. **Independensi**: Observasi dalam setiap kelompok independen
        2. **Normalitas**: Data dalam setiap kelompok terdistribusi normal
        3. **Homogenitas Varians**: Varians antar kelompok homogen (sama)
        
        ### Formula F-statistik
            """)
        
            st.latex(r"F = \frac{MS_{between}}{MS_{within}} = \frac{SS_{between}/(k-1)}{SS_{within}/(N-k)}")
        
            st.markdown("""
        Di mana:
        - k = jumlah kelompok
        - N = total jumlah observasi
        - SS = Sum of Squares
        - MS = Mean Square
            """)
    
        with tab2:
            st.markdown("## 📐 Metode Uji Post-hoc")
        
            col1, col2 = st.columns(2)
        
            with col1:
                st.markdown("""
            ### 1️⃣ Tukey HSD (Honest Significant Difference)
            
            **Karakteristik:**
            - Paling populer dan banyak digunakan
            - Mengontrol family-wise error rate
            - Konservatif namun powerful
            
            **Rumus:**
            """)
            st.latex(r"HSD = q_{\alpha} \times \sqrt{\frac{MS_{within}}{n}}")
            
            st.markdown("""
            **Kapan Digunakan:**
            - ✅ Ukuran sampel sama atau hampir sama
            - ✅ Membandingkan semua pasangan kelompok
            - ✅ Ingin keseimbangan antara Type I dan Type II error
            """)
        
            with col2:
                st.markdown("""
            ### 2️⃣ Bonferroni
            
            **Karakteristik:**
            - Sangat konservatif
            - Mudah dipahami dan dihitung
            - Koreksi alpha untuk multiple comparisons
            
            **Rumus:**
            """)
                st.latex(r"\alpha_{adjusted} = \frac{\alpha}{m}")
            
                st.markdown("""
            Di mana m = jumlah perbandingan
            
            **Kapan Digunakan:**
            - ✅ Jumlah perbandingan sedikit
            - ✅ Ingin sangat yakin (menghindari False Positive)
            - ✅ Ukuran sampel besar
            """)
        
                st.markdown("---")
        
            col3, col4 = st.columns(2)
        
            with col3:
                st.markdown("""
            ### 3️⃣ LSD (Least Significant Difference)
            
            **Karakteristik:**
            - Paling liberal (kurang konservatif)
            - Tidak mengkoreksi untuk multiple comparisons
            - Power statistik tinggi
            
            **Rumus:**
            """)
                st.latex(r"LSD = t_{\alpha/2} \times \sqrt{MS_{within} \times (\frac{1}{n_i} + \frac{1}{n_j})}")
            
                st.markdown("""
            **Kapan Digunakan:**
            - ✅ Perbandingan sudah direncanakan (planned comparisons)
            - ✅ Jumlah perbandingan sangat sedikit
            - ⚠️ Hati-hati: Risiko Type I error lebih tinggi
            """)
        
            with col4:
                st.markdown("""
            ### 4️⃣ Scheffé
            
            **Karakteristik:**
            - Paling konservatif
            - Dapat digunakan untuk semua jenis perbandingan
            - Fleksibel untuk perbandingan kompleks
            
            **Kapan Digunakan:**
            - ✅ Perbandingan tidak direncanakan sebelumnya
            - ✅ Ingin melakukan perbandingan kompleks
            - ✅ Ukuran sampel tidak sama
            """)
    
        with tab3:
            st.markdown("## 🧮 Contoh Perhitungan")
        
            st.markdown("""
        ### Studi Kasus: Efektivitas Metode Belajar
        
        Seorang peneliti ingin mengetahui apakah ada perbedaan nilai ujian dari 3 metode belajar berbeda.
        """)
        
            # Data contoh
            metode_a = [85, 88, 90, 87, 89]
            metode_b = [78, 80, 79, 82, 81]
            metode_c = [92, 94, 93, 95, 91]
        
            df_example = pd.DataFrame({
            'Metode A (Visual)': metode_a,
            'Metode B (Audio)': metode_b,
            'Metode C (Kinestetik)': metode_c
            })
        
            st.dataframe(df_example, use_container_width=True)
        
            # Langkah 1: ANOVA
            st.markdown("### Langkah 1: Uji ANOVA")
            f_stat, p_val = f_oneway(metode_a, metode_b, metode_c)
        
            col1, col2 = st.columns(2)
            with col1:
                st.metric("F-statistic", f"{f_stat:.4f}")
            with col2:
                st.metric("p-value", f"{p_val:.6f}")
        
            if p_val < 0.05:
                st.markdown("""
            <div class='success-box'>
                ✅ <b>Hasil ANOVA Signifikan!</b> (p < 0.05)<br>
                Ada perbedaan signifikan di antara metode belajar. Lanjutkan dengan uji Post-hoc.
            </div>
                """, unsafe_allow_html=True)
            
                # Langkah 2: Post-hoc
                st.markdown("### Langkah 2: Uji Post-hoc (Tukey HSD)")
            
                data_groups = [metode_a, metode_b, metode_c]
                group_names = ['Metode A', 'Metode B', 'Metode C']
            
                results_tukey = tukey_hsd(data_groups, group_names)
                st.dataframe(results_tukey.round(3), use_container_width=True)
            
                # Visualisasi
                fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
            
                # Boxplot
                data_long = []
                for name, data in zip(group_names, data_groups):
                    for val in data:
                        data_long.append({'Metode': name, 'Nilai': val})
                df_long = pd.DataFrame(data_long)
            
                sns.boxplot(data=df_long, x='Metode', y='Nilai', ax=ax1, palette='Set2')
                ax1.set_title('Distribusi Nilai per Metode Belajar', fontsize=14, fontweight='bold')
                ax1.set_ylabel('Nilai Ujian')
                ax1.grid(axis='y', alpha=0.3)
            
                # Bar plot dengan error bars
                means = [np.mean(d) for d in data_groups]
                stds = [np.std(d) for d in data_groups]
            
                bars = ax2.bar(group_names, means, yerr=stds, capsize=5, 
                          color=['#66c2a5', '#fc8d62', '#8da0cb'], alpha=0.7, edgecolor='black')
                ax2.set_ylabel('Rata-rata Nilai')
                ax2.set_title('Perbandingan Rata-rata Nilai', fontsize=14, fontweight='bold')
                ax2.grid(axis='y', alpha=0.3)
            
                # Tambahkan nilai di atas bar
                for bar, mean in zip(bars, means):
                    height = bar.get_height()
                    ax2.text(bar.get_x() + bar.get_width()/2., height,
                        f'{mean:.1f}', ha='center', va='bottom', fontweight='bold')
            
                plt.tight_layout()
                st.pyplot(fig)
            
                st.markdown("""
            ### Interpretasi:
            Berdasarkan hasil Tukey HSD, kita dapat melihat pasangan metode belajar mana yang memiliki 
            perbedaan signifikan. Metode dengan selisih > HSD dianggap berbeda secara signifikan.
            """)
    
        with tab4:
            st.markdown("## 💡 Tips Pemilihan Metode Post-hoc")
        
            st.markdown("""
            ### Diagram Alur Pemilihan Metode
            """)
        
            # Flowchart sederhana
            st.markdown("""
        ```
        Mulai
          │
          ├─→ Perbandingan sudah direncanakan? 
          │   ├─→ Ya → Gunakan LSD atau Perbandingan Terencana
          │   └─→ Tidak → Lanjut
          │
          ├─→ Ukuran sampel sama?
          │   ├─→ Ya → Tukey HSD (Rekomendasi)
          │   └─→ Tidak → Games-Howell atau Dunnett's T3
          │
          ├─→ Jumlah perbandingan sedikit?
          │   ├─→ Ya → Bonferroni
          │   └─→ Banyak → Tukey HSD
          │
          └─→ Perlu sangat konservatif?
              ├─→ Ya → Scheffé atau Bonferroni
              └─→ Tidak → Tukey HSD
        ```
        """)
        
            st.markdown("---")
        
            # Tabel perbandingan
            comparison_df = pd.DataFrame({
            'Metode': ['Tukey HSD', 'Bonferroni', 'LSD', 'Scheffé'],
            'Konservatisme': ['Sedang', 'Tinggi', 'Rendah', 'Sangat Tinggi'],
            'Power': ['Tinggi', 'Sedang', 'Sangat Tinggi', 'Rendah'],
            'Ukuran Sampel': ['Sama/Mirip', 'Bebas', 'Bebas', 'Berbeda'],
            'Rekomendasi': ['Umum', 'Sedikit perbandingan', 'Planned', 'Kompleks']
            })
        
            st.markdown("### 📊 Tabel Perbandingan Metode")
            st.dataframe(comparison_df, use_container_width=True)
        
            st.markdown("""
        ### 🎯 Rekomendasi Umum:
        
        1. **Sebagian besar kasus**: Gunakan **Tukey HSD**
           - Keseimbangan baik antara Type I dan Type II error
           - Cocok untuk hampir semua situasi dengan ukuran sampel yang sama
        
        2. **Sangat menghindari False Positive**: Gunakan **Bonferroni**
           - Penelitian medis atau klinik
           - Konsekuensi error sangat serius
        
        3. **Perbandingan terencana**: Gunakan **LSD**
           - Hipotesis spesifik sudah dibuat sebelum pengumpulan data
           - Jumlah perbandingan sangat terbatas
        
        4. **Ukuran sampel sangat berbeda**: Gunakan **Games-Howell**
           - Tidak mengasumsikan homogenitas varians
           - Robust terhadap pelanggaran asumsi
        """)

    # SIMULASI INTERAKTIF
    elif menu == "🎯 Simulasi Interaktif":
        st.markdown("<h1 class='main-header'>🎯 Simulasi Interaktif</h1>", unsafe_allow_html=True)
    
        st.markdown("""
    Buat data simulasi Anda sendiri dan lihat bagaimana berbagai metode Post-hoc bekerja!
    """)
    
        # Pengaturan simulasi
        st.sidebar.markdown("## ⚙️ Pengaturan Simulasi")
    
        n_groups = st.sidebar.slider("Jumlah Kelompok", 3, 5, 3)
        sample_size = st.sidebar.slider("Ukuran Sampel per Kelompok", 10, 50, 20)
        alpha = st.sidebar.slider("Level Signifikansi (α)", 0.01, 0.10, 0.05, 0.01)
    
        st.sidebar.markdown("### 📊 Parameter Data")
    
        # Buat input untuk setiap kelompok
        group_data = []
        group_names = []
    
        for i in range(n_groups):
            st.sidebar.markdown(f"**Kelompok {i+1}**")
            col1, col2 = st.sidebar.columns(2)
            with col1:
                mean = st.sidebar.number_input(f"Mean {i+1}", value=50.0 + i*10, key=f"mean_{i}")
            with col2:
                std = st.sidebar.number_input(f"Std Dev {i+1}", value=10.0, min_value=1.0, key=f"std_{i}")
        
            group_name = st.sidebar.text_input(f"Nama Kelompok {i+1}", value=f"Kelompok {chr(65+i)}", key=f"name_{i}")
        
            # Generate data
            data = np.random.normal(mean, std, sample_size)
            group_data.append(data)
            group_names.append(group_name)
    
        if st.sidebar.button("🔄 Generate Data Baru", use_container_width=True):
            st.rerun()
    
        # Tampilkan data
        st.markdown("## 📊 Data yang Dihasilkan")
    
        # Buat DataFrame
        df_sim = pd.DataFrame({name: data for name, data in zip(group_names, group_data)})
    
        col1, col2 = st.columns([2, 1])
    
        with col1:
            st.dataframe(df_sim.describe(), use_container_width=True)
    
        with col2:
            st.markdown("### 📈 Statistik Deskriptif")
            for name, data in zip(group_names, group_data):
                st.metric(f"{name} (Mean ± SD)", f"{np.mean(data):.2f} ± {np.std(data):.2f}")
    
        # Visualisasi data
        st.markdown("## 📈 Visualisasi Data")
    
        fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    
        # 1. Boxplot
        data_long = []
        for name, data in zip(group_names, group_data):
            for val in data:
                data_long.append({'Kelompok': name, 'Nilai': val})
        df_long = pd.DataFrame(data_long)
    
        sns.boxplot(data=df_long, x='Kelompok', y='Nilai', ax=axes[0, 0], palette='Set2')
        axes[0, 0].set_title('Boxplot Distribusi Data', fontsize=12, fontweight='bold')
        axes[0, 0].grid(axis='y', alpha=0.3)
    
        # 2. Violin plot
        sns.violinplot(data=df_long, x='Kelompok', y='Nilai', ax=axes[0, 1], palette='Set3')
        axes[0, 1].set_title('Violin Plot', fontsize=12, fontweight='bold')
        axes[0, 1].grid(axis='y', alpha=0.3)
    
        # 3. Strip plot dengan mean
        sns.stripplot(data=df_long, x='Kelompok', y='Nilai', ax=axes[1, 0], 
                  alpha=0.5, palette='Set2')
        means = [np.mean(d) for d in group_data]
        axes[1, 0].scatter(range(len(means)), means, color='red', s=200, marker='D', 
                       zorder=3, label='Mean', edgecolor='black', linewidth=2)
        axes[1, 0].set_title('Strip Plot dengan Mean', fontsize=12, fontweight='bold')
        axes[1, 0].legend()
        axes[1, 0].grid(axis='y', alpha=0.3)
    
        # 4. Bar plot dengan error bars
        means = [np.mean(d) for d in group_data]
        stds = [np.std(d) for d in group_data]
        axes[1, 1].bar(group_names, means, yerr=stds, capsize=5, 
                   color=sns.color_palette('Set2', n_groups), alpha=0.7, edgecolor='black')
        axes[1, 1].set_title('Rata-rata dengan Error Bars', fontsize=12, fontweight='bold')
        axes[1, 1].set_ylabel('Nilai')
        axes[1, 1].grid(axis='y', alpha=0.3)
    
        plt.tight_layout()
        st.pyplot(fig)
    
        # ANOVA Test
        st.markdown("## 🔬 Hasil ANOVA")
    
        f_stat, p_val = f_oneway(*group_data)
    
        col1, col2, col3 = st.columns(3)
    
        with col1:
            st.metric("F-statistic", f"{f_stat:.4f}")
        with col2:
            st.metric("p-value", f"{p_val:.6f}")
        with col3:
            if p_val < alpha:
                st.markdown("**Keputusan**: ✅ Tolak H₀")
            else:
                st.markdown("**Keputusan**: ❌ Terima H₀")
    
        if p_val < alpha:
            st.markdown(f"""
        <div class='success-box'>
            ✅ <b>Hasil Signifikan!</b> (p = {p_val:.6f} < {alpha})<br>
            Terdapat perbedaan signifikan antar kelompok. Lanjutkan dengan uji Post-hoc.
        </div>
            """, unsafe_allow_html=True)
        
            # Post-hoc Tests
            st.markdown("## 🎯 Hasil Uji Post-hoc")
        
            tab1, tab2, tab3 = st.tabs(["Tukey HSD", "Bonferroni", "LSD"])
        
            with tab1:
                st.markdown("### 📊 Tukey HSD Test")
                results_tukey = tukey_hsd(group_data, group_names, alpha)
                st.dataframe(results_tukey.round(4), use_container_width=True)
            
                # Heatmap untuk Tukey
                n = len(group_names)
                matrix = np.zeros((n, n))
                for _, row in results_tukey.iterrows():
                    i = group_names.index(row['Kelompok 1'])
                    j = group_names.index(row['Kelompok 2'])
                    if row['Signifikan'] == 'Ya':
                        matrix[i, j] = 1
                        matrix[j, i] = 1
            
                fig, ax = plt.subplots(figsize=(8, 6))
                sns.heatmap(matrix, annot=True, fmt='.0f', cmap='RdYlGn', 
                           xticklabels=group_names, yticklabels=group_names,
                           cbar_kws={'label': 'Signifikan (1=Ya, 0=Tidak)'}, ax=ax)
                ax.set_title('Heatmap Signifikansi Tukey HSD', fontsize=14, fontweight='bold')
                plt.tight_layout()
                st.pyplot(fig)
            
                st.markdown("""
            **Interpretasi Tukey HSD:**
            - HSD (Honest Significant Difference) adalah nilai threshold
            - Jika selisih mean > HSD, maka perbedaan signifikan
            - Metode ini mengontrol family-wise error rate
            """)
        
            with tab2:
                st.markdown("### 📊 Bonferroni Test")
                results_bonf = bonferroni_test(group_data, group_names, alpha)
                st.dataframe(results_bonf.round(4), use_container_width=True)
            
                # Heatmap untuk Bonferroni
                n = len(group_names)
                matrix = np.zeros((n, n))
                for _, row in results_bonf.iterrows():
                    i = group_names.index(row['Kelompok 1'])
                    j = group_names.index(row['Kelompok 2'])
                    if row['Signifikan'] == 'Ya':
                        matrix[i, j] = 1
                        matrix[j, i] = 1
            
                fig, ax = plt.subplots(figsize=(8, 6))
                sns.heatmap(matrix, annot=True, fmt='.0f', cmap='RdYlGn', 
                       xticklabels=group_names, yticklabels=group_names,
                       cbar_kws={'label': 'Signifikan (1=Ya, 0=Tidak)'}, ax=ax)
                ax.set_title('Heatmap Signifikansi Bonferroni', fontsize=14, fontweight='bold')
                plt.tight_layout()
                st.pyplot(fig)
            
                st.markdown(f"""
            **Interpretasi Bonferroni:**
            - Alpha terkoreksi: {alpha}/{len(results_bonf)} = {results_bonf['α terkoreksi'].iloc[0]:.6f}
            - Metode sangat konservatif untuk menghindari Type I error
            - Cocok untuk jumlah perbandingan yang sedikit
            """)
        
            with tab3:
                st.markdown("### 📊 LSD (Least Significant Difference) Test")
                results_lsd = lsd_test(group_data, group_names, alpha)
                st.dataframe(results_lsd.round(4), use_container_width=True)
            
                # Heatmap untuk LSD
                n = len(group_names)
                matrix = np.zeros((n, n))
                for _, row in results_lsd.iterrows():
                    i = group_names.index(row['Kelompok 1'])
                    j = group_names.index(row['Kelompok 2'])
                    if row['Signifikan'] == 'Ya':
                        matrix[i, j] = 1
                        matrix[j, i] = 1
            
                fig, ax = plt.subplots(figsize=(8, 6))
                sns.heatmap(matrix, annot=True, fmt='.0f', cmap='RdYlGn', 
                       xticklabels=group_names, yticklabels=group_names,
                       cbar_kws={'label': 'Signifikan (1=Ya, 0=Tidak)'}, ax=ax)
                ax.set_title('Heatmap Signifikansi LSD', fontsize=14, fontweight='bold')
                plt.tight_layout()
                st.pyplot(fig)
            
                st.markdown("""
            **Interpretasi LSD:**
            - Metode paling liberal (power tinggi)
            - Tidak mengkoreksi untuk multiple comparisons
            - ⚠️ Risiko Type I error lebih tinggi
                """)
        
            # Perbandingan metode
            st.markdown("## 🔄 Perbandingan Antar Metode")
        
            comparison_df = pd.DataFrame({
            'Pasangan': results_tukey['Kelompok 1'] + ' vs ' + results_tukey['Kelompok 2'],
            'Tukey': results_tukey['Signifikan'],
            'Bonferroni': results_bonf['Signifikan'],
            'LSD': results_lsd['Signifikan']
            })
        
            st.dataframe(comparison_df, use_container_width=True)
        
            st.markdown("""
        **Catatan:**
        - **Tukey HSD**: Keseimbangan antara konservatif dan powerful
        - **Bonferroni**: Paling konservatif (paling sedikit menolak H₀)
        - **LSD**: Paling liberal (paling banyak menolak H₀)
            """)
        
        else:
            st.markdown(f"""
        <div class='warning-box'>
            ❌ <b>Hasil Tidak Signifikan</b> (p = {p_val:.6f} ≥ {alpha})<br>
            Tidak ada perbedaan signifikan antar kelompok. Uji Post-hoc tidak diperlukan.
        </div>
        """, unsafe_allow_html=True)

    # UPLOAD DATA
    elif menu == "📊 Upload Data":
        st.markdown("<h1 class='main-header'>📊 Analisis Data Anda</h1>", unsafe_allow_html=True)
    
        st.markdown("""
    Upload file CSV Anda untuk melakukan analisis ANOVA dan uji Post-hoc.
    
    **Format Data:**
    - Setiap kolom mewakili satu kelompok
    - Baris berisi nilai observasi
    - Tidak ada missing values
    """)
    
        # Upload file
        uploaded_file = st.file_uploader("Upload file CSV", type=['csv'])
    
        if uploaded_file is not None:
            try:
                df = pd.read_csv(uploaded_file)
            
                st.markdown("### 📋 Preview Data")
                st.dataframe(df.head(10), use_container_width=True)
            
                # Statistik deskriptif
                st.markdown("### 📊 Statistik Deskriptif")
                st.dataframe(df.describe(), use_container_width=True)
            
                # Pengaturan analisis
                st.markdown("### ⚙️ Pengaturan Analisis")
            
                col1, col2 = st.columns(2)
            
                with col1:
                    selected_columns = st.multiselect(
                    "Pilih kolom untuk dianalisis",
                        df.columns.tolist(),
                        default=df.columns.tolist()[:3] if len(df.columns) >= 3 else df.columns.tolist()
                    )
            
                with col2:
                    alpha_upload = st.slider("Level Signifikansi (α)", 0.01, 0.10, 0.05, 0.01, key="alpha_upload")
            
                if len(selected_columns) >= 3:
                    # Ekstrak data
                    group_data_upload = [df[col].dropna().values for col in selected_columns]
                
                    # Visualisasi
                    st.markdown("### 📈 Visualisasi Data")
                
                    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
                
                    # Boxplot
                    data_long_upload = []
                    for col in selected_columns:
                        for val in df[col].dropna():
                            data_long_upload.append({'Kelompok': col, 'Nilai': val})
                    df_long_upload = pd.DataFrame(data_long_upload)
                
                    sns.boxplot(data=df_long_upload, x='Kelompok', y='Nilai', ax=axes[0], palette='Set2')
                    axes[0].set_title('Boxplot Distribusi Data', fontsize=12, fontweight='bold')
                    axes[0].tick_params(axis='x', rotation=45)
                    axes[0].grid(axis='y', alpha=0.3)
                
                    # Bar plot
                    means = [np.mean(d) for d in group_data_upload]
                    stds = [np.std(d) for d in group_data_upload]
                    axes[1].bar(selected_columns, means, yerr=stds, capsize=5,
                           color=sns.color_palette('Set2', len(selected_columns)), 
                           alpha=0.7, edgecolor='black')
                    axes[1].set_title('Rata-rata dengan Error Bars', fontsize=12, fontweight='bold')
                    axes[1].set_ylabel('Nilai')
                    axes[1].tick_params(axis='x', rotation=45)
                    axes[1].grid(axis='y', alpha=0.3)
                
                    plt.tight_layout()
                    st.pyplot(fig)
                
                    # ANOVA
                    st.markdown("### 🔬 Hasil ANOVA")
                
                    f_stat_upload, p_val_upload = f_oneway(*group_data_upload)
                
                    col1, col2, col3 = st.columns(3)
                
                    with col1:
                        st.metric("F-statistic", f"{f_stat_upload:.4f}")
                    with col2:
                        st.metric("p-value", f"{p_val_upload:.6f}")
                    with col3:
                        if p_val_upload < alpha_upload:
                            st.markdown("**Keputusan**: ✅ Tolak H₀")
                        else:
                            st.markdown("**Keputusan**: ❌ Terima H₀")
                
                    if p_val_upload < alpha_upload:
                        st.markdown(f"""
                        <div class='success-box'>
                        ✅ <b>Hasil Signifikan!</b> (p = {p_val_upload:.6f} < {alpha_upload})<br>
                        Terdapat perbedaan signifikan antar kelompok. Lanjutkan dengan uji Post-hoc.
                    </div>
                        """, unsafe_allow_html=True)
                    
                        # Post-hoc tests
                        st.markdown("### 🎯 Hasil Uji Post-hoc")
                    
                        method = st.selectbox(
                            "Pilih Metode Post-hoc",
                            ["Tukey HSD", "Bonferroni", "LSD", "Semua Metode"]
                        )
                    
                        if method == "Tukey HSD" or method == "Semua Metode":
                            st.markdown("#### 📊 Tukey HSD")
                            results_tukey_upload = tukey_hsd(group_data_upload, selected_columns, alpha_upload)
                            st.dataframe(results_tukey_upload.round(4), use_container_width=True)
                        
                            # Download hasil
                            csv_tukey = results_tukey_upload.to_csv(index=False)
                            st.download_button(
                            label="📥 Download Hasil Tukey HSD (CSV)",
                            data=csv_tukey,
                            file_name="tukey_hsd_results.csv",
                            mime="text/csv"
                            )
                    
                        if method == "Bonferroni" or method == "Semua Metode":
                            st.markdown("#### 📊 Bonferroni")
                            results_bonf_upload = bonferroni_test(group_data_upload, selected_columns, alpha_upload)
                            st.dataframe(results_bonf_upload.round(4), use_container_width=True)
                        
                            csv_bonf = results_bonf_upload.to_csv(index=False)
                            st.download_button(
                            label="📥 Download Hasil Bonferroni (CSV)",
                            data=csv_bonf,
                            file_name="bonferroni_results.csv",
                            mime="text/csv"
                            )
                    
                        if method == "LSD" or method == "Semua Metode":
                            st.markdown("#### 📊 LSD")
                            results_lsd_upload = lsd_test(group_data_upload, selected_columns, alpha_upload)
                            st.dataframe(results_lsd_upload.round(4), use_container_width=True)
                        
                            csv_lsd = results_lsd_upload.to_csv(index=False)
                            st.download_button(
                            label="📥 Download Hasil LSD (CSV)",
                            data=csv_lsd,
                            file_name="lsd_results.csv",
                            mime="text/csv"
                            )
                    
                    else:
                        st.markdown(f"""
                    <div class='warning-box'>
                        ❌ <b>Hasil Tidak Signifikan</b> (p = {p_val_upload:.6f} ≥ {alpha_upload})<br>
                        Tidak ada perbedaan signifikan antar kelompok. Uji Post-hoc tidak diperlukan.
                    </div>
                    """, unsafe_allow_html=True)
            
                else:
                    st.warning("⚠️ Pilih minimal 3 kolom untuk analisis ANOVA!")
                
            except Exception as e:
                st.error(f"❌ Error membaca file: {str(e)}")
                st.info("Pastikan format CSV Anda benar dan tidak ada data yang kosong.")
    
        else:
            st.info("👆 Upload file CSV untuk memulai analisis")
        
            # Contoh format data
            st.markdown("### 📝 Contoh Format Data CSV")
        
            example_data = pd.DataFrame({
            'Kelompok_A': [85, 88, 90, 87, 89, 86, 91],
            'Kelompok_B': [78, 80, 79, 82, 81, 77, 83],
            'Kelompok_C': [92, 94, 93, 95, 91, 96, 90]
            })
        
            st.dataframe(example_data, use_container_width=True)
        
            # Download template
            csv_template = example_data.to_csv(index=False)
            st.download_button(
            label="📥 Download Template CSV",
            data=csv_template,
            file_name="template_anova.csv",
            mime="text/csv"
            )

    # TENTANG
    elif menu == "ℹ️ Tentang":
        st.markdown("<h1 class='main-header'>ℹ️ Tentang Aplikasi</h1>", unsafe_allow_html=True)
    
        st.markdown("""
    ## 📚 Aplikasi Uji Post-hoc untuk ANOVA 1 Jalur
    
    Aplikasi ini dirancang untuk membantu mahasiswa, peneliti, dan praktisi dalam memahami dan 
    melakukan analisis ANOVA 1 jalur beserta uji Post-hoc.
    
    ### ✨ Fitur Utama:
    
    1. **📖 Materi Pembelajaran Lengkap**
       - Penjelasan konsep ANOVA dan Post-hoc
       - Formula matematika
       - Contoh perhitungan manual
       - Tips pemilihan metode
    
    2. **🎯 Simulasi Interaktif**
       - Generate data dengan parameter yang dapat disesuaikan
       - Visualisasi real-time
       - Perbandingan berbagai metode Post-hoc
       - Interpretasi hasil otomatis
    
    3. **📊 Analisis Data Sendiri**
       - Upload file CSV
       - Analisis otomatis
       - Export hasil dalam format CSV
       - Visualisasi profesional
    
    ### 🔧 Metode Post-hoc yang Tersedia:
    
    - **Tukey HSD**: Metode paling populer dan seimbang
    - **Bonferroni**: Sangat konservatif, cocok untuk menghindari False Positive
    - **LSD**: Liberal, cocok untuk perbandingan terencana
    
    ### 📖 Referensi:
    
    1. Montgomery, D. C. (2017). *Design and Analysis of Experiments*. John Wiley & Sons.
    2. Field, A. (2013). *Discovering Statistics Using IBM SPSS Statistics*. Sage Publications.
    3. Maxwell, S. E., & Delaney, H. D. (2004). *Designing Experiments and Analyzing Data*. 
       Lawrence Erlbaum Associates.
    
    ### 👨‍💻 Teknologi yang Digunakan:
    
    - **Python**: Bahasa pemrograman
    - **Streamlit**: Framework web app
    - **Pandas & NumPy**: Manipulasi data
    - **SciPy**: Analisis statistik
    - **Matplotlib & Seaborn**: Visualisasi
    
    ### 📧 Kontak & Feedback:
    
    Aplikasi ini dibuat untuk tujuan edukasi. Jika Anda memiliki saran, masukan, atau 
    menemukan bug, silakan berikan feedback melalui tombol thumbs up/down di Streamlit.
    
    ---
    
    **Versi**: 1.0.0  
    **Terakhir Diperbarui**: Desember 2024
    
    ### ⚖️ Disclaimer:
    
    Aplikasi ini disediakan untuk tujuan edukasi. Untuk penelitian yang akan dipublikasikan,
    pastikan untuk melakukan validasi tambahan dan konsultasi dengan ahli statistik.
    """)
    
        st.markdown("---")
    
        # Tips penggunaan
        st.markdown("## 💡 Tips Penggunaan Aplikasi")
    
        col1, col2 = st.columns(2)
    
        with col1:
            st.markdown("""
        ### 🎓 Untuk Pembelajaran:
        1. Mulai dari menu **Materi** untuk memahami konsep
        2. Lanjut ke **Simulasi** untuk eksplorasi interaktif
        3. Coba berbagai parameter dan amati hasilnya
        4. Bandingkan hasil dari berbagai metode
        """)
    
        with col2:
            st.markdown("""
        ### 🔬 Untuk Penelitian:
        1. Siapkan data dalam format CSV
        2. Upload melalui menu **Upload Data**
        3. Pilih metode Post-hoc yang sesuai
        4. Download hasil untuk dokumentasi
        """)
    
        st.markdown("---")
    
        st.markdown("""
    <div class='success-box'>
        <h3>🎉 Terima Kasih telah Menggunakan Aplikasi Ini!</h3>
        <p>Semoga aplikasi ini bermanfaat untuk pembelajaran dan penelitian Anda.</p>
    </div>
    """, unsafe_allow_html=True)

    # Footer
    st.markdown("---")
    st.markdown("""
<div style='text-align: center; color: #666; padding: 1rem;'>
    <p>📊 Aplikasi Uji Post-hoc ANOVA | Dibuat dengan ❤️ menggunakan Streamlit</p>
    <p style='font-size: 0.8rem;'>© 2024 | Untuk Tujuan Edukasi</p>
</div>
""", unsafe_allow_html=True)
#================================

if st.session_state.tampilan1:
    tampilkan_materi1()
if st.session_state.tampilan2:
    tampilkan_materi2()
if st.session_state.tampilan3:
    latar()
if st.session_state.tampilan4:
    tampilkan_materi3()
if st.session_state.tampilan5:
    tampilkan_materi4()
if st.session_state.tampilan6:
    tampilkan_materi5()
if st.session_state.tampilan7:
    tampilkan_tugas()
if st.session_state.tampilan8:
    tampilkan_latihan1()
if st.session_state.tampilan9:
    tampilkan_materi6()
if st.session_state.tampilan10:
    tampilkan_materi7()
if st.session_state.tampilan11:
    tampilkan_materi8()
if st.session_state.tampilan12:
    tampilkan_materi9()
if st.session_state.tampilan13:
    tampilkan_materi10()
if st.session_state.tampilan14:
    tampilkan_materi11()
if st.session_state.tampilan15:
    tampilkan_materi12()
if st.session_state.tampilan16:
    tampilkan_materi13()
if st.session_state.tampilan17:
    tampilkan_materi14()
if st.session_state.tampilan18:
    tampilkan_materi15()
if st.session_state.tampilan19:
    tampilkan_materi16()
if st.session_state.tampilan20:
    tampilkan_materi17()
if st.session_state.tampilan21:
    tampilkan_materi18()
if st.session_state.tampilan22:
    tampilkan_materi19()
if st.session_state.tampilan23:
    tampilkan_materi20()
if st.session_state.tampilan24:
    tampilkan_materi21()
if st.session_state.tampilan25:
    tampilkan_materi22()
if st.session_state.tampilan26:
    tampilkan_materi23()
if st.session_state.tampilan27:
    tampilkan_materi24()
if st.session_state.tampilan28:
    tampilkan_materi25()
if st.session_state.tampilan29:
    tampilkan_materi26()
if st.session_state.tampilan30:
    tampilkan_materi27()
#======================================
if st.sidebar.button("Masukan Tugas"):
    st.session_state.tampilan1=False
    st.session_state.tampilan2=False
    st.session_state.tampilan3 = False
    st.session_state.tampilan4 = False
    st.session_state.tampilan5 = False
    st.session_state.tampilan6 = False
    st.session_state.tampilan7 = True
    st.session_state.tampilan8 = False
    st.session_state.tampilan9 = False
    st.session_state.tampilan10 = False
    st.session_state.tampilan11 = False
    st.session_state.tampilan12 = False
    st.session_state.tampilan13 = False
    st.session_state.tampilan14 = False
    st.session_state.tampilan15 = False
    st.session_state.tampilan16 = False
    st.session_state.tampilan17 = False
    st.session_state.tampilan18 = False
    st.session_state.tampilan19 = False
    st.session_state.tampilan20 = False
    st.session_state.tampilan21 = False
    st.session_state.tampilan22 = False
    st.session_state.tampilan23 = False
    st.session_state.tampilan24 = False
    st.session_state.tampilan25 = False
    st.session_state.tampilan26 = False
    st.session_state.tampilan27 = False
    st.session_state.tampilan28 = False
    st.session_state.tampilan29 = False
    st.session_state.tampilan30 = False
    st.rerun()
if st.sidebar.button("Contoh Data Nilai"):
    st.session_state.tampilan1=False
    st.session_state.tampilan2=False
    st.session_state.tampilan3 = False
    st.session_state.tampilan4 = False
    st.session_state.tampilan5 = False
    st.session_state.tampilan6 = False
    st.session_state.tampilan7 = False
    st.session_state.tampilan8 = False
    st.session_state.tampilan9 = False
    st.session_state.tampilan10 = False
    st.session_state.tampilan11 = False
    st.session_state.tampilan12 = False
    st.session_state.tampilan13 = False
    st.session_state.tampilan14 = False
    st.session_state.tampilan15 = False
    st.session_state.tampilan16 = False
    st.session_state.tampilan17 = False
    st.session_state.tampilan18 = False
    st.session_state.tampilan19 = False
    st.session_state.tampilan20 = False
    st.session_state.tampilan21 = True
    st.session_state.tampilan22 = False
    st.session_state.tampilan23 = False
    st.session_state.tampilan24 = False
    st.session_state.tampilan25 = False
    st.session_state.tampilan26 = False
    st.session_state.tampilan27 = False
    st.session_state.tampilan28 = False
    st.session_state.tampilan29 = False
    st.session_state.tampilan30 = False
    st.rerun()
st.sidebar.markdown("Penguasaan Uji 1 Sampel")
if st.sidebar.button("Test Penguasaan 1"):
    st.session_state.tampilan1=False
    st.session_state.tampilan2=False
    st.session_state.tampilan3 = False
    st.session_state.tampilan4 = False
    st.session_state.tampilan5 = False
    st.session_state.tampilan6 = False
    st.session_state.tampilan7 = False
    st.session_state.tampilan8 = False
    st.session_state.tampilan9 = False
    st.session_state.tampilan10 = False
    st.session_state.tampilan11 = False
    st.session_state.tampilan12 = False
    st.session_state.tampilan13 = False
    st.session_state.tampilan14 = False
    st.session_state.tampilan15 = False
    st.session_state.tampilan16 = False
    st.session_state.tampilan17 = False
    st.session_state.tampilan18 = False
    st.session_state.tampilan19 = False
    st.session_state.tampilan20 = True
    st.session_state.tampilan21 = False
    st.session_state.tampilan22 = False
    st.session_state.tampilan23 = False
    st.session_state.tampilan24 = False
    st.session_state.tampilan25 = False
    st.session_state.tampilan26 = False
    st.session_state.tampilan27 = False
    st.session_state.tampilan28 = False
    st.session_state.tampilan29 = False
    st.session_state.tampilan30 = False
    st.rerun()
st.sidebar.markdown("---")
st.sidebar.markdown("Evaluasi Instrumen Soal")
if st.sidebar.button("Evaluasi Soal"):
    st.session_state.tampilan1=False
    st.session_state.tampilan2=False
    st.session_state.tampilan3 = False
    st.session_state.tampilan4 = False
    st.session_state.tampilan5 = False
    st.session_state.tampilan6 = False
    st.session_state.tampilan7 = False
    st.session_state.tampilan8 = False
    st.session_state.tampilan9 = False
    st.session_state.tampilan10 = False
    st.session_state.tampilan11 = False
    st.session_state.tampilan12 = False
    st.session_state.tampilan13 = False
    st.session_state.tampilan14 = False
    st.session_state.tampilan15 = False
    st.session_state.tampilan16 = False
    st.session_state.tampilan17 = False
    st.session_state.tampilan18 = True
    st.session_state.tampilan19 = False
    st.session_state.tampilan20 = False
    st.session_state.tampilan21 = False
    st.session_state.tampilan22 = False
    st.session_state.tampilan23 = False
    st.session_state.tampilan24 = False
    st.session_state.tampilan25 = False
    st.session_state.tampilan26 = False
    st.session_state.tampilan27 = False
    st.session_state.tampilan28 = False
    st.session_state.tampilan29 = False
    st.session_state.tampilan30 = False
    st.rerun()
st.sidebar.markdown("---")
if st.sidebar.button("Pengenalan"):
    st.session_state.tampilan1=False
    st.session_state.tampilan2=False
    st.session_state.tampilan3 = True
    st.session_state.tampilan4 = False
    st.session_state.tampilan5 = False
    st.session_state.tampilan6 = False
    st.session_state.tampilan7 = False
    st.session_state.tampilan8 = False
    st.session_state.tampilan9 = False
    st.session_state.tampilan10 = False
    st.session_state.tampilan11 = False
    st.session_state.tampilan12 = False
    st.session_state.tampilan13 = False
    st.session_state.tampilan14 = False
    st.session_state.tampilan15 = False
    st.session_state.tampilan16 = False
    st.session_state.tampilan17 = False
    st.session_state.tampilan18 = False
    st.session_state.tampilan19 = False
    st.session_state.tampilan20 = False
    st.session_state.tampilan21 = False
    st.session_state.tampilan22 = False
    st.session_state.tampilan23 = False
    st.session_state.tampilan24 = False
    st.session_state.tampilan25 = False
    st.session_state.tampilan26 = False
    st.session_state.tampilan27 = False
    st.session_state.tampilan28 = False
    st.session_state.tampilan29 = False
    st.session_state.tampilan30 = False
    st.rerun()
if st.sidebar.button("Skala Pengukuran Data"):
    st.session_state.tampilan1=True
    st.session_state.tampilan2=False
    st.session_state.tampilan3 = False
    st.session_state.tampilan4 = False
    st.session_state.tampilan5 = False
    st.session_state.tampilan6 = False
    st.session_state.tampilan7 = False
    st.session_state.tampilan8 = False
    st.session_state.tampilan9 = False
    st.session_state.tampilan10 = False
    st.session_state.tampilan11 = False
    st.session_state.tampilan12 = False
    st.session_state.tampilan13 = False
    st.session_state.tampilan14 = False
    st.session_state.tampilan15 = False
    st.session_state.tampilan16 = False
    st.session_state.tampilan17 = False
    st.session_state.tampilan18 = False
    st.session_state.tampilan19 = False
    st.session_state.tampilan20 = False
    st.session_state.tampilan21 = False
    st.session_state.tampilan22 = False
    st.session_state.tampilan23 = False
    st.session_state.tampilan24 = False
    st.session_state.tampilan25 = False
    st.session_state.tampilan26 = False
    st.session_state.tampilan27 = False
    st.session_state.tampilan28 = False
    st.session_state.tampilan29 = False
    st.session_state.tampilan30 = False
    st.rerun()
if st.sidebar.button("Pengantar Statistik dalam Penelitian R&D"):
    st.session_state.tampilan1=False
    st.session_state.tampilan2=True
    st.session_state.tampilan3 = False
    st.session_state.tampilan4 = False
    st.session_state.tampilan5 = False
    st.session_state.tampilan6 = False
    st.session_state.tampilan7 = False
    st.session_state.tampilan8 = False
    st.session_state.tampilan9 = False
    st.session_state.tampilan10 = False
    st.session_state.tampilan11 = False
    st.session_state.tampilan12 = False
    st.session_state.tampilan13 = False
    st.session_state.tampilan14 = False
    st.session_state.tampilan15 = False
    st.session_state.tampilan16 = False
    st.session_state.tampilan17 = False
    st.session_state.tampilan18 = False
    st.session_state.tampilan19 = False
    st.session_state.tampilan20 = False
    st.session_state.tampilan21 = False
    st.session_state.tampilan22 = False
    st.session_state.tampilan23 = False
    st.session_state.tampilan24 = False
    st.session_state.tampilan25 = False
    st.session_state.tampilan26 = False
    st.session_state.tampilan27 = False
    st.session_state.tampilan28 = False
    st.session_state.tampilan29 = False
    st.session_state.tampilan30 = False
    st.rerun()
if st.sidebar.button("Statistik Deskriptif"):
    st.session_state.tampilan1=False
    st.session_state.tampilan2=False
    st.session_state.tampilan3 = False
    st.session_state.tampilan4 = True
    st.session_state.tampilan5 = False
    st.session_state.tampilan6 = False
    st.session_state.tampilan7 = False
    st.session_state.tampilan8 = False
    st.session_state.tampilan9 = False
    st.session_state.tampilan10 = False
    st.session_state.tampilan11 = False
    st.session_state.tampilan12 = False
    st.session_state.tampilan13 = False
    st.session_state.tampilan14 = False
    st.session_state.tampilan15 = False
    st.session_state.tampilan16 = False
    st.session_state.tampilan17 = False
    st.session_state.tampilan18 = False
    st.session_state.tampilan19 = False
    st.session_state.tampilan20 = False
    st.session_state.tampilan21 = False
    st.session_state.tampilan22 = False
    st.session_state.tampilan23 = False
    st.session_state.tampilan24 = False
    st.session_state.tampilan25 = False
    st.session_state.tampilan26 = False
    st.session_state.tampilan27 = False
    st.session_state.tampilan28 = False
    st.session_state.tampilan29 = False
    st.session_state.tampilan30 = False
    st.rerun()
if st.sidebar.button("Grafik Z"):
    st.session_state.tampilan1=False
    st.session_state.tampilan2=False
    st.session_state.tampilan3 = False
    st.session_state.tampilan4 = False
    st.session_state.tampilan5 = True
    st.session_state.tampilan6 = False
    st.session_state.tampilan7 = False
    st.session_state.tampilan8 = False
    st.session_state.tampilan9 = False
    st.session_state.tampilan10 = False
    st.session_state.tampilan11 = False
    st.session_state.tampilan12 = False
    st.session_state.tampilan13 = False
    st.session_state.tampilan14 = False
    st.session_state.tampilan15 = False
    st.session_state.tampilan16 = False
    st.session_state.tampilan17 = False
    st.session_state.tampilan18 = False
    st.session_state.tampilan19 = False
    st.session_state.tampilan20 = False
    st.session_state.tampilan21 = False
    st.session_state.tampilan22 = False
    st.session_state.tampilan23 = False
    st.session_state.tampilan24 = False
    st.session_state.tampilan25 = False
    st.session_state.tampilan26 = False
    st.session_state.tampilan27 = False
    st.session_state.tampilan28 = False
    st.session_state.tampilan29 = False
    st.session_state.tampilan30 = False
    st.rerun()
if st.sidebar.button("Grafik Uji Z"):
    st.session_state.tampilan1=False
    st.session_state.tampilan2=False
    st.session_state.tampilan3 = False
    st.session_state.tampilan4 = False
    st.session_state.tampilan5 = False
    st.session_state.tampilan6 = True
    st.session_state.tampilan7 = False
    st.session_state.tampilan8 = False
    st.session_state.tampilan9 = False
    st.session_state.tampilan10 = False
    st.session_state.tampilan11 = False
    st.session_state.tampilan12 = False
    st.session_state.tampilan13 = False
    st.session_state.tampilan14 = False
    st.session_state.tampilan15 = False
    st.session_state.tampilan16 = False
    st.session_state.tampilan17 = False
    st.session_state.tampilan18 = False
    st.session_state.tampilan19 = False
    st.session_state.tampilan20 = False
    st.session_state.tampilan21 = False
    st.session_state.tampilan22 = False
    st.session_state.tampilan23 = False
    st.session_state.tampilan24 = False
    st.session_state.tampilan25 = False
    st.session_state.tampilan26 = False
    st.session_state.tampilan27 = False
    st.session_state.tampilan28 = False
    st.session_state.tampilan29 = False
    st.session_state.tampilan30 = False
    st.rerun()
if st.sidebar.button("Latihan Uji Z"):
    st.session_state.tampilan1=False
    st.session_state.tampilan2=False
    st.session_state.tampilan3 = False
    st.session_state.tampilan4 = False
    st.session_state.tampilan5 = False
    st.session_state.tampilan6 = False
    st.session_state.tampilan7 = False
    st.session_state.tampilan8 = True
    st.session_state.tampilan9 = False
    st.session_state.tampilan10 = False
    st.session_state.tampilan11 = False
    st.session_state.tampilan12 = False
    st.session_state.tampilan13 = False
    st.session_state.tampilan14 = False
    st.session_state.tampilan15 = False
    st.session_state.tampilan16 = False
    st.session_state.tampilan17 = False
    st.session_state.tampilan18 = False
    st.session_state.tampilan19 = False
    st.session_state.tampilan20 = False
    st.session_state.tampilan21 = False
    st.session_state.tampilan22 = False
    st.session_state.tampilan23 = False
    st.session_state.tampilan24 = False
    st.session_state.tampilan25 = False
    st.session_state.tampilan26 = False
    st.session_state.tampilan27 = False
    st.session_state.tampilan28 = False
    st.session_state.tampilan29 = False
    st.session_state.tampilan30 = False
    st.rerun()
if st.sidebar.button("Uji Hipotesis"):
    st.session_state.tampilan1=False
    st.session_state.tampilan2=False
    st.session_state.tampilan3 = False
    st.session_state.tampilan4 = False
    st.session_state.tampilan5 = False
    st.session_state.tampilan6 = False
    st.session_state.tampilan7 = False
    st.session_state.tampilan8 = False
    st.session_state.tampilan9 = True
    st.session_state.tampilan10 = False
    st.session_state.tampilan11 = False
    st.session_state.tampilan12 = False
    st.session_state.tampilan13 = False
    st.session_state.tampilan14 = False
    st.session_state.tampilan15 = False
    st.session_state.tampilan16 = False
    st.session_state.tampilan17 = False
    st.session_state.tampilan18 = False
    st.session_state.tampilan19 = False
    st.session_state.tampilan20 = False
    st.session_state.tampilan21 = False
    st.session_state.tampilan22 = False
    st.session_state.tampilan23 = False
    st.session_state.tampilan24 = False
    st.session_state.tampilan25 = False
    st.session_state.tampilan26 = False
    st.session_state.tampilan27 = False
    st.session_state.tampilan28 = False
    st.session_state.tampilan29 = False
    st.session_state.tampilan30 = False
    st.rerun()
st.sidebar.markdown("---")
st.sidebar.markdown("Flowchart Penelitian")
if st.sidebar.button("FlowChart"):
    st.session_state.tampilan1=False
    st.session_state.tampilan2=False
    st.session_state.tampilan3 = False
    st.session_state.tampilan4 = False
    st.session_state.tampilan5 = False
    st.session_state.tampilan6 = False
    st.session_state.tampilan7 = False
    st.session_state.tampilan8 = False
    st.session_state.tampilan9 = False
    st.session_state.tampilan10 = False
    st.session_state.tampilan11 = False
    st.session_state.tampilan12 = False
    st.session_state.tampilan13 = False
    st.session_state.tampilan14 = False
    st.session_state.tampilan15 = False
    st.session_state.tampilan16 = False
    st.session_state.tampilan17 = False
    st.session_state.tampilan18 = False
    st.session_state.tampilan19 = True
    st.session_state.tampilan20 = False
    st.session_state.tampilan21 = False
    st.session_state.tampilan22 = False
    st.session_state.tampilan23 = False
    st.session_state.tampilan24 = False
    st.session_state.tampilan25 = False
    st.session_state.tampilan26 = False
    st.session_state.tampilan27 = False
    st.session_state.tampilan28 = False
    st.session_state.tampilan29 = False
    st.session_state.tampilan30 = False
    st.rerun()
st.sidebar.markdown("---")
if st.sidebar.button("Uji Normalitas"):
    st.session_state.tampilan1=False
    st.session_state.tampilan2=False
    st.session_state.tampilan3 = False
    st.session_state.tampilan4 = False
    st.session_state.tampilan5 = False
    st.session_state.tampilan6 = False
    st.session_state.tampilan7 = False
    st.session_state.tampilan8 = False
    st.session_state.tampilan9 = False
    st.session_state.tampilan10 = True
    st.session_state.tampilan11 = False
    st.session_state.tampilan12 = False
    st.session_state.tampilan13 = False
    st.session_state.tampilan14 = False
    st.session_state.tampilan15 = False
    st.session_state.tampilan16 = False
    st.session_state.tampilan17 = False
    st.session_state.tampilan18 = False
    st.session_state.tampilan19 = False
    st.session_state.tampilan20 = False
    st.session_state.tampilan21 = False
    st.session_state.tampilan22 = False
    st.session_state.tampilan23 = False
    st.session_state.tampilan24 = False
    st.session_state.tampilan25 = False
    st.session_state.tampilan26 = False
    st.session_state.tampilan27 = False
    st.session_state.tampilan28 = False
    st.session_state.tampilan29 = False
    st.session_state.tampilan30 = False
    st.rerun()
if st.sidebar.button("Uji Homogen"):
    st.session_state.tampilan1=False
    st.session_state.tampilan2=False
    st.session_state.tampilan3 = False
    st.session_state.tampilan4 = False
    st.session_state.tampilan5 = False
    st.session_state.tampilan6 = False
    st.session_state.tampilan7 = False
    st.session_state.tampilan8 = False
    st.session_state.tampilan9 = False
    st.session_state.tampilan10 = False
    st.session_state.tampilan11 = False
    st.session_state.tampilan12 = True
    st.session_state.tampilan13 = False
    st.session_state.tampilan14 = False
    st.session_state.tampilan15 = False
    st.session_state.tampilan16 = False
    st.session_state.tampilan17 = False
    st.session_state.tampilan18 = False
    st.session_state.tampilan19 = False
    st.session_state.tampilan20 = False
    st.session_state.tampilan21 = False
    st.session_state.tampilan22 = False
    st.session_state.tampilan23 = False
    st.session_state.tampilan24 = False
    st.session_state.tampilan25 = False
    st.session_state.tampilan26 = False
    st.session_state.tampilan27 = False
    st.session_state.tampilan28 = False
    st.session_state.tampilan29 = False
    st.session_state.tampilan30 = False
    st.rerun()
st.sidebar.markdown("---")
st.sidebar.markdown("Data Parametrik")
if st.sidebar.button("Uji t 1 sampel"):
    st.session_state.tampilan1=False
    st.session_state.tampilan2=False
    st.session_state.tampilan3 = False
    st.session_state.tampilan4 = False
    st.session_state.tampilan5 = False
    st.session_state.tampilan6 = False
    st.session_state.tampilan7 = False
    st.session_state.tampilan8 = False
    st.session_state.tampilan9 = False
    st.session_state.tampilan10 = False
    st.session_state.tampilan11 = False
    st.session_state.tampilan12 = False
    st.session_state.tampilan13 = False
    st.session_state.tampilan14 = False
    st.session_state.tampilan15 = False
    st.session_state.tampilan16 = True
    st.session_state.tampilan17 = False
    st.session_state.tampilan18 = False
    st.session_state.tampilan19 = False
    st.session_state.tampilan20 = False
    st.session_state.tampilan21 = False
    st.session_state.tampilan22 = False
    st.session_state.tampilan23 = False
    st.session_state.tampilan24 = False
    st.session_state.tampilan25 = False
    st.session_state.tampilan26 = False
    st.session_state.tampilan27 = False
    st.session_state.tampilan28 = False
    st.session_state.tampilan29 = False
    st.session_state.tampilan30 = False
    st.rerun()
if st.sidebar.button("Uji t 1 sampel Berpasangan"):
    st.session_state.tampilan1=False
    st.session_state.tampilan2=False
    st.session_state.tampilan3 = False
    st.session_state.tampilan4 = False
    st.session_state.tampilan5 = False
    st.session_state.tampilan6 = False
    st.session_state.tampilan7 = False
    st.session_state.tampilan8 = False
    st.session_state.tampilan9 = False
    st.session_state.tampilan10 = False
    st.session_state.tampilan11 = False
    st.session_state.tampilan12 = False
    st.session_state.tampilan13 = False
    st.session_state.tampilan14 = False
    st.session_state.tampilan15 = False
    st.session_state.tampilan16 = False
    st.session_state.tampilan17 = False
    st.session_state.tampilan18 = False
    st.session_state.tampilan19 = False
    st.session_state.tampilan20 = False
    st.session_state.tampilan21 = False
    st.session_state.tampilan22 = True
    st.session_state.tampilan23 = False
    st.session_state.tampilan24 = False
    st.session_state.tampilan25 = False
    st.session_state.tampilan26 = False
    st.session_state.tampilan27 = False
    st.session_state.tampilan28 = False
    st.session_state.tampilan29 = False
    st.session_state.tampilan30 = False
    st.rerun()
if st.sidebar.button("Uji t' 2 sampel Independent"):
    st.session_state.tampilan1=False
    st.session_state.tampilan2=False
    st.session_state.tampilan3 = False
    st.session_state.tampilan4 = False
    st.session_state.tampilan5 = False
    st.session_state.tampilan6 = False
    st.session_state.tampilan7 = False
    st.session_state.tampilan8 = False
    st.session_state.tampilan9 = False
    st.session_state.tampilan10 = False
    st.session_state.tampilan11 = False
    st.session_state.tampilan12 = False
    st.session_state.tampilan13 = False
    st.session_state.tampilan14 = False
    st.session_state.tampilan15 = False
    st.session_state.tampilan16 = False
    st.session_state.tampilan17 = False
    st.session_state.tampilan18 = False
    st.session_state.tampilan19 = False
    st.session_state.tampilan20 = False
    st.session_state.tampilan21 = False
    st.session_state.tampilan22 = False
    st.session_state.tampilan23 = False
    st.session_state.tampilan24 = False
    st.session_state.tampilan25 = False
    st.session_state.tampilan26 = True
    st.session_state.tampilan27 = False
    st.session_state.tampilan28 = False
    st.session_state.tampilan29 = False
    st.session_state.tampilan30 = False
    st.rerun()
if st.sidebar.button("Uji t 2 sampel Independent"):
    st.session_state.tampilan1=False
    st.session_state.tampilan2=False
    st.session_state.tampilan3 = False
    st.session_state.tampilan4 = False
    st.session_state.tampilan5 = False
    st.session_state.tampilan6 = False
    st.session_state.tampilan7 = False
    st.session_state.tampilan8 = False
    st.session_state.tampilan9 = False
    st.session_state.tampilan10 = False
    st.session_state.tampilan11 = False
    st.session_state.tampilan12 = False
    st.session_state.tampilan13 = False
    st.session_state.tampilan14 = False
    st.session_state.tampilan15 = False
    st.session_state.tampilan16 = False
    st.session_state.tampilan17 = False
    st.session_state.tampilan18 = False
    st.session_state.tampilan19 = False
    st.session_state.tampilan20 = False
    st.session_state.tampilan21 = False
    st.session_state.tampilan22 = False
    st.session_state.tampilan23 = False
    st.session_state.tampilan24 = True
    st.session_state.tampilan25 = False
    st.session_state.tampilan26 = False
    st.session_state.tampilan27 = False
    st.session_state.tampilan28 = False
    st.session_state.tampilan29 = False
    st.session_state.tampilan30 = False
    st.rerun()
if st.sidebar.button("Uji welch's Anova  > 2 sampel Independent"):
    st.session_state.tampilan1=False
    st.session_state.tampilan2=False
    st.session_state.tampilan3 = False
    st.session_state.tampilan4 = False
    st.session_state.tampilan5 = False
    st.session_state.tampilan6 = False
    st.session_state.tampilan7 = False
    st.session_state.tampilan8 = False
    st.session_state.tampilan9 = False
    st.session_state.tampilan10 = False
    st.session_state.tampilan11 = False
    st.session_state.tampilan12 = False
    st.session_state.tampilan13 = False
    st.session_state.tampilan14 = False
    st.session_state.tampilan15 = False
    st.session_state.tampilan16 = False
    st.session_state.tampilan17 = False
    st.session_state.tampilan18 = False
    st.session_state.tampilan19 = False
    st.session_state.tampilan20 = False
    st.session_state.tampilan21 = False
    st.session_state.tampilan22 = False
    st.session_state.tampilan23 = False
    st.session_state.tampilan24 = False
    st.session_state.tampilan25 = False
    st.session_state.tampilan26 = False
    st.session_state.tampilan27 = False
    st.session_state.tampilan28 = False
    st.session_state.tampilan29 = True
    st.session_state.tampilan30 = False
    st.rerun()
if st.sidebar.button("Uji Anova 1 Jalur"):
    st.session_state.tampilan1=False
    st.session_state.tampilan2=False
    st.session_state.tampilan3 = False
    st.session_state.tampilan4 = False
    st.session_state.tampilan5 = False
    st.session_state.tampilan6 = False
    st.session_state.tampilan7 = False
    st.session_state.tampilan8 = False
    st.session_state.tampilan9 = False
    st.session_state.tampilan10 = False
    st.session_state.tampilan11 = False
    st.session_state.tampilan12 = False
    st.session_state.tampilan13 = False
    st.session_state.tampilan14 = False
    st.session_state.tampilan15 = False
    st.session_state.tampilan16 = False
    st.session_state.tampilan17 = False
    st.session_state.tampilan18 = False
    st.session_state.tampilan19 = False
    st.session_state.tampilan20 = False
    st.session_state.tampilan21 = False
    st.session_state.tampilan22 = False
    st.session_state.tampilan23 = False
    st.session_state.tampilan24 = False
    st.session_state.tampilan25 = False
    st.session_state.tampilan26 = False
    st.session_state.tampilan27 = True
    st.session_state.tampilan28 = False
    st.session_state.tampilan29 = False
    st.session_state.tampilan30 = False
    st.rerun()
st.sidebar.markdown("---")
st.sidebar.markdown("Data non Parametrik")
if st.sidebar.button("Uji Wilcoxon 1 sampel"):
    st.session_state.tampilan1=False
    st.session_state.tampilan2=False
    st.session_state.tampilan3 = False
    st.session_state.tampilan4 = False
    st.session_state.tampilan5 = False
    st.session_state.tampilan6 = False
    st.session_state.tampilan7 = False
    st.session_state.tampilan8 = False
    st.session_state.tampilan9 = False
    st.session_state.tampilan10 = False
    st.session_state.tampilan11 = False
    st.session_state.tampilan12 = False
    st.session_state.tampilan13 = False
    st.session_state.tampilan14 = False
    st.session_state.tampilan15 = False
    st.session_state.tampilan16 = False
    st.session_state.tampilan17 = True
    st.session_state.tampilan18 = False
    st.session_state.tampilan19 = False
    st.session_state.tampilan20 = False
    st.session_state.tampilan21 = False
    st.session_state.tampilan22 = False
    st.session_state.tampilan23 = False
    st.session_state.tampilan24 = False
    st.session_state.tampilan25 = False
    st.session_state.tampilan26 = False
    st.session_state.tampilan27 = False
    st.session_state.tampilan28 = False
    st.session_state.tampilan29 = False
    st.session_state.tampilan30 = False
    st.rerun()
if st.sidebar.button("Uji Wilcoxon 1 sampel Berpasangan"):
    st.session_state.tampilan1=False
    st.session_state.tampilan2=False
    st.session_state.tampilan3 = False
    st.session_state.tampilan4 = False
    st.session_state.tampilan5 = False
    st.session_state.tampilan6 = False
    st.session_state.tampilan7 = False
    st.session_state.tampilan8 = False
    st.session_state.tampilan9 = False
    st.session_state.tampilan10 = False
    st.session_state.tampilan11 = False
    st.session_state.tampilan12 = False
    st.session_state.tampilan13 = False
    st.session_state.tampilan14 = False
    st.session_state.tampilan15 = False
    st.session_state.tampilan16 = False
    st.session_state.tampilan17 = False
    st.session_state.tampilan18 = False
    st.session_state.tampilan19 = False
    st.session_state.tampilan20 = False
    st.session_state.tampilan21 = False
    st.session_state.tampilan22 = False
    st.session_state.tampilan23 = True
    st.session_state.tampilan24 = False
    st.session_state.tampilan25 = False
    st.session_state.tampilan26 = False
    st.session_state.tampilan27 = False
    st.session_state.tampilan28 = False
    st.session_state.tampilan29 = False
    st.session_state.tampilan30 = False
    st.rerun()
if st.sidebar.button("Uji U Mann-Whitney 2 sampel Independen"):
    st.session_state.tampilan1=False
    st.session_state.tampilan2=False
    st.session_state.tampilan3 = False
    st.session_state.tampilan4 = False
    st.session_state.tampilan5 = False
    st.session_state.tampilan6 = False
    st.session_state.tampilan7 = False
    st.session_state.tampilan8 = False
    st.session_state.tampilan9 = False
    st.session_state.tampilan10 = False
    st.session_state.tampilan11 = False
    st.session_state.tampilan12 = False
    st.session_state.tampilan13 = False
    st.session_state.tampilan14 = False
    st.session_state.tampilan15 = False
    st.session_state.tampilan16 = False
    st.session_state.tampilan17 = False
    st.session_state.tampilan18 = False
    st.session_state.tampilan19 = False
    st.session_state.tampilan20 = False
    st.session_state.tampilan21 = False
    st.session_state.tampilan22 = False
    st.session_state.tampilan23 = False
    st.session_state.tampilan24 = False
    st.session_state.tampilan25 = True
    st.session_state.tampilan26 = False
    st.session_state.tampilan27 = False
    st.session_state.tampilan28 = False
    st.session_state.tampilan29 = False
    st.session_state.tampilan30 = False
    st.rerun()
if st.sidebar.button("Uji Kruskal-Wallis > 2 sampel Independen"):
    st.session_state.tampilan1=False
    st.session_state.tampilan2=False
    st.session_state.tampilan3 = False
    st.session_state.tampilan4 = False
    st.session_state.tampilan5 = False
    st.session_state.tampilan6 = False
    st.session_state.tampilan7 = False
    st.session_state.tampilan8 = False
    st.session_state.tampilan9 = False
    st.session_state.tampilan10 = False
    st.session_state.tampilan11 = False
    st.session_state.tampilan12 = False
    st.session_state.tampilan13 = False
    st.session_state.tampilan14 = False
    st.session_state.tampilan15 = False
    st.session_state.tampilan16 = False
    st.session_state.tampilan17 = False
    st.session_state.tampilan18 = False
    st.session_state.tampilan19 = False
    st.session_state.tampilan20 = False
    st.session_state.tampilan21 = False
    st.session_state.tampilan22 = False
    st.session_state.tampilan23 = False
    st.session_state.tampilan24 = False
    st.session_state.tampilan25 = False
    st.session_state.tampilan26 = False
    st.session_state.tampilan27 = False
    st.session_state.tampilan28 = True
    st.session_state.tampilan29 = False
    st.session_state.tampilan30 = False
    st.rerun()
st.sidebar.markdown("---")
if st.sidebar.button("Uji PostHoc"):
    st.session_state.tampilan1=False
    st.session_state.tampilan2=False
    st.session_state.tampilan3 = False
    st.session_state.tampilan4 = False
    st.session_state.tampilan5 = False
    st.session_state.tampilan6 = False
    st.session_state.tampilan7 = False
    st.session_state.tampilan8 = False
    st.session_state.tampilan9 = False
    st.session_state.tampilan10 = False
    st.session_state.tampilan11 = False
    st.session_state.tampilan12 = False
    st.session_state.tampilan13 = False
    st.session_state.tampilan14 = False
    st.session_state.tampilan15 = False
    st.session_state.tampilan16 = False
    st.session_state.tampilan17 = False
    st.session_state.tampilan18 = False
    st.session_state.tampilan19 = False
    st.session_state.tampilan20 = False
    st.session_state.tampilan21 = False
    st.session_state.tampilan22 = False
    st.session_state.tampilan23 = False
    st.session_state.tampilan24 = False
    st.session_state.tampilan25 = False
    st.session_state.tampilan26 = False
    st.session_state.tampilan27 = False
    st.session_state.tampilan28 = False
    st.session_state.tampilan29 = False
    st.session_state.tampilan30 = True
    st.rerun()
st.sidebar.markdown("---")
if st.sidebar.button("Angket dan Saran"):
    st.session_state.tampilan1=False
    st.session_state.tampilan2=False
    st.session_state.tampilan3 = False
    st.session_state.tampilan4 = False
    st.session_state.tampilan5 = False
    st.session_state.tampilan6 = False
    st.session_state.tampilan7 = False
    st.session_state.tampilan8 = False
    st.session_state.tampilan9 = False
    st.session_state.tampilan10 = False
    st.session_state.tampilan11 = True
    st.session_state.tampilan12 = False
    st.session_state.tampilan13 = False
    st.session_state.tampilan14 = False
    st.session_state.tampilan15 = False
    st.session_state.tampilan16 = False
    st.session_state.tampilan17 = False
    st.session_state.tampilan18 = False
    st.session_state.tampilan19 = False
    st.session_state.tampilan20 = False
    st.session_state.tampilan21 = False
    st.session_state.tampilan22 = False
    st.session_state.tampilan23 = False
    st.session_state.tampilan24 = False
    st.session_state.tampilan25 = False
    st.session_state.tampilan26 = False
    st.session_state.tampilan27 = False
    st.session_state.tampilan28 = False
    st.session_state.tampilan29 = False
    st.session_state.tampilan30 = False
    st.rerun()




    
