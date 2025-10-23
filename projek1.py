import streamlit as st
import numpy as np
import pandas as pd
from statistics import mean, median, mode, stdev, multimode
import matplotlib.pyplot as plt
from scipy.stats import norm
import requests
import base64
import math

import seaborn as sns
from scipy import stats
from scipy.stats import shapiro, normaltest, anderson, kstest
import plotly.express as px
import plotly.graph_objects as go

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
    pilihan = st.tabs(['Pengertian','Simulasi'])
    with pilihan[0]:
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
    with pilihan[1]:
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
    st.rerun()
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
    st.rerun()
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
    st.rerun()
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
    st.rerun()



    
