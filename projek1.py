import streamlit as st



if "tampilan1" not in st.session_state:
    st.session_state.tampilan1 = False

if "tampilan2" not in st.session_state:
    st.session_state.tampilan2 = False

if "tampilan3" not in st.session_state:
    st.session_state.tampilan3 = True

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


if st.session_state.tampilan1:
    tampilkan_materi1()
if st.session_state.tampilan2:
    tampilkan_materi2()
if st.session_state.tampilan3:
    latar()


if st.sidebar.button("Pengenalan"):
    st.session_state.tampilan1=False
    st.session_state.tampilan2=False
    st.session_state.tampilan3 = True
    st.rerun()
if st.sidebar.button("Skala Pengukuran Data"):
    st.session_state.tampilan1=True
    st.session_state.tampilan2=False
    st.session_state.tampilan3 = False
    st.rerun()
if st.sidebar.button("Pengantar Statistik dalam Penelitian R&D"):
    st.session_state.tampilan1=False
    st.session_state.tampilan2=True
    st.session_state.tampilan3 = False
    st.rerun()

    
