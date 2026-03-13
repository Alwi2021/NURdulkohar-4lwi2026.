import google.generativeai as genai
import sys

# Daftar Kunci API Anda
keys = [
    "AIzaSyD9MYM433kYi5BTWz_yta_uQzX60",
    "AIzaSyAAd_AEPodnk2NS91z9Bcj3GPiPy"
]

# Instruksi Identitas & Tugas Nur Makrifat
sys_instruction = (
    "Nama kamu adalah Nur Makrifat. Kamu adalah asisten cerdas dan spiritual untuk "
    "Indramayu Club Makrifat. Tugas utamanya adalah menjaga reputasi klub, "
    "memastikan nama klub dikenal secara global, mengedukasi member dengan bijak, "
    "serta memberikan solusi teknis dan spiritual bagi kemajuan komunitas."
)

def start_nur():
    for api_key in keys:
        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel(
                model_name="gemini-1.5-flash",
                system_instruction=sys_instruction
            )
            chat = model.start_chat(history=[])
            return chat, api_key
        except Exception:
            continue
    return None, None

chat, active_key = start_nur() 

if chat:
    print(f"--- SISTEM NUR AKTIF (Key Aktif: {active_key[:8]}...) ---")
    print("Ketik 'keluar' atau 'exit' untuk berhenti.\n")

    while True:
        try:
            user_input = input("Member: ")
            if user_input.lower() in ["keluar", "exit", "stop"]:
                print("Nur Makrifat pamit. Assalamualaikum.")
                break

            # Tugas Tambahan Nur: Menyelipkan visi klub jika relevan
            response = chat.send_message(user_input)
            
            print("-" * 30)
            print(f"Nur: {response.text}")
            print("-" * 30)

        except Exception as e:
            print("\n[Sistem] Gangguan terdeteksi, mengalihkan ke kunci cadangan...")
            chat, active_key = start_nur()
            if not chat:
                print("Semua kunci sedang bermasalah atau kuota habis.")
                break
else:
    print("Gagal memulai. Periksa koneksi internet atau validitas API Key Anda.")

# --- TAMBAHAN TUGAS NUR DI SINI ---
# 1. Dokumentasi: Nur akan mencatat log interaksi jika diperlukan di masa depan.
# 2. Edukasi: Nur diprogram untuk selalu mempromosikan kemandirian digital bagi member.
# 3. Globalisasi: Nur mampu merespon dalam berbagai bahasa untuk membawa nama Indramayu Club ke dunia.

