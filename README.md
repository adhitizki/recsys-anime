# Pendahuluan

Dalam era digital ini, kita telah dibombardir dengan berbagai pilihan hiburan, dan salah satunya adalah anime. Anime adalah suatu bentuk hiburan yang sangat populer di kalangan berbagai kelompok usia. Dengan begitu banyak judul anime yang tersedia, mungkin sulit bagi penonton untuk menemukan anime yang sesuai dengan preferensi mereka. Untuk mengatasi masalah ini, kita dapat menggunakan teknologi dan data untuk membangun sistem rekomendasi yang akan membantu pengguna menemukan anime yang sesuai dengan selera mereka. Dalam artikel ini, kita akan menjelajahi pengembangan sistem rekomendasi anime berdasarkan data rating, dengan fokus pada pemilihan model dan evaluasi kinerja model.

## Problem
Masalah bisnis yang ingin kita selesaikan adalah membantu pengguna menemukan anime yang mereka nikmati. Ini akan membantu sebuah platform streaming anime meningkatkan dan menjaga jumlah pengguna dengan tujuan meningkatkan pendapatan streaming platform anime.

## Goals
Solusi yang kita tawarkan adalah membangun sebuah sistem rekomendasi. Sistem ini akan menggunakan data rating yang diberikan oleh pengguna untuk anime-anime tertentu. Dengan menganalisis pola rating pengguna, sistem ini akan memberikan rekomendasi anime yang sesuai dengan selera pengguna.

## Model Development

Sistem rekomendasi yang kita kembangkan adalah sistem rekomendasi berdasarkan regresi. Artinya, kita akan memprediksi rating yang akan diberikan oleh seorang pengguna untuk anime tertentu.

Saat ini, kita menggunakan model Singular Value Decomposition (SVD) sebagai model rekomendasi. Model ini bersifat "personalized," yang berarti rekomendasi akan disesuaikan dengan preferensi unik masing-masing pengguna.

Sistem rekomendasi SVD bekerja dengan memproyeksikan data rating ke dalam ruang dimensi yang lebih rendah dan menemukan pola tersembunyi dalam data. Dengan cara ini, kita dapat memprediksi rating yang mungkin diberikan oleh seorang pengguna untuk anime yang belum pernah mereka tonton.

Dalam pengembangan model SVD, dilakukan eksperimen dengan berbagai konfigurasi model, seperti jumlah faktor, jumlah iterasi, learning rate, dan regularization. Kami menggunakan HPO untuk mencari parameter terbaik yang menghasilkan RMSE terendah pada data pengujian.
Untuk mengevaluasi kinerja sistem rekomendasi, kita melakukan validasi silang (cross-validation) dan mengukur Root Mean Square Error (RMSE) pada data pengujian. RMSE adalah metrik yang mengukur seberapa baik model kita dalam memprediksi rating pengguna. Semakin rendah RMSE, semakin baik kinerja model.

## Workflow Modelling
1. **Data Collection**: Mengumpulkan data rating dari pengguna anime (mengunduh dat dari kaggle).
2. **Data Preprocessing**: Melakukan filtering pada data.
3. **Permodelan**: MElatih model SVD dan Baseline (Mean Prediction)
4. **Validasi Silang**: Melakukan validasi silang untuk mengukur kinerja model.
5. **Hyperparameter Optimization**: Melakukan pencarian parameter yang menghasilkan model terbaik.
6. **Evaluasi**: Mengukur kinerja model dengan RMSE pada data pengujian.
7. **Sistem Rekomendasi**: Memberikan rekomendasi anime kepada pengguna.

## Conclusion
Hingga ditemukan nilai RMSE terendah sebesar 1,166147 pada model SVD yang diharapkan sistem rekomendasi mampu memberikan rekomendasi anime sesuai dengan pengguna, sehingga pengguna dapat terus memakai platform streaming anime. Sehingga dapat menaikkan jumlah keuntungan perusahaan platform anime.

**Referensi**:
- https://www.kaggle.com/datasets/CooperUnion/anime-recommendations-database
- https://towardsdatascience.com/recsys-implementation-on-variants-of-svd-based-recommender-system-a3dc1d059c83
